from dataclasses import dataclass
from datetime import datetime


@dataclass
class CompanyOverview:
    symbol: str
    asset_type: str
    name: str
    description: str
    cik: str
    exchange: str
    currency: str
    country: str
    sector: str
    industry: str
    address: str
    official_site: str
    fiscal_year_end: str
    latest_quarter: datetime
    market_capitalization: float
    ebitda: float
    pe_ratio: float
    peg_ratio: float
    book_value: float
    dividend_per_share: float
    dividend_yield: float
    eps: float
    revenue_per_share_ttm: float
    profit_margin: float
    operating_margin_ttm: float
    return_on_assets_ttm: float
    return_on_equity_ttm: float
    revenue_ttm: float
    gross_profit_ttm: float
    diluted_eps_ttm: float
    quarterly_earnings_growth_yoy: float
    quarterly_revenue_growth_yoy: float
    analyst_target_price: str
    analyst_rating_strong_buy: float
    analyst_rating_buy: float
    analyst_rating_hold: float
    analyst_rating_sell: float
    analyst_rating_strong_sell: float
    trailing_pe: float
    forward_pe: float
    price_to_sales_ratio_ttm: float
    price_to_book_ratio: float
    ev_to_revenue: float
    ev_to_ebitda: float
    beta: float
    fifty_two_week_high: float
    fifty_two_week_low: float
    fifty_day_moving_average: float
    two_hundred_day_moving_average: float
    shares_outstanding: float
    dividend_date: datetime | None
    ex_dividend_date: datetime | None
