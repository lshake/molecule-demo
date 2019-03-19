import os
import sys

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_caddy_docroot_directory(host):
    directory = host.file('/var/www/caddy')
    assert directory.exists
    assert directory.user == 'caddy'
    assert directory.group == 'caddy'
    if sys.version_info[0] <= (2):
        assert oct(directory.mode) == '0775'
    else:
        assert oct(directory.mode) == '0o775'
    assert directory.is_directory


def test_caddy_binary_directory(host):
    directory = host.file('/opt/caddy')
    assert directory.exists
    assert directory.user == 'root'
    assert directory.group == 'root'
    if sys.version_info[0] <= (2):
        assert oct(directory.mode) == '0755'
    else:
        assert oct(directory.mode) == '0o755'
    assert directory.is_directory


def test_caddy_binary(host):
    bin = host.file('/opt/caddy/caddy')
    assert bin.exists
    assert bin.user == 'root'
    assert bin.group == 'root'
    if sys.version_info[0] <= (2):
        assert oct(bin.mode) == '0755'
    else:
        assert oct(bin.mode) == '0o755'
    assert bin.is_file


def test_caddy_user(host):
    user = host.user("caddy")
    assert user.exists
    assert user.name == "caddy"
    assert user.uid != 0
    assert user.gid != 0
    assert user.group == "caddy"
    assert user.shell == "/sbin/nologin"
    assert user.home == "/home/caddy"
    assert user.password == "*"


def test_version(host):
    cmd = host.command('/opt/caddy/caddy -version')
    expected = ('Caddy 0.11.5 (non-commercial use only)')
    assert cmd.rc == 0
    assert expected == cmd.stdout


def test_listening(host):
    socket = host.socket('tcp://0.0.0.0:80')
    assert socket.is_listening


def test_response(host):
    cmd = host.command('curl http://localhost:80/.static_test.html')
    expected = ('Response from')
    assert cmd.rc == 0
    assert expected in cmd.stdout
