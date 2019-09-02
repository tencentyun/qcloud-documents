Tencent Cloud Anycast public network acceleration can achieve IP transmission quality optimization and multi-entry access, the following will introduce you to its application scenarios.
## **Gaming Acceleration**
An Anycast IP can serve as a gaming accelerator. A gaming request enters Tencent Cloud through the nearest node and then reaches the game server through Tencent Cloud's private Direct Connect line, significantly shortening the Internet path distance and reduces latency, jitter and packet loss. Compared with traditional acceleration services, AIA simplifies DNS deployment as IP entries do not require deployment of additional traffic receiving devices and IPs do not need to be geographically differentiated.

![p](https://mc.qcloudimg.com/static/img/5aad2b50ac0b5d400dfe829da06407e8/image.png)

## **Live Video Interaction**
Clear video and voice have to be relayed without delay during cross-region transfer of live streaming content, meaning the live streaming platform must build a dedicated network and access points covering multiple regions. With the help of AIA, the platform can directly utilize Tencent Cloud's backbone networks and POPs to serve live streaming users without the need to set up a dedicated network.

![Scenario 2](https://mc.qcloudimg.com/static/img/b95923a67c69b3b225a29c59390c9321/image.png)

## **Financial Services**
Financial services such as securities require high real-time performance, making unstable Internet transfers completely unsatisfactory. The access layer of an application in this field can be bound to an Anycast IP for multi-region coverage, made possible by private network transfer on Tencent Cloud's backbone networks. Further, AIA enables the use of the same IP for multiple regions, simplifying the paperwork for IP-related approvals such as ICP license filing and registration with financial regulatory authorities.

![Scenario 3](https://mc.qcloudimg.com/static/img/fbc711c2b3c9b219c42f3b3f08cecb16/image.png)

## **Security Services**
Security cleansing service providers, gaming platforms and large-scale website applications are often faced with various traffic-based attacks such as SYN floods and ICMP floods. A common public IP is published in one single region, so all the attacking traffic is concentrated in the same entry. With AIA, the IP is published simultaneously in multiple regions, and the attacking traffic can be diverted to multiple entries for absorption without the need to modify the DNS configuration.

![Scenario 4](https://mc.qcloudimg.com/static/img/456fe104ee331e7c1b7e3156671256b3/image.png)
