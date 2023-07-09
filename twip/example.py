from twip import Twip, Donate, Follow, Subscribe, Hosting, Cheer, Sound, Slotmachine


class MyTwip(Twip):
    def on_ready(self):
        print("Twip is ready!")

    def on_donate(self, donate: Donate):
        print(donate)

    def on_follow(self, follow: Follow):
        print(follow)

    def on_subscribe(self, subscribe: Subscribe):
        print(subscribe)

    def on_hosting(self, hosting: Hosting):
        print(hosting)

    def on_cheer(self, cheer: Cheer):
        print(cheer)

    def on_sound(self, sound: Sound):
        print(sound)


if __name__ == "__main__":
    myTwip = MyTwip()
    myTwip.run("your alert box id", "your twip api token")
