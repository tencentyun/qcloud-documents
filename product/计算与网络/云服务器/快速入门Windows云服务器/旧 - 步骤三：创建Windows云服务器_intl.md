1) Log in to the Tencent Cloud official website, select "Cloud Services" - "Compute and Network" - "Cloud Virtual Machine", then click "Buy Now" button, enter the [CVM purchase page](https://buy.qcloud.com/buy/cvm).

2) Select the billing mode: annual or monthly plan or charge by quantity (If you are not able to purchase CVMs on a charge-by-quantity basis, please go through a [Qualification](https://console.qcloud.com/developer/infomation) process first). With these two modes, the fee is charged on a monthly basis and by the seconds for which the server is used, respectively. For more information, see [here](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E).
![](//mccdn.qcloud.com/static/img/2116de97fc48aa340e08d3ebb982bbde/image.png)

3) Select a region and availability zone. When you need more than one CVMs, it's recommended that you choose different availability zones so as to ensure disaster tolerance.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Based on different underlying hardware, Tencent Cloud offers two series of instances - *Series 1* and *Series 2* (also referred to as *last-generation instance* and *current-generation instance*). They respectively provide the following instance types:

**Current-generation instance types**: [Standard S2](https://www.qcloud.com/doc/product/213/7154), [High IO I2](https://www.qcloud.com/doc/product/213/7155), [Memory M2](https://www.qcloud.com/doc/product/213/7156), [Computational C2](https://www.qcloud.com/doc/product/213/7157)
**Last-generation instance type**: standard S1, High-I/O I1, memory type M1

Select the specification for your instance based on the configuration specified in Step 2.
![](//mccdn.qcloud.com/static/img/0a506ce5c9c271ee09ea237ce1d34944/image.png)

5) Those who have just started using Tencent Cloud can select public images, which contain the legitimate Windows systems. You need to build subsequent operating environment on your own. You can select Windows Server as the operating system, and choose the version as needed.
![](//mccdn.qcloud.com/static/img/aaf71863f01a1b6c28c7e3eadeb3734a/image.png)
- The system contains legitimate activation key at no extra charge (except for the North America region). 
- Suitable for running programs developed under Windows, such as .NET. 
- Support SQL Server and other more databases (you need to install it yourself). 

6) Select the type of hard disk and the size of data disk.
Tencent Cloud provides Cloud Block Storage and local hard disk.
- Cloud Block Storage: delivers high data reliability with the distributed three-copy mechanism.
- Local hard disk: a storage located on the physical machine where the CVM resides; it allows low latency but may cause single-point loss risk. For the comparison, see [here](http://www.qcloud.com/document/product/213/5798).

Whichever type of disk you choose, a complimentary 50GB system disk will be supplied with each Windows CVM purchase by default. You can select the data disk size as needed when making the purchase.
![](//mccdn.qcloud.com/static/img/1c4de34635ffabffedd7207b8d495c5e/image.png)

7) Choose the type of network (basic network or VPC) and public network bandwidth (charge by fixed bandwidth or by traffic).
- Basic network: suitable for new users; CVM private networks of the same user are interconnected.
- Virtual Private Cloud: suitable for higher-level users; there is logic isolation between different VPCs.
> NOTE: Windows CVM cannot be used as the [Public Network Gateway](http://www.qcloud.com/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关). The users who need public network gateway can refer to the Linux CVM QuickStart.

- Charge by fixed bandwidth: a fixed bandwidth is selected; exceeding this bandwidth will lead to packet loss. Suitable for scenarios with a low level of network fluctuation.
- Charge by traffic: the fee will be charged by the actually consumed traffic. You may set a peak bandwidth limit to avoid any cost arising from unexpected traffic. Packet loss will happen when the instantaneous bandwidth exceeds that peak value. Suitable![](//mccdn.qcloud.com/static/img/bca65a7bc1681058e3810810f18a23d4/image.png)

8) Determine the number of servers and the length of purchase (only for CVMs with an annual and monthly plan).

9) Choose a Security Group (<font color="red">make sure the login port 3389 is open.</font> For more information, see [Security Group](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84)). Click "Buy Now" button and complete the payment, and then you can enter [Console](https://console.qcloud.com/cvm) to check and accept your CVM.

