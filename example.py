import twip

Twip = twip.Twip()

@Twip.event
def on_donate(ctx):
    print("=on_donate==============")
    print(f"id : {ctx.id}")
    print(f"nickname : {ctx.nickname}")
    print(f"amount : {ctx.amount}")
    print(f"comment : {ctx.comment}")
    print(f"watcher_id : {ctx.watcher_id}")
    print(f"subbed : {ctx.subbed}")
    print(f"repeat : {ctx.repeat}")
    print(f"ttstype : {ctx.tts_type}")
    print(f"ttsurl : {ctx.tts_url}")
    print(f"slotmachine.items : {ctx.slotmachine.items}")
    print(f"slotmachine.result : {ctx.slotmachine.result}")
    print(f"slotmachine.reward_id : {ctx.slotmachine.reward_id}")
    print(f"slotmachine.sound : {ctx.slotmachine.sound}")
    print(f"slotmachine.point : {ctx.slotmachine.point}")
    print(f"slotmachine.duration : {ctx.slotmachine.duration}")
    print(f"effect : {ctx.effect}")
    print(f"variation_id : {ctx.variation_id}")

@Twip.event
def on_subscribe(ctx):
    print("=on_subscribe===========")
    print(f"username : {ctx.username}")
    print(f"months : {ctx.months}")
    print(f"message : {ctx.message}")
    print(f"method : {ctx.method}")
    print(f"repeat : {ctx.repeat}")
    print(f"variation_id : {ctx.variation_id}")
    
@Twip.event
def on_hosting(ctx):
    print("=on_hosting=============")
    print(f"username : {ctx.username}")
    print(f"viewers : {ctx.viewers}")
    print(f"repeat : {ctx.repeat}")
    print(f"variation_id : {ctx.variation_id}")
    
@Twip.event
def on_cheer(ctx):
    print("=on_cheer===============")
    print(f"nickname : {ctx.nickname}")
    print(f"amount : {ctx.amount}")
    print(f"comment : {ctx.comment}")
    print(f"repeat : {ctx.repeat}")
    print(f"variation_id : {ctx.variation_id}")
    
@Twip.event
def on_follow(ctx):
    print("=on_follow==============")
    print(f"nickname : {ctx.nickname}")
    print(f"repeat : {ctx.repeat}")
    print(f"variation_id : {ctx.variation_id}")

@Twip.event
def on_sound(ctx):
    print("=on_sound===============")
    print(f"type : {ctx.type}")
    print(f"url : {ctx.url}")
    print(f"volume : {ctx.volume}")

Twip.run("your alert box id")