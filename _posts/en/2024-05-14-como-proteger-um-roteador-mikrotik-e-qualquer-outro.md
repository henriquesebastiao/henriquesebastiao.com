---
title: How to secure a Mikrotik router (and any other)
description: Techniques and best practices to protect your RouterOS router against malicious attacks.
author: henriquesebastiao
date: 2024-05-16 17:00:00 -0400
categories: [Network, Mikrotik]
tags: [mikrotik, security, network, firewall]
image: img/preview-image-posts/2024/en/2024-05-16.png
---

Since 2021, I have been working predominantly as a network technician. I am really the guy on the technical support field. In the meantime, I never really needed to learn how to configure Mikrotik routers, but since I ended up getting interested and later enrolled in a higher education technology course, I kind of got into this world out of enthusiasm.

I have been thinking for some time about the negligence that many people, and even companies, end up having when configuring Mikrotik routers, leaving their networks completely vulnerable to possible attacks. Obviously, this should not be the intention, but some things end up going unnoticed by the less experienced eye. In view of this failure, today I come to share a little of everything I have learned in life, from mistakes and from other people much more capable than me.

> Most of the steps mentioned in this article are aimed at Mikrotik routers, but the concepts can be applied to any other routers, and even other types of devices.
{: .prompt-info }

## Information security principles

The security of a computer system concerns the guarantee of some fundamental properties associated with the information and resources present in the system. When we say “information”, we are referring to all the resources available in the system such as processing, files, memory, network traffic, configurations, etc.

For Nieles, Dempsey and Pillitteri (2017), the term “computer security” can be defined as the protection offered to an automated information system in order to guarantee the applicable objectives of preserving the **integrity**, **availability** and **confidentiality** of the information system resources, which includes hardware, software, firmware, information, data and telecommunications.

- **Integrity**: the system resources can only be modified or destroyed by users authorized to perform such operations;
- **Availability**: the resources must be available to users who have the right to use them, at any time;
- **Confidentiality**: the resources present in the system can only be consulted by users duly authorized to do so.

## The most common mistake

The most common error, and without a doubt the most problematic, is routers with default login and password:

- User: `admin`
- Password: blank

