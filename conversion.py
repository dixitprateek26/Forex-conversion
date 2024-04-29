import requests

from_currency = str(input("Enter the currency you'd like to convert from: ")).upper()                   #using upper to make them in a uniform format like usd becomes USD 
to_currency = str(input("Enter the currency you'd like to convert to: ")).upper() 

amount = float(input("Enter amount: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is equal to {response.json()['rates'] [to_currency]} {to_currency}")