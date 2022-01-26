# Twip

[![PyPI version](https://badge.fury.io/py/twip-api.svg)](https://badge.fury.io/py/twip-api)

## Introduction

이 라이브러리는 [Twip](www.twip.kr)의 공식 라이브러리가 아니며, [Twip](www.twip.kr)에서 스트리머들에게 제공하는 Alert Box를 이용해서 도네이션, 팔로우, 호스팅 등의 이벤트에 대해서 간편하게 대응하기 위해서 만들어졌습니다.

This library is not an official library of twip. It was created to conveniently respond to events such as donation, follow, and hosting using the Alert Box provided by twip to streamers.

## Installation

```shell
pip install twip-api
```

## Examlpe

```py
import twip

Twip = twip.Twip()

@Twip.event
def on_donate(ctx):
    print(f"id : {ctx.id}")
    print(f"nickname : {ctx.nickname}")
    print(f"amount : {ctx.amount}")
    print(f"comment : {ctx.comment}")
    
Twip.run("your alert box id", "your twip api token"")
```

More examples on github [example.py](https://github.com/junah201/Twip/blob/main/twip/example.py)

## Events

- **on_donate** : New Donation, Video, Slotmachines
- **on_subscribe** : New subscription
- **on_hosting** : New hosting
- **on_cheer** : New bits cheer
- **on_follow** : New follower
- **on_sound** : Sound (If you do not access the twip alert box you will not receive any sound events.)

## Features

- Class corresponding to each event element
- Using Websockets (Not socket.io)
- Use of decorators

## Tech

Twip uses a number of open source projects to work properly:

- [websocket-client](https://github.com/websocket-client/websocket-client)- It provides access to low level APIs for WebSockets.
- [requests](https://github.com/psf/requests) - An elegant and simple HTTP library for Python.
- [urllib](https://docs.python.org/3/library/urllib.html) - A package that collects several modules for working with URLs.
- [re](https://docs.python.org/3/library/re.html?highlight=re#module-re) - Regular expression matching operations.
- [warnings](https://docs.python.org/ko/3/library/warnings.html) - Issue warnings by calling the warn() function defined in this module.
## License

MIT

## Version

- 0.0.7 : Fixed bug that occurred when there was no sound event.
- 0.0.8 : Convert to receive api key input ([#1](https://github.com/junah201/Twip/issues/1))
- 0.0.8.1 : Add token_crawl option ([#1](https://github.com/junah201/Twip/issues/1))