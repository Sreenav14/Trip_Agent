import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        # Ensure base URL doesn't end with a trailing slash so constructing
        # the request URL is predictable.
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest"

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert the amount from one currency to another using ExchangeRate-API.

        Args:
            amount: numeric amount to convert
            from_currency: ISO currency code for source (e.g. "USD")
            to_currency: ISO currency code for target (e.g. "EUR")

        Returns:
            Converted amount in target currency.
        """
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("API call failed:", response.text)
        data = response.json()
        rates = data.get("conversion_rates", {})
        if to_currency not in rates:
            raise ValueError(f"Unsupported currency: {to_currency}")
        return amount * rates[to_currency]