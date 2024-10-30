from dataclasses import dataclass
from datetime import datetime


@dataclass
class AnnualEarnings:
    ticker: str
    fiscalDateEnding: datetime
    reportedEPS: float

    def pretty_print(self):
        print(f"{self.ticker}")
        print(f"\tFiscal date ending: {self.fiscalDateEnding}")
        print(f"\tReported EPS: {self.reportedEPS}")


@dataclass
class QuarterlyEarnings():
    ticker: str
    fiscalDateEnding: datetime
    reportedEPS: float
    reportedDate: datetime
    estimatedEPS: float
    surprise: float
    surprisePercentage: float
    reportTime: str

    def pretty_print(self):
        print(f"{self.ticker}")
        print(f"\tFiscal date ending: {self.fiscalDateEnding}")
        print(f"\tReported date: {self.reportedDate}")
        print(f"\tReported EPS: {self.reportedEPS}")
        print(f"\tEstimated EPS: {self.estimatedEPS}")
        print(f"\tSurprise: {self.surprise}")
        print(f"\tSurprise percentage: {self.surprisePercentage}")
        print(f"\tReport time: {self.reportTime}")
