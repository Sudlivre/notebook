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



