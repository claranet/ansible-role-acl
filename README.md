# Ansible role - acl
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-acl?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-acl?style=flat-square)](https://github.com/claranet/ansible-role-acl/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-acl/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-acl/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/acl)


> :star: Star us on GitHub — it motivates us a lot!

Install acl packages and setup access

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.acl
```

## :gear: Role variables

<table>
<tr>
<td><strong>Variable</strong></td> <td><strong>Default value</strong></td> <td><strong>Description</strong></td>
</tr>
<tr>
<td> acl_config </td>
<td>

```yaml
  - path: /etc/foo.conf
    default: false           # can be omit
    entity: "root"
    etype: "user" 
    follow: true             # can be omit
    permissions: "rwx"
    state: query
    recursive: false         # can be omit
```

</td>

<td>acl to set</td>
</tr>

</table>

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - claranet.acl
  vars:
  acl_config:
    - name:        /etc/acl_directory
      entity:      user01
      etype:       user
      permissions: "rw"
      state:       present
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
