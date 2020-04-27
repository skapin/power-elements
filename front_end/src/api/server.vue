<script>

import {getWebSocket} from './http.js';

const AP_NAME = '';

var nbr_msg_send = 0;

function getStrikeLabel(image) {
  var ws = getWebSocket()
  if ( ws ) {
    if(nbr_msg_send > 25) {
      nbr_msg_send = 0
      ws.close()
    }
  }
  return new Promise(function(resolve, reject){
    if ( ws.readyState == 1 ){
      nbr_msg_send += 1;
      ws.send(image)
      ws.onmessage = function (event) {
        nbr_msg_send -= 1;
        resolve(event.data);
      }
    }
  })

}

function closeWebsocket(ws) {
  ws.close
}


export default{
  getStrikeLabel
}

</script>