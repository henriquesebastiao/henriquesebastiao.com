---
title: Como instalar uma antena externa no Cardputer
description: Passo a passo de como soldar uma antena ao Cardputer v1 da M5 Stack.
author: henriquesebastiao
date: 2026-01-28 04:46:00 -0400
categories: [Microcontroladores, Cardputer]
tags: [arduino, stamps3, cardputer, m5stack]
post_image:
  path: /img/2026-01-28/main.jpg
---

A ideia aqui é documentar o processo de instalação de uma antena externa no Cardputer, para melhorar o poder do sinal Wi-Fi, juntando o máximo de informações possíveis para facilitar a vida de quem quiser fazer o mesmo. Se você já fez isso e tem alguma dica, por favor, faça um pull request com suas informações.

Caso você tenha alguma dúvida, abra uma issue para que possamos te ajudar.

## Notas

Tenha em mente que você precisará abrir o Cardputer para instalar a antena externa, ele é um pouco delicado internamente, principalmente os componentes referentes a sua tela, logo todo o cuidado se faz necessário para não danificar seu aparelho.

As imagens referentes a polaridades das malhas do conetor IPX presentes nesse passo a passo são oriundas do servidor Azur Firmware no Discord, cujo o crédito é devido aos usuários `@Cyber.odare` e `@keebasg`, agradeço a eles por compartilharem suas experiências.

Agradeço às seguintes pessoa por compartilharem imagens e informações que ajudaram a compor esse passo a passo:

