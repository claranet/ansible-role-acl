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


def test_directory_exists_and_mode_has_changed(host):
    """Validate acl directory."""
    _directory_controlled_by_acl = host.file("/etc/acl_directory")

    assert _directory_controlled_by_acl.exists
    assert _directory_controlled_by_acl.is_directory
    assert _directory_controlled_by_acl.mode == 0o775
