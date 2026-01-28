---
title: How to install an external antenna on the Cardputer
description: Step-by-step instructions on how to solder an antenna to the M5 Stack Cardputer v1.
author: henriquesebastiao
date: 2026-01-28 04:46:00 -0400
categories: [Microcontroladores, Cardputer]
tags: [arduino, stamps3, cardputer, m5stack]
post_image:
  path: /img/2026-01-28/main.jpg
---

The idea here is to document the process of installing an external antenna on the Cardputer to improve the Wi-Fi signal strength, gathering as much information as possible to make life easier for anyone who wants to do the same. If you have already done this and have any tips, please submit a pull request with your information.

If you have any questions, open an issue so we can help you.

## Notes

Keep in mind that you will need to open the Cardputer to install the external antenna. It is somewhat delicate internally, especially the components related to its screen, so care is necessary to avoid damaging your device.

The images showing the polarities of the IPX connector braids in this guide come from the Azur Firmware server on Discord, and credit is due to users `@Cyber.odare` and `@keebasg`. Thank you for sharing your experiences.

I would like to thank the following person for sharing images and information that helped compose this guide:

- [@Lucas-Simoes-Lisboa](https://github.com/Lucas-Simoes-Lisboa)

## Signal level tests obtained

In order to try to measure the improvement of the Wi-Fi signal with the external antenna, signal level tests were performed with the Cardputer in two different scenarios and with 5 different antenna configurations.

When analyzing the Cardputer's performance for Wi-Fi signal reception, we must keep in mind that the context of the tests is very important, since the Wi-Fi signal is influenced by several factors, such as the distance from the router, the presence of obstacles, interference from other devices, among others. Knowing this, I will try to describe below in as much detail as possible the scenarios and antenna configurations used.

The test scenarios were:

- **Scenario 1**: Tests performed in an urban environment from a modest bakery.
- **Scenario 2**: Tests performed in a rural area from the balcony of a house and open area.

Antenna configurations used:

- **No antenna**: Only the SMA connector, no antenna.

- **Antenna 1**: [Antenna 2.4/5.8GHz 3dBi](https://s.click.aliexpress.com/e/_oEylIq5).
- **Antenna 2**: [2.4GHz 3dBi Antenna](https://pt.aliexpress.com/item/32957527411.html).
- **Antenna 3**: [LTE Antenna 10dBi 700-2700MHz](https://s.click.aliexpress.com/e/_oncECQd).
- **Antenna 4**: [Antenna 2.4GHz 6dBi](https://s.click.aliexpress.com/e/_opXW0nJ).

Regarding the antenna specifications, I follow the information provided by the sellers, since I do not have any tool to measure the real power of the antennas.

For each antenna, 3 tests were performed, and the average of the received signal values ​​was calculated. I also omitted the names of the Wi-Fi networks to maintain the privacy of the establishments. Instead of the network names, I used "Network 1", "Network 2"...

The signals marked with `-` indicate that the signal was not detected.

Below are the test results:

### Scenario 1

| Network | Distance (m) | Channel | No antenna | Antenna 1 | Antenna 2 | Antenna 3 | Antenna 4 |
|------|---------------|-------|------------|----|----------|----------|----------|
| Network 1 | 4 | 1 | -67 | -51 | -45 | -46 | -45 |
| Network 2 | 5 | 4 | -73 | -66 | -59 | -66 | -60 |
| Network 3 | 9 | 2 | -88 | -67 | -63 | -68 | -68 |
| Network 4 | 34 | 6 | -95 | -77 | -72 | -85 | -70 |
| Network 5 | 35 | 1 | -96 | -90 | -87 | -85 | -85 |
| Network 6 | 41 | 11 | -92 | -84 | -80 | -80 | -75 |
| Network 7 | 41 | 1 | -94 | -89 | -86 | -84 | -84 |
| Network 8 | 41 | - | -94 | - | -76 | -79 | -73 |
| Network 9 | 43 | 8 | -94 | -90 | -83 | -84 | -75 |
| Network 10 | 74 | 3 | - | -93 | -82 | -87 | -78 |
| Network 11 | 80 | - | - | - | - | - | -93 |
| Network 12 | 105 | 11 | - | - | -89 | -88 | -87 | -77 |
| Network 13 | 106 | - | - | - | - | - | -92 |
| Network 14 | 117 | - | - | - | - | - | -93 |
| Network 15 | 122 | - | - | - | -89 | -95 | -82 |

### Scenario 2

| Network | Distance (m) | Channel | No antenna | Antenna 1 | Antenna 2 | Antenna 3 | Antenna 4 |
|------|---------------|-------|------------|----------|----------|----------|----------|
| Network 1 | 3 | 11 | -68 | -55 | -50 | -51 | -47 |
| Network 2 | 5 | 1 | -69 | -60 | -57 | -63 | -63 |
| Network 3 | 240 | 6 | - | -87 | -85 | -91 | -87 |
| Network 4 | 246 | 6 | - | -93 | -89 | -89 | -86 |

### Conclusion

Of the four antennas tested, antenna 4 performed best, being able to receive signals from further away, up to 122 meters in urban areas and up to 246 meters in open rural areas. It also achieved better signal levels from closer networks when compared to the other antennas. However, if you prefer a smaller and more compact antenna, antenna 2 also proved to be a good alternative with interesting results, although inferior to antenna 4.

## Precautions to Take When Opening the Cardputer

Be careful when opening the Cardputer, as the display flat connector is fragile and is connected at the bottom of the STAMP.

![STAMP flat connector](/img/2026-01-28/img9.jpg){: width="500" }
_STAMP flat connector_

Be careful not to bend the STAMP pins.

## Materials

- SMA Wi-Fi antenna and IPX to SMA adapter (recommended: <https://a.aliexpress.com/_mK5YhoU>)
- Soldering iron
- Solder

You must choose an antenna that has a connector compatible with the IPX to SMA adapter, as there are two types of SMA connectors (SMA and RP-SMA), and you might get confused. See the image below:

![Difference between SMA and RP-SMA connectors](/img/2026-01-28/rp-sma_sma.jpg){: width="600" }
_Difference between SMA and RP-SMA connectors_

## Procedure

Use the soldering iron to heat and remove the solder from the integrated 3D antenna of the Cardputer.

![Stripped tip of the adapter.](/img/2026-01-28/peeled-tip.jpg){: width="500" }
_Stripped tip of the adapter_

Use the soldering iron to heat and remove the solder from the integrated 3D antenna of the Cardputer.

![3D antenna on the STAMP](/img/2026-01-28/3d-antenna.jpg){: width="500" }
_3D antenna on the STAMP_

In the photo below, you can see where to solder the positive and negative wires of the external antenna.

![Where to solder the antenna](/img/2026-01-28/solder-antenna.jpg){: width="500" }
_Where to solder the antenna_

After soldering:

![Soldered antenna location](/img/2026-01-28/welded-antenna.jpg){: width="500" }
_Soldered antenna location_

Now, adapt the SMA connector to the Cardputer case and connect the antenna. I believe there is not much more to say about this part.

Below are all the other images that can help you better understand the process:

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

## Out of Context 😅

An experience I, [@henriquesebastiao](/en/about/), had:

- During the process of reassembling the Cardputer, I almost gave up; it just wasn’t working!
- And while I was finding space for the SMA plug, I opted to use nothing less than a drill to make a hole in the Cardputer case. Too bad I didn't record it.

<img src="/img/2026-01-28/cool.jpg" alt="img" width="500"/>
