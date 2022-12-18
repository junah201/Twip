# Twip

[![PyPI version](https://badge.fury.io/py/twip-api.svg)](https://badge.fury.io/py/twip-api) [![Downloads](https://pepy.tech/badge/twip-api)](https://pepy.tech/project/twip-api) [![Downloads](https://pepy.tech/badge/twip-api/month)](https://pepy.tech/project/twip-api)

이 라이브러리는 [Twip](www.twip.kr)의 공식 라이브러리가 아니며, [Twip](www.twip.kr)에서 스트리머들에게 제공하는 Alert Box를 이용해서 도네이션, 팔로우, 호스팅 등의 이벤트에 대해서 간편하게 대응하기 위해서 만들어졌습니다.

------------


## 📥 설치

```shell
pip install twip-api
```

## ✍️ 사용 예시

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

더 많은 예제는 Github [example.py](https://github.com/junah201/Twip/blob/main/twip/example.py) 에서 확인하세요.

## 🔥 Events

- **on_ready** : 트윕과 처음으로 연결되었을 때
- **on_donate** : 후원, 영상후원, 슬롯머신(룰렛)
- **on_subscribe** : 구독
- **on_hosting** : 호스팅
- **on_cheer** : 비트
- **on_follow** : 팔로우
- **on_sound** : 소리

## 🖥️ Tech

- [websocket-client](https://github.com/websocket-client/websocket-client)- It provides access to low level APIs for WebSockets.
- [requests](https://github.com/psf/requests) - An elegant and simple HTTP library for Python.
- [urllib](https://docs.python.org/3/library/urllib.html) - A package that collects several modules for working with URLs.
- [re](https://docs.python.org/3/library/re.html?highlight=re#module-re) - Regular expression matching operations.
- [warnings](https://docs.python.org/ko/3/library/warnings.html) - Issue warnings by calling the warn() function defined in this module.


## 📖 Version

- **[0.0.7](https://pypi.org/project/twip-api/0.0.7/)** : 사운드 이벤트가 없을 때 발생하던 버그 수정
- **[0.0.8](https://pypi.org/project/twip-api/0.0.8/)** : api key를 직접 입력 받도록 수정 ([#1](https://github.com/junah201/Twip/issues/1))
- **[0.0.8.1](https://pypi.org/project/twip-api/0.0.8.1/)** : 토큰 크롤링 옵션 추가 ([#1](https://github.com/junah201/Twip/issues/1))
- **[0.0.8.2](https://pypi.org/project/twip-api/0.0.8.2/)** : 함수 이름 관련 버그 수정
- **[0.0.9](https://pypi.org/project/twip-api/0.0.9/)** : on_ready 이벤트 추가
- **[0.0.9.1](https://pypi.org/project/twip-api/0.0.9.1/)** : 크롤링된 토큰이 유효기간이 지난 후에도 계속해서 사용되던 버그 수정

## ✔️ 업데이트 예정

- 비동기 설정 추가


## 🕮 License

- [MIT](https://github.com/junah201/Twip/blob/main/LICENSE)

## 기타문의

- Email : junah.dev@gmail.com
