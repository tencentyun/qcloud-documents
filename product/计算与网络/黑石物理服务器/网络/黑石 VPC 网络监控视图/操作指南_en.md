## Viewing BM Network Topology
- Log in to Tencent Cloud Console, select "BM VPC" tab, and select "Network Topology".
- Select the following parameters:
 - Region
 - Availability zone
 - VPC
- After selection, the BM network topology structure is displayed.
- Move the mouse curser over the CPM, and the information of CPM, the uplink switch, the uplink switch port and port status is displayed.

The information of EIP, public network LB/private network LB and NAT gateway under your VPC is displayed as follows:
![](https://mc.qcloudimg.com/static/img/ae7949d10c1f9551e72a6a81af548fb2/image.png)

The information of subnets, CPMs, the uplink switch, the uplink switch port and port status under your VPC is displayed as follows:
![](https://mc.qcloudimg.com/static/img/a3eb064e518a738ef2274fff58987d9f/image.png)

## Viewing BM Network Traffic Monitoring Data
- Log in to Tencent Cloud Console, select "Cloud Monitor" tab, and select "BM Network Monitoring".
- Select the following parameters:
 - Region
 - VPC
 - Monitoring type: public network traffic monitoring/private network LB monitoring
 - Monitoring metric: outbound bandwidth/inbound bandwidth/outbound packets/inbound packets
 - Time point when monitoring data is collected
- Choose to view the monitoring data of LB, NAT gateway and EIP
- Sort data by clicking on the arrow icon of outbound bandwidth/inbound bandwidth/outbound packets/inbound.

The monitoring data of public network traffic is displayed as follows:
![](https://mc.qcloudimg.com/static/img/8fc38b9da84bb04af14b6e399f1817a4/image.png)

In the above figure, area graphs are used to display the outbound bandwidth of LB, NAT gateway and EIP: three independent areas are used to represent the outbound bandwidth of LB, NAT gateway and EIP.

The monitoring data of private network LB traffic is displayed as follows:
![](https://mc.qcloudimg.com/static/img/a75420dbf6c9fd2dda150833a58a2da8/image.png)
 
## Viewing Detailed Monitoring Information of a Single LB in BM Network Traffic Monitoring Data
- Log in to Tencent Cloud Console, select "Cloud Monitor" tab, and select "BM Network Monitoring".
- Select the following parameters:
 - Region
 - VPC
 - Monitoring type: public network traffic monitoring/private network LB monitoring
 - Monitoring metric: outbound bandwidth/inbound bandwidth/outbound packets/inbound packets
 - Time point when monitoring data is collected
- Choose to view LB
- Click the ID of the LB instance to be viewed to go to its monitoring page

The LB monitoring data is displayed as follows:
![](https://mc.qcloudimg.com/static/img/db6bf932774ab704222c7dd5815e195d/image.png)

Outbound bandwidth, inbound bandwidth, outbound packets and inbound packets are displayed.
You can also unfold the listener, CVM under this LB to view more detailed monitoring data:
![](https://mc.qcloudimg.com/static/img/bb0386d4f1e915e63a026b8f6e993a8d/image.png)

## View Detailed Monitoring Information of a Single NAT Gateway in BM Network Traffic Monitoring Data
- Log in to Tencent Cloud Console, select "Cloud Monitor" tab, and select "BM Network Monitoring".
- Select the following parameters:
 - Region
 - VPC
 - Monitoring Type: public network traffic monitoring
 - Monitoring metric: outbound bandwidth/inbound bandwidth/outbound packets/inbound packets
 - Time point when monitoring data is collected
- Choose to view NAT Gateway
- Click the ID of the NAT gateway instance to be viewed to go to its monitoring page

The NAT gateway monitoring data is displayed as follows:
![](https://mc.qcloudimg.com/static/img/f9271c2c2cd389c259a0b027bc7f5a8d/image.png)

The displayed monitoring data of NAT gateway includes:
- The outbound bandwidth, inbound bandwidth, outbound packets and inbound packets and number of connections of the entire NAT gateway.
- Monitoring details: the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of each backend IP in this NAT gateway at a certain time point.
 
Click "<" in the above figure to get a detailed list of NAT gateways:
![](https://mc.qcloudimg.com/static/img/505cabad8c6aa1dbeee842d3f86c420b/image.png)

## Viewing Detailed Monitoring Information of a Single EIP in BM Network Traffic Monitoring Data
- Log in to Tencent Cloud Console, select "Cloud Monitor" tab, and select "BM Network Monitoring".
- Select the following parameters:
 - Region
 - VPC
 - Monitoring Type: public network traffic monitoring
 - Monitoring metric: outbound bandwidth/inbound bandwidth/outbound packets/inbound packets
 - Time point when monitoring data is collected
- Choose to view EIP
- Click the ID of the EIP instance to be viewed to go to its monitoring page

The EIP monitoring data is displayed as follows:
![](https://mc.qcloudimg.com/static/img/8b1d634ce0db446f4cfae21c1c04e882/image.png)

Outbound bandwidth, inbound bandwidth, outbound packets and inbound packets are displayed.
Click "<" in the above figure to get a detailed list of EIPs:
![](https://mc.qcloudimg.com/static/img/80968998d9246f33663e39acfc1290e1/image.png)






