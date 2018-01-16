SSL certificates can be deployed to the Cloud Load Balance (CLB) as follows:

### 1. Selecting a Certificate
Apply for a certificate (refer to [DV Certificate Application](https://cloud.tencent.com/document/product/400/6814) or select a certificate to upload, click **More**, and select **Deploy to CLB**.
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2. Select a CLB Instance
Select only one CLB instance according to the project and region (South China region - Shenzhen Finance not supported).
![](https://mc.qcloudimg.com/static/img/b6261451a354dac96679737014938e52/2.png)

### 3. Create a Listener
Redirect to the CLB Console, open the **Create a Listener** pop-up window, switch the protocol port to HTTPS, select the specified server certificate , and then complete the rest configurations.
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 4. Complete Other Configurations
Go on to complete other configurations to create a listener, and then you can implement HTTPS for CLB.

