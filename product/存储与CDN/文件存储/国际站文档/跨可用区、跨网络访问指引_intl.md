## Cross-availability zone and Cross-network Access to File System

### Cross-availability zone access in a VPC

When you need to have the file storage shared among multiple CVMs distributed in different availability zones of the same region, you can set these CVMs and the CFS in the same VPC to achieve resource access across availability zones.
Take Shanghai as an example. You have a CVM in Shanghai Zone 1 and you need to use CFS. However, you cannot directly create a file system, because the resources have been sold out in Shanghai Zone 1.

If the CVM resides in the "subnet of Shanghai Zone 1" in a VPC, you can log in to the [VPC console](https://console.cloud.tencent.com/vpc) to find the VPC and create a subnet of "Shanghai zone 2" for it.

![](https://main.qcloudimg.com/raw/a849aa72a6419206d43ab084a3e72f3d.png)
![](https://main.qcloudimg.com/raw/13d6a643a5a47d041ecfb5c01e24257f.png)
![](https://main.qcloudimg.com/raw/eab7adc8dc279c2baca89b9baec3a7fd.png)

After creating the subnet successfully, go back to the CFS console, and select this VPC and the subnet you just created to create resources in Shanghai Zone 2. The CFS file system can be directly mounted to the CVM in the subnet of Shanghai Zone 1 in this VPC. [View the file system mounting help documentation](https://cloud.tencent.com/document/product/582/11523).


### Cross-VPC and cross-region access

* When you need to have the file storage shared among multiple CVMs distributed in different VPCs, 
* or when your CVMs and the CFS are in different VPCs,
* or when your CVMs and the CFS are in different regions (for better access performance, it is recommended that the CVMs and the CFS be in the same region),

you can achieve resource access across the CVMs distributed in VPC-A/VPC-B and the CFS distributed in VPC-C by configuring a "peering connection". [Click to see how to configure a peering connection](https://cloud.tencent.com/document/product/215/5000).


### Cross-network access

When you need to have the file storage shared among multiple CVMs distributed in a basic network or a VPC, you can create a CFS file system in the VPC.
Access between the CVMs in a basic network and the CFS in a VPC: "Classiclink" can be configured to achieve resource access between the CVMs in a basic network and the CFS in a VPC. [Click to see how to configure Classiclink](https://cloud.tencent.com/document/product/215/5002). *Note: The access between the CFS in a basic network and the CVMs in a VPC is not supported currently.*
Access between the CVMs in VPC-A and the CFS in VPC-B: See the configuration method in the last section.
