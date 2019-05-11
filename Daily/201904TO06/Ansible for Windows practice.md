# Ansible管理Windows实践

#### Ansible简介

ansible是新出现的自动化运维工具，基于Python开发，集合了众多运维工具（puppet、cfengine、chef、func、fabric）的优点，实现了批量系统配置、批量程序部署、批量运行命令等功能。ansible是基于模块工作的，本身没有批量部署的能力。真正具有批量部署的是ansible所运行的模块，ansible只是提供一种框架。

#### Ansible管理机部署安装

```shell
pip install ansible

pip install paramiko PyYAML Jinja2 httplib2 six
```

```shell
vim /etc/ansible/hosts
```

```
[windows]
192.168.18.132 ansible_ssh_user="Administrator" ansible_ssh_pass="123456" ansible_ssh_port=5985 ansible_connection="winrm" ansible_winrm_server_cert_validation=ignore
```

192.168.18.132是windows服务器的IP

#### Windows系统配置

```powershell
set-executionpolicy remotesigned
```

```
winrm enumerate winrm/config/listener

winrm quickconfig

winrm e winrm/config/listener

winrm set winrm/config/service/auth @{Basic="true"}

winrm set winrm/config/service @{AllowUnencrypted="true"}
```

#### Windows下可用模块测试

```shell
ansible windows -m win_ping

ansible windows -m raw -a "CMD /C ipconfig"
```

