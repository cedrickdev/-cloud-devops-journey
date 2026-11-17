## Install ssh server on vm

```bash
sudo apt install openssh-server
```

check status

```bash
sudo systemctl status ssh
```

start/enable server

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Open the ssh port

```bash
sudo ufw allow ssh
```

note the vm Ip adress

```bash
ifconfig
```

note the vm user

```bash
whoami
```

Then on host pc acces the vm via ssh

```bash
ssh user@ipAdress
```

Trace ssh logs

```bash
sudo journalctl -u ssh -f
```
