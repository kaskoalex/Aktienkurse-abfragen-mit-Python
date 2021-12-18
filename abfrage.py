#%pip install yfinance
import yfinance, json

symbol = "MSF.DE"
microsoft=yfinance.Ticker(symbol)
daten = microsoft.info
print(microsoft)
print(json.dumps(daten, indent=4))
print(f'{daten["regularMarketPrice"]} {daten["currency"]}')
print(microsoft.history(period='1d',interval='1m'))