## Show hardware information

`lshw` to list hardware components
`lscpu` to display information about the CPU architecture
`lsblk` to list block devices
`lspci` to list all PCI devices
`lsusb` to list USB devices

## Memory and CPU usages

`free -h` and `vmstat` to list memory usage
`df -h` to list hard disk usage

## Network

`ifconfig` of `ip address` to show network interfaces and ip addresses
`ss` show socket status

## Navigate the file system

cd, cd -, pushd, popd

## Open files

cat, nano, more ,less

## Find Things

which, find, which ,grep

## Users and Group

```bash
## add user
sudo add user $username
## give password
sudo passwd $username

## adding a new group
sudo groupadd $groupname

## adding a user to an existing group
usermod -a -G $groupname $username
```

## compressing files

`gzip -vk $file` : to compress and keep the uncompressed file. remove the `-vk` argument to replace the original file
`gzip d $file.gz` : to decompress the file
