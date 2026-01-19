---
title: Como usar um HD externo criptografado em um servidor Linux
description: Como configurar um HD externo criptografado para uso em um servidor Linux e mapear diretórios para uso em serviços como Jellyfin via Docker
author: henriquesebastiao
date: 2026-01-18 23:47:00 -0400
categories: [Linux, Docker]
tags: [linux, cli, docker, docker-compose, self-host]
post_image:
  path: img/2026-01-18-post_image.jpg
  alt: HD externo Seagate Foto de <a href="https://unsplash.com/pt-br/@uwukuriemery?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Uwukuri Emery</a> no <a href="https://unsplash.com/pt-br/fotografias/um-close-up-de-um-porta-cartao-preto-em-uma-superficie-de-madeira-se1G--2c6JU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
---

Há algum tempo comprei minicomputador da Lenovo, um ThinkCentre, para usá-lo como meu servidor pessoal como uma espécie de *homelab*, mas meio que acabo usando ele em “produção” hoje em dia, seja para hospedar meus projetos pessoais, ou ferramentas *self-hosted* que utilizo. De qualquer forma este servidor em si e o que rodo nele são assunto para outro post.

Ele possui apenas 512 GB de armazenamento por meio de um SSD SATA, o que é bem modesto e o bastante para que eu já possa me divertir. Um dos serviços que executo no servidor e que mais uso no dia a dia (de fato todo dia) é o [Jellyfin](https://jellyfin.org/){:target="_blank"}, uma ferramenta open source de streaming de vídeo e áudio auto-hospedada e sob meu controle, **é como se fosse meu Netflix e Spotify pessoal e o melhor, gratuito**.

O Jellyfin funciona muito bem, no entanto, cabe ao usuário baixar os conteúdos que serão hospedados nele, como músicas, filmes, séries, etc. Com isso um usuário mais *hardcore* poderia ocupar os poucos 512 GB de armazenamento rapidamente, o que não foi o meu caso até agora, uma vez que baixei alguns poucos filmes e músicas e fiquei consumindo eles por um tempo. Entretanto, desejo baixar algumas vídeo aulas de cursos e quero colocá-las no meu Jellyfin para poder assisti-las com mais comodidade e até mesmo de fora da minha casa. Para isso preciso de mais armazenamento.

Para minha felicidade eu tenho um HD de 1 TB parado e que não estou utilizando, ou melhor, não estava até agora. O problema inicial é que meu servidor não tem espaço nem slots para instalar um HD de 3,5”, além disso, **o HD é criptografado** e não tenho motivação alguma para o formatar e como se não bastasse, gostaria de mantê-lo externo ao servidor para transportá-lo com facilidade caso fosse preciso.

Eu já vinha pensando há algum tempo que seria possível usá-lo com o servidor nessas condições. Mas estava procrastinando para reservar um tempo e pesquisar como configurá-lo, hoje isso acabou. E venho descrever aqui como foi o processo, até mesmo para que eu possa me relembrar um dia.

## Identificar o HD externo

Primeiro pluguei meu HD externo ao servidor por meio de uma porta USB 3.0 para garantir a maior taxa de transferência possível e utilizei o comando `lsblk` para verificar o nome do dispositivo:

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

Aqui podemos ver que meu dispositivo é o `/dev/sdb1`.

## Desbloquear o disco criptografado

Como meu HD é criptografado, o próximo passo vai ser desbloqueá-lo usando a ferramenta `cryptsetup`:

```bash
sudo cryptsetup luksOpen /dev/sdb1 hd_externo
```

Onde `/dev/sdb1` é a partição criptografada e `hd_externo` o nome lógico que escolhi para identificar meu disco. Agora ele aparecerá como `/dev/mapper/hd_externo`.

Digite a senha utilizada para criptografar o disco quando ela for solicitada.

## Montar o disco

Agora precisamos montar o disco, para isso criamos um ponto de montagem com o seguinte comando:

```bash
sudo mkdir -p /mnt/hd_externo
```

Para montar o disco vamos executar:

```bash
sudo mount /dev/mapper/hd_externo /mnt/hd_externo
```

Para verificar se o disco foi montado corretamente execute:

```bash
df -h
```

Você deve receber um retorno como o seguinte na última linha.

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

## Desmontar o disco quando terminar de usar

Caso deseje usar o HD apenas temporariamente em seu servidor é importante o fim do processo, desmontar adequadamente seu disco para evitar quais eventuais danos, para isso execute o seguinte comando para desmontar e bloquear novamente seu disco.

```bash
sudo umount /mnt/hd_externo
sudo cryptsetup luksClose hd_externo
```

## Montando o disco automaticamente

No meu caso, para **usar o disco continuamente com o servidor** para armazenamento de arquivos é **importante que o mesmo seja montado automaticamente sempre que o servidor reiniciar**, para isso precisaremos de algumas configurações a mais.

Para montar o disco automaticamente durante o boot do servidor sem a necessidade de digitar a senha de desbloqueio iremos criar um arquivo keyfile aleatório de 4 KB com o seguinte comando:

```bash
sudo dd if=/dev/urandom of=/root/hd_externo.key bs=4096 count=1
```

Agora iremos proteger nosso keyfile para que apenas o usuário root tenha acesso a ele.

```bash
sudo chmod 600 /root/hd_externo.key
sudo chown root:root /root/hd_externo.key
```

Verificamos se apenas o root tem acesso a esse arquivo.

```bash
ls -l /root/hd_externo.key
```

Deve aparecer algo como `-rw------- 1 root root`:

```
root@server:/home/hick# ls -l /root/hd_externo.key
-rw------- 1 root root 4096 jan 18 23:03 /root/hd_externo.key
```

Agora vamos **adicionar o keyfile como uma nova chave** para desbloquear nosso disco, sem remover a senha atual.

```bash
sudo cryptsetup luksAddKey /dev/sdb1 /root/hd_externo.key
```

Digite a **senha atual do disco** quando for solicitada.

Agora para testar se a chave foi adicionada com sucesso, feche o disco se ele estiver desbloqueado com o seguinte comando:

```bash
sudo cryptsetup luksClose hd_externo
```

Agora teste desbloquear o disco usando o keyfile:

```bash
sudo cryptsetup luksOpen /dev/sdb1 hd_externo --key-file /root/hd_externo.key
```

Se desbloquear sem pedir senha significa que está tudo certo 😉.

Agora para o dispositivo seja desbloqueado corretamente durante o boot do servidor precisamos fazer mais duas configurações.

Adicione a linha `hd_externo /dev/sdb1 /root/hd_externo.key luks` ao arquivo `/etc/crypttab` com seguinte comando:

```bash
sudo echo "hd_externo /dev/sdb1 /root/hd_externo.key luks" >> /etc/crypttab
```

Onde `hd_externo` é o nome do mapper, `/dev/sdb1` é a partição criptografada, `/root/hd_externo.key` é o keyfile e `luks` é o tipo de criptografia.

E adicione a linha `/dev/mapper/hd_externo /mnt/hd_externo ext4 defaults,nofail 0 2` ao arquivo `/etc/fstab` com o seguinte comando:

```bash
sudo echo "/dev/mapper/hd_externo /mnt/hd_externo ext4 defaults,nofail 0 2" >> /etc/fstab
```

> Use `nonfail` para evitar travar o boot se o HD não estiver conectado.
> Ajuste `ext4` se o filesystem for outro (`xfs`, `btrfs`, etc).
{: .prompt-warning }

Agora para que as mudanças entrem em vigor reinicie o deamon do cryptsetup e monte de volta os discos com o seguinte comando:

```bash
sudo systemctl restart systemd-cryptsetup@hd_externo
sudo mount -a
```

Agora se executar um `ls` dentro de `/mnt/hd_externo` você será capaz de ver seus arquivos :)

```
root@server:/mnt/hd_externo# ls
estudos  lost+found  Videos
```

## Acessando os arquivos do HD via web por meio do filebrowser

Umas das ferramentas que utilizo para manusear os arquivos do meu servidor de maneira prática e rápida sem precisar necessariamente de um cliente FTP o SSH é o [filebrowser](https://github.com/filebrowser/filebrowser){:target="_blank"}.

Para poder acessar os arquivos do HD pelo filebrowser apenas mapeei o conteúdo de `/mnt/hd_externo` do servidor para uma pasta chamada `hd` dentro o filebrowser, veja como ficou a configuração no `docker-compose.yml`:

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

Na imagem abaixo você pode ver a pasta `hd` mapeada para `/data/hd` dentro do filebrowser:

![Desktop View](img/2026-01-18-filebrowser.png)
_Captura de tela do filebrowser_

## Acessando as mídias do HD pelo Jellyfin

Para consumir meus arquivos de mídia presentes no HD pelo Jellyfin tive apenas que realizar uma configuração semelhante à feita no filebrowser, mas desta vez mapeando a pasta `/mnt/hd_externo/Videos` para a pasta `/media/hd/Videos` dentro do contêiner do Jellyfin, veja como ficou o `docker-compose.yml`:

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