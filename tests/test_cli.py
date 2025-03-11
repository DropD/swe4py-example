from click import testing

from swe4py_example import cli


def test_hello():
    runner = testing.CliRunner()

    result = runner.invoke(cli.swe4py_example)
    assert result.exit_code == 0
    assert result.output == "Hello world!\n"
