1) Log in to the Tencent Cloud official website, select "Cloud Services" - "Compute and Network" - "Cloud Virtual Machine", then click "Buy Now" button, enter the [CVM purchase page](https://buy.qcloud.com/buy/cvm).

2) Select the billing mode: annual or monthly plan or charge by quantity (If you are not able to purchase CVMs on a charge-by-quantity basis, please go through a [Qualification](https://console.qcloud.com/developer/infomation) process first). With these two modes, the fee is charged on a monthly basis and by the seconds for which the server is used, respectively. For more information, see [here](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E).
![](//mccdn.qcloud.com/static/img/2116de97fc48aa340e08d3ebb982bbde/image.png)

3) Select a region and availability zone. When you need more than one CVMs, it's recommended that you choose different availability zones so as to ensure disaster tolerance.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Based on different underlying hardware, Tencent Cloud offers two series of instances - *Series 1* and *Series 2* (also referred to as *last-generation instance* and *current-generation instance*). They respectively provide the following instance types:

**Current-generation instance types**: [Standard S2](https://www.qcloud.com/doc/product/213/7154), [High IO I2](https://www.qcloud.com/doc/product/213/7155), [Memory M2](https://www.qcloud.com/doc/product/213/7156), [Computational C2](https://www.qcloud.com/doc/product/213/7157)
**Last-generation instance type**: standard S1, High-I/O I1, memory type M1


![](//mccdn.qcloud.com/static/img/0a506ce5c9c271ee09ea237ce1d34944/image.png)

5) Those who have just started using Tencent Cloud products can select public images. The operating systems made available by Tencent Cloud include but not limited to CentOS, Ubuntu, Debian, SUSE, OpenSUSE and FreeBSD. Please build subsequent operating environment on your own.

You can select any Linux system of any version as needed.
![](//mccdn.qcloud.com/static/img/fe36402379bbc70d9e17591568a6e1f6/image.png)

- Linux is an open source system that supports a variety of popular programming languages and databases like MySQL (need to be installed by user). 

6) Select the type of hard disk and the size of data disk.
Tencent Cloud provides Cloud Block Storage and local hard disk.
- Cloud Block Storage: delivers high data reliability with the distributed three-copy mechanism.
- Local hard disk: a storage located on the physical machine where the CVM resides; it allows low latency but may cause single-point loss risk. For the comparison, see [here](http://www.qcloud.com/doc/product/362/%E7%A1%AC%E7%9B%98%E5%AF%B9%E6%AF%94).

Whichever type of disk you choose, a complimentary 20GB system disk will be provided for each Linux CVM purchase by default, and if you choose Cloud Block Storage, you can adjust the capacity to 50GB through the billing mode. You can select the data disk size as needed when making the purchase.
![](//mccdn.qcloud.com/static/img/ef73fc3a1b4d6d1579b322d92d536ac1/image.png)
![](//mccdn.qcloud.com/static/img/72eb6b4c7c89b332394c0e10b0d39ab8/image.png)

7) Choose the type of network (basic network or VPC) and public network bandwidth (charge by fixed bandwidth or by traffic).
- Basic network: suitable for new users; CVM private networks of the same user are interconnected.
- Virtual Private Cloud: suitable for higher-level users; there is logic isolation between different VPCs.
> Public network gateway is an interface between private and public networks, and can forward CVM requests that are from different subnets of the VPC and without an extranet IP. For more details, see [Public network gateway](http://www.qcloud.com/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关)
- Charge by fixed bandwidth: a fixed bandwidth is selected; exceeding this bandwidth will lead to packet loss. Suitable for scenarios with a low level of network fluctuation.
- Charge by traffic: the fee will be charged by the actually consumed traffic. You may set a peak bandwidth limit to avoid any cost arising from unexpected traffic. Packet loss will happen when the instantaneous bandwidth exceeds that peak value. Suitable![](//mccdn.qcloud.com/static/img/3a09b6af11caeb074282dd23006dd818/image.png)

8) Determine the number of servers and the length of purchase (only for CVMs with an annual and monthly plan).

9) Select a login method.
- Password login: the system automatically generates the initial password and sends it to you via an internal message. Once the initial password is received, you use the default username and password to log in to the Linux CVM.
- Key login: more secure than password login and requires you to [create a pair of keys](http://www.qcloud.com/doc/product/213/%E5%AF%86%E9%92%A5%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#1.-创建密钥)first.

10) Choose a Security Group (make sure the login port 22 is open and see [Security Group](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84) for more information), click "Buy Now" button and complete the payment, and then you may enter the [Console](https://console.qcloud.com/cvm) to check and accept your CVM.

After the CVM is created, the user will get an internal message containing such information as instance name, public IP address, private IP address, login name, and initial login password. You can use these information to log in to and manage instances. To ensure the security of your CVM, please change your Windows login password as soon as possible.
