# Python interacts with cmd

```python
import subprocess

path = r'C:\Tools'
def excute_cmd(cmd):
    s = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    # time.sleep(2)
    s.stdin.write('y\n'.encode('gbk'))
    s.stdin.write(path.encode('gbk'))
    out, err = s.communicate()
    if err:
        return err
    return out
```