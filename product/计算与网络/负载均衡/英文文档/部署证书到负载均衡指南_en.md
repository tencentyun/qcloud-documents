SSL certificates can be deployed to the cloud load balancer as follows:

### 1. Select a Certificate
Apply for a certificate (refer to [Apply for a Free Domain Certificate](https://cloud.tencent.com/document/product/400/6814) or select a certificate to upload, expand "More" operation, and select "Deploy to Cloud Load Balancer".
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2. Select an LB Instance
Select only one LB instance according to the project and region (South China region - Shenzhen Finance not supported).
![](https://mc.qcloudimg.com/static/img/b6261451a354dac96679737014938e52/2.png)

### 3. Create a Listener
Go to the CLB console, open the "Create a Listener" pop-up window, switch the protocol port to Https, select the specified server certificate, and then complete the rest configurations.
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 4. Complete Other Configurations
Continue completing other configurations to create a listener, and then you can get a cloud load balancer with Https.

