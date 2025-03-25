---
title: Como proteger um roteador Mikrotik (e qualquer outro)
description: Técnicas e boas práticas para proteger seu roteador RouterOS contra ataques maliciosos.
author: henriquesebastiao
date: 2024-05-16 17:00:00 -0400
categories: [Network, Mikrotik]
tags: [mikrotik, security, network, firewall]
image: /480a268a-49e3-458c-df9f-748528b4a100/public
---

Desde o ano de 2021 tenho trabalhado predominantemente como técnico de redes, eu realmente sou o cara de campo do suporte técnico. Nesse meio tempo eu nunca precisei de fato aprender a configurar roteadores Mikrotik, mas como eu acabei tendo interesse e posteriormente ingressando em um curso superior de tecnologia, eu meio que entrei nesse mundo por entuasiasmo mesmo.

Já faz algum tempo que venho pensando sobre a negligencia que muitas pessoas, e até empresas acabam tendo ao configurar roteadores Mikrotik, deixando sua redes totalmente vulnerávels para eventuais ataques, óbviamente essa não devia ser a intenção, mas algumas coisas acabam passando despercebidas aos olhos menos experientes. Tendo em vista essa falha, hoje venho compartilhar um pouco de tudo que já aprendi na vida, com os erros e com outras pessoas muito mais capacitadas do que eu.

> A maioria dos passos citados nesse artigo são voltados para roteadores Mikrotik, mas os conceitos podem ser aplicados em quaisquer outros roteadores, e até mesmo outros tipos de dispositivos.
{: .prompt-info }

## Princípios de segurança da informação

A segurança de um sistema computacional diz respeito à garantia de algumas propriedades fundamentais associadas às informações e recursos presentes no sistema. Quando dizemos “informação”, estamos nos referindo à todos os recursos disponíveis no sistema tais como processamento, arquivos, memória, tráfego de rede, configurações e etc.

Para Nieles, Dempsey e Pillitteri (2017), o termo “segurança computacional” pode ser definido como a proteção oferecida a um sistema de informações automatizado a fim de garantir os objetivos aplicáveis de preservar a **integridade**, **disponibilidade** e a **confidencialidade** dos recursos do sistema de informações, o qual inclui hardware, software, firmware, informações, dados e telecomunicações.

- **Integridade**: os recursos do sistema só podem ser modificados ou destruídos pelos usuários autorizados a efetuar tais operações;
- **Disponibilidade**: os recursos devem estar disponíveis para os usuários que tiverem direito de usá-los, a qualquer momento;
- **Confidencialidade**: os recursos presentes no sistema só podem ser consultados por usuários devidamente autorizados a isso.

## O erro mais comum

O erro mais comum e sem sombra de dúvidas, o mais problemático, são os roteadores com login e senha padrão:

- Usuário: `admin`
- Senha: em branco

