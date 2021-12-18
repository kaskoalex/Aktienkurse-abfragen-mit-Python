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

workbook = openpyxl.Workbook()
sheet_dictionary = workbook.active
sheet_dictionary.title = 'Daten als Dictionary'

header = ['Symbol',	'Aktueller Preis',	'52-Wochen-Hoch', '52-Wochen-Tief',	'Unternehmenswert / EBITDA',	'Durchschnittliche Dividendenrendite über 5 Jahre',	'Eigenkapitalrendite',	'Schulden / Equity (gesamt) (mrq)']
sheet_dictionary.append(header)

for key, value in stock_data.items():
  line = []
  line.append(key)
  line.extend(list(value.values()))
  sheet_dictionary.append(line)

workbook.save('test.xlsx')

print('Fertig!')