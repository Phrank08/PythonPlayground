import requests #   this code doesn't work because the pip and request module have not been installed

base_currency = input(str('Enter currency you want to convert from: ')).upper()

converted_currency = input(str('Enter the currency you are converting to: ')).upper()

value = input(float('How much are you converting? '))

api_response = requests.get(
    f'https://frankfurter.app/latest?from={base_currency}&to={converted_currency}&amount={value}'
)
exchange_rates = api_response.json()

print(f'{value} {base_currency} is {exchange_rates['rates'][converted_currency]} {converted_currency}')