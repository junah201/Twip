from dataclasses import dataclass
from typing import Optional


@dataclass
class Slotmachine:
    items: list = None
    result: str = None
    sound: str = None
    point: int = None
    duration: int = None

    def __str__(self):
        return f"Slotmachine(items={self.items}, result={self.result}, sound={self.sound}, point={self.point}, duration={self.duration})"

    def __repr__(self):
        return f"Slotmachine(items={self.items}, result={self.result}, sound={self.sound}, point={self.point}, duration={self.duration})"


@dataclass
class Donate:
    type: str
    id: str
    nickname: str
    amount: int
    comment: str
    watcher_id: str
    subbed: bool
    repeat: bool
    tts_type: str
    tts_url: list
    effect: dict
    variation_id: str
    slotmachine: Optional[Slotmachine] = None

    def __str__(self):
        return f"Donate(id={self.id}, nickname={self.nickname}, amount={self.amount}, comment={self.comment}, watcher_id={self.watcher_id})"

    def __repr__(self):
        return f"Donate(id={self.id}, nickname={self.nickname}, amount={self.amount}, comment={self.comment}, watcher_id={self.watcher_id})"


@dataclass
class Follow:
    nickname: str
    repeat: bool
    variation_id: str

    def __str__(self):
        return f"Follow(nickname={self.nickname})"

    def __repr__(self):
        return f"Follow(nickname={self.nickname})"


@dataclass
class Subscribe:
    username: str
    months: int
    message: str
    method: str
    repeat: bool
    variation_id: str

    def __str__(self):
        return f"Subscribe(username={self.username}, months={self.months}, message={self.message}, method={self.method})"

    def __repr__(self):
        return f"Subscribe(username={self.username}, months={self.months}, message={self.message}, method={self.method})"


@dataclass
class Hosting:
    username: str
    viewers: int
    repeat: bool
    variation_id: str

    def __str__(self):
        return f"Hosting(username={self.username}, viewers={self.viewers})"

    def __repr__(self):
        return f"Hosting(username={self.username}, viewers={self.viewers})"


@dataclass
class Cheer:
    nickname: str
    amount: int
    comment: str
    repeat: bool
    variation_id: str

    def __str__(self):
        return f"Cheer(nickname={self.nickname}, amount={self.amount}, comment={self.comment})"

    def __repr__(self):
        return f"Cheer(nickname={self.nickname}, amount={self.amount}, comment={self.comment})"


@dataclass
class Sound:
    type: str
    volume: int
    url: str

    def __str__(self):
        return f"Sound(type={self.type}, volume={self.volume}, url={self.url})"

    def __repr__(self):
        return f"Sound(type={self.type}, volume={self.volume}, url={self.url})"
