本文档主要介绍将腾讯云直播截图或鉴黄数据存储至腾讯云对象存储中，以实现通过存储桶（COS Bucket）存储云直播截图或鉴黄数据。首先要创建 COS Bucket ，然后通过 COS Bucket 给云直播授权，最后在直播控制台进行直播截图鉴黄设置，云直播截图或鉴黄数据即可写入指定 COS Bucket（新版控制台功能）。

### 创建 COS Bucket
1. 登录对象存储控制台选择[【存储桶列表】](https://console.cloud.tencent.com/cos5/bucket)。
2. 单击【创建储存桶】在弹出页填写相应信息后，单击【确定】即可成功创建存储桶 COS Bucket。
![](https://main.qcloudimg.com/raw/87c9c42d4c271675b73e3970214a7945.png)
>!
>- Bucket name 为 test，不含 `-125****577`。  
>- 以上信息均可按照业务实际需要配置。
3. 您可以根据业务需求开启 COS bucket 的 CDN 加速，单击已创建的存储桶名称或【配置管理】，单击左侧的【域名与传输管理】>【默认 CDN 加速域名】，在【默认 CDN 加速域名】配置项中单击【编辑】，把当前状态设置为开启，然后配置下方选项，具体配置方法可参见 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636)，配置完成之后点击【保存】即可开启 CDN 加速。
![](https://main.qcloudimg.com/raw/96538f69d6de9e987f206aa8b26bfa5d.png)

 

### 授权给云直播截图存储

1. 为腾讯云截图存储开通数据写入权限，授权的根账号 ID：`-125****577`。
   1. 在存储桶的【[存储桶列表](https://console.cloud.tencent.com/cos5/bucket)】选择授权的存储桶，单击右侧【配置管理】进入该存储桶配置管理界面，选择【权限管理】>【[存储桶访问权限](https://console.cloud.tencent.com/cos5/bucket/setting?type=aclconfig&anchorType=accessPermission&bucketName=text-1258968577&projectId=&path=%252F&region=ap-guangzhou)】添加用户，用户类型选择根账号，<b>并输入根账号 ID：`-125****577`</b>。单击【保存】。
![](https://main.qcloudimg.com/raw/9105686a61bb5b846741d7326c9b8d1b.png)
![](https://main.qcloudimg.com/raw/1002e8d48a20f7bbaf8a674423976bdb.png)
或单击【授权管理】进入授权管理界面，勾选需授权的存储桶，打开【公共权限】和【用户权限】按钮添加用户。用户类型选择根账号，<b>并输入根账号 ID：`-125****577`</b>。单击【保存】并【确定】。
![](https://main.qcloudimg.com/raw/e7e90c31cccdda1f9b9ede3024346e0f.png)
![](https://main.qcloudimg.com/raw/2848fee89c03a70cc4aa6b55087e7c8b.png)
>! <b>账号 ID 需填入根账号（也就是主账号） ID：`125****577` 进行授权。（根账号 ID：`125****577` 即为云直播服务 APPID，直接输入 `125****577` 即可）</b>。
   2. 存储桶访问权限设置 API 请参考 [PUT Bucket acl 文档](https://cloud.tencent.com/document/product/436/7737)。
2. 获取已授权 COS Bucket 信息。
   1. 在存储桶的【[概览](https://console.cloud.tencent.com/cos5/bucket/setting?type=bucketoverview&bucketName=text-1258968577&projectId=&path=%252F&region=ap-guangzhou)】里即可查看到 COS 的所有信息。访问域名（源站域名）包含 bucket name、cos appid 和 bucket region。
![](https://main.qcloudimg.com/raw/81d6c9907a6ead48a83451be4a62843e.png)
    - bucket name：`test`
    - cos appid：`125****577`
    - bucket region：`ap-nanjing`

   2. 提交以上3个字段信息，系统将会把直播截图数据存于已授权的 COS Bucket 中。
