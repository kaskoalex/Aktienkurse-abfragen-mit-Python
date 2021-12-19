#%pip install yfinance openpyxl

import yfinance, json, openpyxl

# Microsoft, AMD, Apple, RWE
symbols = ['MSF.DE', 'AMD.DE', 'APC.DE', 'RWE.DE']
stock_data = {}


for symbol in symbols:
  print(f'Daten für {symbol} werden abgefragt...')
  stock = yfinance.Ticker(symbol)
  info = stock.info

  # Aktieninformationen als Dictionary
  data = {
      'Aktueller Preis': info['regularMarketPrice'],
      '52-Wochen-Hoch': info['fiftyTwoWeekHigh'],
      '52-Wochen-Tief': info['fiftyTwoWeekLow'],
      'Unternehmenswert / EBITDA': info['enterpriseToEbitda'],
      'Durchschnittliche Dividendenrendite über 5 Jahre': info['fiveYearAvgDividendYield'],
      'Eigenkapitalrendite': info['returnOnEquity'],
      'Schulden / Equity (gesamt) (mrq)': info['debtToEquity']
  }
  stock_data[symbol] = data

print(json.dumps(stock_data, indent=4, ensure_ascii=False))
print('Daten in Excel Datei schreiben...')
