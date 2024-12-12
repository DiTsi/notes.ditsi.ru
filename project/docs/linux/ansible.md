# ansible

## Commands

```bash
# see password stored in file
ansible-vault view keyfile
```

## Useful playbooks

```yml
- hosts: localhost
  connection: local
  vars:
    list_of_groups:
      - test_servers
    exclude_hosts: []
    list_of_hosts: "{{ list_of_groups|map('extract', groups) | flatten | difference (exclude_hosts) }}"
  tasks:
  - debug:
      var: list_of_hosts
```

```yml
- hosts: localhost
  connection: local
  vars:
    list1: "{{ groups['germany'] }}"
    list2: "{{ groups['germany_failed'] }}"
    list: "{{ list1 | difference(list2) }}"
  tasks:
  - debug:
      var: list
```


## Vault

Set vault-password-file
```ini
[defaults]
vault_password_file=~/.ansible_vault
```
