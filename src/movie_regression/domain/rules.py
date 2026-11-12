"""Domain rules: constants and pure functions that need no library."""

from datetime import datetime
from typing import Any

BUDGET = "USD_Production_Budget"
WORLDWIDE = "USD_Worldwide_Gross"
DOMESTIC = "USD_Domestic_Gross"
RELEASE_DATE = "Release_Date"
DECADE = "Decade"

MONEY_COLUMNS: tuple[str, ...] = (BUDGET, WORLDWIDE, DOMESTIC)
CHARS_TO_REMOVE: tuple[str, ...] = (",", "$")

DATA_COLLECTION_DATE = datetime(2018, 5, 1)
# Films released after this date had not reached the box office yet.

OLD_FILMS_BEFORE_YEAR = 1970
# Films of an earlier decade are the "old films" of the lecture.

YEARS_PER_DECADE = 10


# Any: the same floor division serves an int, a NumPy array and a pandas Index.
def to_decade(years: Any) -> Any:
    """Convert years to decades with floor division: 1992 and 1999 give 1990.

    Works on an int, a NumPy array or a pandas Index or Series of years.
    """
    return years // YEARS_PER_DECADE * YEARS_PER_DECADE
