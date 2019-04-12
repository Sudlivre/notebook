# PsExec工具使用

```
Usage: psexec [\\computer[,computer2[,...] | @file][-u user [-p psswd]][-n s][-l][-s|-e][-x][-i [session]][-c [-f|-v]][-w directory][-d][-<priority>][-a n,n,... ] cmd [arguments]
```

#### 远程运行程序
以system的身份启动regedit.exe
```
psexec -s -i regedit.exe
```
-s就是以system身份
-i就是交互式，意思是让你看到注册表编辑器的这个窗口，不然他就在后台运行
-d不等待程序执行结束

#### 创建/执行远程命令代码。
执行远程进程的前提条件是对方机器必须开启ipc$，以及admin$
```
net share ipc$
net share admin$
```

```
C:\>psexec \\192.168.100.2 -u administrator -p 123456 -d -s calc
```

```
C:\>psexec \\192.168.100.2 -u administrator -p 123456 -d calc
```

```
C:\>psexec \\192.168.100.2 -u administrator -p 123456 -i -d cmd /c start http://www.baidu.com
```

``` 
.\psexec \\192.168.18.132 -u administrator -p zhendeaini -i -d cmd /c python c:\install\install.py
```

#### 命令详解
https://docs.microsoft.com/en-us/sysinternals/downloads/psexec