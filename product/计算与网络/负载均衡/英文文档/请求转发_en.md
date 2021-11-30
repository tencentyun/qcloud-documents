Tencent Cloud supports two listener modes: layer 4 forwarding and layer 7 forwarding, for different protocol types. They work on transport layer and application layer in the network model, respectively. For more information about which listener modes are supported by certain types of cloud load balancer instances, refer to [Public Network Cloud Load Balancer Instance](/doc/product/214/6147) and [Private Network Cloud Load Balancer Instance](/doc/product/214/6148).

## Layer 4 Forwarding Listener Protocol and Port Configuration
The cloud load balancer listener listens to layer 4 requests (the 4th layer of OSI network protocol, the transport layer) on the cloud load balancer instance and distributes TCP and UDP requests to backend servers for processing. Layer 4 forwarding is achieved by the following configurations:

| Front-end and Back-end Protocol | Front-end Port (Cloud Load Balancer Port) | Back-end Port (Server Port) | Note |
|--|--|--|--|
| Layer 4 protocol (TCP and UDP) | Front-end ports used by cloud load balancers to receive requests when providing internal or external services. <br><br>Users can perform cloud load balancing for the following TCP ports: 21 (FTP), 25 (SMTP), 80 (Http), 443 (Https) and ports from 1024 to 65535. | Ports that are used to receive traffic distributed by the cloud load balancer. In the same cloud load balancer instance, one cloud load balancer port may correspond to multiple CVM ports | **Front-end ports can be used repeatedly within the same cloud load balancer instance**. For example, a user can create ports such as TCP: 22-23, UDP: 22-24.<br><br>**Back-end port must be unique within the same cloud load balancer instance**<br><br>For layer 4 forwarding, the client source IP will directly send requests to backend servers. The feature of acquiring client IP is enabled by default (not applicable for private network cloud load balancer instances in VPCs) |


## Layer 7 Forwarding Listener Protocol and Port Configuration
The cloud load balancer listener listens to layer 7 requests (the 7th layer of OSI network protocol, the application layer) on the cloud load balancer instance and distributes HTTP(s) requests to backend servers for processing. Layer 7 forwarding is achieved by the following configurations:

| Front-end and Back-end Protocol | Front-end Port (Cloud Load Balancer Port) | Back-end Port (Server Port) | Note |
|--|--|--|--|
| Layer 7 protocol (HTTP or HTTPS protocol) | Front-end ports used by cloud load balancers to receive requests when providing internal or external services. <br>Ports from 1 to 65535 are supported | Ports that are used to receive traffic distributed by the cloud load balancer. In the same cloud load balancer, one cloud load balancer port may correspond to multiple CVM ports | **Front-end ports can be used repeatedly within the same cloud load balancer instance**<br><br>**Back-end port must be unique within the same cloud load balancer instance**<br><br>For layer 7 forwarding, the client source IP will directly send requests to backend servers (by configuring proxy_set_header X-Forwarded). The feature of acquiring client IP is enabled by default. (not applicable for private network cloud load balancer instances in VPCs) |



