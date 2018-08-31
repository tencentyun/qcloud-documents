## How do I backup data for CVMs?

- If your CVM uses a cloud disk, you can back up your business data by creating a system disk custom image and a data disk snapshot. 
  - For more information on how to create a custom image, please see: [image operation guide](https://cloud.tencent.com/document/product/213/4942) 
  - For more information on how to create a snapshot, please see: [snapshot operation guide](https://cloud.tencent.com/document/product/362/5755)
- If your CVM uses a local disk, you can back up data on system disk by creating a custom image. For the business data in your data disk, you still need to customize your backup policy. 
  You can use FTP to back up the data in the server to other places. For more information on how to deploy FTP, please see: 
  - Windows: [Setting up FTP Service](/document/product/213/10414)

  - Linux: [Setting up FTP Service](/document/product/213/10912) 
- In addition, if you have higher requirements for data security, you can also purchase more specialized third-party customized backup services. [Cloud Marketplace>>](https://market.cloud.tencent.com/)

## What are the common data backup and recovery solutions?

The applicable data backup and recovery solutions vary with different application scenarios and businesses. The following are some recommended approaches that can be used based on your actual needs:

- Back up the instance regularly using the [CBS Snapshot](https://cloud.tencent.com/doc/product/362/5754) feature.
- Deploy key components of the application across multiple availability zones and replicate the data appropriately.
- Use [EIP](https://cloud.tencent.com/doc/product/213/5733) for domain name mapping to ensure that the service IP can be quickly redirected to another CVM instance when the server is unavailable.
- Check the monitoring data regularly and set the relevant alarms. For more information, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).
- Process emergent requests with Auto Scaling. For more information, please see [Auto Scaling Product Documentation](https://cloud.tencent.com/doc/product/377).

## How do I recover CVM files?

For CVM file recovery, use the relevant free or paid service from [Cloud Marketplace](https://market.cloud.tencent.com/).

