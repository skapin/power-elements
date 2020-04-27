<template>
  <video id="back-camera" autoplay></video>
</template>

<script src="https://webrtc.github.io/adapter/adapter-latest.js"></script>

<script>
import server from '../../api/server.vue'

const FRAMERATE_MS = 100

function permError() {
  console.log('Shit, no camera permissions')
  alert('Camera permission is not turned on');
}

function permSuccess( status ) {
  if( !status.hasPermission ) error();
}

export default {
  name: 'VueCamera',
  props: ['striker'],
  data() {
    return {
        isConnected: false,
        streamCapture: null
      };
  },
  mounted() {
    //console.log(this.$el);
    //var permissions = cordova.plugins.permissions
    //permissions.requestPermissions([permissions.CAMERA, permissions.INTERNET], permSuccess, permError)

    navigator.mediaDevices.enumerateDevices().then( devices =>
    {
      devices= devices.filter( v => (v.kind=="videoinput"));
      console.log("Found "+devices.length +" video devices");

      let lastDevice= devices[devices.length-1];
      devices= devices.filter( v => (v.label.indexOf("back")>0));

      let device= null;
      if( devices.length > 0 ) {
        console.log("Taking a 'back' camera");
        device= devices[devices.length-1];
      }
      else {
        console.log("Taking last camera");
        device= lastDevice;
      }

      if( !device ) {
        console.log("No devices!");
        return;
      }

      let constraints = {
        audio: false, 
        video: {
          deviceId: { ideal: device.deviceId },
          width: { ideal: window.innerWidth },
          height: { ideal: window.innerHeight }
        }
      };

      navigator.mediaDevices.getUserMedia(constraints)
      .then( stream => {
        try {
          this.$el.srcObject = stream;
          console.log(stream.getVideoTracks())
          const track = stream.getVideoTracks()[0];
          this.streamCapture = new ImageCapture(track);
        } catch (error) {
          console.log(error)
          this.$el.srcObject = URL.createObjectURL(stream);
        }

        console.log("DONE");
      })
      .catch( err => {
        console.log(err.name + ": " + err.message);
      });
    })
    .catch( err => {
      console.log(err.name + ": " + err.message);
    });

    this.sendCameraFrame()
  },
  methods: {
    sendCameraFrame() {
      if( this.striker.isStreaming ){
        this.streamCapture.takePhoto()
        .then( blobImg => {
          blobImg.arrayBuffer()
          .then(buffer => {
            server.getStrikeLabel(buffer)
            .then(data => {
              this.striker.strikeLabel = data
            })
          })
        })
      }

      setTimeout(function () {
        this.sendCameraFrame();
      }.bind(this), FRAMERATE_MS);
    }
  }
}
</script>