If your router is receiving a public IP (also called a valid IP by some network professionals) or even if it is behind a NAT that does not have a firewall to protect you, this will probably be your first problem. Every device that is accessible from the internet is a constant target of unauthorized access attempts by malicious agents spread all over the world, who try to invade your device in order to turn it into a bot to attack third parties. You may not necessarily be the target, but if your device is invaded, it will be used as a puppet, integrating a network (called a botnet) with thousands of other infected IoT devices, in order to carry out [DDoS](https://www.cloudflare.com/pt-br/learning/ddos/what-is-a-ddos-attack/){:target="_blank"} attacks and whatever else comes to the attacker's mind. A famous case is the [Mirai](https://www.cloudflare.com/pt-br/learning/ddos/glossary/mirai-botnet/){:target="_blank"} botnet.

Therefore, make sure to configure a user with a sufficiently secure password for your router, with uppercase and lowercase letters, numbers and special characters.

## Some good practices

Okay, so we know that it's not at all professional to leave default logins and passwords on our devices, and we set them up at the first opportunity. Now let's move on to the good habits to follow.

### Keep your router always updated

It is crucial to keep your router’s firmware up to date. Firmware updates often contain new features and security fixes that can protect your router from the latest threats. Therefore, it is recommended to regularly check if there are firmware updates available for your router.

In the programming world, I have heard people say, “Oh, I use Python 3.7 because it is more stable…”. The problem is that this argument falls apart as quickly as it is said. If this version were stable and reliable, there would be no new versions released with only bug fixes.

The same goes for routers. Most network professionals still use relatively old firmware versions to this day, a quick search for Mikrotik devices on [Shodan.io](https://www.shodan.io/){:target="_blank"} shows this:

Here we see version 6.48.6 being used by most Mikrotik devices visible on the internet, this version was announced on December 12, 2021, and currently at the time of writing this article, the latest v6 version of RouterOS is 6.49.13 (long-term). The problem is that version 6.48.6 itself has known vulnerabilities, as described below.

> [CVE-2023-30799](https://nvd.nist.gov/vuln/detail/CVE-2023-30799){:target="_blank"} - MikroTik RouterOS before 6.49.7 (stable) and up to 6.48.6 (long-term) are vulnerable to a privilege escalation issue. An authenticated, remote attacker may be able to escalate privileges from administrator to super administrator in Winbox or HTTP interface. The attacker could abuse this vulnerability to execute arbitrary code on the system.
{: .prompt-danger }

Another vulnerability that became quite well known in Mikrotik routers was the [CVE-2018-14847](https://nvd.nist.gov/vuln/detail/CVE-2018-14847){:target="_blank"}, in which it was possible to obtain the users and passwords of a router up to version 6.42 through a simple script. See an example of an attack carried out in a laboratory that takes advantage of this flaw:

{% include embed/youtube.html id='fMki-cDjb64' %}

Even if you are not the most up-to-date person on the news, make sure to keep your device up to date, this way you will be protected against the most known vulnerabilities. In the terminal of your Mikrotik, you can check for new updates with the following command:

```bash
/system/package/update/check-for-updates
```
{: .nolineno }

### Change the default ports and disable the ones you don't use

Another good security practice is to change your router’s default ports. This can help prevent automated attacks that target well-known ports. Additionally, it’s important to disable any services or ports that aren’t being used, as this can reduce your router’s exposure to potential vulnerabilities.

Well-known ports such as SSH, HTTP and WINBOX exposed on the internet are frequently targeted by login attempts by [bruteforce](https://en.wikipedia.org/wiki/Brute-force_attack){:target="_blank"}, below are listed the default ports used by Mikrotik and their respective services:

- api: 8728
- api-ssl: 8729
- ftp: 21
- ssh: 22
- telnet: 23
- winbox: 8291
- www (http): 80
- www-ssl: 443

Searching on Shodan for open ports on Mikrotik routers shows that most devices use the default ports, both for Winbox (8291) and for HTTP (80).

To change the default port of a service, you can use the command below in the terminal:

```bash
/ip/service/set ssh port=2222
```
{: .nolineno }

In the above example, we are changing the SSH service port to 2222.

Bad actors can use software like [Nmap](https://nmap.org/){:target="_blank"} and [Hydra](https://github.com/vanhauser-thc/thc-hydra){:target="_blank"} to scan your router and try to brute force your passwords. Therefore, it is essential to change the default ports to make it more difficult for unauthorized access to your device.

## Hands on

Now that we know which habits to practice to make it harder for unauthorized access to our routers, let's move on to the cherry on the cake when it comes to router security: **firewall rules**.

Firewall rules are your router's last line of defense against external attacks. They allow you to control incoming and outgoing traffic from your router, blocking or allowing specific connections. We will detail how to configure effective firewall rules in the following steps.

A brief explanation of what each firewall rule chain means:

- `input`: This chain is used to process packets destined for the router itself.
- `forward`: This chain is used to process packets that are just passing through the router, that is, packets that are not destined for the router itself.
- `output`: This chain is used to process packets that originate from the router itself.

> Pay attention to all comments and warnings before applying each DROP rule below.
{: .prompt-danger }

### Creating the LAN network address list

First we need to create our ADDRESS LIST with all the IPs that we will use in most cases.

**Below you need to change xxxx/x to your management subnet. This subnet will have full access to the router.**

```bash
/ip firewall address-list add address=x.x.x.x/x disabled=no list=support
```
{: .nolineno }

Now we will create the address list `not_in_internet` that contains all possible LAN network IPs.

```bash
/ip firewall address-list
add address=0.0.0.0/8 comment="Self-Identification [RFC 3330]" disabled=no list=not_in_internet
add address=10.0.0.0/8 comment="Private[RFC 1918] - CLASS A # Check if you need this subnet before enable it" disabled=yes list=not_in_internet
add address=127.0.0.0/8 comment="Loopback [RFC 3330]" disabled=no list=not_in_internet
add address=169.254.0.0/16 comment="Link Local [RFC 3330]" disabled=no list=not_in_internet
add address=172.16.0.0/12 comment="Private[RFC 1918] - CLASS B # Check if you need this subnet before enable it" disabled=yes list=not_in_internet
add address=192.168.0.0/16 comment="Private[RFC 1918] - CLASS C # Check if you need this subnet before enable it" disabled=yes list=not_in_internet
add address=192.0.2.0/24 comment="Reserved - IANA - TestNet1" disabled=no list=not_in_internet
add address=192.88.99.0/24 comment="6to4 Relay Anycast [RFC 3068]" disabled=no list=not_in_internet
add address=198.18.0.0/15 comment="NIDB Testing" disabled=no list=not_in_internet
add address=198.51.100.0/24 comment="Reserved - IANA - TestNet2" disabled=no list=not_in_internet
add address=203.0.113.0/24 comment="Reserved - IANA - TestNet3" disabled=no list=not_in_internet
add address=224.0.0.0/4 comment="MC, Class D, IANA # Check if you need this subnet before enable it" disabled=yes list=not_in_internet
```
{: .nolineno }

Accepting valid connections and rejecting invalid ones that have the router as their destination.

```bash
/ip firewall filter
add action=accept chain=input comment="Accepts established and related connections" connection-state=established,related
add action=drop chain=input comment="Discards invalid connections" connection-state=invalid
```
{: .nolineno }

### Opening access ports

Now we will open all protocols that we use on our router and block all those that we do not use to reduce the attack surface. To open access via SSH, Winbox and Webfig to the management subnet, we use the following rules:

```bash
add action=accept chain=input comment="Release SSH" dst-port=2222 protocol=tcp src-address-list=support
add action=accept chain=input comment="Release Winbox" dst-port=8291 protocol=tcp src-address-list=support
add action=accept chain=input comment="Release Webfig (HTTP)" dst-port=80 protocol=tcp src-address-list=support
```
{: .nolineno }

### Releasing necessary services

Now let's add all the rules that our router needs to work in a scenario where it is receiving an internet link via DHCP client through the `ether1` interface and provides a DHCP server for devices connected to the LAN network.

> Make sure that you have released the entry of all the protocols you need before applying any DROP rule! Here is the link to the official Mikrotik documentation that lists the protocols and their respective service ports: [https://help.mikrotik.com/docs/display/ROS/Services](https://help.mikrotik.com/docs/display/ROS/Services){:target="_blank"}
{: .prompt-warning }

Adding the necessary rules:

```bash
/ip firewall filter
add action=accept chain=input comment="Accept ICMP" in-interface=ether1 protocol=icmp
add action=accept chain=input comment="Accept DHCP Client" dst-port=68 in-interface=ether1 protocol=udp
add action=accept chain=input comment="Accept DHCP Server" dst-port=67 in-interface=ether1 protocol=udp
add action=accept chain=input comment="Release DNS TCP" dst-port=53 in-interface=ether1 protocol=tcp
add action=accept chain=input comment="Release DNS UDP" dst-port=53 in-interface=ether1 protocol=udp
```
{: .nolineno }

### Adding LAN Network Defense Rules

Now we can add firewall rules to handle the traffic passing through the router.

> “bridge” is the local network interface.
{: .prompt-info }

```bash
/ip firewall filter
add action=drop chain=forward comment="Blocks connections trying to reach non-public LAN addresses" dst-address-list=not_in_internet in-interface=bridge log=yes log-prefix=!public_from_LAN out-interface=!bridge
add action=drop chain=forward comment="Discard incoming packets that are not NAT" connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix=!NAT
add action=drop chain=forward comment="Drop the Internet entry that is not a public IP" in-interface=ether1 log=yes log-prefix=!public src-address-list=not_in_internet
```
{: .nolineno }

### Port Knocking

Let's assume that you are configuring a router that is receiving a public IP, but you want to allow access to it only for your home or office IP address. And if by chance during a trip you need to access it remotely for some reason. One approach to solve this problem is using the Port Knocking technique.

Port Knocking is a security technique that involves "knocking" (or connecting) to a predefined sequence of network ports to gain access to a service. This technique is generally used to hide services such as SSH or Telnet from port scanners.

In our example, we can use knocking so that after "knocking" on certain ports, our public IP address is added to the list of allowed access for a certain period of time.

We can use the following sequence of commands to implement Port Knocking in Mikrotik:

```bash
/ip firewall filter
add action=add-src-to-address-list address-list=knock1 address-list-timeout=5s chain=input comment="Port Knock - Stage1 - TCP 50000" dst-address=10.0.0.0/24 dst-port=50000 in-interface=ether1 protocol=tcp
add action=add-src-to-address-list address-list=knock2 address-list-timeout=5s chain=input comment="Port Knock - Stage2 - UDP 5000" dst-address=10.0.0.0/24 dst-port=5000 in-interface=ether1 protocol=udp src-address-list=knock1
add action=add-src-to-address-list address-list=support address-list-timeout=30m chain=input comment="Port Knock - Stage3 - TCP 40000 - RELEASED por 30min" dst-address=10.0.0.0/24 dst-port=40000 in-interface=ether1 protocol=tcp src-address-list=knock2
```
{: .nolineno }

Each rule above is part of a sequence of "knocks". Here's what each rule does, step by step:

1. The first rule adds the source IP address to the `knock1` list of addresses if a connection is made on port 50000 over TCP. The IP address is removed from the list after 5 seconds.

2. The second rule adds the source IP address to the `knock2` list of addresses if a connection is made on port 5000 over UDP. The IP address is removed from the list after 5 seconds.

3. The third rule adds the source IP address to the `support` list of addresses if a connection is made on port 40000 over TCP. The IP address is removed from the list after 30 minutes.

After that, you can configure your firewall to allow connections from IP addresses in the `support` list. This means that an attacker would have to guess the correct sequence of ports to "knock" in order to gain access to your router. This is a great way to hide services like SSH or Winbox from port scanners and increase the security of your router.

## Blocking everything that is not necessary

Now comes the tricky part, we will create the firewall rule that blocks everything that was not previously allowed. This should be the last rule on your list.

> Make sure you have enabled all the services you need before proceeding.
{: .prompt-danger }

```bash
/ip firewall filter add action=drop chain=input comment="Block everything else!"  # DO NOT ACTIVATE THIS RULE UNTIL YOU ARE SURE YOU HAVE ALL THE ACCEPTANCE RULES YOU NEED" disabled=yes
```
{: .nolineno }
