import zlib
import requests


def save_to_file(data):
    with open('begin_file.txt', 'wb') as f:
        f.write(data)


# zlib.compress 用来压缩字符串的bytes类型
def str_zlib():
    response = requests.get("http://www.sudlivre.com/index.php/2018/10/21/jingmisipdera/")
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
