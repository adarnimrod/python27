from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_tls12(Command):
    pycommand = '''import urllib2, json
print(json.loads(urllib2.urlopen(urllib2.Request(
'https://www.howsmyssl.com/a/check')).read())['tls_version'])'''
    assert 'TLS 1.2' == Command('python2 -c \"%s\"' % pycommand).stdout.strip()
