## 简介

CloudBerry Explorer 是一款可用于管理对象存储（Cloud Object Storage，COS）的客户端工具。通过 CloudBerry Explorer 可实现将 COS 挂载在 Windows 等操作系统上，方便用户访问、移动和管理 COS 文件。


## 支持系统

支持 Windows、macOS 系统。

## 下载地址

前往 [CloudBerry 官方下载](https://www.cloudberrylab.com/download-thanks.aspx?prod=cbes3free&src=ms)。

## 安装和配置

>! 以下配置步骤以 CloudBerry Explorer Windows v6.3版本为例，其他版本的配置过程可能存在一定差异，请注意相应调整。
>

1. 双击安装包，按照提示完成安装。
2. 打开工具，选择并双击 S3 Compatible。
3. 在弹窗中配置以下信息，单击 Test Connection 显示连接成功即可。
![](https://qcloudimg.tencent-cloud.cn/raw/c7c351ac3c8fbabcf635ae7699fb3dba.png)
配置项说明如下：
 - Display name：输入自定义用户名。
 - Service point：格式为 `cos.<Region>.myqcloud.com`，例如访问成都地域的存储桶，则输入 `cos.ap-chengdu.myqcloud.com`，适用的地域简称（region）请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
 - Access key：输入访问密钥信息 SecretId，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
 - Secret key：输入访问密钥信息 Secretkey，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
4. 账户信息添加完成后，在 Source 中选择之前设置的用户名，可查看该用户名下的存储桶列表，即表示已配置完成。
![](https://qcloudimg.tencent-cloud.cn/raw/5b001159dea9eada859a06014d1cbdfd.png)

## 管理 COS 文件

### 查询存储桶列表

在 Source 中选择之前设置的用户名，可查看该用户名下的存储桶列表。

>! 只能查看 Service point 配置的地域所对应的存储桶。如需查看其它地域的存储桶，可单击 **File > Edit Accounts**，并选择用户名，修改 Service point 参数为其他地域即可。
>

### 创建存储桶

单击图中的图标，在弹窗中输入完整的存储桶名称，例如 examplebucket-1250000000。输入无误后，单击 **OK** 即可创建完成。
关于存储桶的命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。
![](https://qcloudimg.tencent-cloud.cn/raw/9192916f402017e27f8b233ac2c72c9e.png)

### 删除存储桶

在存储桶列表中选择需删除存储桶，右键单击 **Delete** 即可删除。


### 上传对象

在存储桶列表中选择需上传对象的存储桶或路径，然后在本地计算机中选择需上传的对象，并将其拖拽到左侧窗口中，即可完成上传操作。
![](https://qcloudimg.tencent-cloud.cn/raw/92aea7e39697ab46bb29f430bc58206a.png)

### 下载对象

在左侧窗口中选择需下载的对象，然后将对象拖拽到右侧本地计算机的文件夹中，即可完成下载操作。
![](https://qcloudimg.tencent-cloud.cn/raw/1ed1432256fd44ac2f9739f6fda263b1.png)

### 复制对象

在工具的右侧窗口中，选择对象被复制后的目标路径，然后在左侧窗口中选择需复制的对象，右键单击 **Copy**，确认弹窗信息，即可完成对象复制操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5d1801cd20fe1885ee6e16ddec1139c5.png)

### 重命名对象

在存储桶中找到需重命名的对象，并右键单击 **Rename**，输入新名称即可。


### 删除对象

在存储桶中找到需删除的对象，并右键单击 **Delete**，即可删除对象。

### 移动对象

在工具的右侧窗口中，选择对象被移动后的目标路径，然后在左侧窗口中选择需移动的对象，并右键单击 **Move**，确认弹窗信息，即可完成对象移动操作。
![](https://qcloudimg.tencent-cloud.cn/raw/5b4f20a2f400bf24f70dde5b93ed8053.png)


### 其他功能

除了以上功能，CloudBerry Explorer 还支持其他功能，例如设置对象 ACL、查看对象元数据、自定义 Headers、获取对象 URL 等。用户可根据实际需求进行操作。


## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！


