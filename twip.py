import websocket

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