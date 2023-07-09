import websocket
from json import loads
from requests import get
from re import search
from urllib import parse
from warnings import warn, filterwarnings
from models import Donate, Follow, Subscribe, Hosting, Cheer, Sound, Slotmachine
from data_convert import convert_donate, convert_follow, convert_subscribe, convert_hosting, convert_cheer, convert_sound


class TwipBase():
    def on_ready(self) -> None:
        pass

    def on_donate(self, donate: Donate) -> None:
        pass

    def on_follow(self, follow: Follow) -> None:
        pass

    def on_subscribe(self, subscribe: Subscribe) -> None:
        pass

    def on_hosting(self, hosting: Hosting) -> None:
        pass

    def on_cheer(self, cheer: Cheer) -> None:
        pass

    def on_sound(self, sound: Sound) -> None:
        pass


class Twip(TwipBase):
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
        self.__is_ready = False
        self.token_crawl = False

    def on_message(self, wsapp, message):
        # 0 open Sent from the server when new transport is opened (recheck)
        if message[0] == "0":
            wsapp.send(message)
            # on_ready event
            if self.__is_ready == False:
                self.__is_ready = True
                self.on_ready()

        elif message[:2] == "42":
            result = loads(message[2:])
            if result[0] == "new donate":
                self.on_donate(convert_donate(result))
            elif result[0] == "new follow":
                self.on_follow(convert_follow(result))
            elif result[0] == "new sub":
                self.on_subscribe(convert_subscribe(result))
            elif result[0] == "new hosting":
                self.on_hosting(convert_hosting(result))
            elif result[0] == "new cheer":
                self.on_cheer(convert_cheer(result))
            elif result[0] == "sound:play":
                self.on_sound(convert_sound(result))
            elif result[0] == "sound:stop":
                self.on_sound(convert_sound(result))

    def on_ping(self, wsapp):
        wsapp.send(self.ping_payload)

    def on_close(self, wsapp, code, reason):
        # Because crawled tokens have time out, set the url to be valid by crawling again.
        if self.token_crawl == True:
            response = get(f"https://twip.kr/widgets/alertbox/"+self.id)
            self.token = search(r"window.__TOKEN__ = '(.+);",
                                response.text).group()[20:-2]
            self.sio.url = f"wss://io.mytwip.net/socket.io/?alertbox_key={self.id}&version={self.version}&{parse.urlencode([('token', self.token)], doseq = True)}&transport=websocket"

        self.sio.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
        )

    def on_error(self, wsapp, error):
        raise Exception(error)

    def run(self, alert_id: str, api_token: str = None, token_crawl: bool = False) -> None:
        """alert_id : The back of twip's the alert box url
        ex) https://twip.kr/widgets/alertbox/1A2B3CXXXX -> 1A2B3CXXXX

        api_token : You can get it from the bottom of https://twip.kr/dashboard/security

        token_crawl : If you don't have api_token, set this to True
        """

        self.id = alert_id
        response = get(f"https://twip.kr/widgets/alertbox/"+self.id)

        self.version = search(
            r"version: '\d{1,3}.\d{1,3}.\d{1,3}',", response.text).group()[10:-2]
        self.token_crawl = token_crawl

        if api_token == None:
            if token_crawl == True:
                filterwarnings("always")
                warn("You don't enter api_token so you get token from alert box url. This token has expiration date and is not recommended. Please visit the page below and issue API Token: https://twip.kr/dashboard/security.", Warning)
                self.token = search(
                    r"window.__TOKEN__ = '(.+);", response.text).group()[20:-2]
            else:
                raise (Exception("You don't enter api_token and token_crawl option is False. Please visit the page below and issue API Token: https://twip.kr/dashboard/security.\n\nIf you want to run with alert_id only, set token_crawl option to True"))
        else:
            self.token = api_token

        self.sio.url = f"wss://io.mytwip.net/socket.io/?alertbox_key={alert_id}&version={self.version}&{parse.urlencode([('token', self.token)], doseq = True)}&transport=websocket"

        self.sio.run_forever(
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout,
            ping_payload=self.ping_payload
        )
