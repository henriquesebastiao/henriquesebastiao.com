---
title: How to use an encrypted external hard drive on a Linux server
description: How to configure an encrypted external hard drive for use on a Linux server and map directories for use in services like Jellyfin via Docker.
author: henriquesebastiao
date: 2026-01-18 23:47:00 -0400
categories: [Linux, Docker]
tags: [linux, cli, docker, docker-compose, self-host]
post_image:
  path: img/2026-01-18-post_image.jpg
  alt: Seagate external hard drive Photo by <a href="https://unsplash.com/pt-br/@uwukuriemery?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Uwukuri Emery</a> on <a href="https://unsplash.com/pt-br/fotografias/um-close-up-de-um-porta-cartao-preto-em-uma-superficie-de-madeira-se1G--2c6JU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
---

Some time ago I bought a Lenovo ThinkCentre minicomputer to use as my personal server, a sort of homelab, but I end up using it in "production" these days, either to host my personal projects or self-hosted tools I use. Anyway, this server itself and what I run on it are topics for another post.

It only has 512 GB of storage via a SATA SSD, which is quite modest and enough for me to have some fun. One of the services I run on the server and use most often on a daily basis (actually every day) is [Jellyfin](https://jellyfin.org/){:target="_blank"}, an open-source, self-hosted video and audio streaming tool under my control; **it's like my personal Netflix and Spotify, and best of all, it's free**.

Jellyfin works very well; however, it's up to the user to download the content that will be hosted on it, such as music, movies, series, etc. Because of this, a more hardcore user could quickly fill up the limited 512 GB of storage, which hasn't been my case so far, since I've only downloaded a few movies and songs and consumed them for a while. However, I want to download some video lessons from courses and put them on my Jellyfin so I can watch them more conveniently, even from outside my house. For that, I need more storage.

To my delight, I have a 1TB hard drive that I'm not using, or rather, wasn't using until now. The initial problem is that my server doesn't have the space or slots to install a 3.5" hard drive. Furthermore, **the hard drive is encrypted**, and I have no motivation to format it. And to make matters worse, I'd like to keep it external to the server so I can easily transport it if needed.

I'd been thinking for a while that it would be possible to use it with the server under these conditions. But I kept procrastinating, putting off taking the time to research how to configure it, but that's over today. And I'm here to describe the process, so I can even look it up someday.

## Identify the external hard drive.

First, I plugged my external hard drive into the server via a USB 3.0 port to ensure the highest possible transfer rate and used the `lsblk` command to check the device name:

```
hick@server:~$ lsblk
NAME                      MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
loop0                       7:0    0  66,8M  1 loop  /snap/core24/1243
loop2                       7:2    0  66,8M  1 loop  
loop3                       7:3    0 140,6M  1 loop  /snap/docker/3265
loop4                       7:4    0 151,4M  1 loop  /snap/docker/3377
loop5                       7:5    0  66,8M  1 loop  /snap/core24/1267
loop6                       7:6    0  50,9M  1 loop  /snap/snapd/25577
loop7                       7:7    0  73,9M  1 loop  /snap/core22/2216
loop8                       7:8    0    74M  1 loop  /snap/core22/2193
loop9                       7:9    0  48,1M  1 loop  /snap/snapd/25935
sda                         8:0    0 476,9G  0 disk  
├─sda1                      8:1    0     1M  0 part  
├─sda2                      8:2    0     2G  0 part  /boot
└─sda3                      8:3    0 474,9G  0 part  
  └─ubuntu--vg-ubuntu--lv 252:0    0 474,9G  0 lvm   /
sdb                         8:16   0 931,5G  0 disk  
└─sdb1                      8:17   0 931,5G  0 part
```

Here we can see that my device is `/dev/sdb1`.

## Unlock the encrypted disk

Since my hard drive is encrypted, the next step will be to unlock it using the `cryptsetup` tool:

```bash
sudo cryptsetup luksOpen /dev/sdb1 hd_externo
```

Where `/dev/sdb1` is the encrypted partition and `hd_externo` is the logical name I chose to identify my disk. Now it will appear as `/dev/mapper/hd_externo`.

Enter the password used to encrypt the disk when prompted.

## Mount the disc

Now we need to mount the disk. To do this, we create a mount point using the following command:

```bash
sudo mkdir -p /mnt/hd_externo
```

To mount the disk, we will run:

```bash
sudo mount /dev/mapper/hd_externo /mnt/hd_externo
```

To verify that the disk was mounted correctly, run:

```bash
df -h
```

You should receive a response like the following on the last line.

```
hick@server:~$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              1,6G  5,6M  1,6G   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  467G  238G  210G  54% /
tmpfs                              7,8G     0  7,8G   0% /dev/shm
tmpfs                              5,0M     0  5,0M   0% /run/lock
/dev/sda2                          2,0G  197M  1,6G  11% /boot
tmpfs                              1,6G   12K  1,6G   1% /run/user/1000
/dev/mapper/hd_externo             916G  318G  552G  37% /mnt/hd_externo
```

## Remove the disk when you are finished using it.

If you wish to use the hard drive only temporarily on your server, it is important to properly unmount your disk to avoid any potential damage. To do this, run the following command to unmount and re-lock your disk.

```bash
sudo umount /mnt/hd_externo
sudo cryptsetup luksClose hd_externo
```

## Mounting the disk automatically

In my case, **to use the disk continuously with the server** for file storage, **it's important that it's automatically mounted whenever the server restarts**; for that, we'll need some additional configurations.

To automatically mount the disk during server boot without needing to enter the unlock password, we will create a random 4 KB keyfile using the following command:

```bash
sudo dd if=/dev/urandom of=/root/hd_externo.key bs=4096 count=1
```

Now we will protect our keyfile so that only the root user has access to it.

```bash
sudo chmod 600 /root/hd_externo.key
sudo chown root:root /root/hd_externo.key
```

We checked if only root has access to that file.

```bash
ls -l /root/hd_externo.key
```

It should say something like `-rw------- 1 root root`:

```
root@server:/home/hick# ls -l /root/hd_externo.key
-rw------- 1 root root 4096 jan 18 23:03 /root/hd_externo.key
```

Now we'll **add the keyfile as a new key to unlock our disk**, without removing the current password.

```bash
sudo cryptsetup luksAddKey /dev/sdb1 /root/hd_externo.key
```

Enter **the current disk password** when prompted.

Now, to test if the key was added successfully, close the disk if it is unlocked using the following command:

```bash
sudo cryptsetup luksClose hd_externo
```

Now try unlocking the disk using the keyfile:

```bash
sudo cryptsetup luksOpen /dev/sdb1 hd_externo --key-file /root/hd_externo.key
```

If it unlocks without asking for a password, it means everything is fine 😉.

Now, in order for the device to be unlocked correctly during server boot, we need to make two more configurations.

Add the line `hd_externo /dev/sdb1 /root/hd_externo.key luks` to the `/etc/crypttab` file using the following command:

```bash
sudo echo "hd_externo /dev/sdb1 /root/hd_externo.key luks" >> /etc/crypttab
```

Where `hd_externo` is the mapper name, `/dev/sdb1` is the encrypted partition, `/root/hd_externo.key` is the keyfile, and `luks` is the encryption type.

And add the line `/dev/mapper/hd_externo /mnt/hd_externo ext4 defaults,nofail 0 2` to the `/etc/fstab` file using the following command:

```bash
sudo echo "/dev/mapper/hd_externo /mnt/hd_externo ext4 defaults,nofail 0 2" >> /etc/fstab
```

> Use `nonfail` to avoid booting if the hard drive is not connected.
> Adjust `ext4` if the filesystem is different (`xfs`, `btrfs`, etc).
{: .prompt-warning }

Now, for the changes to take effect, restart the cryptsetup daemon and remount the disks with the following command:

```bash
sudo systemctl restart systemd-cryptsetup@hd_externo
sudo mount -a
```

Now if you run `ls` inside `/mnt/hd_externo` you will be able to see your files :)

