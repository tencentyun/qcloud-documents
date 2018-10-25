Cloud Load Balance service is mainly provided by cloud load balancer listener. The listener is responsible for listening for requests on cloud load balancer instance, delivering policies to back-end CVMs and other services, providing the following features:

## 1. Layer-4 Forwarding
The cloud load balancer listener listens to Layer-4 requests (the 4th layer of OSI network protocol, the transport layer) on the cloud load balancer instance and distributes these requests to back-end CVMs for processing. Layer-4 forwarding is achieved by the following configurations:
### 1.1. Port Configuration
- Protocol: Support for Layer-4 protocols, including TCP and UDP.
- Cloud load balancer ports: Front-end ports used by cloud load balancers to receive requests when providing internal or external services. Users can perform cloud load balancing for the following TCP ports: 21 (FTP), 25 (SMTP), 80 (Http), 443 (Https) and ports from 1024 to 65535. *** Front-end ports can be used repeatedly within the same cloud load balancer instance***. For example, a user can create ports such as TCP: 22-23, UDP: 22-24.
- Back-end CVM ports: Ports that are used to receive traffic distributed by the cloud load balancer on back-end CVMs. Within one cloud load balancer, a balancer port can correspond to multiple CVM ports.*** Back-end port must be unique within the same cloud load balancer instance.***

For Layer-4 forwarding, the client source IP will directly send requests to back-end CVMs. The feature of acquiring client IP is enabled by default.
>Note: For private network cloud load balancer instances in VPCs, back-end CVMs cannot acquire the client IP and can only get the VIP of the cloud load balancer.

### 1.2. Health Check
Health check is designed to help users automatically identify the running status of back-end CVMs and isolate abnormal CVMs.

Under the health check mechanism for Layer-4 forwarding, cloud load balancer initiates an access request to the CVM port specified in the configuration. If the access to the port is normal, the back-end CVM is considered normal, otherwise it is considered abnormal. For TCP services, SYN packet is used for the check. For UDP services, Ping command is used for the check.

- Response timeout:  2-60 seconds 
- Check interval:  5-300 seconds 
- Unhealthy threshold: 2-10 times (When the response timeout has happened to a healthy back-end CVM for the specified number of times, the back-end CVM is considered unhealthy)
- Healthy threshold: 2-10 times (When the response timeout has happened to an unhealthy back-end CVM for the specified number of times, the back-end CVM is considered healthy)

### 1.3. Back-end CVM Weight Configuration
Layer-4 forwarding uses Weighted Round-Robin Scheduling to allocate traffic, and the traffic is allocated to different back-end CVMs based on the weight ratio by the cloud load balancer. The weight for back-end CVM defaults to 10, which can be set to any integer between 0 to 100.

> Note:
- When the weight for back-end CVM is set to 0, the cloud load balancer instance will not forward traffic to the CVM.
- The traffic forwarded from the cloud load balancer instance to the back-end CVM is calculated based on the set weight ratio. For example, if a cloud load balancer instance is bound to two back-end CVMs, when the weights for A CVM and B CVM are set to 40 and 60 respectively, the ratio of two CVMs receiving the traffic is 2 : 3.
- When the weights for all back-end CVMs are set to the same value (such as the default value 10), the traffic will be equally forwarded to all back-end CVMs. For example, if a cloud load balancer instance is bound to two back-end CVMs, when both weights are set to 10 (the default value), the traffic will be forwarded at a ratio of 50 : 50. If a back-end CVM with the weight set to 10 is added to the cloud load balancer instance, the traffic will be forwarded at a rate of 33 : 33 : 33; if another back-end CVM with the weight set to 10 is added to such instance, the traffic will be forwarded at a rate of 25 : 25 : 25 : 25.
- When session persistence is enabled, the traffic will not be forwarded by weight ratio.  

### 1.4. Session Persistence
Session persistence allows the requests from the same IP (network segment) to be forwarded to the same back-end CVM.

