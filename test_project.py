from click.testing import CliRunner

from calCLI import cli
from mylib.calc import add, sub, mul, div, power


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(8, 2) == 4


def test_power():
    assert power(2, 3) == 8


def test_add_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])

    assert result.exit_code == 0
    assert "2.0 + 3.0 = 5.0" in result.output


def test_sub_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "5", "3"])

    assert result.exit_code == 0
    assert "5.0 - 3.0 = 2.0" in result.output


def test_mul_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "4", "3"])

    assert result.exit_code == 0
    assert "4.0 * 3.0 = 12.0" in result.output


def test_div_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "8", "2"])

    assert result.exit_code == 0
    assert "8.0 / 2.0 = 4.0" in result.output


def test_power_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["pow", "2", "3"])

    assert result.exit_code == 0
    assert "2.0 ** 3.0 = 8.0" in result.output