```
root@server:/mnt/hd_externo# ls
estudos  lost+found  Videos
```

## Accessing hard drive files via the web using a filebrowser.

One of the tools I use to manage files on my server quickly and easily without necessarily needing an FTP or SSH client is [filebrowser](https://github.com/filebrowser/filebrowser){:target="_blank"}.

To access the files on the hard drive via the file browser, I simply mapped the contents of `/mnt/hd_externo` on the server to a folder called `hd` within the file browser. See the configuration in `docker-compose.yml` below:

```yaml
filebrowser:
    image: filebrowser/filebrowser:v2.54.0
    container_name: filebrowser
    restart: unless-stopped
    user: "0:0" # Run as root to avoid permission issues
    ports:
      - 8015:80
    volumes:
      - filebrowser_data:/srv
      - filebrowser_database:/database
      - filebrowser_config:/config
      - /home/hick:/data
      - /mnt/hd_externo:/data/hd
    environment:
      - FB_ROOT=/data
      - FB_NOAUTH=true
```

In the image below you can see the `hd` folder mapped to `/data/hd` within the file browser:

![Desktop View](img/2026-01-18-filebrowser.png)
_filebrowser screenshot_

## Accessing hard drive media via Jellyfin

To access my media files from my hard drive using Jellyfin, I only had to perform a configuration similar to the one I did in FileBrowser, but this time mapping the folder `/mnt/hd_externo/Videos` to the folder `/media/hd/Videos` inside the Jellyfin container. See how the `docker-compose.yml` file looks:

```yaml
jellyfin:
    image: jellyfin/jellyfin:10.11.5
    container_name: jellyfin
    network_mode: 'host'
    volumes:
      - /home/hick/homelab/containers/jellyfin/config:/config
      - /home/hick/homelab/containers/jellyfin/cache:/cache
      - type: bind
        source: /home/hick/homelab/containers/jellyfin/media
        target: /media
      - type: bind
        source: /mnt/hd_externo/Videos
        target: /media/hd/Videos
    restart: 'unless-stopped'
    # Optional - alternative address used for autodiscovery
    environment:
      - JELLYFIN_PublishedServerUrl=http://server.local:8096
```