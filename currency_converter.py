import requests
import sys

try:
    import requests
except ImportError:
    print("The 'requests' module is not installed. Please install it by running 'pip install requests'.")
    sys.exit(1)

def get_exchange_rate(base_currency, converted_currency, value):
    try:
        api_response = requests.get(
            f'https://frankfurter.app/latest?from={base_currency}&to={converted_currency}&amount={value}'
        )
        api_response.raise_for_status()  # Raise an exception for HTTP errors
        exchange_rates = api_response.json()
        return exchange_rates['rates'][converted_currency]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None
    except KeyError:
        print("Invalid currency code.")
        return None

def main():
    base_currency = input('Enter currency you want to convert from: ').upper()
    converted_currency = input('Enter the currency you are converting to: ').upper()
    try:
        value = float(input('How much are you converting? '))
    except ValueError:
        print("Please enter a valid number for the amount.")
        return

    exchange_rate = get_exchange_rate(base_currency, converted_currency, value)
    if exchange_rate is not None:
        print(f'{value} {base_currency} is {exchange_rate} {converted_currency}')

if __name__ == "__main__":
    main()
