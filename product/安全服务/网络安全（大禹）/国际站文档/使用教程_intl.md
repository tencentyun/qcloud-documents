
## For Business Deployed outside Tencent Cloud
The procedure to use High Defense IP:
![](https://main.qcloudimg.com/raw/ef38f7a984d6ca8b142d1a7c93357e93.png)

### Login to Console

1. Log in to the console of [Dayu Anti-DDos](https://console.cloud.tencent.com/dayu/bgpip), and locate your high defense IP instance whose forwarding target is not Tencent cloud.
 ![1](https://main.qcloudimg.com/raw/464f1a9d0289f2e21b25dea217add1e1.png)
2. Click the instance ID to enter the configuration page.

### Creating Forwarding Rule

1. In the "Forwarding Rules" configuration bar, click **New** button to create a forwarding rule.
 ![2](https://main.qcloudimg.com/raw/4408dc9019be2f7d776bffc482722e4f.png)
2. As shown in the figure below, select TCP in Forwarding Protocol, and enter the forwarding port (namely the port used to access to the high defense IP, which is usually the same as the origin server port), and then enter the origin server port (real service port) and the origin server IP. Finally, click **OK** to generate a forwarding rule.
 ![3](https://main.qcloudimg.com/raw/af31955bf91d13464940496c00e92312.png)
 
> **Note:**
- Separate IPs by pressing Enter. A maximum of 20 public IPs from the target IP forwarding area can be added.
- Load balancing of multiple origin servers is performed in polling mode.
- A maximum of 60 forwarding rules can be configured for a high defense IP.

### Modifying DNS Resolution
Finally, change the IP address that is pointed to by the A record to the high defense IP.

## For Business Deployed in Tencent Cloud
The procedure to use High Defense IP:
![](https://main.qcloudimg.com/raw/7cf34e2d417ab888a8dda804c5a94a7a.png)

### Login to Console
1. Log in to the console of [Dayu Anti-DDos](https://console.cloud.tencent.com/dayu/bgpip), and locate your high defense IP instance with the business deployed in Tencent Cloud on the "High Defense IP" control page.
 ![4](https://main.qcloudimg.com/raw/cb571f1fef4ec2f83486a048c3d518b0.png)
2. Click the instance ID to enter the configuration page.

### Creating a Listener
1. In Basic Configuration, set the protocol port based on your business needs. The high defense IP uses layer-4 forwarding, so select TCP (for layer-7 application protocol, such as HTTP, also select TCP), as shown below:
 ![5](https://main.qcloudimg.com/raw/6da402eaf207544f2cef5d03f5a5b4d2.png)
2. In Advanced Configuration, configure according to actual business conditions. If you are not sure, keep the default configuration.
 ![6](https://main.qcloudimg.com/raw/4235e3c7a062c4d3c027e27f1f7c08c5.png)
3. Health Check is enabled by default. You are recommended not to modify the configuration. This module can automatically remove failed service ports and keep the business available.
 
### Binding CVM
Bind a CVM and set weight
![7](https://main.qcloudimg.com/raw/b8367df8400d5b83e58d834af4c933d3.png)


