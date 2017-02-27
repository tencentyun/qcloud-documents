## Introduction of Tencent Cloud CVM
Tencent Cloud Cloud Virtual Machine (CVM) provides extendable calculated capacity on the cloud, and avoids the situation where estimation of resources usage and early-stage investment is required in advance with traditional servers. With Tencent Cloud CVM, users can quickly enable CVMs of any number in a short period of time and deploy applications immediately. Tencent Cloud CVM supports user customization of all resources, such as CPU, memory, hard drive, network, security and so on. It also allows for easy adjustment of the resources in case of changes in visits, load and other demands.

The understanding of Tencent Cloud CVM often involves the following concepts:

- Virtual computing resources on the cloud, namely [Instance](/doc/product/213/4939).
- Enable position for instances and other resources, namely [Region and availability zone](/doc/product/213/6091).
- Instance preset template, including pre-configuration environment of the server (operating system and other already installed software), namely [Image](/doc/product/213/4940).
- Different configurations of instance:  CPU, memory, storage, network, etc., namely [Instance type](/doc/product/213/4833).
- Devices that are located on the same physical server with instances and can be used for persistent storage by instances, namely [Local disk](/doc/product/213/5798).
- Distributed persistent block storage devices provided, can be used as system disk for instances or expandable data disk, namely [Cloud Block Storage](/doc/product/213/4953).
- Use [SSH key pairs](/doc/product/213/6092) of high security (Public keys are stored by Tencent Cloud, and private keys are stored in secure locations by users) and [Login Password](/doc/product/213/6093) using ordinary password as the login methods.
- Internal and external service address of the instance, namely [Private IP address](/doc/product/213/5225) and [Public IP address](/doc/product/213/5224).
- Secure access control of instances that specifies rules for IP, protocol and port of incoming and outbound instances, namely [Security Group] (/doc/product/213/5221).
- Customized virtual cyberspace, logically isolated from other resources, namely [Virtual Private Cloud] (/doc/product/215/4927).
- Static Public IP designed specifically for dynamic network to meet demands for fast troubleshooting, namely [Elastic IP] (/doc/product/213/5733).
- Tag for identifying instance sources within the instances, namely [Metadata](/doc/product/213/4934).
- Web-based user interface, namely [Tencent Cloud console](https://console.qcloud.com/).


If it is the first time for the user to use Tencent Cloud CVM, please refer to [Quick start for Windows CVM](/doc/product/213/2764) and [Quick start for Linux CVM](/doc/product/213/2936).


## Related Services

- You may use a preset template to enable new CVM. The preset template may include any environment or application that you want to be included in the CVM during initialization. Tencent Cloud provides a large number of approved third-party preset templates to help users quickly build environment. For more information, please refer to [Service marketplace](http://market.qcloud.com/).

- Cloud Load Balance may realize automatic distribution of request traffic from clients across multiple CVM instances. For more information, see [Cloud Load Balance Product Documentation](https://www.qcloud.com/doc/product/214).

- Auto Scaling may automatically increase or decrease the quantity of server clusters at regular time or based on specific conditions. For more information, see [Auto Scaling Product Documentation](https://www.qcloud.com/doc/product/377).

- Cloud Monitor can be used to monitor operation statistical data for CVM instances. For more information, see [Cloud Monitoring Product Documentation](https://www.qcloud.com/doc/product/248).

- Tencent Cloud Cloud Database can be used to deploy your relational database on the cloud. For more information, see relevant Cloud Database product documentation, such as [Cloud Database MySQL](https://www.qcloud.com/doc/product/236).


## Pricing of Tencent Cloud CVM

For information on billing mode and specific prices of the CVM, see [Cloud Virtual Machine instance prices](https://www.qcloud.com/doc/product/213/2176).

