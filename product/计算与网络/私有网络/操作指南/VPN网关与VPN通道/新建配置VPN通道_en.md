You can create a new VPN tunnel in VPN tunnel page or in the peer gateway creation page.

Log in to [CVM Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar, select "VPN Connection" - "VPN Tunnel" tab in the VPC console, and click "New" to create a VPN tunnel.

2) Enter the basic information, select the VPN gateway and peer gateway, and enter the pre-shared key.
![](//mccdn.qcloud.com/img567fa26c5d9e1.png) 

3) Enter the SPD policy (establish proxy identity for VPN tunnel). The model is as shown below.
![](//mccdn.qcloud.com/img5695cb5a1920c.png)

Each SPD policy corresponds to a local network segment, and the local network segments cannot overlap. In each SPD policy, a local network segment can correspond to multiple peer network segments, and the peer network segments cannot overlap. For example:
- SPD Policy 1: local network segment: 10.0.0.0/24; peer network segment: 192.168.0.0/24,192.168.1.0/24
- SPD Policy 2: local network segment: 10.0.0.0/24; peer network segment: 192.168.0.0/24,192.168.1.0/24
 
4) Configure IKE parameters (optional). If you do not need these parameters, click "Next".

5) Configure IPsec parameters (optional). If you do not need these parameters, click "Finish" to complete the configuration.

 ![](//mccdn.qcloud.com/img567fa298af1b0.png)
 
