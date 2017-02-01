import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('error', [
    'InsecureRequestWarning', 'InsecurePlatformWarning', 'SNIMissingWarning'
])
def test_sni(Command, error):
    assert error not in Command('pip2 install nonexistant-package').stderr


def test_tls12(Command):
    pycommand = '''import requests;
print(requests.get('https://www.howsmyssl.com/a/check',
verify=False).json()['tls_version'])'''
    assert 'TLS 1.2' == Command('python2 -c \"%s\"' % pycommand).stdout.strip()
