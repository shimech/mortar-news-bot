class Message:
    new_lottery_message = "<!channel> 【MORTAR TOKYO】" + "\n"
    new_lottery_message += "{}" + "\n"
    new_lottery_message += "の抽選販売が開始しました！" + "\n"
    new_lottery_message += "{}" + "\n"

    @classmethod
    def make_message(cls, lottery):
        return cls.new_lottery_message.format(lottery.get("name"), lottery.get("url"))
