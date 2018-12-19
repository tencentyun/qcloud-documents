SSL certificates can be deployed to load balancer as follows:

### 1. Select Certificate
Apply for a certificate (refer to [How to Apply for a Free DV Certificate](https://cloud.tencent.com/document/product/400/6814) or select a certificate to upload, expand **More** operation, and select **Deploy to Load Balancer**.
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2. Select LB Instance
Select only one LB instance according to the project and region.
![](https://mc.qcloudimg.com/static/img/81157ad8528ad639623b32177e534624/123lb.jpg)

### 3. Create Listener
Go to the CLB console, open the "Create Listener" pop-up window, on which switch the protocol port to HTTPS, then select an existing server certificate, and complete the remaining configurations.
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 4. Complete Other Configurations
Complete other configurations to create a listener before you can forward HTTPS requests from a load balancer.

