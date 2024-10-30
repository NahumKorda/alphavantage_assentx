from dataclasses import dataclass
from datetime import datetime


@dataclass
class NewsArticle:
    ticker: str
    date: datetime
    title: str
    source: str
    sentiment: float

    def pretty_print(self):
        print(f"{self.ticker}")
        print(f"\t{self.title}")
        print(f"\tsource: {self.source}")
        print(f"\tdate: {self.date}")
        print(f"\tsentiment: {self.sentiment}")
