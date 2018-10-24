## Connection Process

![Quick Start](https://mc.qcloudimg.com/static/img/8fbd4b6fe3c5694b4d664b31d590fc4a/image.png)
### Creating Anycast-based EIP

1. Log in to the [EIP Console](https://console.cloud.tencent.com/cvm/eip
), and click the **Apply** button.

 ![p1](https://mc.qcloudimg.com/static/img/a18a018f87701fd94182da23fb47188b/image.png)

2. Select the region, bandwidth limit, quantity, and IP address type based on your needs, then select **Accelerated IP**, and click **OK** to create an Antcast-based EIP.

 ![p2](https://main.qcloudimg.com/raw/f5a79c4df0aa779f3ff3c1327a250258.png)
 
## Binding Backend Resources

Log in to the [EIP Console](https://console.cloud.tencent.com/cvm/eip
), select **More** -> **Bind** to bind a specified resource. This document uses CVM as an example.

 ![p3](https://mc.qcloudimg.com/static/img/22bf3f0500051c8929c39e7c60151ee2/image.png)
 
### Using Accelerated EIP to Connect to the Internet

After logging in to the bound backend resource, you can connect to the Internet through the accelerated EIP and use AIA for acceleration. Since the CVM is bound in this document, you can use AIA for acceleration after logging in to the CVM.

## Other Common Operations
### Changing the Configuration of Anycast-based EIP
#### Adjusting Bandwidth

Log in to the [EIP Console](https://console.cloud.tencent.com/cvm/eip), select the EIP to be used from the EIP list, and then click **Adjust Bandwidth**.

 ![p4](https://mc.qcloudimg.com/static/img/18b5b10ac608d096578495f3e0c69d73/image.png)

