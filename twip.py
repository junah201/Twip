import websocket
from json import loads
from requests import get
from re import search
from urllib import parse


class Twip:
    def __init__(self):
        self.id = None
        self.version = None
        self.token = None
        self.sio = websocket.WebSocketApp(
            None,
            on_message=self.on_message,
            on_ping=self.on_ping,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ping_interval = 20
        self.ping_timeout = 10
        self.ping_payload = "2"
        self.events = {}
    
    class Donate:
        def __init__(self):
            self.type = "donate"
            self.id = None
            self.nickname = None
            self.amount = None
            self.comment = None
            self.watcher_id = None
            self.subbed = None
            self.repeat = None
            self.tts_type = None
            self.tts_url = None
            self.slotmachine = self.Slotmachine()
            self.effect = None
            self.variation_id = None
    
        class Slotmachine:
            def __init__(self):
                self.items = None
                self.result = None
                self.reward_id = 2
                self.sound = None
                self.point = None
                self.duration = None   
    
    class Follow:
        def __init__(self):
            self.nickname = None
            self.repeat = None
            self.variation_id = None
            
    class Subscribe:
        def __init__(self):
            self.username = None
            self.months = None
            self.message = None
            self.method = None
            self.repeat = None
            self.variation_id = None
    
    class Hosting:
        def __init__(self):
            self.username = None
            self.viewers = None
            self.repeat = None
            self.variation_id = None
    
    class Cheer:
        def __init__(self):
            self.nickname = None
            self.amount = None
            self.comment = None
            self.repeat = None
            self.variation_id = None
    
    class Sound:
        def __init__(self):
            self.type = None
            self.volume = None
            self.url = None
    
    def event(self, func):
        if func.__name__[:3] != "on_":
            raise Exception("Event name must start with 'on_'")
        self.events[self.event_name_convert(func.__name__)] = func

    @staticmethod
    def event_name_convert(name: str) -> str:
        if name == "on_donate":
            return "new donate"
        elif name == "on_follow":
            return "new follow"
        elif name == "on_subscribe":
            return "new sub"
        elif name == "on_hosting":
            return "new hosting"
        elif name == "on_cheer":
            return "new cheer"
        elif name == "on_sound":
            return "sound"
        else:
            raise Exception("Event name must be one of the following: on_donate, on_follow, on_subscribe, on_hosting, on_cheer, on_sound")

    @staticmethod
    def data_convert(data: list):
        data_type = data[0]
        if data_type == "new donate":
            data_value = data[1]
            donate = Twip.Donate()
            
            donate.id = data_value.get("_id")
            donate.nickname = data_value.get("nickname")
            donate.amount = data_value.get("amount")
            donate.comment = data_value.get("comment")
            donate.watcher_id = data_value.get("watcher_id")
            donate.subbed = data_value.get("subbed")
            donate.repeat = data_value.get("repeat")
            donate.tts_type = data_value.get("ttstype")
            donate.tts_url = data_value.get("ttsurl")
            if data_value.get("slotmachine_data") != None:
                donate.slotmachine.items = data_value.get("slotmachine_data").get("items")
                donate.slotmachine.result = data_value.get("slotmachine_data").get("gotcha")
                donate.slotmachine.sound = data_value.get("slotmachine_data").get("config").get("sound")
                donate.slotmachine.point = data_value.get("slotmachine_data").get("config").get("point")
                donate.slotmachine.duration = data_value.get("slotmachine_data").get("config").get("duration")
            donate.effect = data_value.get("effect")
            donate.variation_id = data_value.get("variation_id")
            
            return donate
        
        elif data_type == "new follow":
            data_value = data[1]
            follow = Twip.Follow()
            
            follow.nickname = data_value.get("nickname")
            follow.repeat = data_value.get("repeat")
            follow.variation_id = data_value.get("variation_id")
            
            return follow
        
        elif data_type == "new sub":
            data_value = data[1]
            subscribe = Twip.Subscribe()
            
            subscribe.username = data_value.get("username")
            subscribe.months = data_value.get("months")
            subscribe.message = data_value.get("message")
            subscribe.method = data_value.get("method")
            subscribe.repeat = data_value.get("repeat")
            subscribe.variation_id = data_value.get("variation_id")
            
            return subscribe
        
        elif data_type == "new hosting":
            data_value = data[1]
            hosting = Twip.Hosting()
            
            hosting.username = data_value.get("username")
            hosting.viewers = data_value.get("viewers")
            hosting.repeat = data_value.get("repeat")
            hosting.variation_id = data_value.get("variation_id")
            
            return hosting
        
        elif data_type == "new cheer":
            data_value = data[1]
            cheer = Twip.Cheer()
            
            cheer.nickname = data_value.get("nickname")
            cheer.amount = data_value.get("amount")
            cheer.comment = data_value.get("comment")
            cheer.repeat = data_value.get("repeat")
            cheer.variation_id = data_value.get("variation_id")
            
            return cheer
        
        # The type comes in as 'sound:play' or 'sound:stop'
        elif data_type[:6] == "sound:":
            if len(data) == 2:
                data_value = data[1]
                sound = Twip.Sound()
                
                sound.type = data_type[6:]
                sound.volume = data_value.get("volume")
                sound.url = data_value.get("url")
            else:
                sound = Twip.Sound()
                sound.type = data_type[6:]
                
            return sound
        
        else:
            return None
    
    def on_message(self, wsapp, message):
        # 0 open Sent from the server when new transport is opened (recheck)
        if message[0] == "0":
            wsapp.send(message)
        elif message[:2] == "42":
            result = loads(message[2:])
            if result[0] in self.events.keys():
                self.events[result[0]](self.data_convert(result))
            # The type comes in as 'sound:play' or 'sound:stop'
            elif result[0][:5] == "sound":
                self.events[result[0][:5]](self.data_convert(result))
 
    def on_ping(self, wsapp):
        wsapp.send(self.ping_payload)
        
    def on_close(self, wsapp, code, reason):
        wsapp.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
            )
        
    def on_error(self, wsapp, error):
        raise Exception(error)
    
    def run(self, alert_id: str):
        """id : The back of the twip's alert box url
        ex) https://twip.kr/widgets/alertbox/1A2B3CXXXX -> 1A2B3CXXXX
        """
        
        self.id = alert_id
        response = get(f"https://twip.kr/widgets/alertbox/"+self.id)
        
        self.version = search(r"version: '\d{1,3}.\d{1,3}.\d{1,3}',", response.text).group()[10:-2]
        self.token = search(r"window.__TOKEN__ = '(.+);", response.text).group()[20:-2]
        
        self.sio.url = f"wss://io.mytwip.net/socket.io/?alertbox_key={alert_id}&version={self.version}&{parse.urlencode([('token',self.token)], doseq = True)}&transport=websocket"
        
        self.sio.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
            )
