#!/usr/bin/env python

import os
import stat

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_acl_is_installed(host):
    _acl_package = host.package("acl")
    assert _acl_package.is_installed


def test_file_exist_and_perm_change(host):
    """Validate acl file."""
    _file_controlled_by_acl = host.run("sudo getfacl /etc/acl_file | grep user01")
    assert _file_controlled_by_acl.succeeded


def test_directory_exist_and_mode_change(host):
    """Validate acl directory."""
    _directory_controlled_by_acl = host.file("/etc/acl_directory")

    assert _directory_controlled_by_acl.exists
    assert _directory_controlled_by_acl.is_directory
    assert _directory_controlled_by_acl.mode == 0o775
