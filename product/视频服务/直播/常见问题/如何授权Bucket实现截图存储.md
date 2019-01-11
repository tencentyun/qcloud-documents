本文档主要介绍将腾讯云直播截图或鉴黄数据存储至腾讯云对象存储中，以实现通过存储桶（COS Bucket）存储云直播截图或鉴黄数据。通过对 COS Bucket 授权和直播截图鉴黄设置，云直播截图或鉴黄数据可写入指定COS Bucket（新版控制台功能）。
## 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5) 
2. 创建存储桶 COS Bucket
 ![](https://main.qcloudimg.com/raw/f2c439303d6945e5122824b56196db70.png)
其中 Bucket name 为 buckettest123，不含-1271775094。
>! 以上信息均可按照业务实际需要配置。

3. 根据业务需求开启加速域名
![](https://main.qcloudimg.com/raw/0a22c79de6524d85ff000c7f2a3548ab.png)

## 授权给云直播截图存储
 1. 为 腾讯云截图存储 开通【数据写入】权限，授权的根账号ID：3508645126。
 
  **方法一：通过【存储桶访问权限】开通**
   1. 在存储桶的【权限管理】-【存储桶访问权限】，添加用户，用户类型选择根账号，账号ID：3508645126。
 ![](https://main.qcloudimg.com/raw/10fbab5c8fa5a4a6435c7af6a079c9bc.png)
   2. 存储桶访问权限设置API可参考 [PUT Bucket acl文档](https://cloud.tencent.com/document/product/436/7737)。

  **方法二： 通过【Policy权限设置】开通**
   1. 在存储桶的【权限管理】-【Policy权限设置】，添加策略。
   ![](https://main.qcloudimg.com/raw/d70bbcb727bfc1505725bcad87d491b8.png)
   2. 在添加策略中，添加根账号用户，账号ID：3508645126。
	![](https://main.qcloudimg.com/raw/95f2478b98d1e9ad64825ede3ca296cf.png)
   3.  Policy权限设置 API参考[PUT Bucket policy文档](https://cloud.tencent.com/document/product/436/8282)



 2. 获取已授权COS Bucket信息。
1. 在存储桶的【基础配置】里即可查看到COS的所有信息
![](https://main.qcloudimg.com/raw/238ce3abafa0d10614a47c422e16db65.png)
 【访问域名】即为源站域名，包含bucket name、cos appid和bucket region（以上图为例）：
 cos appid：1251775094
 bucket name：buckettest123
 bucket region：ap-chengdu
2.提交以上3个字段信息，系统将会把直播截图数据存于此已授权的COS Bucket中，
