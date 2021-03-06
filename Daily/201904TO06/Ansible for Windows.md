# Ansible for Windows

[http://www.ansible.com.cn/docs/intro_windows.html](http://www.ansible.com.cn/docs/intro_windows.html)

[https://github.com/ansible/ansible-examples](https://github.com/ansible/ansible-examples)

#### windows下的运行方式
就如你刚所了解到的,Ansible默认是通过SSH协议来管理Linux/Unix服务器.
从1.7版本开始,Ansible也开始支持Windows机器的管理.不过是通过本机的PowerShell来实现远程管理,而不是SSH.
Ansible仍然通过一台Linux系统机器来进行集中管理,使用Python的 “winrm” 模块来和远程主机交互.
在管理的过程是 Ansible无需在远程主机上安装任何额外的软件,Ansible仍然使用 agentless(非c/s架构) 来保证其在 Linux/Unix的流行度.

#### 安装管理机
On a Linux control machine:
```
pip install http://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm
```
如果你想通过活动目录连接域帐户进行发布(相对本地帐户在远程主机上创建):
```
pip install kerberos
```
Kerberos 在 OS X 和许多 Linux 发行版中是默认安装且配置好的.如果你的管理机上还没有安装,那你需要执行如上的命令.

#### Inventory
Ansible’s支持windows需要依赖于少量标准变量来表明远程主机的username, password, and connection type (windows).这些变量大部分都很容易被设置好.在 Ansible 中通过用来代替 SSH-keys 或 密码输入:
```
[windows]
winserver1.example.com
winserver2.example.com
```
在 group_vars/windows.yml,定义如下 inventory 变量:
```
# it is suggested that these be encrypted with ansible-vault:
# ansible-vault edit group_vars/windows.yml

ansible_ssh_user: Administrator
ansible_ssh_pass: SecretPasswordGoesHere
ansible_ssh_port: 5986
ansible_connection: winrm
```
需要注意的是这里的 ssh_port 不是真正的SSH协议的端口,but this is a holdover variable name from how Ansible is mostly an SSH-oriented system.(这句也没看懂)再重复一遍,Windows 管理主机不是通过SSH协议.

如果你已经安装了 kerberos 模块和 ansible_ssh_user 包括 @ (e.g. username@realm), Ansible会先尝试Kerberos认证. * 这种方式主要用你通过Kerberos在远程主机上的认证而不是 ansible_ssh_user * .如果上述办法失败了,要么是因为你没有在管理机上签署(signed into)Kerberos,要么是因为远程主机上对应的域帐户不可用,接着 Ansible 将返回原始(“plain”)username/password的认证方式.

当你使用 playbook 时,请不要忘记指定 –ask-vault-pass 提供密码来解锁文件.

使用如下命令来测试你的配置,尝试连接你的 Windows 节点.注意:这不是ICMP ping,只是利用 Windows 远程工具来检测 Ansible 的信道是否正常:

ansible windows [-i inventory] -m win_ping --ask-vault-pass
如果你还没有在你的系统上做任何准备工作,那上面的命令是无法正常工作的. 在下面最近的章节将会介绍 “how to enable PowerShell remoting” - 如果有需要的话也将介绍 “how to upgrade PowerShell to a version that is 3 or higher” .

#### Windows System Prep
为了 Ansible 能管理你的windows机器,你将必须开启并配置远程机器上PowerShell.
为了能自动化设置 WinRM,你可以在远程机器上执行 [this PowerShell script](./res/ConfigureRemotingForAnsible.ps1)


#### 可用的windows模块

大多数 Ansible 模块尤其核心Ansible设计来组合 Linux/Unix 机器和任意 web services. 尽管[“windows” subcategory of the Ansible module index ]  (https://docs.ansible.com/ansible/latest/modules/list_of_windows_modules.html)列举了各种各校的 Windows 模块.
```
win_acl – Set file/directory/registry permissions for a system user or group
win_acl_inheritance – Change ACL inheritance
win_audit_policy_system – Used to make changes to the system wide Audit Policy
win_audit_rule – Adds an audit rule to files, folders, or registry keys
win_certificate_store – Manages the certificate store
win_chocolatey – Manage packages using chocolatey
win_chocolatey_config – Manages Chocolatey config settings
win_chocolatey_feature – Manages Chocolatey features
win_chocolatey_source – Manages Chocolatey sources
win_command – Executes a command on a remote Windows node
win_copy – Copies files to remote locations on windows hosts
win_defrag – Consolidate fragmented files on local volumes
win_disk_facts – Show the attached disks and disk information of the target host
win_disk_image – Manage ISO/VHD/VHDX mounts on Windows hosts
win_dns_client – Configures DNS lookup on Windows hosts
win_domain – Ensures the existence of a Windows domain
win_domain_computer – Manage computers in Active Directory
win_domain_controller – Manage domain controller/member server state for a Windows host
win_domain_group – Creates, modifies or removes domain groups
win_domain_membership – Manage domain/workgroup membership for a Windows host
win_domain_user – Manages Windows Active Directory user accounts
win_dotnet_ngen – Runs ngen to recompile DLLs after .NET updates
win_dsc – Invokes a PowerShell DSC configuration
win_environment – Modify environment variables on windows hosts
win_eventlog – Manage Windows event logs
win_eventlog_entry – Write entries to Windows event logs
win_feature – Installs and uninstalls Windows Features on Windows Server
win_file – Creates, touches or removes files or directories
win_file_version – Get DLL or EXE file build version
win_find – Return a list of files based on specific criteria
win_firewall – Enable or disable the Windows Firewall
win_firewall_rule – Windows firewall automation
win_get_url – Downloads file from HTTP, HTTPS, or FTP to node
win_group – Add and remove local groups
win_group_membership – Manage Windows local group membership
win_hostname – Manages local Windows computer name.
win_hotfix – Install and uninstalls Windows hotfixes
win_iis_virtualdirectory – Configures a virtual directory in IIS
win_iis_webapplication – Configures IIS web applications
win_iis_webapppool – Configure IIS Web Application Pools
win_iis_webbinding – Configures a IIS Web site binding
win_iis_website – Configures a IIS Web site
win_lineinfile – Ensure a particular line is in a file, or replace an existing line using a back-referenced regular expression
win_mapped_drive – Map network drives for users
win_msg – Sends a message to logged in users on Windows hosts
win_msi – Installs and uninstalls Windows MSI files (D)
win_nssm – NSSM - the Non-Sucking Service Manager
win_owner – Set owner
win_package – Installs/uninstalls an installable package
win_pagefile – Query or change pagefile configuration
win_path – Manage Windows path environment variables
win_pester – Run Pester tests on Windows hosts
win_ping – A windows version of the classic ping module
win_power_plan – Changes the power plan of a Windows system
win_product_facts – Provides Windows product information (product id, product key)
win_psexec – Runs commands (remotely) as another (privileged) user
win_psmodule – Adds or removes a Powershell Module
win_rabbitmq_plugin – Manage RabbitMQ plugins
win_reboot – Reboot a windows machine
win_reg_stat – Get information about Windows registry keys
win_regedit – Add, change, or remove registry keys and values
win_region – Set the region and format settings
win_regmerge – Merges the contents of a registry file into the windows registry
win_robocopy – Synchronizes the contents of two directories using Robocopy
win_route – Add or remove a static route
win_say – Text to speech module for Windows to speak messages and optionally play sounds
win_scheduled_task – Manage scheduled tasks
win_scheduled_task_stat – Get information about Windows Scheduled Tasks
win_security_policy – Change local security policy settings
win_service – Manage and query Windows services
win_share – Manage Windows shares
win_shell – Execute shell commands on target hosts
win_shortcut – Manage shortcuts on Windows
win_stat – Get information about Windows files
win_tempfile – Creates temporary files and directories
win_template – Templates a file out to a remote server
win_timezone – Sets Windows machine timezone
win_toast – Sends Toast windows notification to logged in users on Windows 10 or later hosts
win_unzip – Unzips compressed files and archives on the Windows node
win_updates – Download and install Windows updates
win_uri – Interacts with webservices
win_user – Manages local Windows user accounts
win_user_right – Manage Windows User Rights
win_wait_for – Waits for a condition before continuing
win_wait_for_process – Waits for a process to exist or not exist before continuing.
win_wakeonlan – Send a magic Wake-on-LAN (WoL) broadcast packet
win_webpicmd – Installs packages using Web Platform Installer command-line
win_whoami – Get information about the current user and process
win_xml – Add XML fragment to an XML parent
```
浏览上面的索引查看可用模块.
很多情况下, 其实没有必要写或者使用 Ansible 模块.
尤其, “script” 模块可以用来执行任意 PowerShell 脚本,允许 Windows administrators 组所有用户通过 PowerSehll 以非常本地化的方式做任何事情.就像如下的 playbook:

```
- hosts: windows
  tasks:
    - script: foo.ps1 --argument --other-argument
```
注意: 有一小部分 Ansible 模块不是以 “win” 开头但依然是函数,包括 “slurp”,”raw”,和”setup”(fact 收集的工作原理).

#### 开发者:支持的模块及工作原理
开发 ansible 模块主要在 later section of the documentation 介绍,专注于 Linux/Unix 平台. 如果你想编写 Windows 的 ansible 模块该怎么办呢?
Windows 平台主要通过 PowerShell 模块实现. 开始之前可以先略过 Linux/Unix 模块开发章节.
Windows 模块在 Ansible “library/” 子目录下的 “windows/” 子目录下. 例如,如果一个模块命名为 “library/windows/win_ping”,那将会在 “win_ping” 文件中嵌入一个文档,实际的 PowerShell 代码将存在 “win_ping.ps1” 文件. 看下源代码会有更深入的了解.
模块(ps1 files)文件应该以如下格式开头:
```
#!powershell
# <license>

# WANT_JSON
# POWERSHELL_COMMON

# code goes here, reading in stdin as JSON and outputting JSON
```
如上代码是为了告诉 ansible 合入一些代码并且 The above magic is necessary to tell Ansible to mix in some common code and also know how to push modules out. 常规代码包括好包装例如哈希数据结构,jason格式标准输出,还有一些更有用的东西.常规 Ansible 有着重复利用 Python 代码的理念 - 这点 Windows 也是等同的. 你刚看到的 windows/ 模块只是一个开始. 附加模块已经被 git push 到 github上了.

>提醒:控制机必须是Linux系统

Windows 控制机不是这个项目的目标. Ansible 不会开发这个功能,因为受限于技术,产品和我们未来主要项目使用的代码. 一台Linux控制机是必须的,可以用来管理 Windows 机器. Cygwin 也是不被支持的,所以请不要要求 Ansible 基于 Cygwin 来运行.

#### Windows Facts
Just as with Linux/Unix, facts can be gathered for windows hosts, which will return things such as the operating system version. To see what variables are available about a windows host, run the following:
```
ansible winhost.example.com -m setup
```
Note that this command invocation is exactly the same as the Linux/Unix equivalent.

#### Windows Playbook Examples
Look to the list of windows modules for most of what is possible, though also some modules like “raw” and “script” also work on Windows, as do “fetch” and “slurp”.

Here is an example of pushing and running a PowerShell script:
```
- name: test script module
  hosts: windows
  tasks:
    - name: run test script
      script: files/test_script.ps1
```
Running individual commands uses the ‘raw’ module, as opposed to the shell or command module as is common on Linux/Unix operating systems:
```
- name: test raw module
  hosts: windows
  tasks:
    - name: run ipconfig
      raw: ipconfig
      register: ipconfig
    - debug: var=ipconfig
```
And for a final example, here’s how to use the win_stat module to test for file existence. Note that the data returned by the win_stat module is slightly different than what is provided by the Linux equivalent:
```
- name: test stat module
  hosts: windows
  tasks:
    - name: test stat module on file
      win_stat: path="C:/Windows/win.ini"
      register: stat_file

    - debug: var=stat_file

    - name: check stat_file result
      assert:
          that:
             - "stat_file.stat.exists"
             - "not stat_file.stat.isdir"
             - "stat_file.stat.size > 0"
             - "stat_file.stat.md5"
```

Again, recall that the Windows modules are all listed in the Windows category of modules, with the exception that the “raw”, “script”, and “fetch” modules are also available. These modules do not start with a “win” prefix.