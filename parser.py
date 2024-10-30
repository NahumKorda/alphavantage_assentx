import pickle
import inspect


def parse_company_overview():

    with open("/Users/nahumkorda/code/resources/assentx/company_overview.pkl", "rb") as input_file:
        overview_index = pickle.load(input_file)

    for ticker, company_overviews in overview_index.items():
        for timestamp, company_overview in company_overviews.items():
            for attribute in inspect.getmembers(company_overview):
                if not attribute[0].startswith('_'):
                    if not inspect.ismethod(attribute[1]):
                        print(attribute[0])
        break


def parse_annual_earnings():
    with open("/Users/nahumkorda/code/resources/assentx/annual_earnings.pkl", "rb") as input_file:
        earning_index = pickle.load(input_file)

    for ticker, earnings in earning_index.items():
        for timestamp, annual_earnings in earnings.items():
            for annual_earning in annual_earnings:
                for attribute in inspect.getmembers(annual_earning):
                    if not attribute[0].startswith('_'):
                        if not inspect.ismethod(attribute[1]):
                            print(attribute[0])
                break
            break
        break


def parse_quarterly_earnings():
    with open("/Users/nahumkorda/code/resources/assentx/quarterly_earnings.pkl", "rb") as input_file:
        earning_index = pickle.load(input_file)

    for ticker, earnings in earning_index.items():
        for timestamp, quarterly_earnings in earnings.items():
            for quarterly_earning in quarterly_earnings:
                for attribute in inspect.getmembers(quarterly_earning):
                    if not attribute[0].startswith('_'):
                        if not inspect.ismethod(attribute[1]):
                            print(attribute[0])
                break
            break
        break


def parse_news_articles():
    with open("/Users/nahumkorda/code/resources/assentx/news.pkl", "rb") as input_file:
        news_index = pickle.load(input_file)

    for ticker, news in news_index.items():
        for timestamp, news_articles in news.items():
            for news_article in news_articles:
                for attribute in inspect.getmembers(news_article):
                    if not attribute[0].startswith('_'):
                        if not inspect.ismethod(attribute[1]):
                            print(attribute[0])
                break
            break
        break


if __name__ == '__main__':

    # parse_company_overview()
    # parse_annual_earnings()
    # parse_quarterly_earnings()
    parse_news_articles()
