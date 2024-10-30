from datetime import datetime
import requests
from tqdm import tqdm
from companyoverview import CompanyOverview
from earnings import AnnualEarnings, QuarterlyEarnings
from functions import Functions
from newsarticle import NewsArticle


class Retriever:

    def __init__(self):
        self.__base_url = "https://www.alphavantage.co/query?"
        self.__long_date_time_format = r"%Y%m%dT%H%M%S"
        self.__short_date_time_format = r"%Y-%m-%d"
        self.__count = 0

    def retrieve(self, function: Functions, tickers: list[str], api_key: str):

        retval = dict()

        for ticker in tqdm(tickers, total=len(tickers)):

            self.__count += 1

            if function == Functions.NEWS:
                url = f"{self.__base_url}function={function.value}&tickers={ticker}&apikey={api_key}&limit=1000"
                response = requests.get(url)
                feed = response.json()["feed"]
                news_articles = self.__parse_news_feed(feed, ticker)
                retval[ticker] = news_articles

            elif function == Functions.OVERVIEW:
                url = f"{self.__base_url}function={function.value}&symbol={ticker}&apikey={api_key}"
                response = requests.get(url)
                retval[ticker] = self.__parse_company_overview(response.json())

            elif function == Functions.EARNINGS:
                url = f"{self.__base_url}function={function.value}&symbol={ticker}&apikey={api_key}"
                response = requests.get(url)
                annual_earnings = self.__parse_annual_earnings(response.json()["annualEarnings"], ticker)
                quarterly_earnings = self.__parse_quarterly_earnings(response.json()["quarterlyEarnings"], ticker)
                retval[ticker] = {"annualEarnings": annual_earnings, "quarterlyEarnings": quarterly_earnings}

        return retval

    def __parse_news_feed(self, feed: dict, ticker: str) -> dict[float, list[NewsArticle]]:

        retval = dict()

        for article in feed:
            title = article["title"]
            time_published = article["time_published"]
            date = datetime.strptime(time_published, self.__long_date_time_format)
            source = article["source"]
            sentiment = self.__extract_sentiment(article["ticker_sentiment"], ticker)
            if sentiment is not None:
                news_article = NewsArticle(ticker, date, title, source, sentiment)
                timestamp = datetime.timestamp(date)
                if timestamp in retval.keys():
                    retval[timestamp].append(news_article)
                else:
                    retval[timestamp] = [news_article]

        return retval

    @staticmethod
    def __extract_sentiment(ticker_sentiment: list[dict], ticker: str) -> float | None:
        for item in ticker_sentiment:
            if item["ticker"] == ticker:
                return item["ticker_sentiment_score"]
        return None

    def __parse_company_overview(self, overview: dict[str]) -> dict[float, CompanyOverview]:

        retval = dict()

        symbol = overview["Symbol"]
        asset_type = overview["AssetType"]
        name = overview["Name"]
        description = overview["Description"]
        cik = overview["CIK"]
        exchange = overview["Exchange"]
        currency = overview["Currency"]
        country = overview["Country"]
        sector = overview["Sector"]
        industry = overview["Industry"]
        address = overview["Address"]
        official_site = overview["OfficialSite"]
        fiscal_year_end = overview["FiscalYearEnd"]
        latest_quarter = overview["LatestQuarter"]
        latest_quarter_date = datetime.strptime(latest_quarter, self.__short_date_time_format)
        timestamp = datetime.timestamp(latest_quarter_date)
        market_capitalization = overview["MarketCapitalization"]
        ebitda = overview["EBITDA"]
        pe_ratio = overview["PERatio"]
        peg_ratio = overview["PEGRatio"]
        book_value = overview["BookValue"]
        dividend_per_share = overview["DividendPerShare"]
        dividend_yield = overview["DividendYield"]
        eps = overview["EPS"]
        revenue_per_share_ttm = overview["RevenuePerShareTTM"]
        profit_margin = overview["ProfitMargin"]
        operating_margin_ttm = overview["OperatingMarginTTM"]
        return_on_assets_ttm = overview["ReturnOnAssetsTTM"]
        return_on_equity_ttm = overview["ReturnOnEquityTTM"]
        revenue_ttm = overview["RevenueTTM"]
        gross_profit_ttm = overview["GrossProfitTTM"]
        diluted_eps_ttm = overview["DilutedEPSTTM"]
        quarterly_earnings_growth_yoy = overview["QuarterlyEarningsGrowthYOY"]
        quarterly_revenue_growth_yoy = overview["QuarterlyRevenueGrowthYOY"]
        analyst_target_price = overview["AnalystTargetPrice"]
        analyst_rating_strong_buy = overview["AnalystRatingStrongBuy"]
        analyst_rating_buy = overview["AnalystRatingBuy"]
        analyst_rating_hold = overview["AnalystRatingHold"]
        analyst_rating_sell = overview["AnalystRatingSell"]
        analyst_rating_strong_sell = overview["AnalystRatingStrongSell"]
        trailing_pe = overview["TrailingPE"]
        forward_pe = overview["ForwardPE"]
        price_to_sales_ratio_ttm = overview["PriceToSalesRatioTTM"]
        price_to_book_ratio = overview["PriceToBookRatio"]
        ev_to_revenue = overview["EVToRevenue"]
        ev_to_ebitda = overview["EVToEBITDA"]
        beta = overview["Beta"]
        fifty_two_week_high = overview["52WeekHigh"]
        fifty_two_week_low = overview["52WeekLow"]
        fifty_day_moving_average = overview["50DayMovingAverage"]
        two_hundred_day_moving_average = overview["200DayMovingAverage"]
        shares_outstanding = overview["SharesOutstanding"]
        dividend_date = overview["DividendDate"]
        if dividend_date is not None and dividend_date != 'None':
            dividend_date_date = datetime.strptime(dividend_date, self.__short_date_time_format)
        else:
            dividend_date_date = None
        ex_dividend_date = overview["ExDividendDate"]
        if ex_dividend_date is not None and ex_dividend_date != 'None':
            ex_dividend_date_date = datetime.strptime(ex_dividend_date, self.__short_date_time_format)
        else:
            ex_dividend_date_date = None

        company_overview = CompanyOverview(
            symbol=symbol,
            asset_type=asset_type,
            name=name,
            description=description,
            cik=cik,
            exchange=exchange,
            currency=currency,
            country=country,
            sector=sector,
            industry=industry,
            address=address,
            official_site=official_site,
            fiscal_year_end=fiscal_year_end,
            latest_quarter=latest_quarter_date,
            market_capitalization=market_capitalization,
            ebitda=ebitda,
            pe_ratio=pe_ratio,
            peg_ratio=peg_ratio,
            book_value=book_value,
            dividend_per_share=dividend_per_share,
            dividend_yield=dividend_yield,
            eps=eps,
            revenue_per_share_ttm=revenue_per_share_ttm,
            profit_margin=profit_margin,
            operating_margin_ttm=operating_margin_ttm,
            return_on_assets_ttm=return_on_assets_ttm,
            return_on_equity_ttm=return_on_equity_ttm,
            revenue_ttm=revenue_ttm,
            gross_profit_ttm=gross_profit_ttm,
            diluted_eps_ttm=diluted_eps_ttm,
            quarterly_earnings_growth_yoy=quarterly_earnings_growth_yoy,
            quarterly_revenue_growth_yoy=quarterly_revenue_growth_yoy,
            analyst_target_price=analyst_target_price,
            analyst_rating_strong_buy=analyst_rating_strong_buy,
            analyst_rating_buy=analyst_rating_buy,
            analyst_rating_hold=analyst_rating_hold,
            analyst_rating_sell=analyst_rating_sell,
            analyst_rating_strong_sell=analyst_rating_strong_sell,
            trailing_pe=trailing_pe,
            forward_pe=forward_pe,
            price_to_sales_ratio_ttm=price_to_sales_ratio_ttm,
            price_to_book_ratio=price_to_book_ratio,
            ev_to_revenue=ev_to_revenue,
            ev_to_ebitda=ev_to_ebitda,
            beta=beta,
            fifty_two_week_high=fifty_two_week_high,
            fifty_two_week_low=fifty_two_week_low,
            fifty_day_moving_average=fifty_day_moving_average,
            two_hundred_day_moving_average=two_hundred_day_moving_average,
            shares_outstanding=shares_outstanding,
            dividend_date=dividend_date_date,
            ex_dividend_date=ex_dividend_date_date
        )

        retval[timestamp] = company_overview

        return retval

    def __parse_annual_earnings(self, annual_earnings: list[dict], ticker: str) -> dict[float, list[AnnualEarnings]]:

        retval = dict()

        for earning in annual_earnings:
            fiscal_date_ending = earning["fiscalDateEnding"]
            date = datetime.strptime(fiscal_date_ending, self.__short_date_time_format)
            timestamp = datetime.timestamp(date)
            reported_eps = earning["reportedEPS"]
            if timestamp in retval.keys():
                retval[timestamp].append(AnnualEarnings(ticker, date, reported_eps))
            else:
                retval[timestamp] = [AnnualEarnings(ticker, date, reported_eps)]

        return retval

    def __parse_quarterly_earnings(self, quarterly_earnings: list[dict], ticker: str) -> dict[float, list[QuarterlyEarnings]]:

        retval = dict()

        for earning in quarterly_earnings:
            fiscal_date_ending = earning["fiscalDateEnding"]
            fiscal_date_date = datetime.strptime(fiscal_date_ending, self.__short_date_time_format)
            timestamp = datetime.timestamp(fiscal_date_date)
            reported_eps = earning["reportedEPS"]
            reported_date = earning["reportedDate"]
            reported_date_date = datetime.strptime(reported_date, self.__short_date_time_format)
            estimated_eps = earning["estimatedEPS"]
            surprise = earning["surprise"]
            surprise_percentage = earning["surprisePercentage"]
            report_time = earning["reportTime"]
            quarterly_earning = QuarterlyEarnings(ticker=ticker,
                                                  fiscalDateEnding=fiscal_date_date,
                                                  reportedEPS=reported_eps,
                                                  reportedDate=reported_date_date,
                                                  estimatedEPS=estimated_eps,
                                                  surprise=surprise,
                                                  surprisePercentage=surprise_percentage,
                                                  reportTime=report_time)
            if timestamp in retval.keys():
                retval[timestamp].append(quarterly_earning)
            else:
                retval[timestamp] = [quarterly_earning]

        return retval

    def get_count(self):
        return self .__count
