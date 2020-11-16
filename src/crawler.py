import os
import time
from dotenv import load_dotenv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
load_dotenv()


class Crawler:
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "database/database.csv")
    SLEEP = 1.0

    @classmethod
    def run(cls):
        df = pd.read_csv(cls.DATABASE_PATH)
        lottery_list = []

        html = urlopen(os.environ["URL"])
        time.sleep(cls.SLEEP)
        bs = BeautifulSoup(html, "html.parser")
        ul = bs.find("ul", {"id": "itemList"})
        if ul is None:
            print("No lottery")
            return lottery_list
        lis = ul.find_all("li")
        print("{} lotteries were detected.".format(len(lis)))
        for li in lis:
            lottery = {}
            p = li.find("p")
            a = li.find("a")
            lottery = {
                "name": p.text,
                "url": a["href"]
            }
            if not lottery.get("url") in df["url"].values.tolist():
                lottery_list.append(lottery)
                df = df.append(lottery, ignore_index=True)
        df.to_csv(cls.DATABASE_PATH, index=False)
        return lottery_list
