# API Website: https://exchangerate.host/#/docs
# Cryptocurrencies URL: https://api.exchangerate.host/cryptocurrencies
import requests

orig_currency_symbols = {}
currency_symbols = {}
symbol_currencies = {}

def get_available_currencies():
  url = 'https://api.exchangerate.host/symbols'
  response = requests.get(url)
  data = response.json()["symbols"]
  for code in data:
    orig_currency_symbols[code] = data[code]["description"]
    currency_symbols[code.upper()] = data[code]["description"].upper()
  
  with open("currencies.txt", "w") as f:
    for x in orig_currency_symbols:
      f.write(x + " : " + orig_currency_symbols[x] + "\n")


get_available_currencies()


def get_conversion_rate(cur1, cur2):
  exchange_url = f'https://api.exchangerate.host/convert?from={cur1}&to={cur2}'

  response = requests.get(exchange_url)
  # print(response.json())
  date = response.json()["date"]
  rate = response.json()["result"]

  print("Date:", date)
  print("Exchange Rate:", rate)
  print(f"\n 1 {cur1} = {rate} {cur2}")
  
  return [date, rate]


def welcome_screen():
  print("Welcome to Currency Exchange!\nPlease input the symbols for 2 currencies which you would like to exchange:")
  

welcome_screen()


def get_input():
  invalid_input = True
  while invalid_input:
    try:
      code = ""
      currency = input("\nEnter a currency symbol (3-digits) or the exact name of the currency: \n").upper()
      if currency in list(currency_symbols.keys()):
        code = currency
      elif currency in list(currency_symbols.values()):
        for k, v in currency_symbols.items(): 
          if v == currency:
            code = k
      else:
        raise
      invalid_input = False
    except:
      print("Invalid input. Try again.")

  return code

# get input for symbols
cur1, cur2 = get_input(), get_input()

print()
get_conversion_rate(cur1, cur2)
# get_conversion_rate("USD", "GBP")

'''
# Test
exchange_url = f'https://api.exchangerate.host/convert?from=USD&to=GBP'

response = requests.get(exchange_url)
date = response.json()["date"]
rate = response.json()["result"]
print(date, rate)
'''

"""
# Find exchange rate data from a past date
url = 'https://api.exchangerate.host/2020-04-04'
response = requests.get(url)
data = response.json()
# print(data)
"""