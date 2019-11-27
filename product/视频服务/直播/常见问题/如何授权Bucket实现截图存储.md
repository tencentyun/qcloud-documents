本文档主要介绍将腾讯云直播截图或鉴黄数据存储至腾讯云对象存储中，以实现通过存储桶（COS Bucket）存储云直播截图或鉴黄数据。首先要创建 COS Bucket ，然后通过 COS Bucket 给云直播授权，最后在直播控制台进行直播截图鉴黄设置，云直播截图或鉴黄数据即可写入指定 COS Bucket（新版控制台功能）。
### 创建 COS Bucket
1. 登录对象存储控制台选择[【存储桶列表】](https://console.cloud.tencent.com/cos5/bucket)。
2. 单击【创建储存桶】在弹出页填写相应信息后，单击【确定】即可成功创建存储桶 COS Bucket。
 ![](https://main.qcloudimg.com/raw/31b306873ac7f72aa96d86b0ba91a948.png)
>!
> - Bucket name 为 buckettest123，不含 -1271775094。  
> - 以上信息均可按照业务实际需要配置。
3. 您可以根据业务需求开启 COS bucket 的 CDN 加速，单击已创建的存储桶名称或【配置管理】，选择“域名管理”项，单击【编辑】即可进行加速设置，设置完成后单击【保存】即可。
 ![](https://main.qcloudimg.com/raw/1e4e66a47fadaa39601d31960c0085c3.png)

### 授权给云直播截图存储
1. 为腾讯云截图存储开通数据写入权限，授权的根账号 ID：3508645126。
	1. 在存储桶的【[存储桶列表](https://console.cloud.tencent.com/cos5/bucket)】>【权限管理】>【存储桶访问权限】添加用户，用户类型选择根账号，**并输入根账号 ID：3508645126**
	>! **账号 ID 需填入根账号（也就是主账号） ID：3508645126 进行授权。（根账号 ID：3508645126 即为云直播服务，直接输入 3508645126 即可）**。
	![](https://main.qcloudimg.com/raw/2417cd97ea3ae2f3ebf57ff1f8834ba1.png)
	2. 存储桶访问权限设置 API 可参考 [PUT Bucket acl 文档](https://cloud.tencent.com/document/product/436/7737)。
2. 获取已授权 COS Bucket 信息。
	1. 在存储桶的【基础配置】里即可查看到 COS 的所有信息。访问域名（源站域名）包含 bucket name、cos appid 和 bucket region。
	![](https://main.qcloudimg.com/raw/f442ced48355a2c94b858cebd8928cb5.png)
	 - bucket name：buckettest123
	 - cos appid：1259200900
	 - bucket region：ap-chengdu
	2. 提交以上3个字段信息，系统将会把直播截图数据存于已授权的 COS Bucket 中。
