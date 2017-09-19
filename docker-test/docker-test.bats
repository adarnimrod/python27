#!/usr/bin/env bats

setup () {
    docker build -t python27_tls_test ./
}

@test 'test sni' {
    run docker run --entrypoint /bin/sh python27_tls_test -c "pip install nonexistant-package"
    ! ( echo "$output" | grep -qi warning )
}

#@test 'test tls 1.2' {
#    run docker run --entrypoint /usr/bin/python2 python27_tls_test -c "import urllib2, json; print(json.loads(urllib2.urlopen(urllib2.Request('https://www.howsmyssl.com/a/check')).read())['tls_version'])"
#    echo "$output" | grep -qi 'TLS 1\.2'
#}
