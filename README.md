# Indian Stock Exchange

## It accepts a stock symbol and returns with the Live Stock price.

If you have list of stocks which you want to monitor continously you can write a script to iteratively go through the list and send a request to my API.

To avoid abusive usage of the API I have removed the URL's and stored it away in a .env file.

This API has an endpoit `/stock_price/{symbol}` which accepts the symbol as a parameter and returns the data. Sometimes the Symbol is not updated at the provider end, at that time it will return with the scrip number by getting it from BSE which you can feed it again to the API.

Sample Data:

```
{
    "symbol": "TATAMOTORS",
    "open": 417.35,
    "day_high": 427.8,
    "day_low": 413.1,
    "previous_close": 416.7,
    "last_trading_price": 421.6,
    "lowPriceRange": 379.45,
    "highPriceRange": 463.75,
    "volume": 50949198,
    "day_change": 4.900000000000034,
    "day_change_percent": 1.1759059275258061,
    "totalBuyQty": 52144,
    "totalSellQty": 0
}
```
Contact me at muktheeswaran.m@gmail.com, if you want more information about the API.
