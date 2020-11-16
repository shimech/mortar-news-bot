import os
from dotenv import load_dotenv
from argument_parser import ArgumentParser
from utils import Utils
from crawler import Crawler
from message import Message
from slack_bot import SlackBot


def main():
    load_dotenv()
    argument_parser = ArgumentParser()

    Utils.print_log("start bot")

    lottery_list = Crawler.run()

    if len(lottery_list) > 0:
        slack_bot = SlackBot(
            os.environ["CHANNEL"], os.environ["TEST_CHANNEL"], os.environ["SLACK_API_TOKEN"])
        for lottery in lottery_list:
            message = Message.make_message(lottery)
            slack_bot.post_message(
                message,
                is_test=argument_parser.arguments.test
            )

    Utils.print_log("stop bot")


if __name__ == "__main__":
    main()
