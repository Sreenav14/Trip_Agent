
class Calculator:

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers and return the product."""
        return a * b

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers and return the sum."""
        return a + b

    @staticmethod
    def calculate_total(*x: float) -> float:
        """Calculate the total (sum) of the given numbers."""
        return sum(x)

    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """Calculate per-day budget from total and number of days."""
        return total / days if days > 0 else 0.0