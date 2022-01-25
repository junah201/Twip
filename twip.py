import websocket
from json import loads

class Twip():
    def __init__(self):
        self.sio = websocket.WebSocketApp(
            None,
            on_message=self.on_message,
            on_ping=self.on_ping,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ping_interval = 20
        self.ping_timeout=10
        self.ping_payload="2"
        self.events = {}
       
    def on_message(self, wsapp, message):
        # 0 open Sent from the server when a new transport is opened (recheck)
        if message[0] == "0":
            wsapp.send(message)
        elif message[:2] == "42":
            result = loads(message[2:])
            if result[0] in self.events.keys():
                self.events[result[0]](self.data_convert(result))       
 
    def on_ping(self,wsapp):
        wsapp.send(self.ping_payload)
        
    def on_close(self,wsapp, code, reason):
        wsapp.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
            )
        
    def on_error(self, wsapp, error):
        raise Exception(error)