# Python – zlib/hashlib/rsa

####  zlib-数据压缩解压缩库

```python
import zlib
import requests
 
 
def save_to_file(data):
    with open('begin_file.txt', 'wb') as f:
        f.write(data)
 
 
# zlib.compress 用来压缩字符串的bytes类型
def str_zlib():
    response = requests.get("https://www.baidu.com")
    message = response.text
    bytes_message = str.encode(message)
    save_to_file(bytes_message)
    compressed = zlib.compress(bytes_message, zlib.Z_BEST_COMPRESSION)
    decompressed = zlib.decompress(compressed)
    print("original string:", len(message))
    print("original bytes:", len(bytes_message))
    print("compressed:", len(compressed))
    print("decompressed:", len(decompressed))
 
 
# zlib.compressobj 用来压缩数据流，用于文件传输
def file_compress(begin_file, zlib_file, level):
    infile = open(begin_file, "rb")
    zfile = open(zlib_file, "wb")
    compressobj = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        zfile.write(compressobj.compress(data))
        # 继续读取文件中的下一个size的内容
        data = infile.read(1024)
    # compressobj.flush()包含剩余压缩输出的字节对象，将剩余的字节内容写入到目标文件中
    zfile.write(compressobj.flush())
 
 
def file_decompress(zlib_file, end_file):
    zlib_file = open(zlib_file, "rb")
    end_file = open(end_file, "wb")
    decompressobj = zlib.decompressobj()
    data = zlib_file.read(1024)
    while data:
        end_file.write(decompressobj.decompress(data))
        data = zlib_file.read(1024)
    end_file.write(decompressobj.flush())
 
 
def main():
    # 测试字符串的压缩与解压
    str_zlib()
 
    # 测试数据流压缩
    begin_file = "./begin_file.txt"
    zlib_file = "./zlib_file.txt"
    level = 9
    file_compress(begin_file, zlib_file, level)
 
    # 测试数据流解压
    zlib_file = "./zlib_file.txt"
    end_file = "./end_file.txt"
    file_decompress(zlib_file, end_file)
 
 
if __name__ == "__main__":
    main()
```



#### hashlib-哈希摘要生成器

```python
from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512
 
 
class StreamHasher():
    """哈希摘要生成器"""
 
    def __init__(self, algorithm='md5', size=1024):
        self.size = size
        alg = algorithm.lower()
        if alg == 'md5':
            self.hasher = md5()
        elif alg == 'sha1':
            self.hasher = sha1()
        elif alg == 'sha256':
            self.hasher = sha256()
        elif alg == 'sha512':
            self.hasher = sha512()
        else:
            raise ValueError('不支持指定的摘要算法')
 
    # 魔法方法: 让对象可以像函数一样被调用
    def __call__(self, stream):
        return self.to_digest(stream)
 
    def to_digest(self, stream):
        """生成十六进制形式的哈希摘要字符串"""
        for data in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()
 
 
def main():
    """主函数"""
    hasher = StreamHasher('sha1', 4096)
    with open('Python魔法方法指南.pdf', 'rb') as stream:
        # print(hasher.to_digest(stream))
        print(hasher(stream))
 
 
if __name__ == '__main__':
    main()
```



#### rsa-加密库

```python
import rsa
 
# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)
 
# 保存密钥
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())
 
with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())
 
# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
 
with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
 
# 明文
message = 'zhezhendeshiyigemima'
 
# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)
print(crypto)
 
# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)
 
# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')
print(signature)
 
# 公钥验证
result = rsa.verify(message.encode(), signature, pubkey)
print(result)
```

