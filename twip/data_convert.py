from models import Donate, Follow, Subscribe, Hosting, Cheer, Sound, Slotmachine


def convert_donate(data: list) -> Donate:
    data_type = data[0]
    data_value = data[1]
    donate = Donate(
        type=data_type,
        id=data_value.get("_id"),
        nickname=data_value.get("nickname"),
        amount=data_value.get("amount"),
        comment=data_value.get("comment"),
        watcher_id=data_value.get("watcher_id"),
        subbed=data_value.get("subbed"),
        repeat=data_value.get("repeat"),
        tts_type=data_value.get("ttstype"),
        tts_url=data_value.get("ttsurl"),
        effect=data_value.get("effect"),
        variation_id=data_value.get("variation_id"),
        slotmachine=Slotmachine()
    )

    if data_value.get("slotmachine_data"):
        slotmachine_data = data_value.get("slotmachine_data")
        donate.slotmachine = Slotmachine(
            items=slotmachine_data.get("items"),
            result=slotmachine_data.get("gotcha"),
            sound=slotmachine_data.get("config").get("sound"),
            point=slotmachine_data.get("config").get("point"),
            duration=slotmachine_data.get("config").get("duration")
        )

    return donate


def convert_follow(data: list) -> Follow:
    data_type = data[0]
    data_value = data[1]
    follow = Follow(
        nickname=data_value.get("nickname"),
        repeat=data_value.get("repeat"),
        variation_id=data_value.get("variation_id")
    )

    return follow


def convert_subscribe(data: list) -> Subscribe:
    data_type = data[0]
    data_value = data[1]
    subscribe = Subscribe(
        username=data_value.get("username"),
        months=data_value.get("months"),
        message=data_value.get("message"),
        method=data_value.get("method"),
        repeat=data_value.get("repeat"),
        variation_id=data_value.get("variation_id")
    )

    return subscribe


def convert_hosting(data: list) -> Hosting:
    data_value = data[1]
    hosting = Hosting(
        username=data_value.get("username"),
        viewers=data_value.get("viewers"),
        repeat=data_value.get("repeat"),
        variation_id=data_value.get("variation_id")
    )

    return hosting


def convert_cheer(data: list) -> Cheer:
    data_type = data[0]
    data_value = data[1]
    cheer = Cheer(
        nickname=data_value.get("nickname"),
        amount=data_value.get("amount"),
        comment=data_value.get("comment"),
        repeat=data_value.get("repeat"),
        variation_id=data_value.get("variation_id")
    )

    return cheer


def convert_sound(data: list) -> Sound:
    data_type = data[0]
    if len(data) == 2:
        data_value = data[1]
        sound = Sound(
            type=data_type[6:],
            volume=data_value.get("volume"),
            url=data_value.get("url")
        )
    else:
        sound = Sound(
            type=data_type[6:],
            volume=0,
            url=""
        )

    return sound
