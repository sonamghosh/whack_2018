'use strict';

import React, { Component } from 'react';

import {StyleSheet} from 'react-native';

import {
  ViroARScene,
  ViroMaterials,
  ViroNode,
  ViroAnimations,
  Viro3DObject,
  ViroLightingEnvironment,
  ViroARImageMarker,
  ViroARTrackingTargets,
  ViroSphere,
  ViroSpotLight,
  ViroQuad,
  ViroBox,
  ViroText,
  ViroVideo,
  ViroAnimatedImage,
  ViroParticleEmitter
} from 'react-viro';

var createReactClass = require('create-react-class');


var ARCarDemo = createReactClass({
  getInitialState() {
    return {
      texture: "white",
      playAnim: false,
      animateCar: false,
      tapWhite: false,
      tapBlue: false,
      tapGrey: false,
      tapRed: false,
      tapYellow: false,
    }
  },

  render: function() {
    return (
      <ViroARScene>
        <ViroLightingEnvironment source={require('./res/tesla/garage_1k.hdr')}/>
      {/*<ViroText text="Stock FindAR!" scale={[.5, .5, .5]} position={[0, .3, -.5]} extrusionDepth={10} color = "#42f4bc"/>*/}
        <ViroBox position={[0, .6, -2]} scale={[1, 1, 1]} materials={["TeamLogo"]} />
        <ViroARImageMarker target={"logo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["tsla"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Tesla" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} color = "#42f4bc"/>
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .30, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>

          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"fidelitylogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["ftqgx"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Fidelity" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={3} color = "#267a17" />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={3} color = "#42f492"/>
            <ViroVideo
              source={require('./res/teslavideo.mp4')}
              loop={true}
              position={[.35, .25, 0]}
              rotation = {[0,-40,0]}
              scale={[.25, .25, 0]}
           />
           <ViroText text="Media" scale={[.30, .30, .30]} position={[.45, .30, 0]} rotation = {[0,-40,0]} extrusionDepth={3} color = "lightblue"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"microsoftlogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["msft"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Microsoft" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} color = "#173b7a"/>
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"applelogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["aapl"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Apple" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"googlelogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["goog"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Google" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"netflixlogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["nflx"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Netflix" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} color = "#ce2323" />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"tripadvisorlogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["trip"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Trip Advisor" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>

        <ViroARImageMarker target={"amazonlogo"} onAnchorFound={this._onAnchorFound} pauseUpdates={this.state.pauseUpdates}>
          <ViroNode scale={[0, 0, 0]} transformBehaviors={["billboardY"]} animation={{name:this.state.animName, run:this.state.playAnim,}}>
            <ViroBox position={[0, .25, 0]} scale={[.2, .2, .2]} materials={["amzn"]} animation={{name: "rotate", run: true, loop: true}} />
            <ViroText text="Amazon" scale={[.3, .3, .2]} position={[.1, .30, 0]} extrusionDepth={10} />
            <ViroBox position={[-.35, .25, 0]} scale={[.1, .1, .1]} materials={["robinhood"]} animation={{name: "nrotate", run: true, loop: true}} />
            <ViroText text="Buy & Sell" scale={[.30, .30, .30]} position={[-.30, .27, 0]} rotation = {[0,40,0]} extrusionDepth={10} color = "#42f492"/>
          </ViroNode>
          <Viro3DObject
            scale={[0, 0, 0]}
            source={require('./res/tesla/Lightbulb.obj')}
            resources={[require('./res/tesla/object_car.mtl'),
                        ]}
            type="OBJ"
            materials={this.state.texture}
            onClick={this._toggleButtons}
            animation={{name:"scaleCar", run:this.state.animateCar,}} />
          <ViroSpotLight
            innerAngle={5}
            outerAngle={25}
            direction={[0,-1,0]}
            position={[0, 5, 1]}
            color="#ffffff"
            castsShadow={true}
            shadowMapSize={2048}
            shadowNearZ={2}
            shadowFarZ={7}
            shadowOpacity={.7} />
          <ViroQuad
            rotation={[-90, 0, 0]}
            position={[0, -0.001, 0]}
            width={2.5} height={2.5}
            arShadowReceiver={true} />
        </ViroARImageMarker>
      </ViroARScene>


    );
  },
  _onAnchorFound() {
    this.setState({
      animateCar: true,
    })
  },
  _toggleButtons() {
    this.setState({
      animName: (this.state.animName == "scaleUp" ? "scaleDown" : "scaleUp"),
      playAnim: true
    })
  },
  _selectWhite(){
    this.setState({
      texture : "white",
      tapWhite: true
    })
  },
  _selectBlue(){
    this.setState({
      texture : "blue",
      tapBlue: true
    })
  },
  _selectGrey(){
    this.setState({
      texture : "grey",
      tapGrey: true
    })
  },
  _selectRed(){
    this.setState({
      texture : "red",
      tapRed: true
    })
  },
  _selectYellow(){
    this.setState({
      texture : "yellow",
      tapYellow: true
    })
  },
  _animateFinished(){
    this.setState({
      tapWhite: false,
      tapBlue: false,
      tapGrey: false,
      tapRed: false,
      tapYellow: false,
    })
  },
});

