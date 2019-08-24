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



### Python3

```shell
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
mkdir -p /usr/local/python3
tar -zxvf Python-3.7.0.tgz
cd Python-3.7.0
#/usr/local/python3 install dir
./configure --prefix=/usr/local/python3   
make
make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python37
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip37
```

PATH

```shell
vim /etc/profile
# add 
# export PATH=$PATH:/usr/local/python3/bin
source /etc/profile
```

