## 简介

S3 Browser 是一款 Windows 客户端管理工具，可用于管理 Amazon S3、腾讯云 COS 等云存储资源。


## 支持系统

支持 Windows 系统。

## 下载地址

前往 [S3 Browser 官方下载](https://s3browser.com/)。


## 安装和配置

>! 以下配置步骤以 S3 Browser Windows v10.3.1版本为例，其他版本的配置过程可能存在一定差异，请注意相应调整。

1. 双击安装包，按照提示完成安装。
2. 打开工具，单击 Accounts > Add new account。
3. 在弹窗中配置以下信息，然后单击 Add new account。
   ![](https://qcloudimg.tencent-cloud.cn/raw/eec9c22d1ee9b904708122f0359f161d.png)

 - Display name：输入自定义用户名。
 - Account type：选择 S3 Compatible Storage。
 - REST Endpoint：格式为 `cos.<Region>.myqcloud.com`，例如访问成都地域的存储桶，则输入 `cos.ap-chengdu.myqcloud.com`，适用的地域简称（region）请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
 - Access Key ID：输入访问密钥信息 SecretId，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
 - Secret Access Key：输入访问密钥信息 Secretkey，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。

4. 账户信息添加完成后，在左侧窗口中可查看该用户名下的存储桶列表，即表示已配置完成。
   ![](https://qcloudimg.tencent-cloud.cn/raw/350c01b602a6d6dc11eb765e7af65e83.png)



## 管理 COS 文件

### 查询存储桶列表

在 Accounts 中选择之前设置的用户名，可查看该用户名下的存储桶列表。

>! 只能查看 REST Endpoint 配置的地域所对应的存储桶。如需查看其它地域的存储桶，可单击 **Accounts > Manage accounts**，并选择用户名，修改 REST Endpoint 参数为其他地域即可。



### 创建存储桶

单击 New bucket，在弹窗中输入完整的存储桶名称，例如 examplebucket-1250000000。存储桶所属地域默认为配置信息中的 REST Endpoint 所配置的地域。输入无误后，单击 **Create new bucket** 即可创建完成。

关于存储桶的命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。
![](https://qcloudimg.tencent-cloud.cn/raw/94c770854fd761b205ebe8a0c3a4a4c2.png)

>!在 S3 Browser 工具中创建存储桶，并查看该存储桶的所属地域始终为 us-east-1，可忽略。实际上创建的存储桶所属地域为配置信息中的 REST Endpoint 所配置的地域，以 COS 控制台上显示的地域为准。

### 删除存储桶

在存储桶列表中选择需删除的存储桶，右键单击 **Delete bucket**，并在弹窗中勾选复选框提示，最后单击 Delete Bucket 即可删除。


### 查询对象列表

单击对应的存储桶名称，即可查看该存储桶下的对象列表。

### 上传对象

在存储桶列表中选择需上传对象的存储桶或路径，然后单击 **Upload**，并选择想上传的文件或文件夹即可。

### 下载对象

在存储桶中选择需下载的对象，右键单击 **Download**，并选择对象存放的目标路径，即可下载。


### 复制对象

在存储桶中选择需复制的对象，右键单击 **Copy**，并选择对象复制后的目标路径，再右键单击 **Paste**，即可完成对象复制操作。

>!如果源对象路径和复制后的目标路径一致，则无法进行复制操作。

### 重命名对象

在存储桶中找到需重命名的对象，并右键单击 **Rename**，输入新名称即可。


### 删除对象

在存储桶中找到需删除的对象，并右键单击 **Delete**，即可删除对象。


### 移动对象

在存储桶中选择需移动的对象，并右键单击 **Move to**，然后在弹窗中选择目标存储桶或目标路径，最后单击 **OK** 即可。




### 其他功能

除了以上功能，S3 Browser 还支持其他功能，例如设置对象 ACL、查看对象元数据、自定义 Headers、获取对象 URL 等。用户可根据实际需求进行操作。



