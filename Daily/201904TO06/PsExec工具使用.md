# PsExec工具使用

```
Usage: psexec [\\computer[,computer2[,...] | @file][-u user [-p psswd]][-n s][-l][-s|-e][-x][-i [session]][-c [-f|-v]][-w directory][-d][-<priority>][-a n,n,... ] cmd [arguments]
```

#### 以系统身份运行指定应用程序
Windows系统中administrator的权限不是最大的，最大的是system，很多信息只有system才能查看，比如注册表的sam信息，administrator是看不了的，如果你非要强行修改sam的权限而不顾安全的话，拿就是另外一种情况。那么现在我们要以system的身份启动regedit.exe，命令如下：
```psexec -s -i regedit.exe```
-s就是以system身份
-i就是交互式，意思是让你看到注册表编辑器的这个窗口，不然他就在后台运行

#### 创建/执行远程命令代码。
执行远程进程的前提条件是对方机器必须开启ipc$，以及admin$,否则无法执行。下面我们来看详细命令：

开启ipc$
```net share ipc$```
开启admin$
```net share admin$```

#### 在对方电脑上运行程序
```C:\>psexec \\192.168.100.2 -u administrator -p 123456 -d -s calc```

运行calc后返回，对方计算机上会有一个calc进程，是以系统身份运行的，因为calc前面是-s(system的意思)。窗口对方是看不到的，如果需要对方看到这个窗口，需要加参数-i。

```C:\>psexec \\192.168.100.2 -u administrator -p 123456 -d calc```
承上，就以当前身份运行calc，然后返回
```C:\>psexec \\192.168.100.2 -u administrator -p 123456 -i -d cmd /c start http://www.baidu.com```
为对方以当前用户身份打开百度网页，并让他看到这个网页

``` .\psexec \\192.168.18.132 -u administrator -p zhendeaini -i -d cmd /c python c:\install\install.py```

```C:\>psexec \\192.168.100.2 -u administrator -p 123456 -s cmd```

这个命令执行成功之后，命令提示符窗口在我这边，可以直接在我这边输入命令，而命令在对端执行，相当于远端应用程序虚拟化到本地，很有用。
-i，交互式，也就是能不能看到窗口的意思，-s以系统身份运行，否则就是当前用户，-d执行命令后返回，不等待命令结束。

#### 命令详解
https://docs.microsoft.com/en-us/sysinternals/downloads/psexec