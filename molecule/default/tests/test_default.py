"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_php_is_installed(host):
    """
    Tests that php is installed
    """
    php = host.package("php7.0-common")
    assert php.is_installed


def test_php_running_and_enabled(host):
    """
    Tests that php is running and enabled
    """
    php = host.service("php7.0-fpm")
    assert php.is_running
    assert php.is_enabled