- [@Lucas-Simoes-Lisboa](https://github.com/Lucas-Simoes-Lisboa)

## Testes de nível de sinais obtidos

A fim de tentar mensurar a melhora do sinal Wi-Fi com a antena externa, foram feitos testes de nível de sinal com o Cardputer em dois cenários diferentes e com 5 configurações de antena diferentes.

Se tratando de analisar a performance do Cardputer para recepção de sinal Wi-Fi, temos que ter em mente que o contexto dos testes importa muito, pois o sinal Wi-Fi é influenciado por diversos fatores, como a distância do roteador, a presença de obstáculos, a interferência de outros dispositivos, entre outros. Sabendo disso tentarei descrever a baixo com máximo de detalhes possível os cenários e as configurações de antena utilizadas.

Os cenários de teste foram:

- **Cenário 1**: Testes realizados em ambiente urbano a partir de modesta padaria.
- **Cenário 2**: Testes realizados em zona rural a partir da varanda de uma casa e área aberta.

Configurações de antena utilizadas:

- **Sem antena**: Apenas o conector SMA, sem antena.
- **Antena 1**: [Antenna 2.4/5.8GHz 3dBi](https://s.click.aliexpress.com/e/_oEylIq5).
- **Antena 2**: [2.4GHz 3dBi Antenna](https://pt.aliexpress.com/item/32957527411.html).
- **Antena 3**: [LTE Antenna 10dBi 700-2700MHz](https://s.click.aliexpress.com/e/_oncECQd).
- **Antena 4**: [Antenna 2.4GHz 6dBi](https://s.click.aliexpress.com/e/_opXW0nJ).

Quanto as especificações das antenas, sigo as informações passadas pelos vendedores, uma vez que não tenho nenhuma ferramenta para medir a real potência das antenas.

Para cada antena foram realizados 3 testes, e a média dos valores de sinal recebido foi calculada, também omiti os nomes das redes Wi-Fi para manter a privacidade dos estabelecimentos, no lugar dos nomes das redes utilizei "Rede 1", "Rede 2"...

Os sinais marcados com `-` indicam que o sinal não foi detectado.

Segue abaixo os resultados dos testes:

### Cenário 1

| Rede | Distância (m) | Canal | Sem antena | Antena 1 | Antena 2 | Antena 3 | Antena 4 |
|------|---------------|-------|------------|----------|----------|----------|----------|
| Rede 1 | 4 | 1 | -67 | -51 | -45 | -46 | -45 |
| Rede 2 | 5 | 4 | -73 | -66 | -59 | -66 | -60 |
| Rede 3 | 9 | 2 | -88 | -67 | -63 | -68 | -68 |
| Rede 4 | 34 | 6 | -95 | -77 | -72 | -85 | -70 |
| Rede 5 | 35 | 1 | -96 | -90 | -87 | -85 | -85 |
| Rede 6 | 41 | 11 | -92 | -84 | -80 | -80 | -75 |
| Rede 7 | 41 | 1 | -94 | -89 | -86 | -84 | -84 |
| Rede 8 | 41 | - | -94 | - | -76 | -79 | -73 |
| Rede 9 | 43 | 8 | -94 | -90 | -83 | -84 | -75 |
| Rede 10 | 74 | 3 | - | -93 | -82 | -87 | -78 |
| Rede 11 | 80 | - | - | - | - | - | -93 |
| Rede 12 | 105 | 11 | - | -89 | -88 | -87 | -77 |
| Rede 13 | 106 | - | - | - | - | - | -92 |
| Rede 14 | 117 | - | - | - | - | - | -93 |
| Rede 15 | 122 | - | - | - | -89 | -95 | -82 |

### Cenário 2

| Rede | Distância (m) | Canal | Sem antena | Antena 1 | Antena 2 | Antena 3 | Antena 4 |
|------|---------------|-------|------------|----------|----------|----------|----------|
| Rede 1 | 3 | 11 | -68 | -55 | -50 | -51 | -47 |
| Rede 2 | 5 | 1 | -69 | -60 | -57 | -63 | -63 |
| Rede 3 | 240 | 6 | - | -87 | -85 | -91 | -87 |
| Rede 4 | 246 | 6 | - | -93 | -89 | -89 | -86 |

### Conclusão

Das quatro antenas testadas, a antena 4 foi a que se saiu melhor, conseguindo receber sinais mais distantes até 122 metros em área urbana e até 246 em área rural aberta. E conseguindo níveis de sinais melhores da redes mais próximas se comparados com as outras antenas. Contudo, caso você prefira uma antena menor e mais compacta a antena 2 também se mostrar uma boa alternativa com resultados interessantes, porém inferiores a antena 4.

## Cuidados a serem tomados ao abrir o Cardputer

Tome cuidado ao abrir o Cardputer, pois o conector flat do display é frágil e é conectado na parte de baixo do STAMP.

![Conector flat do STAMP](/img/2026-01-28/img9.jpg){: width="500" }
_Conector flat do STAMP_

Cuidado para não entortar os pinos do STAMP.

## Materiais

- Antena Wi-Fi SMA e adaptador IPX para SMA (recomendado: <https://a.aliexpress.com/_mK5YhoU>)
- Ferro de solda
- Estanho

Você deve escolher uma antena que tenha o conector compatível com o adaptador IPX para SMA, pois existem dois tipos de conectores SMA (SMA e RP-SMA), e você pode acabar se confundindo, veja a imagem abaixo:

![Diferença entre conectores SMA e RP-SMA](/img/2026-01-28/rp-sma_sma.jpg){: width="600" }
_Diferença entre conectores SMA e RP-SMA_

## Procedimento

Corte a ponta IPX do adaptador e descasque a ponta do cabo, separe a malha externa da interna, a malha externa representa o cabo negativo, já a interna representa o cabo positivo.

![Ponta descascada do adaptador](/img/2026-01-28/peeled-tip.jpg){: width="500" }
_Ponta descascada do adaptador_

Com o ferro de solda esquente a solda da antena 3D integrada do Cardputer e a remova.

![Antena 3D no STAMP](/img/2026-01-28/3d-antenna.jpg){: width="500" }
_Antena 3D no STAMP_

Na foto abaixo você pode ver onde deve soldar os fios positivo e negativo da antena externa.

![Onde soldar a antena](/img/2026-01-28/solder-antenna.jpg){: width="500" }
_Onde soldar a antena_

Após soldar:

![Como ficam os fios soldados](/img/2026-01-28/welded-antenna.jpg){: width="500" }
_Como ficam os fios soldados_

Agora basta adaptar o conector SMA na carcassa do Cardputer e conectar a antena. Creio que não há muito a ser dito sobre essa parte.

Segue abaixo todas as demais imagens que podem lhe ajudar a entender melhor o processo:

<table>
  <tr>
    <td><img src="/img/2026-01-28/img2.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img3.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img4.jpg" width="300" alt="img"/></td>
  </tr>
  <tr>
    <td><img src="/img/2026-01-28/img5.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img6.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img7.jpg" width="300" alt="img"/></td>
  </tr>
  <tr>
    <td><img src="/img/2026-01-28/img8.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img1.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img10.jpg" width="300" alt="img"/></td>
  </tr>
  <tr>
    <td><img src="/img/2026-01-28/img11.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img12.jpg" width="300" alt="img"/></td>
    <td><img src="/img/2026-01-28/img13.jpg" width="300" alt="img"/></td>
  </tr>
</table>

## Fora de contexto 😅

Experiencia que eu, [@henriquesebastiao](/about/) tive:

- Durante o processo de montar o Cardputer de volta eu quase desisti, o trem que não dava certo!
- E enquanto eu acho um espaço para caber o plug SMA eu optei por usar nada mais nada menos que uma furadeira para fazer um buraco na carcaça do Cardputer, pena que nao registrei isso.

<img src="/img/2026-01-28/cool.jpg" alt="img" width="500"/>
