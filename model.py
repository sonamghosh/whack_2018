import torch 
from torch import nn 
from torch.autograd import Variable 
from torch.nn import functional as tf

"""
Dual-Stage Attention-Based Recurrent Neural netowkr that is stacked
for time series based on Chandler Zuo and Sean Aubin

DA-RNN links:
http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/
http://colah.github.io/posts/2015-08-Understanding-LSTMs/

Research Paper:
A Dual-Stage Attention-Based Recurrent Neural Network
for Time Series Prediction
Yao Qin1∗
, Dongjin Song2
, Haifeng Chen2
, Wei Cheng2
, Guofei Jiang2
, Garrison W. Cottrell1
1University of California, San Diego
2NEC Laboratories America, Inc.

https://arxiv.org/pdf/1704.02971.pdf

Equations in code below are from paper above^^

there is a exclusion of using contemporary values of exogeneous factors

def. of exogenous - relating to or developing from external factors

individual stock prices = exogenous factors
nasdaq stock index = target time series

DA-RNN Model:

Two LSTM networks with attention mechanism.
First LSTM encodes information among historical exogenous data
Attention mechanism performs feature selection to select the most import
the most exogenous factors. 
Second LSTM further combines the information from exogenous data to perform
feature selection in time domain.  (apply weight to info at diff. historical time pts)
Final pred is based on feature selection in both dimensions of exogenous factors and time.
DA-RNN selects features dynamically -- weights on factors and time points change over time
Traditional statistical models rely on classical feature selection.
"""

def init_hidden(x, hidden_size: int):
    """
    Train initial value of hidden state:
    https://r2rt.com/non-zero-initial-states-for-recurrent-neural-networks.html

    """

    return Variable(torch.zeros(1, x.size(0), hidden_size))


class Encoder(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, T: int):
        """
        Params:
        input_size - number of underlying factors (18)
        T - number of time steps (10)
        hidden_size - dimension of hidden state
        """

        super(Encoder, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.T = T

        self.lstm_layer = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=1)
        self.attn_linear = nn.Linear(in_features=2*hidden_size+T-1, out_features=1)


    def forward(self, input_data):
        """
        Params:
        input_data - dimensions of (batch_size, T - 1, input_size)

        Methods clarifications:
        Permute(*dims) --> Tensor: Permute the dimensions of a tensor
        >>> x = torch.randn(2, 3, 5)
        >>> x.size() 
        >>> torch.Size([2, 3, 5])
        >>> x.permute(2,0,1).size()
        >>> torch.Size([5, 2, 3])
        Repeat(*sizes) --> Tensor: Repeats tensor along specific dimensions
        >>> x = torch.tensor([1, 2, 3])
        >>> x.repeat(4, 2)
        tensor([[ 1,  2,  3,  1,  2,  3],
                [ 1,  2,  3,  1,  2,  3],
                [ 1,  2,  3,  1,  2,  3],
                [ 1,  2,  3,  1,  2,  3]])
        >>> x.repeat(4, 2, 1).size()
        torch.Size([4, 2, 3]
        """

        input_weighted = Variable(torch.zeros(input_data.size(0), self.T - 1, self.input_size))
        input_encoded = Variable(torch.zeros(input_data.size(0), self.T - 1, self.hidden_size))
        # hidden, cell - initial states with dimension hidden_size
        hidden = init_hidden(input_data, self.hidden_size)  # 1 * batch_size * hidden_size
        cell = init_hidden(input_data, self.hidden_size)

        for t in range(self.T - 1):
            # Eqn. 8 - concat hidden state with each predictor
            # e of kth input at time t
            # e = v_e.T * tanh(W_e[h_(t-1); s_(t-1)] + U_e*x)
            # [h_(t-1); s_(t-1)] is the hidden state and unit cell concatted
            # v (size T), W (size T x 2m) , U (size T x T) learning params
            x = torch.cat((hidden.repeat(self.input_size, 1, 1).permute(1, 0, 2),
                           cell.repeat(self.input_size, 1, 1).permute(1, 0, 2),
                           input_data.permute(0, 2, 1)), dim=2)
            # batch size = 2 * hiddensize + T - 1
            # Eqn. 8 Attention weights , (batch size * input size) * 1
            x = self.attn_linear(x.view(-1, self.hidden_size * 2 + self.T - 1))
            # Eqn. 9 Softmax (batch_size, input_size)
            attn_weights = tf.softmax(x.view(-1, self.input_size), dim=1)
            # Eqn. 10 LSTM
            weighted_input = torch.mul(attn_weights, input_data[:, t, :])  # batch_size, input_size
            self.lstm_layer.flatten_parameters()
            _, lstm_states = self.lstm_layer(weighted_input.unsqueeze(0), (hidden, cell))
            hidden = lstm_states[0]
            cell = lstm_states[1]
            # Save output
            input_weighted[:, t, :] = weighted_input
            input_encoded[:, t, :] = hidden

        return input_weighted, input_encoded


