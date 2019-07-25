本文档主要介绍将腾讯云直播截图或鉴黄数据存储至腾讯云对象存储中，以实现通过存储桶（COS Bucket）存储云直播截图或鉴黄数据。首先要创建 COS Bucket ，然后通过 COS Bucket 给云直播授权，最后在直播控制台进行直播截图鉴黄设置，云直播截图或鉴黄数据即可写入指定 COS Bucket（新版控制台功能）。
## 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 创建存储桶 COS Bucket。

 ![](https://main.qcloudimg.com/raw/53c954ec28c7137382945d115638e59c.png)
>!
	 * Bucket name 为 buckettest123，不含 -1271775094。  
	 * 以上信息均可按照业务实际需要配置。
	 
3. 根据您业务需求开启 COS bucket 的 CDN 加速。
![](https://main.qcloudimg.com/raw/d8c518dc038bb276d254858dd7085620.png)

## 授权给云直播截图存储
1. 为腾讯云截图存储开通数据写入权限，授权的根账号 ID：3508645126。
	1. 在存储桶的【权限管理】>【存储桶访问权限】添加用户，用户类型选择根账号，**并输入根账号 ID：3508645126**
	>! **此处需填入根账号（也就是主账号） ID：3508645126 进行授权。（根账号 ID：3508645126 即为腾讯云直播服务，直接输入 3508645126 即可）**。
	![](https://main.qcloudimg.com/raw/e355595166fcdbbde4a1ae50001777d2.png)
	2. 存储桶访问权限设置 API 可参考 [PUT Bucket acl 文档](https://cloud.tencent.com/document/product/436/7737)。

2. 获取已授权 COS Bucket 信息。
	1. 在存储桶的【基础配置】里即可查看到 COS 的所有信息。访问域名（源站域名）包含 bucket name、cos appid 和 bucket region。
	![](https://main.qcloudimg.com/raw/ccc156b63dd5103f1cf722c7256b130d.png)
	 - bucket name：buckettest123
	 - cos appid：1259200900
	 - bucket region：ap-chengdu
	2. 提交以上3个字段信息，系统将会把直播截图数据存于已授权的 COS Bucket 中。
