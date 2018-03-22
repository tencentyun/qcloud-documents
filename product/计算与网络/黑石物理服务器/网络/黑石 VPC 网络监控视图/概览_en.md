When you use BM network, the VPC network topology status and network traffic monitoring views are provided, which include:
- The information of EIP, public network LB/private network LB, NAT gateway under your VPC.
- The information of subnets, CPMs, the uplink switch, the uplink switch port and port status under your VPC.
- The monitoring of overall public network traffic under your VPC, including public network LB, EIP, NAT gateway.
- The monitoring of the private network traffic of private network LB under your VPC.
 
## BM Network Topology
The following information is displayed in BM network topology:
- The information of EIP, public network LB/private network LB and NAT gateway under your VPC.
- The information of subnets, CPMs, the uplink switch, the uplink switch port and port status under your VPC.

## Monitoring of BM Network Traffic
The BM network traffic monitoring is provided in Cloud Monitor for the following purposes:
- Monitor the overall public network traffic under your VPC, including the public network traffic for public network LB, EIP, NAT gateway.
- Monitor the private network traffic of private network LB under your VPC.
 
The public network traffic monitoring includes the display of the public network outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of public network LB, NAT gateway and EIP.

When the data is displayed in ascending/descending order:
- Click the ID of a public network LB instance to go to its monitoring page where the detailed monitoring data of this LB is displayed, including outbound bandwidth, inbound bandwidth, outbound packets and inbound packets.
- Click the ID of an NAT gateway instance to go to its monitoring page where the detailed monitoring data of this NAT gateway is displayed, including outbound bandwidth, inbound bandwidth, outbound packets, inbound packets and number of connections.
- Click the ID of an EIP instance to go to its monitoring page where the detailed monitoring data of this EIP is displayed, including outbound bandwidth, inbound bandwidth, outbound packets and inbound packets.

The private network LB traffic monitoring includes the display of the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of private network LB.

When the data is displayed in ascending/descending order:
- Click the ID of a private network LB instance to go to its monitoring page where the detailed monitoring data of this LB is displayed, including outbound bandwidth, inbound bandwidth, outbound packets and inbound packets.
 
## Monitoring of BM LB
The monitoring of public network traffic and private network LB traffic includes the display of the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of LB.
When the data is displayed in ascending/descending order, click the ID of this LB to go to its monitoring page.
LB monitoring data includes outbound bandwidth, inbound bandwidth, outbound packets and inbound packets.
You can also unfold the listener, CVM under this LB to view more detailed monitoring data.
 
## Monitoring of BM NAT
The public network traffic monitoring displays the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of NAT gateway.
When the data is displayed in ascending/descending order, click the ID of this NAT gateway to go to its monitoring page.

The displayed monitoring data of NAT gateway includes:
- The outbound bandwidth, inbound bandwidth, outbound packets and inbound packets and number of connections of the entire NAT gateway.
- Monitoring details: the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of each backend IP in this NAT gateway at a certain time point.

## Monitoring of BM EIP
The public network traffic monitoring displays the outbound bandwidth, inbound bandwidth, outbound packets and inbound packets sorted in ascending/descending order and the total data of EIP. When the data is displayed in ascending/descending order, click the ID of this EIP to go to its monitoring page.
EIP monitoring data includes outbound bandwidth, inbound bandwidth, outbound packets and inbound packets.

