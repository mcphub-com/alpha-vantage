import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/alphavantage/api/alpha-vantage'

mcp = FastMCP('alpha-vantage')

@mcp.tool()
def time_series_intraday(interval: Annotated[str, Field(description='Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min')],
                         function: Annotated[str, Field(description='The time series of your choice.')],
                         symbol: Annotated[str, Field(description='The equity of your choice.')],
                         datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None,
                         output_size: Annotated[Union[str, None], Field(description='Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.')] = None) -> dict: 
    '''This API returns intraday time series (timestamp, open, high, low, close, volume) of the equity specified.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'interval': interval,
        'function': function,
        'symbol': symbol,
        'datatype': datatype,
        'output_size': output_size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_daily_adjusted(function: Annotated[str, Field(description='The time series of your choice.')],
                               symbol: Annotated[str, Field(description='The name of the equity of your choice.')],
                               outputsize: Annotated[Union[str, None], Field(description='Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The "compact" option is recommended if you would like to reduce the data size of each API call.')] = None,
                               datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns daily time series (date, daily open, daily high, daily low, daily close, daily volume, daily adjusted close, and split/dividend events) of the global equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
        'outputsize': outputsize,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_daily(function: Annotated[str, Field(description='The time series of your choice.')],
                      symbol: Annotated[str, Field(description='The name of the equity of your choice.')],
                      outputsize: Annotated[Union[str, None], Field(description='Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data. The \\"compact\\" option is recommended if you would like to reduce the data size of each API call.')] = None,
                      datatype: Annotated[Union[str, None], Field(description='Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
        'outputsize': outputsize,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_weekly_adjusted(function: Annotated[str, Field(description='The time series of your choice.')],
                                symbol: Annotated[str, Field(description='The equity of your choice.')],
                                datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns weekly adjusted time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly adjusted close, weekly volume, weekly dividend) of the global equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_weekly(function: Annotated[str, Field(description='The time series of your choice.')],
                       symbol: Annotated[Union[str, None], Field(description='The name of the equity of your choice.')] = None,
                       datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns weekly time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly volume) of the global equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_monthly_adjusted(symbol: Annotated[str, Field(description='The equity of your choice.')],
                                 function: Annotated[str, Field(description='The time series of your choice.')],
                                 datatype: Annotated[Union[str, None], Field(description='Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns monthly adjusted time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend) of the equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'function': function,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_series_monthly(symbol: Annotated[str, Field(description='The equity of your choice.')],
                        function: Annotated[str, Field(description='The time series of your choice.')],
                        datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns monthly time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly volume) of the global equity specified, covering 20+ years of historical data.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'function': function,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def quote_endpoint(function: Annotated[str, Field(description='The API function of your choice.')],
                   symbol: Annotated[str, Field(description='The equity of your choice.')],
                   datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''A lightweight alternative to the time series APIs, this service returns the price and volume information for a security of your choice.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_endpoint(keywords: Annotated[str, Field(description='A text string of your choice.')],
                    function: Annotated[str, Field(description='The API function of your choice.')],
                    datatype: Annotated[Union[str, None], Field(description='Strings json and csv are accepted with the following specifications: json returns the search results in JSON format; csv returns the search results as a CSV (comma separated value) file.')] = None) -> dict: 
    '''Looking for some specific symbols or companies? We've got you covered! The Search Endpoint returns the best-matching symbols and market information based on keywords of your choice. The search results also contain match scores that provide you with the full flexibility to develop your own search and filtering logic.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keywords': keywords,
        'function': function,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def customizable_endpoint(function: Annotated[str, Field(description='The function of you choice (This is required for all API calls)')],
                          symbol: Annotated[Union[str, None], Field(description='Any additional optional parameters may be added. Some functions have multiple required parameters, check the documentation for more information.')] = None) -> dict: 
    '''Build your own query from the [documentation, located here.](https://www.alphavantage.co/documentation/) There is one master catch-all endpoint, but the additional following "endpoints" give you samples of how to build URLs.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fx_intraday(function: Annotated[str, Field(description='The time series of your choice.')],
                interval: Annotated[str, Field(description='Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min')],
                to_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: to_symbol=USD')],
                from_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: from_symbol=EUR')],
                datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None,
                outputsize: Annotated[Union[str, None], Field(description='By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.')] = None) -> dict: 
    '''This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'interval': interval,
        'to_symbol': to_symbol,
        'from_symbol': from_symbol,
        'datatype': datatype,
        'outputsize': outputsize,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fx_weekly(function: Annotated[str, Field(description='The time series of your choice.')],
              from_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: from_symbol=EUR')],
              to_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: to_symbol=USD')],
              datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the weekly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime. The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'from_symbol': from_symbol,
        'to_symbol': to_symbol,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fx_daily(from_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: from_symbol=EUR')],
             function: Annotated[str, Field(description='The time series of your choice.')],
             to_symbol: Annotated[Union[str, None], Field(description='A three-letter symbol from the forex currency list. For example: to_symbol=USD')] = None,
             outputsize: Annotated[Union[str, None], Field(description='By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the daily time series; full returns the full-length daily time series. The "compact" option is recommended if you would like to reduce the data size of each API call.')] = None,
             datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from_symbol': from_symbol,
        'function': function,
        'to_symbol': to_symbol,
        'outputsize': outputsize,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def currency_exchange_rate(to_currency: Annotated[str, Field(description='The currency you want to convert to')],
                           function: Annotated[str, Field(description='The function of your choice. (In this case CURRENCY_EXCHANGE_RATE)')],
                           from_currency: Annotated[str, Field(description='The currency you want to convert')]) -> dict: 
    '''This API returns the realtime exchange rate for any pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD). Data returned for physical currency (Forex) pairs also include realtime bid and ask prices.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'to_currency': to_currency,
        'function': function,
        'from_currency': from_currency,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fx_monthly(from_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: from_symbol=EUR')],
               to_symbol: Annotated[str, Field(description='A three-letter symbol from the forex currency list. For example: from_symbol=USD')],
               function: Annotated[str, Field(description='The time series of your choice.')],
               datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime. The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from_symbol': from_symbol,
        'to_symbol': to_symbol,
        'function': function,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def digital_currency_weekly(market: Annotated[str, Field(description='The exchange market of your choice. It can be any of the market in the market list. For example: market=CNY.')],
                            function: Annotated[str, Field(description='The time series of your choice.')],
                            symbol: Annotated[str, Field(description='The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.')]) -> dict: 
    '''This API returns the weekly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'function': function,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def digital_currency_daily(market: Annotated[str, Field(description='The exchange market of your choice. It can be any of the market in the market list. For example: market=CNY.')],
                           symbol: Annotated[str, Field(description='The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.')],
                           function: Annotated[str, Field(description='The time series of your choice.')]) -> dict: 
    '''This API returns the daily historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'symbol': symbol,
        'function': function,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def digital_currency_monthly(function: Annotated[str, Field(description='The time series of your choice.')],
                             market: Annotated[str, Field(description='The exchange market of your choice. It can be any of the market in the market list. For example: market=CNY.')],
                             symbol: Annotated[Union[str, None], Field(description='The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.')] = None) -> dict: 
    '''This API returns the monthly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., CNY/Chinese Yuan), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'market': market,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def technical_indicators(time_period: Annotated[Union[int, float], Field(description='Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., time_period=60, time_period=200) Default: 60')],
                         interval: Annotated[str, Field(description='Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly')],
                         series_type: Annotated[str, Field(description='The desired price type in the time series. Four types are supported: close, open, high, low')],
                         function: Annotated[str, Field(description='The technical indicator of your choice. In this case, function=SMA')],
                         symbol: Annotated[str, Field(description='The name of the security of your choice. For example: symbol=MSFT')],
                         datatype: Annotated[Union[str, None], Field(description='By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.')] = None) -> dict: 
    '''For more information on how to build all the different technical indicators there are, [please visit here](https://www.alphavantage.co/documentation/#technical-indicators).'''
    url = 'https://alpha-vantage.p.rapidapi.com/query'
    headers = {'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'time_period': time_period,
        'interval': interval,
        'series_type': series_type,
        'function': function,
        'symbol': symbol,
        'datatype': datatype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
