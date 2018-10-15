
Tencent Cloud supports two listener modes, Layer-4 forwarding and Layer-7 forwarding. For different protocol types, they work on transport layer and application layer in the network model, respectively. For more information about listener modes supported by different types of CLB instances, please see [Public Network CLB Instance](https://intl.cloud.tencent.com/document/product/214/6147) and [Private Network CLB Instance](https://intl.cloud.tencent.com/document/product/214/6148).


## Layer-4 Forwarding Listener Protocol and Port Configuration
The CLB listener listens to Layer-4 requests (the 4th layer of OSI network protocol, the transport layer) on the cloud load balancer instance and distributes TCP and UDP requests to backend servers for processing. Layer-4 forwarding is achieved by the following configurations:

| Frontend and Backend Protocol | Frontend Port (CLB Port) | Backend Port (Server Port) | Note |
|--|--|--|--|
| Layer-4 protocol (TCP and UDP) | Frontend ports used by CLB instances to receive requests when providing internal or external services. <br><br>You can perform cloud load balance for the following TCP ports: 21 (FTP), 25 (SMTP), 80 (Http), 443 (Https), 1024-65535, etc. | Backend ports used by CVMs to provide services such as receiving traffic distributed by the CLB. In the application CLB instance, a listener port corresponds to multiple backend ports. In the conventional CLB instance, a listener port corresponds to the same port on the backend. | **A frontend port must be unique**. For example, TCP port 23 and UDP port 23 cannot co-exist. <br><br>**The backend ports of a conventional CLB instance must be unique while those of an application LB instance can be used repeatedly.**<br><br>For Layer-4 forwarding, the client source IP requests are directly sent to backend servers. The feature of acquiring client IP is enabled by default (not applicable to private network CLB instances in VPCs) |


## Layer-7 Forwarding Listener Protocol and Port Configuration
The CLB listener listens to Layer-7 requests (the 7th layer of OSI network protocol, the application layer) on the cloud load balancer instance and distributes HTTP(s) requests to backend servers for processing. Layer-7 forwarding is achieved by the following configurations:

| Frontend and Backend Protocol | Frontend Port (CLB Port) | Backend Port (Server Port) | Note |
|--|--|--|--|
| Layer-7 protocol (HTTP or HTTPS protocol) | Frontend ports used by CLB instances to receive requests when providing internal or external services. <br>Ports from 1 to 65535 are supported. | Backend ports used by CVMs to provide services such as receiving traffic distributed by the CLB. In the application CLB instance, a listener port corresponds to multiple backend ports. In the conventional CLB instance, a listener port corresponds to the same port on the backend. | **A frontend port must be unique**. For example, HTTP 80 and TCP 80 cannot co-exist. <br><br>**The backend ports of a conventional CLB instance must be unique while those of an application LB instance can be used repeatedly.**<br><br>For Layer-7 forwarding, the client source IP requests are directly sent to backend servers through configuring proxy_set_header X-Forwarded. The feature of acquiring client IP is enabled by default (not applicable to private network CLB instances in VPCs) |



