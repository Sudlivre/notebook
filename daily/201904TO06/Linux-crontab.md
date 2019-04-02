# Linux – crontab

crontab可以在指定的时间执行一个shell脚本或者一系列Linux命令，当然也可以定时的运行Python脚本或者是爬虫任务，当然这里面存在大坑……

>脚本中会有涉及读取配置文件或者读写文件的动作，定时任务不会执行
>
>因为你的脚本在执行时,由于是通过crontab去执行的,他的执行目录会变成当前用户的家目录,如果是root,就会在/root/下执行

#### crontab执行Python脚本

**解决方法一：**

将Python路径和脚本路径以及脚本中涉及文件操作的路径设置为绝对路径，当然这样并不好用

**解决方法二：**

通过在/etc/cron.d下新建一个文件去指定定时任务执行目录的方式去设置定时任务

例如我新建了一个test_cron的文件

```shell
cd /etc/cron.d
vim test_cron
```

输入以下内容

HOME指定文件执行的路径

```shell
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/home/src/spider
* * * * * root python3 test_crontab.py
* * * * * root echo 'nimeide' >> haha.txt
```



#### crontab使用

```shell
[root@izwz94dva5frwtxtld4w3vz ~]# cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
 
# For details see man 4 crontabs
 
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```

**基本格式**

{minute} {hour} {day-of-month} {month} {day-of-week} {full-path-to-shell-script}

- minute: 区间为 0 – 59
- hour: 区间为0 – 23
- day-of-month: 区间为0 – 31
- month: 区间为1 – 12. 1 是1月. 12是12月
- Day-of-week: 区间为0 – 7. 周日可以是0或7



#### crontab示例

```shell
# 在 12:01 a.m 运行，即每天凌晨过一分钟。这是一个恰当的进行备份的时间，因为此时系统负载不大
1 0 * * * /root/bin/backup.sh
 
# 每个工作日(Mon – Fri) 11:59 p.m 都进行备份作业
59 11 * * 1,2,3,4,5 /root/bin/backup.sh
 
# 下面例子与上面的例子效果一样
59 11 * * 1-5 /root/bin/backup.sh
 
# 每5分钟运行一次命令
*/5 * * * * /root/bin/check-status.sh
 
# 每个月的第一天 1:10 p.m 运行
10 13 1 * * /root/bin/full-backup.sh
 
# 每个工作日 11 p.m 运行
0 23 * * 1-5 /root/bin/incremental-backup.sh
```

**crontab 选项**

- crontab –e : 修改 crontab 文件，如果文件不存在会自动创建
- crontab –l : 显示 crontab 文件
- crontab -r : 删除 crontab 文件
- crontab -ir : 删除 crontab 文件前提醒用户

linux平台上如果需要实现任务调度功能可以编写cron脚本来实现，crond进程负责读取调度任务并执行，用户只需要将相应的调度脚本写入cron的调度配置文件中。

**cron的调度文件有以下几个**

- crontab
- cron.d
- cron.daily
- cron.hourly
- cron.monthly
- cron.weekly

如果用的任务不是以hourly monthly weekly方式执行，则可以将相应的crontab写入到crontab 或cron.d目录中