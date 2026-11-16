# 01 · Linux

**Estimate:** 3 weeks · **Environment:** Ubuntu Server (VM via Multipass/UTM, or a cheap cloud VM)

## Objectives

- Administer a Linux server from the terminal only.
- Manage users, permissions, processes, services and logs.
- Connect securely over SSH and automate routine tasks with Bash.

## Labs and checkpoints

### Lab 01.1 — Terminal and filesystem

- [ ] Navigate the filesystem hierarchy and explain `/etc`, `/var`, `/home`, `/opt`, `/tmp`
- [ ] Use `find`, `grep`, `less`, `head`, `tail -f`, pipes and redirections
- [ ] Edit files with `vim` or `nano` without leaving the terminal

### Lab 01.2 — Users, groups and permissions

- [ ] Create users and groups, add a user to `sudo`
- [ ] Explain and set `rwx`, octal modes, `chown`, `chmod`
- [ ] Explain setuid, setgid and the sticky bit with one example each

### Lab 01.3 — Processes, services and logs

- [ ] Inspect processes with `ps`, `top`/`htop`, send signals with `kill`
- [ ] Create a **systemd service** that runs the [Tasks API](../app/) and restarts on failure
- [ ] Read service logs with `journalctl -u <service> -f`

### Lab 01.4 — Packages, disks and resources

- [ ] Install and remove packages with `apt`
- [ ] Check disk usage (`df`, `du`) and memory (`free`)
- [ ] Find which process listens on a port (`ss -tulpn`)

### Lab 01.5 — SSH

- [ ] Generate an SSH key pair and log in with key authentication
- [ ] Disable password and root login in `sshd_config`
- [ ] Use `~/.ssh/config` and copy files with `scp` or `rsync`

### Lab 01.6 — Bash scripting

- [ ] Write a script with variables, conditions, loops and functions
- [ ] Handle errors with `set -euo pipefail` and exit codes
- [ ] Write a **backup script** (archive + rotation) and schedule it with `cron` or a systemd timer

## Module done when

- [ ] I can set up a fresh server, deploy the Tasks API as a service and secure SSH **without notes**
- [ ] `cheatsheet.md` written in my own words

## Resources

- [Ubuntu Server documentation](https://documentation.ubuntu.com/server/)
- `man` pages — always first
