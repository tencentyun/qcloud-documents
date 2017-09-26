## 1. Public network-based hybrid cloud deployment
Virtual Private Cloud provides VPN virtual gateway connection, which enables users to deploy encrypted VPN tunnels connecting your current IT resources and Tencent Cloud VPC in the public network, to achieve a stable and reliable hybrid cloud deployment.

![](//mccdn.qcloud.com/img56b091565f2c9.jpg)
Currently, VPN tunnels support IKE/IPesec encryption protocols, and a maximum bandwidth of 100M. If you have special demands, we can also provide customized VPN connection services that will better suit your needs.

Users need to pay for the public network bandwidth occupied by VPN tunnels. If you need a hybrid cloud interconnection bandwidth that is greater than 600M, it is recommended that you choose the Direct Connect-based hybrid cloud deployment scheme in Scenario 2.

The network quality of VPN tunnels depends on the network quality of public network connections. It is recommended that you test the network latency between your own IT resources and Tencent Cloud in different regions when choosing a region to deploy a VPC, so as to get the optimal hybrid cloud deployment architecture.

## 2. Direct Connect-based hybrid cloud deployment
Virtual Private Cloud also provides Direct Connect service. If you need a hybrid cloud deployment scheme with a large bandwidth and low latency, you can contact us.

![](//mccdn.qcloud.com/img56b09189f0e22.jpg)

## 3. Public cloud deployment based on isolated private and public networks
In addition to the network access based on public network and Direct Connect, you can also use the network isolation of VPC to protect your CVM resources.
![](//mccdn.qcloud.com/img56b0923e089b8.jpg)

By dividing the subnet into private network subnet and public network subnet, the CVM in your private network subnet will be able to access the Internet through the public network gateway of the public network subnet. In this way, you don't have to configure a public IP for each CVM any more, and meanwhile, this method can reduce the private network CVM's risk of being attacked by the public network.
