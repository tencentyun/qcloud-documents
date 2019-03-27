本文档主要介绍将腾讯云直播截图或鉴黄数据存储至腾讯云对象存储中，以实现通过存储桶（COS Bucket）存储云直播截图或鉴黄数据。首先要创建 COS Bucket ，然后通过 COS Bucket 给云直播授权，最后在直播控制台进行直播截图鉴黄设置，云直播截图或鉴黄数据即可写入指定 COS Bucket（新版控制台功能）。
## 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 创建存储桶 COS Bucket。
 ![](https://main.qcloudimg.com/raw/f2c439303d6945e5122824b56196db70.png)
>!
	 * Bucket name 为 buckettest123，不含 -1271775094。  
	 * 以上信息均可按照业务实际需要配置。
3. 根据业务需求开启加速域名。
![](https://main.qcloudimg.com/raw/d4c51e17afbf143569f90b06219953d5.jpg)

## 授权给云直播截图存储
 1. 为腾讯云截图存储开通数据写入权限，例如授权的根账号 ID：3508645126。
 
  **方法一：通过【存储桶访问权限】开通**
	1. 在存储桶的【权限管理】-【存储桶访问权限】添加用户，用户类型选择根账号，**并输入根账号 ID：3508645126**。
   >! **此处需填入根账号 ID：3508645126 进行授权**。

		![](https://main.qcloudimg.com/raw/5b34ac022488d04d7a3d88ae1381aacb.jpg)
 
	2. 存储桶访问权限设置 API 可参考 [PUT Bucket acl 文档](https://cloud.tencent.com/document/product/436/7737)。

  **方法二： 通过【Policy 权限设置】开通**
   1. 在存储桶的【权限管理】-【Policy 权限设置】添加策略。
   ![](https://main.qcloudimg.com/raw/4cd148cbb03c8fc3c8e9379587568fd4.jpg)
   2. 单击添加策略，然后添加根账号用户，账号 ID：3508645126。
	![](https://main.qcloudimg.com/raw/95f2478b98d1e9ad64825ede3ca296cf.png)
   3.  Policy 权限设置 API 参考 [PUT Bucket policy 文档](https://cloud.tencent.com/document/product/436/8282)。

 2. 获取已授权 COS Bucket 信息。
1. 在存储桶的【基础配置】里即可查看到 COS 的所有信息。访问域名（源站域名）包含 bucket name、cos appid 和 bucket region。
![](https://main.qcloudimg.com/raw/238ce3abafa0d10614a47c422e16db65.png)
	 - bucket name：buckettest123
	 - cos appid：1251775094
	 - bucket region：ap-chengdu
2. 提交以上3个字段信息，系统将会把直播截图数据存于已授权的 COS Bucket 中。