Layer-4 forwarding scenario supports simple session persistence. The session persistence duration can be set to any integer value within the range of 0-3600 seconds. If the time threshold is exceeded and there is no new request in the session, the session will be disconnected. For more information on simple session persistence, refer to [here](http://cloud.tencent.com/doc/product/214/%E4%BC%9A%E8%AF%9D%E4%BF%9D%E6%8C%81%E5%8E%9F%E7%90%86#3.1.-.E7.AE.80.E5.8D.95.E4.BC.9A.E8.AF.9D.E4.BF.9D.E6.8C.81.EF.BC.88.E5.9B.9B.E5.B1.82.E4.BC.9A.E8.AF.9D.E4.BF.9D.E6.8C.81.EF.BC.89).

## 2. Layer-7 Forwarding
The cloud load balancer listener listens to Layer-7 requests (the 7th layer of OSI network protocol, the application layer) on the cloud load balancer instance and distributes these requests to backend servers for processing. Layer 7 forwarding is achieved by the following configurations:
### 2.1. Port Configuration
- Protocol: Support for HTTP/HTTPS protocol of Layer-7 protocol.
- Cloud load balancer ports: Front-end ports used by cloud load balancers to receive requests when providing internal or external services. ***Front-end ports can be used repeatedly within the same cloud load balancer instance***.
- Back-end CVM ports: Ports that are used to receive traffic distributed by the cloud load balancer on back-end CVMs. Within one cloud load balancer, a balancer port can correspond to multiple CVM ports.*** Back-end port must be unique within the same cloud load balancer instance.***

For Layer-7 forwarding, the client source IP will directly send requests to back-end CVMs (by configuring proxy_set_header X-Forwarded). The feature of acquiring client IP is enabled by default.
>Note: For private network cloud load balancer instances in VPCs, back-end CVMs cannot acquire the client IP and can only get the VIP of the cloud load balancer.

### 2.2. Health Check
Health check is designed to help users automatically identify the running status of back-end CVMs and isolate abnormal CVMs.

Under the health check mechanism for Layer-7 forwarding, the cloud load balancer sends an HTTP request to the back-end CVM to check the back-end services. The cloud load balancer determines the running status of the service based on whether the HTTP returned value is http_2xx or http_4xx. In the future, users will be allowed to customize the descriptions of the statuses represented by response codes. For example, in a certain scenario, HTTP returned values include http_1xx, http_2xx, http_3xx, http_4xx and http_5xx. Users can, based on business needs, define http_1xx and http_2xx as normal status and the values from http_3xx to http_5xx as abnormal status.

- Response timeout cannot be set currently. Default is 5s. 
- Check interval is 6-300s. Default is 6s. 
- Unhealthy threshold: 2-10 times, default is 3 times (When the response timeout has happened to a healthy back-end CVM for the specified number of times, the back-end CVM is considered unhealthy)
- Healthy threshold: 2-10 times, default is 3 times (When the response timeout has happened to an unhealthy back-end CVM for the specified number of times, the back-end CVM is considered healthy)


### 2.3. Back-end CVM Weight Configuration
Layer-7 forwarding uses Weighted Round-Robin Scheduling and ip_hash to allocate traffic. The weight for back-end CVM defaults to 10, which can be set to any integer between 0 to 100. The traffic is allocated to different back-end CVMs based on the weight ratio by the cloud load balancer, or based on the hash result of the access source IP address.

Please note the following when using Weighted Round-Robin Scheduling:
- When the weight for back-end CVM is set to 0, the cloud load balancer instance will not forward traffic to the CVM.
- The traffic forwarded from the cloud load balancer instance to the back-end CVM is calculated based on the set weight ratio. For example, if a cloud load balancer instance is bound to two back-end CVMs, when the weights for A CVM and B CVM are set to 40 and 60 respectively, the ratio of two CVMs receiving the traffic is 2 : 3.
- When the weights for all back-end CVMs are set to the same value (such as the default value 10), the traffic will be equally forwarded to all back-end CVMs. For example, if a cloud load balancer instance is bound to two back-end CVMs, when both weights are set to 10 (the default value), the traffic will be forwarded at a ratio of 50 : 50. If a back-end CVM with the weight set to 10 is added to the cloud load balancer instance, the traffic will be forwarded at a rate of 33 : 33 : 33; if another back-end CVM with the weight set to 10 is added to such instance, the traffic will be forwarded at a rate of 25 : 25 : 25 : 25.
- When session persistence is enabled, the traffic will not be forwarded by weight ratio.  

### 2.4. Session Persistence
Session persistence allows the requests from the same IP (network segment) to be forwarded to the same back-end CVM.

Layer-7 forwarding scenario supports session persistence based on cookie insertion (the cookie is embedded into the client by cloud load balancer).

Session persistence duration is not adjustable currently and the default is 75s. If the time threshold is exceeded and there is no new request in the session, the session will be disconnected. For more information on session persistence based on cookie insertion, refer to [here](http://cloud.tencent.com/doc/product/214/%E4%BC%9A%E8%AF%9D%E4%BF%9D%E6%8C%81%E5%8E%9F%E7%90%86#3.3.-.E5.9F.BA.E4.BA.8Ecookie.E7.9A.84.E4.BC.9A.E8.AF.9D.E4.BF.9D.E6.8C.81.EF.BC.88.E4.B8.83.E5.B1.82.E4.BC.9A.E8.AF.9D.E4.BF.9D.E6.8C.81.EF.BC.89).


