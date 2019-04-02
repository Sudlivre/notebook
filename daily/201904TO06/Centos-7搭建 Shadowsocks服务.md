# Centos-7搭建 Shadowsocks服务

#### 搬瓦工一键搭建酸酸

```shell
#中文版
yum install -y wget && wget --no-check-certificate -O shadowsocks-libev_CN.sh https://raw.githubusercontent.com/uxh/shadowsocks_bash/master/shadowsocks-libev_CN.sh && bash shadowsocks-libev_CN.sh
```

```shell
# 英文版
yum install -y wget && wget --no-check-certificate -O shadowsocks-libev.sh https://raw.githubusercontent.com/uxh/shadowsocks_bash/master/shadowsocks-libev.sh && bash shadowsocks-libev.sh
```

[[链接：搬瓦工一键搭建酸酸图文教程](https://www.banwagongzw.com/7.html)](https://www.banwagongzw.com/7.html)

修改 Shadowsocks 的配置信息

```shell
# 中文版
bash shadowsocks-libev_CN.sh 
# 英文版
bash shadowsocks-libev.sh
```

卸载 Shadowsocks 服务

```shell
# 中文版
bash shadowsocks-libev_CN.sh 
# 英文版
bash shadowsocks-libev.sh
```