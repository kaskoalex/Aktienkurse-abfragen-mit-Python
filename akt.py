import yfinance, jinja2, json


# Microsoft, AMD, Apple, RWE
symbols = ['MSF.DE']#, 'AMD.DE', 'APC.DE', 'RWE.DE']
stock_data = {}

for symbol in symbols:
  print(f'Daten für {symbol} werden abgefragt...')
  stock = yfinance.Ticker(symbol)
  info = stock.info

  # Aktieninformationen als Dictionary
  data = {
      'Aktueller Preis': info['regularMarketPrice'],
      #'52-Wochen-Hoch': info['fiftyTwoWeekHigh'],
      #'52-Wochen-Tief': info['fiftyTwoWeekLow'],
      #'Unternehmenswert / EBITDA': info['enterpriseToEbitda'],
      #'Durchschnittliche Dividendenrendite über 5 Jahre': info['fiveYearAvgDividendYield'],
      #'Eigenkapitalrendite': info['returnOnEquity'],
      #'Schulden / Equity (gesamt) (mrq)': info['debtToEquity']
  }
  stock_data[symbol] = data


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))

jinja_var = {
    'employes': [{
        'name': symbol,
        'office': data
    }, {
        'name': 'Bob',
        'office': 'Germany'
    }]
}

template = jinja_env.get_template('akt.html')
print(template.render(jinja_var))