ViroMaterials.createMaterials({
  white: {
    lightingModel: "PBR",
    diffuseTexture: require('./res/tesla/object_car_main_Base_Color.png'),
    metalnessTexture: require('./res/tesla/object_car_main_Metallic.png'),
    roughnessTexture: require('./res/tesla/object_car_main_Roughness.png'),
  },
  blue: {
    lightingModel: "PBR",
    diffuseTexture: require('./res/tesla/object_car_main_Base_Color_blue.png'),
    metalnessTexture: require('./res/tesla/object_car_main_Metallic.png'),
    roughnessTexture: require('./res/tesla/object_car_main_Roughness.png'),
  },
  grey: {
    lightingModel: "PBR",
    diffuseTexture: require('./res/tesla/object_car_main_Base_Color_grey.png'),
    metalnessTexture: require('./res/tesla/object_car_main_Metallic.png'),
    roughnessTexture: require('./res/tesla/object_car_main_Roughness.png'),
  },
  red: {
    lightingModel: "PBR",
    diffuseTexture: require('./res/tesla/object_car_main_Base_Color_red.png'),
    metalnessTexture: require('./res/tesla/object_car_main_Metallic.png'),
    roughnessTexture: require('./res/tesla/object_car_main_Roughness.png'),
  },
  yellow: {
    lightingModel: "PBR",
    diffuseTexture: require('./res/tesla/object_car_main_Base_Color_yellow.png'),
    metalnessTexture: require('./res/tesla/object_car_main_Metallic.png'),
    roughnessTexture: require('./res/tesla/object_car_main_Roughness.png'),
  },
  white_sphere: {
    lightingModel: "PBR",
    diffuseColor: "rgb(231,231,231)",
  },
  blue_sphere: {
    lightingModel: "PBR",
    diffuseColor: "rgb(19,42,143)",
  },
  grey_sphere: {
    lightingModel: "PBR",
    diffuseColor: "rgb(75,76,79)",
  },
  red_sphere: {
    lightingModel: "PBR",
    diffuseColor: "rgb(168,0,0)",
  },
  yellow_sphere: {
    lightingModel: "PBR",
    diffuseColor: "rgb(200,142,31)",
  },
  grid: {

    diffuseTexture: require('./res/stock.jpg'),
  },
  aapl: {
    diffuseTexture: require('./res/AAPL_graph.png')

  },
  amzn: {
    diffuseTexture: require('./res/AMZN_graph.png')

  },
  ftqgx: {
    diffuseTexture: require('./res/FTQGX_graph.png')

  },
  goog: {
    diffuseTexture: require('./res/GOOG_graph.png')

  },
  msft: {
    diffuseTexture: require('./res/MSFT_graph.png')

  },
  nflx: {
    diffuseTexture: require('./res/NFLX_graph.png')

  },
  tsla: {
    diffuseTexture: require('./res/TSLA_graph.png')

  },
  trip: {
    diffuseTexture: require('./res/TRIP_graph.png')
  },
  TeamLogo: {
    diffuseTexture: require('./res/stockfindar_logo.png')
  },
  robinhood: {
    diffuseTexture: require('./res/robinhood.jpg')
  }
});

ViroARTrackingTargets.createTargets({
  fidelitylogo : {
    source : require('./res/fidelity-logo.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  microsoftlogo : {
    source : require('./res/microsoft.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  applelogo : {
    source : require('./res/apple.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  googlelogo : {
    source : require('./res/google.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  netflixlogo : {
    source : require('./res/netflix.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  tripadvisorlogo : {
    source : require('./res/tripadvisor.png'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },
  amazonlogo : {
    source : require('./res/amazon.jpg'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  },

  //Tesla
  logo : {
    source : require('./res/logo.png'),
    orientation : "Up",
    physicalWidth : 0.165 // real world width in meters
  }
});

ViroAnimations.registerAnimations({
    scaleUp:{properties:{scaleX:1, scaleY:1, scaleZ:1,},
                  duration: 500, easing: "bounce"},
    scaleDown:{properties:{scaleX:0, scaleY:0, scaleZ:0,},
                  duration: 200,},
    scaleCar:{properties:{scaleX:.05, scaleY:.05, scaleZ:.05,},
                  duration: 500, easing: "bounce"},
    scaleSphereUp:{properties:{scaleX:.8, scaleY:.8, scaleZ:.8,},
                  duration: 50, easing: "easeineaseout"},
    scaleSphereDown:{properties:{scaleX:1, scaleY:1, scaleZ:1,},
                  duration: 50, easing: "easeineaseout"},
    tapAnimation:[["scaleSphereUp", "scaleSphereDown"],]
});

//Rotation
ViroAnimations.registerAnimations({
  rotate: {
    properties: {
      rotateY: "+=90",
      rotateX: "+=0"
    },
    duration: 7500, //Rotate Slowly
  },
  nrotate: {
    properties: {
      rotateY: "-=90",
      rotateX: "-=0"
    },
    duration: 4500, //Rotate Faster opposite
  },

});

module.exports = ARCarDemo;
