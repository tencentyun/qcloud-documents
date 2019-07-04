## 1. What is a one-click deployment?
One-click deployment is designed to help you quickly complete the deployment at Mini LVB backend.
![](//mc.qcloudimg.com/static/img/83d9e9a82474f771e6cc223ce71972f5/image.png)

### 1.1 Prepare a CVM
If you have not purchased a Tencent Cloud CVM, you can [click here to purchase one](https://console.cloud.tencent.com/cvm). According to procedure, configure bandwidth, storage capacity, region, memory, CPU and other CVM hardware parameters based on your demands and make a purchase.
Note:
- 1. For mirror, you need to select **Mini LVB Backend Dedicated** mirror in **Service Market**.
- 2. Remember the **root password** of CVM.
- 3. Select **All ports for the security group are allowed by default** as the security group policy of CVM.

![](//mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

![](//mc.qcloudimg.com/static/img/1b38eb9a8199e86c147b1f5e56028c31/image.png)

![](//mc.qcloudimg.com/static/img/a1760be6fb4b7bcec0f65e8268f85dcc/image.png)

If you already have a Tencent Cloud CVM, you just need to reinstall the system.
Note:
- 1. For mirror, you need to select **Mini LVB Backend Dedicated** mirror in **Service Market**.
- 2. Remember the **root password** of CVM.
- 3. Confirm that **All ports for the security group are allowed by default** is selected as the security group policy of CVM.


	Note: Please back up important data in advance. All the data on the CVM will be lost after reinstallation.
![](//mc.qcloudimg.com/static/img/fbdcf5e6938f0e72c9705a28e6f55163/image.png)

### 1.2 Configure a CVM through Web
You can configure the CVM parameters on [one-click deployment page](https://console.cloud.tencent.com/live/onestep/onestep) in the Tencent Cloud console.
- Check whether the services, such as LVB, VOD, IM and COS, are all activated.
- Enter the COS parameter.
- Enter the **public IP** and **root password** of the CVM.
- Click "Start Deployment" button. You need to reconfirm the security group configuration of the CVM if prompted with "Deployment Failed".
- ![](//mc.qcloudimg.com/static/img/9b4f3117157d920d50a2685ee271c392/image.png)

- Modify the LVB console callback URL to `http://Public IP or domain name of the CVM/callback/Live_callback.php`.
- ![](//mc.qcloudimg.com/static/img/00e333a3ab4b4e7737b11e56c725c6c0/image.png)

### 1.3 Verify deployment
Enter the access address for CVM API in a browser. `http://Public IP or domain name of the CVM/interface.php`. The deployment is successful if the following request result is returned. You can ignore the returned error message of JSON string.
![](//mc.qcloudimg.com/static/img/d3e3d8bf476b03ce86989740c760b25f/image.png)

## 2. More information
After one-click deployment is completed, the Mini LVB backend is not a "black box" to you. You can log in to the CVM using SSH, to check backend PHP source codes and relevant configurations.

2.1 How to log in to Tencent Cloud CVM?
- Tencent Cloud provides webShell, which is easy to use.
- ![](//mc.qcloudimg.com/static/img/1b3386560b937b23a60f87e93bcecca5/image.png)
- Connect to the CVM using SSH through putty.
- ![](//mc.qcloudimg.com/static/img/d4e08150c4728a1053019d2ec73b6822/image.png)

### 2.2 Where are the Mini LVB backend PHP source codes?
PHP source codes locate under the directory `/data/live_demo_service/` of the CVM.
![](//mc.qcloudimg.com/static/img/e09de7919e9820744669dc5a9e3c8edd/image.png)
### 2.3 Where is Nginx configuration file?
Nginx configuration file is the file `/etc/nginx/nginx.conf` of the CVM.
### 2.4 How to read more-detailed log?
To enable detailed log, you can create a directory named log under the directory `/data/live_demo_service/`.
## 3. After one-click deployment is completed
### 3.1 How to interface with terminal Mini LVB?
For more information, please see [How to quickly set up Mini LVB - terminal integration](https://cloud.tencent.com/document/product/454/7999#4.-.E7.BB.88.E7.AB.AF.E9.9B.86.E6.88.90)

### 3.2 How to configure uploading feature of UGC Mini LVB manually?
Currently, one-click deployment does not support the configuration item required to configure UGC, so you need to configure it manually.

Execute the following commands in sequence on the business server
a. **`wget -c http://download-1252463788.cossh.myqcloud.com/xiaozhibo_php_svr/xiaozhibo_business_svr_2.0.3.3033.zip`**
b. **`unzip xiaozhibo_business_svr_2.0.3.3033.zip`**
c. **`cp live_demo_service/interface/GetVodSignatureV2.php  /data/live_demo_service/interface/`**
d **`cd /data/live_demo_service/conf/ && vim OutDefine.php`**
e. Press "**I**" button to enter the Insert mode of vim, and add the following texts in bold.
   &emsp;** define('CLOUD_API_SECRETID','xxxxxxxxxxxxxxxxxxxxxxxxx');**  //Personal SecretId of cloud API, used to upload the UGC and implement it to VOD system [Cloud API Key](https://console.cloud.tencent.com/capi)
   &emsp;** define('CLOUD_API_SECRETKEY','xxxxxxxxxxxxxxxxxxxxxxxxx');**  //Personal SecrectKey of cloud API, used to upload the UGC and implement it to VOD system [Cloud API Key](https://console.cloud.tencent.com/capi) 
f. Press "**Esc**" and "**:wq!**", and then press "Enter", to save the modification into configuration file.
g. Execute **service nginx reload**, and restart Nginx service.



