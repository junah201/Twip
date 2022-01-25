# Project description
## Twip

[![PyPI version](https://badge.fury.io/py/Twip.svg)](https://badge.fury.io/py/Twip)

### Introduction

이 라이브러리는 [twip](www.twip.kr)의 공식 라이브러리가 아니며,  [twip](www.twip.kr)에서 스트리머들에게 제공하는 Alert Box를 이용해서 도네이션, 팔로우, 호스팅 등의 이벤트에 대해서 간편하게 대응하기 위해서 만들어졌습니다.

This library is not an official library of twip. It was created to conveniently respond to events such as donation, follow, and hosting using the Alert Box provided by twip to streamers.

### Installation

```shell
pip install twip-api
```

### Examlpe

```py
import twip

Twip = twip.Twip()

@Twip.event
def on_donate(ctx):
    print(f"id : {ctx.id}")
    print(f"nickname : {ctx.nickname}")
    print(f"amount : {ctx.amount}")
    print(f"comment : {ctx.comment}")
    
Twip.run("your alert box id")
```

More examples on github [example.py](https://github.com/junah201/Twip/blob/main/example.py)

## Features

- Class corresponding to each event element
- Using Websockets (Not socket.io)
- Use of decorators

## Tech

Twip uses a number of open source projects to work properly:

- [websocket-client](https://github.com/websocket-client/websocket-client)- It provides access to low level APIs for WebSockets.
- [requests](https://github.com/psf/requests) - An elegant and simple HTTP library for Python.
- [urllib](https://docs.python.org/3/library/urllib.html) - A package that collects several modules for working with URLs.
- [re](https://docs.python.org/3/library/re.html?highlight=re#module-re) - regular expression matching operations.

## License

MIT