Tencent Cloud Anycast Internet Acceleration (AIA) can implement the quality optimization of IP transmission and nearby access to network through multiple entries. This document describes the application scenarios of AIA.
## Game Acceleration
The IP of Anycast can play a role in game acceleration: A game requests to connect to Tencent Cloud from nearby, and reaches the game server through the backbone Direct Connect of Tencent Cloud, which greatly shortens the Internet path to the server and prevents the occurrence of latency, jitter, packet loss and other problems. Compared to the traditional acceleration, the IP entry needs not to be deployed with additional traffic receiving device, and IP is not region-sensitive, thereby simplifying the DNS deployment.

![p](https://mc.qcloudimg.com/static/img/5aad2b50ac0b5d400dfe829da06407e8/image.png)

## LVB for Interaction
If high-quality audio/video without delay is required in an LVB in the case of cross-region transmission, a Dicrect Connect network and access point covering multiple regions must be built for the LVB platform. After using AIA service, the LVB platform can directly use Tencent Cloud's backbone network and POP point to serve LVB users, eliminating the need to build another Direct Connect network.

![Scenario 2](https://mc.qcloudimg.com/static/img/b95923a67c69b3b225a29c59390c9321/image.png)

## Finance Service
Securities and other finance services require very high real-time performance, and unstable public network transmission obviously cannot meet this requirement. After the access layer of these applications is bound with the IP of Anycast, the private network transmission of Tencent Cloud backbone network can be used to make these applications available in multiple regions. In addition, the AIA service also allows the same IP to be used in multiple regions, which simplifies the IP-related approvals, such as filing, registration in finance supervision departments.

![Scenario 3](https://mc.qcloudimg.com/static/img/fbc711c2b3c9b219c42f3b3f08cecb16/image.png)

## Security Service
The security cleaning service providers, games and large website applications always encounter various high-traffic attacks, such as Syn Flood, and ICMP Flood. An ordinary public network IP is generally published in a single region, therefore all attack traffic flows through a single ingress/egress. After AIA is used, an IP is published in multiple regions at a time, without the need to change the DNS configuration, and the attack traffic is diverted to different ingresses for processing.

![Scenario 4](https://mc.qcloudimg.com/static/img/456fe104ee331e7c1b7e3156671256b3/image.png)

