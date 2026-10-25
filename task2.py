import re
from typing import Callable, Iterator

# A number counts only when it stands alone: whitespace (or start/end of text)
# on both sides. So "abc123" or "2024-01-15" are ignored.
NUMBER_PATTERN = re.compile(r'(?<!\S)\d+(?:\.\d+)?(?!\S)')


def generator_numbers(text: str) -> Iterator[float]:
    for match in NUMBER_PATTERN.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
