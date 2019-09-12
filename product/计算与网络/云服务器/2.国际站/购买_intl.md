### Purchase CVMs

All users can purchase CVMs on Tencent Cloud's official website. According to different billing methods, users can purchase prepaid CVMs (on a monthly/yearly basis) or postpaid CVMs (billing is accurate to seconds and is settled on an hourly basis). For more information, please see [Billing Methods](https://cloud.tencent.com/document/product/213/2180).
The purchase process of prepaid and postpaid CVMs is similar, as shown below:

1. Log in to [Purchase Tencent Cloud Service](https://buy.cloud.tencent.com/cvm?tab=custom&regionId=1&zoneId=0&step=1&bandwidthType=BANDWIDTH_PREPAID), and select the Custom Configuration tab.

2. Select a billing method: prepaid or postpaid.

3. Select the region and model, image, storage and bandwidth, security group and CVM, and then confirm the order.
>**Purchase suggestions:**
>- Users with smooth network are recommended to select bill-by-bandwidth. If bill-by-bandwidth is selected, the traffic is unlimited. The billing method is "hardware + bandwidth" (prepaid)
>- Users with fluctuate network are recommended to select bill-by-traffic. If bill-by-traffic is selected, users can freely select the peak bandwidth. The billing method is "Hardware (prepaid) + Traffic (actual traffic)".

4. Payment. You can pay with your balance, Tenpay, WeChat Pay or QQ Wallet, etc.
5. The CVM is activated immediately after the payment is completed. You can see the IP address in 1 to 5 minutes, which can be managed after you logged in to the CVM.

> **Note:**
>
> After a postpaid CVM is activated, make sure that your balance is sufficient.

See [Notes for Purchasing from Console](https://cloud.tencent.com/document/product/213/6998) 

### What are the regions and availability zones of CVMs? How to select?

For more information on available regions and available zones of CVMs, please see [Regions and Availability Zones](https://cloud.tencent.com/document/product/213/6091)

For more information on how to select regions and available zones, please see [Regions and Available Zones](https://cloud.tencent.com/document/product/213/6091#.E5.A6.82.E4.BD.95.E9.80.89.E6.8B.A9.E5.9C.B0.E5.9F.9F.E5.92.8C.E5.8F.AF.E7.94.A8.E5.8C.BA).

### What CVM types are provided?

Multiple CVM instance specifications are provided. For more information, please see [Instance Specification](https://cloud.tencent.com/document/product/213/11518). You can select the appropriate instance type based on your business needs.

If your demand is stable, we recommend that you select the prepaid billing method. So your savings will increase with the length of usage. 

To react to spikes in demand, you can choose the postpaid billing method, which allows you to activate/terminate computing instances at any time and only pay for the actually consumed resources. CVM usage is billed in one-second increments to maximize your savings. 

### How to select the CVM configuration solution?

The following configurations are recommended for you: [**Recommended Selection**](https://cloud.tencent.com/act/recommended) 

Entry: Suitable for start-up personal websites. For example, small websites such as personal blogs.
Basic: Suitable for websites or applications with a certain number of visits. For example, large enterprise official websites and small e-commerce websites.
Universal: Suitable for scenarios where cloud computing is frequently used. For example, portals, SaaS software, and small Apps.
Application: Suitable for applications demanding high concurrency and scenarios with high requirement for CVM network and computing. For example, large portals, e-commerce websites, and game Apps.
If recommended configuration does not meet your needs, you can compare the configurations in **[More Models](https://buy.cloud.tencent.com/cvm?tabIndex=1)** based on your actual needs. You can also [Upgrade Configuration](https://cloud.tencent.com/document/product/213/2178#.E9.85.8D.E7.BD.AE.E5.8D.87.E7.BA.A7) or [Downgrade Configuration](https://cloud.tencent.com/document/product/213/2178#.E9.85.8D.E7.BD.AE.E9.99.8D.E7.BA.A7) at any time based on your business needs after purchasing a CVM.

> **Note:**
>
> Windows CVM cannot be used as [Public Gateway](https://cloud.tencent.com/document/product/215/1682). Users who need public gateway can refer to [Getting Started with Linux CVM](https://cloud.tencent.com/doc/product/213/2936).

### Can I purchase a Windows 2003 CVM?

Because Microsoft ended Windows 2003 support, Tencent Cloud no longer provides Windows 2003 servers. You cannot purchase it.

### How to select storage?

For data that requires extremely high reliability, use [Cloud Block Storage](https://cloud.tencent.com/document/product/213/4953) to ensure the persistent and reliable data storage. Try not to select [Local Disk](https://cloud.tencent.com/doc/product/213/5798) for data storage.
For databases that are frequently accessed and variable in size, use [Tencent Cloud Database](https://cloud.tencent.com/product/cdb-overview).

### What are the limits of purchasing prepaid and postpaid CVMs?

For more information, please see [Quota for CVM Instances](https://cloud.tencent.com/document/product/213/2664).

### What are the CVM purchase channels?

Tencent Cloud allows users to purchase CVMs either from the official website or via the API.

### How long will it take before a purchased CVM can be used?

After the system installation of CVM is completed, the CVM status becomes **Running**, and then you can log in to and use it.

### What if the CVM is not created successfully?

If the CVM creation process takes a long time, wait to see if the CVM is created successfully; if it is not, you can [submit a ticket](https://console.cloud.tencent.com/workorder/category) to report your problems and ask the engineer for help.

### In case of CVM delivery failure, how to terminate the CVM?

You can [submit a ticket](https://console.cloud.tencent.com/workorder/category) to contact customer service, and provide complete screenshots of server information and termination failure indicating **Delivery Failure** to facilitate the troubleshooting.

