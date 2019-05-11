# Automatic remote desktop

Based on Windows Server 2012

**premise** 

- remote machine need open winrm service 
- base host need PsExec.exe for start up display


bat script
```
REM Skip popup
REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Terminal Server Client" /v AuthenticationLevelOverride /t REG_DWORD /d 0 /f
REM Modify group policy
REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CredentialsDelegation\AllowSavedCredentialsWhenNTLMOnly" /v 1 /t RED_SZ /d TERMSRV/* /f
REM Update group policy
gpupdate /force
REM Add login credentials
CMDKEY /add:remote_ip /user:user /pass:password
REM Remote desktop
MSTSC /v:remote_ip:remote_port
```
start the script by command
```
PsExec.exe \\ip -accepteula -u user -p password -i cmd
```
or use `query user` find ID
```
PsExec.exe \\ip -accepteula -u user -p password -i ID cmd
```

**About wmic**

open remote desktop service
```
wmic /node:"[full machine name]" /USER:"[domain]\[username]" PATH win32_terminalservicesetting WHERE (__Class!="") CALL SetAllowTSConnections 1
```
use wmic open remote process
```
wmic /node:ip /user:"administrator" /password:"password" process call create commandline="command"
```
