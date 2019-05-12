# Ubuntu18.04 set the root user login

**set root password**
```shell
sudo passwd root
```

**modify 50-ubuntu.conf**
```
sudo cp /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf.bak
sudo gedit /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
```
content
```
[Seat:*]
user-session=ubuntu
greeter-show-manual-login=true
all-guest=false
```

**modify gdm-autologin and gdm-password**
```shell
cd /etc/pam.d
sudo cp gdm-autologin gdm-autologin.bak
sudo gedit gdm-autologin
# Comment line: #auth required pam_success_if.so user!=root quiet_success
sudo cp gdm-password gdm-password.bak
sudo gedit gdm-password
# Comment line: #auth required pam_success_if.so user!=root quiet_success
```

**modify /root/.profile**

content
```
# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

tty -s && mesg n || true
```

**reboot**