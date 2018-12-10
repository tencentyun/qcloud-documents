本文档主要介绍如何新建 COS Bucket，并授权该 Bucket 给腾讯直播截图用于存储截图数据。
## Step 1：创建 COS Bucket
### 1. 登录 [COS5 控制台](https://console.cloud.tencent.com/cos5) 
### 2. 创建 bucket，如：buckettest123
 ![](https://main.qcloudimg.com/raw/ccc41b01543c7c9d354fc129ca23da7f.png)
其中 Bucket name 为 buckettest123，不含 -1271775094。
>! 以上信息均可按照业务实际需要配置。

### 3. 根据需求开启加速域名等常规操作
![](https://main.qcloudimg.com/raw/10ae9f4ba37443c731cc3ea6d14882f3.png)

## Step 2：授权 COS Bucket 于腾讯云直播截图
### 1. 授数据写入权给腾讯云截图存储，授权根账号为：3508645126
 - **方法一：存储桶访问权限设置**
 ![](https://main.qcloudimg.com/raw/a0f17459b2bac4b05e0792aa7407175e.png)
 存储桶访问权限设置 API [PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737)
 - **方法二： Policy 权限设置**
   ![](https://main.qcloudimg.com/raw/86b6a4ce635dd030304b8ea161a74bc7.png)
	 ![](https://main.qcloudimg.com/raw/bd711fa42f3f0737ecfabc6d8ce9f7a4.png)
 Policy权限设置 API [PUT Bucket policy](https://cloud.tencent.com/document/product/436/8282)
### 2. 得到 COS 信息用于后续开启截图
![](https://main.qcloudimg.com/raw/9481bb800c10c57a04f8418b75cd81a8.png)
由基础配置页面能看到本次例子 COS 的所有信息：
- cos appid：1251775094
- bucket name：buckettest123
- bucket region：ap-chengdu
- 红框访问域名为源站域名
