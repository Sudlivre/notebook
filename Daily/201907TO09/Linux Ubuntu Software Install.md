# Linux Ubuntu Software Install

### node

```shell
# latest stable
wget http://nodejs.org/dist/latest-dubnium/node-v10.16.3-linux-x64.tar.gz
tar xf node-v10.16.3-linux-x64.tar.gz -C /usr/local/
cd /usr/local/
mv node-v10.16.3-linux-x64/ nodejs
ln -s /usr/local/nodejs/bin/node /usr/local/bin
ln -s /usr/local/nodejs/bin/npm /usr/local/bin
```



```shell
# https://registry.npm.taobao.org 
npm install cnpm -g -registry=https://registry.npm.taobao.org
ln -s /usr/local/nodejs/bin/cnpm /usr/local/bin
```



### MongoDB

```shell
wget https://repo.mongodb.org/apt/ubuntu/dists/bionic/mongodb-org/4.2/multiverse/binary-amd64/mongodb-org-server_4.2.0_amd64.deb
dpkg -i mongodb-org-server_4.2.0_amd64.deb
```



### adminMongo

```shell
git clone https://github.com/mrvautin/adminMongo.git && cd adminMongo
cnpm install
cnpm start
# Visit http://127.0.0.1:1234 in your browser
```



### Chrome

```shell
wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
apt-get update
apt-get install google-chrome-stable
# launch Chrome
/usr/bin/google-chrome-stable
```

Launch Error

```shell
# error: coursed by root acount
# ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
# launch Chrome by root
/usr/bin/google-chrome-stable --no-sandbox
# modify /usr/share/applications/google-chrome.desktop
# Exec=/usr/bin/google-chrome-stable --no-sandbox %U 
```



### GNOME Tweaks

```shell
apt install gnome-tweak-tool
apt install gnome-shell-extensions
apt install chrome-gnome-shell
```

