
var ws = false

export function getWebSocket() {
   if ( !ws || ws.readyState == 3 ) {
    ws = new WebSocket('ws://192.168.111.1:9988/')
   }
   if ( ws.readyState == 0) {
     return false
   }

   return ws
}
