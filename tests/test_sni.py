import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('error', ['InsecureRequestWarning',
                                   'InsecurePlatformWarning',
                                   'SNIMissingWarning'])
def test_sni(Command, error):
    assert error not in Command('pip install nonexistant-package').stderr
