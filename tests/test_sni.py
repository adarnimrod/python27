import pytest


@pytest.mark.parametrize('error', ['InsecureRequestWarning',
                                   'InsecurePlatformWarning',
                                   'SNIMissingWarning'])
def test_sni(Command, error):
    assert error not in Command('pip install nonexistant-package').stderr