class Decoder(nn.Module):
    def __init__(self, encoder_hidden_size: int, decoder_hidden_size: int, T: int, out_feats=1):
        """
        Clarifications:
        torch.nn.Sequentual(*args) - Sequential container. Modules are passed through it like a consturctor.
        Ordered dict of modules can be passed in

        model = nn.Sequential(
                    nn.Conv2d(1,20,5),
                    nn.ReLU(),
                    nn.Conv2d(20,64,5),
                    nn.ReLU())
        model = nn.Sequential(OrderedDict([
                    ('conv1', nn.Conv2d(1,20,5)),
                    ('relu1', nn.ReLU()),
                    ('conv2', nn.Conv2d(20,64,5)),
                    ('relu2', nn.ReLU())
                    ]))

        torch.bmm(batch_1, batch_2, out=None --> Tensor
        Perofrms batch matrix-matrix product of matrices from the two batches
        batches must be 3-D tensors containing same number of matrices
        if batch1 is b x n x m tensor and batch2 is b x m x p tensor
        out is b x n x p
        >>> batch1 = torch.randn(10, 3, 4)
        >>> batch2 = torch.randn(10, 4, 5)
        >>> res = torch.bmm(batch1, batch2)
        >>> res.size()
        torch.Size([10, 3, 5])
        """
        super(Decoder, self).__init__()

        self.T = T
        self.encoder_hidden_size = encoder_hidden_size
        self.decoder_hidden_size = decoder_hidden_size

        self.attn_layer = nn.Sequential(nn.Linear(2 * decoder_hidden_size + encoder_hidden_size,
                                                  encoder_hidden_size),
                                                  nn.Tanh(), nn.Linear(encoder_hidden_size, 1))
        self.lstm_layer = nn.LSTM(input_size=out_feats, hidden_size=decoder_hidden_size)
        self.fc = nn.Linear(encoder_hidden_size + out_feats, out_feats)
        self.fc_final = nn.Linear(decoder_hidden_size + encoder_hidden_size, out_feats)

        self.fc.weight.data.normal_()


    def forward(self, input_encoded, y_history):
        # input_encoded - (batch_size, T - 1, encoder_hidden_size)
        # y_history  - (batch_size, T-1)
        # Initialize hidden and cell, (1, batch_size, decoder_hidden_size)
        hidden = init_hidden(input_encoded, self.decoder_hidden_size)
        cell = init_hidden(input_encoded, self.decoder_hidden_size)
        context = Variable(torch.zeros(input_encoded.size(0), self.encoder_hidden_size))

        for t in range(self.T - 1):
            # (batch_size, T, (2*decoder_hidden_size + encoder_hidden_size))
            x = torch.cat((hidden.repeat(self.T - 1, 1, 1).permute(1, 0, 2),
                           cell.repeat(self.T - 1, 1, 1).permute(1, 0, 2),
                           input_encoded), dim=2)
            # Eqn. 12 and 13 - softmax on attention weights
            x = tf.softmax(
                    self.attn_layer(x.view(-1, 2*self.decoder_hidden_size+self.encoder_hidden_size)
                    ).view(-1, self.T - 1), dim=1)  # (batch_size, T- 1)
            # Eqn. 14 compute context vector C
            context = torch.bmm(x.unsqueeze(1), input_encoded)[:, 0, :]

            # Eqn. 15 target series
            y_tilde = self.fc(torch.cat((context, y_history[:, t]), dim=1))  # (batch_size, out_size)
            # Eqn. 16 LSTM 
            self.lstm_layer.flatten_parameters()
            _, lstm_output = self.lstm_layer(y_tilde.unsqueeze(0), (hidden, cell))
            hidden = lstm_output[0]  # 1 * batch_size * decoder_hidden_size
            cell = lstm_output[1]  # 1 * batch_size * decoder_hidden_size

        # Eqn 22: final output
        return self.fc_final(torch.cat((hidden[0], context), dim=1))
            