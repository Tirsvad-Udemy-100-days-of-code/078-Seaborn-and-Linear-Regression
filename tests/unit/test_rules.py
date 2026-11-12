import pandas as pd
import pytest

from movie_regression.domain.rules import to_decade


@pytest.mark.parametrize(
    ("year", "decade"), [(1990, 1990), (1992, 1990), (1999, 1990), (2000, 2000)]
)
def test_to_decade_floors_year_to_decade(year: int, decade: int) -> None:
    assert to_decade(year) == decade


def test_to_decade_works_on_a_pandas_index() -> None:
    assert list(to_decade(pd.Index([1992, 1999, 2001]))) == [1990, 1990, 2000]
