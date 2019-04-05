import json
import os
import sys
import re
from operator import itemgetter
from ftplib import FTP
from multiprocessing import Process


class FTPSync:

    def __init__(self, fir, local):
        self.conn = self.ftp_connect()
        self.conn.cwd(fir)
        os.chdir(local)

    def ftp_connect(self):
        ftp = FTP()
        ftp_file = sys.path[0] + os.path.sep + "ftp_info.json"
        ftp_infos = read_file(ftp_file)
        ftp_ip = ftp_infos.get('ip')
        ftp_port = ftp_infos.get('port')
        ftp_user = ftp_infos.get('user')
        ftp_password = ftp_infos.get('password')
        ftp.connect(ftp_ip, int(ftp_port))
        ftp.login(ftp_user, ftp_password)
        return ftp

    def get_dirs_files(self):
        if os.path.exists('c:\install'):
            pass
        else:
            os.mkdir('c:\install')
        dir_res = []
        self.conn.dir('.', dir_res.append)
        pattern_dir = r'\d{2}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}[A-Z]*\s+<DIR>\s+(.*)'
        pattern_file = r'\d{2}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}[A-Z]*\s+[0-9]\d*\s+(.*)'
        filess = [re.findall(pattern_file, f)[0] for f in dir_res if '<DIR>' in f]
        dirss = [re.findall(pattern_dir, f)[0] for f in dir_res if '<DIR>' in f]
        files = []
        for file in filess:
            files.append(file.encode('iso-8859-1').decode('gbk'))
        dirs = []
        for dir in dirss:
            dirs.append(dir.encode('iso-8859-1').decode('gbk'))
        return (files, dirs)

    def walk(self, next_dir):
        print(f'walking to {next_dir}')
        self.conn.cwd(next_dir)
        try:
            os.mkdir(next_dir)
        except OSError:
            pass
        os.chdir(next_dir)
        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()
        files, dirs = self.get_dirs_files()
        print(f'FILES:{files}')
        print(f'DIRS:{dirs}')
        for f in files:
            print(next_dir, ':', f)
            outf = open(f, 'wb')
            try:
                self.conn.retrbinary('RETR %s' % f.encode('gbk').decode('iso-8859-1'), outf.write)
            finally:
                outf.close()
        for d in dirs:
            os.chdir(local_curr_dir)
            self.conn.cwd(ftp_curr_dir)
            self.walk(d)

    def run(self):
        self.walk('.')


def load(fir, local):
    f = FTP(fir, local)
    f.run()


def read_file(file_path):
    f = open(file_path, 'r')
    configstr = f.read()
    configtmp = json.loads(configstr)
    print(configtmp)
    return configtmp


def install_tools(file_path, software_path):
    tools_infos = read_file(file_path)
    tools_infos = sorted(tools_infos, key=itemgetter('installation_order'), reverse=False)

    for tool in tools_infos:
        if 'python3' not in tool.get('software_package'):
            install_tool = tool.get('software_package')
            install_scripts = tool.get('install_script')
            check_scripts = tool.get('check_script')
            try:
                if type(install_tool) == 'list':
                    for to in install_tool:
                        local_path = software_path + to
                        load_tool(local_path, to)
                else:
                    local_path = software_path + install_tool
                    load_tool(local_path, install_tool)
                print('load finish')
                scripts_path = r'c:\buildtools\all_scripts'
                if type(install_tool) == 'list':
                    scripts_path = scripts_path + install_tool[0]
                else:
                    scripts_path = scripts_path + install_tool
                install_software(scripts_path, install_scripts, software_path, install_tool)
                print('install finish')
                check_software(scripts_path, check_scripts)
                print('check finish')
                path = r'c:\install'
                del_software(path)
            except Exception as e:
                print('install failed')
    print('delete pywinauto')
    os.system('del "c:\\buildtools\\python-3.7.0\\lib\\site-packages\\pywinauto-0.6.5-py3.7.egg"')
    sc_ph = r'c:\buildtools\all_scripts'
    os.system('rd /s /q ' + sc_ph)


def del_software(local_path):
    if os.path.exists(local_path):
        cmd = 'rd /s /q ' + local_path
        os.system(cmd)


def check_software(scripts_path, check_scripts):
    cmd = scripts_path + '\\' + check_scripts
    os.system(cmd)


def install_software(scripts_path, install_scripts, software_path, install_tool):
    install_dir = install_tool.replace('\\', '')
    cmd = scripts_path + os.path.sep + install_scripts
    if install_scripts.endswith('.py'):
        os.system('python ' + cmd + ' ' + software_path + ' ' + install_dir)
    else:
        os.system(cmd + ' ' + software_path)


def load_tool(local_path, install_tool):
    create_install_dir(local_path, install_tool)
    load(install_tool, local_path)


def create_install_path(local_path, install_tool):
    if not os.path.exists(local_path):
        os.makedirs(local_path)


if __name__ == '__main__':
    current_path = sys.path[0]
    software_path = r'c:\install'
    if len(sys.argv) > 1:
        software_path = sys.argv[1]
    software_list_json = current_path + os.path.sep + 'software_list.json'
    p = Process(target=install_tools, args=(software_list_json, software_path,))
    p.start()
    p.join()
    cmd = 'rd /s /q c:\\install'
    os.system(cmd)