Caso seu roteador esteja recebendo um IP público (também chamado de IP válido por alguns profissionais de redes) ou mesmo que esteja por trás de um NAT que não tem um firewall para te proteger, provavelmente esse vai ser o seu primeiro problema. Todo o dispositivo que é acessível apartir da internet é alvo constante de tentativas de acesso indevido realizadas por agentes maliciosos espalhados pelo mundo inteiro, estes tentam invadir seu dispositivo em busca de transforma-lo em um bot para ataques a terceiros. Você não necessariamente pode ser o alvo, mas caso seu dispositivo seja invadido, ele será usado como marionete integrando uma rede (chamada de botnet) com outros milhares de dispositivos IoT infectados, afim de realizar ataques [DDoS](https://www.cloudflare.com/pt-br/learning/ddos/what-is-a-ddos-attack/){:target="_blank"} e o que mais passar pela mente do atacante. Um caso famoso é o botnet [Mirai](https://www.cloudflare.com/pt-br/learning/ddos/glossary/mirai-botnet/){:target="_blank"}.

Portanto, certifique-se de configurar um usuário com uma senha suficientemente segura para seu roteador, com letras maiúsculas, minúsculas, números e caracteres especiais.

## Algumas boas práticas

Ok, partindo do ponto de que sabemos que não é nada profissional deixarmos login e senha padrões em nossos dispositivos, e configuramos isso na primeira oportunidade. Agora vamos nos voltar para os bons hábitos a serem seguidos.

### Mantenha seu roteador sempre atualizado

É crucial manter o firmware do roteador sempre atualizado. As atualizações de firmware geralmente contêm novos recursos e correções de segurança que podem proteger seu roteador contra as ameaças mais recentes. Portanto, é recomendável verificar regularmente se há atualizações de firmware disponíveis para o seu roteador.

No mundo da programação já ouvi pessoas falando, “Ah, eu uso Python 3.7 porque é mais estável…”. O problema é que esse argumento cai por terra tão rápido quanto é dito, se tal versão fosse estável e confiável não haveriam laçamento de novas versões apenas com correções de bugs.

O mesmo vale para roteradores. A maioria das profissionais de redes ainda usam até hoje versões relativamente antigas de firmwares, uma rápida pesquisa por dispositivos Mikrotik no [Shodan.io](https://www.shodan.io/){:target="_blank"} mostra isso:

Aqui vemos a versão 6.48.6 sendo usada pela maioria dos dispositivos Mikrotik visíveis na internet, tal versão foi anunciada no dia 12 de dezembro de 2021, e atualmente na data em que este artigo foi escrito, a versão mais recente v6 do RouterOS é a 6.49.13 (long-term). O problema é que a própria versão 6.48.6 possui vulnerabilidade conhecidas, como descrito a seguir.

> [CVE-2023-30799](https://nvd.nist.gov/vuln/detail/CVE-2023-30799){:target="_blank"} - MikroTik RouterOS antes de 6.49.7 (stable) e até 6.48.6 (long-term) são vulneráveis a um problema de escalonamento de privilégios. Um invasor remoto e autenticado pode escalar privilégios de administrador para superadministrador no Winbox ou na interface HTTP. O invasor pode abusar dessa vulnerabilidade para executar código arbitrário no sistema.
{: .prompt-danger }

Outra vulnerabilidade que ficou bastante conhecida nos roteadores Mikrotik foi  a [CVE-2018-14847](https://nvd.nist.gov/vuln/detail/CVE-2018-14847){:target="_blank"}, na qual era possível por meio de um simples script obter os usuários e senhas de um roteador até a versão 6.42. Veja um exemplo de ataque feito em laboratório que se aproveita dessa falha:

{% include embed/youtube.html id='fMki-cDjb64' %}

Mesmo que você não seja a pessoa mais atualizada nas notícias, certifique-se de manter seu dispositivo sempre atualizado, assim você estará se protegendo contra a maioria das vulnerabilidades conhecidas. No terminal do seu Mikrotik, você pode verificar se existem novas atualizações com o seguinte comando:

```bash
/system/package/update/check-for-updates
```
{: .nolineno }

### Altere as portas default e desative as que não usa

Outra boa prática de segurança é alterar as portas padrão do roteador. Isso pode ajudar a prevenir ataques automatizados que visam portas conhecidas. Além disso, é importante desativar qualquer serviço ou porta que não esteja sendo utilizada, pois isso pode reduzir a exposição do seu roteador a possíveis vulnerabilidades.

Potas conhecidas como SSH, HTTP e WINBOX expostas na internet, são frequentemente alvo de tentativas de login por [bruteforce](https://en.wikipedia.org/wiki/Brute-force_attack){:target="_blank"}, a baixo estão listada as portas default usadas pelo Mikrotik e seus respectivos serviços:

- api: 8728
- api-ssl: 8729
- ftp: 21
- ssh: 22
- telnet: 23
- winbox: 8291
- www (http): 80
- www-ssl: 443

A pesquisa no Shodan por portas abertas em roteadores Mikrotik mostra que a maioria doa dispositivos utilizam as portas padrões, tanto para Winbox (8291), quanto para HTTP(80).

Para alterar a porta default de um serviço, você pode utilizar o comando abaixo no terminal:

```bash
/ip/service/set ssh port=2222
```
{: .nolineno }

No exemplo acima, estamos alterando a porta do serviço SSH para 2222. 

Agentes mal intencionados podem usar softwares com [Nmap](https://nmap.org/){:target="_blank"} e [Hydra](https://github.com/vanhauser-thc/thc-hydra){:target="_blank"} para realizar uma varredura em seu roteador e tentar quebrar as senhas por força bruta. Portanto, é essencial alterar as portas padrão para dificultar o acesso não autorizado ao seu dispositivo.

## Mãos na massa

Agora que já sabemos quais hábitos práticar para dificultar o acesso indevido aos nossos roteadores, vamos partir para a cereja do bolo quando o assunto é segurança de roteadores, as **regras de firewall**.

As regras de firewall são a última linha de defesa do seu roteador contra ataques externos. Elas permitem que você controle o tráfego de entrada e saída do seu roteador, bloqueando ou permitindo conexões específicas. Vamos detalhar como configurar regras de firewall eficazes nos passos a seguir.

Uma breve explicação do que significa cada chain das regras de firewall:

- `input`: Esta chain é utilizada para processar pacotes destinados ao próprio roteador.
- `forward`: Esta chain é utilizada para processar pacotes que estão apenas passando pelo roteador, ou seja, pacotes que não são destinados ao próprio roteador.
- `output`: Esta chain é utilizada para processar pacotes que são originados do próprio roteador.

> Preste atenção a todos os comentários e avisos antes de aplicar cada regra DROP abaixo.
{: .prompt-danger }

### Criando a lista de endereços da rede LAN

Primeiro precisamos criar nossa LISTA DE ENDEREÇOS com todos os IPs que usaremos na maioria dos casos.

**Abaixo você precisa alterar xxxx/x para sua sub-rede de gerência.  Esta sub-rede terá acesso total ao roteador.**

```bash
/ip firewall address-list add address=x.x.x.x/x disabled=no list=support
```
{: .nolineno }

Agora criaremos a address list `not_in_internet` que contém todos os possíveis IPs de redes LAN.

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

Aceitando conexões válidas e rejeitando inválidas que têm o roteador como destino.

```bash
/ip firewall filter
add action=accept chain=input comment="Aceita conexoes estabelecida e relacionadas" connection-state=established,related
add action=drop chain=input comment="Descarta conexoes invalidas" connection-state=invalid
```
{: .nolineno }

### Liberando portas de acesso

Agora iremos liberar todos os protocolos que utilizamos em nosso roteador e bloquer todos os que não usamos para reduzir a superfície de ataque. Para liberar o acesso via SSH, Winbox e Webfig para a sub-rede de gerência, usamos as seguintes regras:

```bash
add action=accept chain=input comment="Libera SSH" dst-port=2222 protocol=tcp src-address-list=support
add action=accept chain=input comment="Libera Winbox" dst-port=8291 protocol=tcp src-address-list=support
add action=accept chain=input comment="Libera Webfig (HTTP)" dst-port=80 protocol=tcp src-address-list=support
```
{: .nolineno }

### Liberando serviços necessários

Agora vamos adicionar todas as regras que nosso roteador precisa para funcionar num cenário em que eles está recebendo um link de internet via DHCP client pela interface `ether1` e disponibiliza um DHCP server para os dispositivos conectados na rede LAN.

> Verifique se você liberou a entrada de todos os os protocolos de que precisa antes de aplicar qual quer regra DROP! Segue o link da documentação oficial da Mikrotik que lista os protocolos e suas respectivas portas de serviço: [https://help.mikrotik.com/docs/display/ROS/Services](https://help.mikrotik.com/docs/display/ROS/Services){:target="_blank"}
{: .prompt-warning }

Adicionando as regras necessárias:

```bash
/ip firewall filter
add action=accept chain=input comment="Aceita ICMP" in-interface=ether1 protocol=icmp
add action=accept chain=input comment="Aceita DHCP Client" dst-port=68 in-interface=ether1 protocol=udp
add action=accept chain=input comment="Aceita DHCP Server" dst-port=67 in-interface=ether1 protocol=udp
add action=accept chain=input comment="Libera DNS TCP" dst-port=53 in-interface=ether1 protocol=tcp
add action=accept chain=input comment="Libera DNS UDP" dst-port=53 in-interface=ether1 protocol=udp
```
{: .nolineno }

### Adicionando regras de defesa da rede LAN

Agora podemos adicionas as regras de firewall para tratar o tráfego que está passando pelo roteador.

> “bridge” é a interface de rede local.
{: .prompt-info }

```bash
/ip firewall filter
add action=drop chain=forward comment="Bloqueia conexões tentando alcançar endereços não públicos da LAN" dst-address-list=not_in_internet in-interface=bridge log=yes log-prefix=!public_from_LAN out-interface=!bridge
add action=drop chain=forward comment="Descarte pacotes recebidos que não sejam NAT" connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix=!NAT
add action=drop chain=forward comment="Solte a entrada da Internet que não é IP público" in-interface=ether1 log=yes log-prefix=!public src-address-list=not_in_internet
```
{: .nolineno }

### Port Knocking

Vamos supor que você está configurando um roteador que está recebendo um IP público, mas quer liberar o acesso dele apenas para o seu endereço de IP residencial ou de seu escritório. E se por acaso durante uma viagem você precise acessá-lo remotamente por algum motivo. Uma abordagem para resolver este problema é usando a técnica de Port Knocking.

Port Knocking é uma técnica de segurança que envolve "bater" (ou conectar-se) em uma sequência predefinida de portas de rede para ganhar acesso a um serviço. Esta técnica geralmente é usada para ocultar serviços como SSH ou Telnet de scanners de porta.

No nosso exemplo podemos usar o knocking para após “batermos” em determinadas portas, o nosso endereço de IP público ser adicionado na lista de acesso liberado por um determinado intervalo de tempo.

Podemos usar a seguinte sequência de comandos para implementar o Port Knocking no Mikrotik:

```bash
/ip firewall filter
add action=add-src-to-address-list address-list=knock1 address-list-timeout=5s chain=input comment="Port Knock - Stage1 - TCP 50000" dst-address=10.0.0.0/24 dst-port=50000 in-interface=ether1 protocol=tcp
add action=add-src-to-address-list address-list=knock2 address-list-timeout=5s chain=input comment="Port Knock - Stage2 - UDP 5000" dst-address=10.0.0.0/24 dst-port=5000 in-interface=ether1 protocol=udp src-address-list=knock1
add action=add-src-to-address-list address-list=support address-list-timeout=30m chain=input comment="Port Knock - Stage3 - TCP 40000 - LIBERADO por 30min" dst-address=10.0.0.0/24 dst-port=40000 in-interface=ether1 protocol=tcp src-address-list=knock2
```
{: .nolineno }

Cada regra acima faz parte de uma sequência de "knocks" ou "batidas". Aqui está o que cada regra faz, passo a passo:

1. A primeira regra adiciona o endereço IP de origem à lista de endereços `knock1` se uma conexão for feita na porta 50000 pelo protocolo TCP. O endereço IP é removido da lista após 5 segundos.
2. A segunda regra adiciona o endereço IP de origem à lista de endereços `knock2` se uma conexão for feita na porta 5000 pelo protocolo UDP. O endereço IP é removido da lista após 5 segundos.
3. A terceira regra adiciona o endereço IP de origem à lista de endereços `support` se uma conexão for feita na porta 40000 pelo protocolo TCP. O endereço IP é removido da lista após 30 minutos.

Depois disso, você pode configurar seu firewall para permitir conexões de endereços IP na lista `support`. Isso significa que um atacante teria que adivinhar a sequência correta de portas para "knock" para obter acesso ao seu roteador. Esta é uma excelente maneira de esconder serviços como SSH ou Winbox de scanners de porta e aumentar a segurança do seu roteador.

## Bloqueando tudo que não é necessário

Agora é a parte delicada, iremos criar a regra de firewall que bloqueia tudo o que não foi liberado anteriormente. Essa deve ser a última regra na sua lista.

> Certifique-se de que liberou todos os serviços dos quais precisa antes de prosseguir.
{: .prompt-danger }

```bash
/ip firewall filter add action=drop chain=input comment="Bloquia todo o resto!"  # NÃO ATIVE ESTA REGRA ANTES DE TER CERTEZA DE TODAS AS REGRAS DE ACEITAÇÃO QUE VOCÊ PRECISA" disabled=yes
```
{: .nolineno }
