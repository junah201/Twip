import websocket
from json import loads
from requests import get
from re import search

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
       
    class Donate():
        def __init__(self):
            self.type = "donate"
            self.id = None
            self.nickname = None
            self.amount = None
            self.comment = None
            self.watcher_id = None
            self.subbed = None
            self.repeat = None
            self.ttstype = None
            self.ttsurl = None
            self.slotmachine = self.Slotmachine()
            self.effect = None
            self.variation_id = None
    
        class Slotmachine():
            def __init__(self):
                self.items = None
                self.result = None
                self.reward_id = 2
                self.sound = None
                self.point = None
                self.duration = None   
                
    class Follow():
        def __init__(self):
            self.nickname = None
            self.repeat = None
            self.variation_id = None
            
    class Subscribe():
        def __init__(self):
            self.username = None
            self.months = None
            self.message = None
            self.method = None
            self.repeat = None
            self.variation_id = None
    
    class Hosting():
        def __init__(self):
            self.username = None
            self.viewers = None
            self.repeat = None
            self.variation_id = None
    
    class Cheer():
        def __init__(self):
            self.nickname = None
            self.amount = None
            self.comment = None
            self.repeat = None
            self.variation_id = None
    
    class Sound():
        def __init__(self):
            self.type = None
            self.volume = None
            self.url = None
    
    def on_message(self, wsapp, message):
        # 0 open Sent from the server when a new transport is opened (recheck)
        if message[0] == "0":
            wsapp.send(message)
        elif message[:2] == "42":
            result = loads(message[2:])
            if result[0] in self.events.keys():
                self.events[result[0]](self.data_convert(result))
            # The type comes in as 'sound:play' or 'sound:stop'
            elif result[0][:5] == "sound":
                self.events[result[0][:5]](self.data_convert(result))
 
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
    
    def run(self,id:str):
        '''id : The back of the twip's alert box url
        ex) https://twip.kr/widgets/alertbox/1A2B3CXXXX -> 1A2B3CXXXX
        '''
        
        self.id = id
        response = get(f"https://twip.kr/widgets/alertbox/"+self.id)
        
        self.version = search(r"version: '\d{1,3}.\d{1,3}.\d{1,3}',",response.text).group()[10:-2]
        self.token = search(r"window.__TOKEN__ = '(.+);",response.text).group()[20:-2]
        
        self.sio.url = f"wss://io.mytwip.net/socket.io/?alertbox_key={id}&version={self.version}&{parse.urlencode([('token',self.token)], doseq = True)}&transport=websocket"
        
        self.sio.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
            )