# 01 · Linux

**Estimate:** 3 weeks · **Environment:** Ubuntu Server (VM via Multipass/UTM, or a cheap cloud VM)

## 🎯 Objectives

By the end of this module, I can:

- Navigate and manage the filesystem using only the terminal
- Manage users, groups and permissions, and explain setuid, setgid and the sticky bit
- Inspect processes and run an application as a **systemd service** with logs in journald
- Connect securely with SSH keys and harden an SSH server
- Write robust Bash scripts and schedule them (cron or systemd timers)
- Diagnose disk, memory and port problems on a server

**Prerequisites:** none — this is the starting point.

## Labs and checkpoints

### Lab 01.1 — Terminal and filesystem

- [x] Navigate the filesystem hierarchy and explain `/etc`, `/var`, `/home`, `/opt`, `/tmp`
- [x] Use `find`, `grep`, `less`, `head`, `tail -f`, pipes and redirections
- [x] Edit files with `vim` or `nano` without leaving the terminal

### Lab 01.2 — Users, groups and permissions

- [x] Create users and groups, add a user to `sudo`
- [x] Explain and set `rwx`, octal modes, `chown`, `chmod`
- [x] Explain setuid, setgid and the sticky bit with one example each

### Lab 01.3 — Processes, services and logs

- [x] Inspect processes with `ps`, `top`/`htop`, send signals with `kill`
- [x] Create a **systemd service** that runs the [Tasks API](../app/) and restarts on failure
- [x] Read service logs with `journalctl -u <service> -f`

### Lab 01.4 — Packages, disks and resources

- [x] Install and remove packages with `apt`
- [x] Check disk usage (`df`, `du`) and memory (`free`)
- [x] Find which process listens on a port (`ss -tulpn`)

### Lab 01.5 — SSH

- [x] Generate an SSH key pair and log in with key authentication
- [x] Disable password and root login in `sshd_config`
- [x] Use `~/.ssh/config` and copy files with `scp` or `rsync`

### Lab 01.6 — Bash scripting

- [x] Write a script with variables, conditions, loops and functions
- [x] Handle errors with `set -euo pipefail` and exit codes
- [x] Write a **backup script** (archive + rotation) and schedule it with `cron` or a systemd timer

## Module done when

- [x] I can set up a fresh server, deploy the Tasks API as a service and secure SSH **without notes**
- [x] `cheatsheet.md` written in my own words

## Free courses and labs

- [Linux Upskill Challenge](https://linuxupskillchallenge.org/) — free month-long course: administer a remote Ubuntu server from the command line (**main course for this module**)
- [Introduction to Linux (LFS101)](https://training.linuxfoundation.org/training/introduction-to-linux/) — Linux Foundation, free
- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) — terminal game to drill commands, permissions and SSH
- [Linux Journey](https://linuxjourney.com/) — short interactive lessons
- [The Linux Command Line (free book)](https://linuxcommand.org/tlcl.php) — reference for Bash and scripting
- [Killercoda playgrounds](https://killercoda.com/playgrounds) — a free Ubuntu VM in the browser
