
初次使用对象存储 COS，建议您先了解 COS [基本概念](https://cloud.tencent.com/document/product/436/6222)、[规格与限制](https://cloud.tencent.com/document/product/436/14518) 和  [常见问题](https://cloud.tencent.com/document/product/436/30748)。

通过对象存储控制台，您可以快速进行创建存储桶、上传/下载对象等操作，基本操作流程如下：





## 步骤1：注册腾讯云账号
如果已在腾讯云注册，可忽略此步骤。
<div style="background-color:#5291F8; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cvm?tab=lite" target="_blank"  style="color: white; font-size:16px;">点此注册腾讯云账号</a></div>

## 步骤2：开通 COS 服务
<div style="background-color:#5291F8; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/cos5" target="_blank"  style="color: white; font-size:16px;">点此开通 COS 服务</a></div>

<br>
勾选“我已阅读并同意”，并单击【立即开通服务】，即可免费开通对象存储 COS 服务。<br>
<img src="https://main.qcloudimg.com/raw/fd9ab29b897288980840a66032b0e143.png" width="80%">


## 步骤3：创建存储桶
1. 在左侧导航栏中单击【存储桶列表】，进入存储桶管理页。
2. 单击【创建存储桶】，输入存储桶信息。
 - 名称：存储桶名称，例如输入 examplebucket。
 - 所属地域：存储桶存放地域，选择与您最近的一个地区，例如我在 “深圳”，地域选择 “广州”。
 - 访问权限：存储桶访问权限，此处我们选择“公有读私有写”。
![](https://main.qcloudimg.com/raw/38addaf41a18eab91259469c30af7b0e.jpg)
3. 单击【确定】，即可创建存储桶。


## 步骤4：上传对象
1. 单击存储桶名称，进入存储桶列表页。
2. 选择【上传文件】>【选择文件】，选择需要上传至存储桶的文件，例如 exampleobjext.txt。
![](https://main.qcloudimg.com/raw/20bb9681345321a06332ce359f8ca979.jpg)
3. 单击【上传】，即可将 exampleobjext.txt 上传至存储桶。



## 步骤5：下载对象
1. 在 exampleobjext.txt 右侧，单击【详情】，进入对象属性页。
2. 在【基本信息】配置项中，复制【对象地址】。
3. 您即可以通过对象地址在浏览器下载对象。



