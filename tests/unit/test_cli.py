import pytest

from movie_regression.presentation.cli import main


def test_main_prints_the_report(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    assert "Movie budget and revenue" in capsys.readouterr().out
