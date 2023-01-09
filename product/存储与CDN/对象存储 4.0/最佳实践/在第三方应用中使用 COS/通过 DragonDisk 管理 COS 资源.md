## 简介

DragonDisk 是一个免费的文件管理工具，提供类似 Windows 资源管理器的图形界面，支持备份、数据共享等功能。用户通过 DragonDisk 工具可方便快捷地管理对象存储（Cloud Object Storage，COS）文件。

## 支持系统

适用于 Windows、Mac OS X 和各种 Linux 发行版。

## 下载地址

前往 [DragonDisk 官方下载](http://download.dragondisk.com/download-s3-compatible-cloud-client.html)。


## 安装和配置

>! 以下配置步骤以 DragonDisk Windows v1.05 版本为例，其他版本的配置过程可能存在一定差异，请注意相应调整。
>

1. 双击安装包，按照提示完成安装。
2. 打开工具，选择 **File > Accounts**，并在弹窗中单击 **New** 添加账号配置信息。
3. 在弹窗中配置以下信息。
![](https://qcloudimg.tencent-cloud.cn/raw/a8d83b57beafd32f916e7d530dd46416.png)
配置项说明如下：
 -  Provider：选择 Other S3 compatible service。
 - Service Endpoint：格式为 `cos.<Region>.myqcloud.com`，例如访问成都地域的存储桶，则输入 `cos.ap-chengdu.myqcloud.com`，适用的地域简称（region）请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
 -  Account name：输入自定义用户名。
 - Access key：输入访问密钥信息 SecretId，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
 - Secret key：输入访问密钥信息 Secretkey，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
4. 账户信息添加完成后，在 Root 中选择之前设置的用户名，可查看该用户名下的存储桶列表，即表示已配置完成。
![](https://qcloudimg.tencent-cloud.cn/raw/95aa5d0160953181856e1531b8e4039b.png)

## 管理 COS 文件

### 查询存储桶列表

在 Root 中选择之前设置的用户名，可查看该用户名下的存储桶列表。

>! 该操作只能查看 Service Endpoint 配置的地域所对应的存储桶。如需查看其它地域的存储桶，可单击 **File > Accounts**，并选择用户名，修改 Service Endpoint 参数为其他地域即可。
>



### 创建存储桶

1. 选择用户名并右键单击 **Create bucket**，在弹窗中输入完整的存储桶名称，例如 examplebucket-1250000000。
![](https://qcloudimg.tencent-cloud.cn/raw/46fd8b1296908a39b2949b7895dd1a60.png)
2. 输入无误后，单击 **OK** 即可创建完成。
关于存储桶的命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。

### 删除存储桶

在存储桶列表中选择需删除存储桶，并右键单击 **Delete bucket** 即可。


### 上传对象

在存储桶列表中选择需上传对象的存储桶或路径，然后在本地计算机中选择需上传的对象，并将其拖拽到对应的存储桶或路径下，即可完成上传操作。


### 下载对象

在存储桶列表中找到对象所在的存储桶，然后将对象拖拽到右侧本地计算机的文件夹中，即可完成下载操作。
![](https://qcloudimg.tencent-cloud.cn/raw/abfa0db54ecfef0e6dd658a964bed0a9.png)


### 复制对象

在左侧窗口中选择需复制的对象，并右键单击 **Copy**，然后在对象被复制后的目标路径下右键单击 **Paste**，即可完成对象复制操作。


### 重命名对象

在存储桶中找到需重命名的对象，并右键单击 **Rename**，输入新名称即可。


### 删除对象

在存储桶中找到需删除的对象，并右键单击 **Delete**，即可删除对象。

### 移动对象

在左侧窗口中选择需移动的对象，并右键单击 **Cut**，然后在对象被移动后的目标路径下右键单击 **Paste**，即可完成对象移动操作。


### 其他功能

除了以上功能，DragonDisk 还支持其他功能，例如设置对象 ACL、查看对象元数据、自定义 Headers、获取对象 URL 等。用户可根据实际需求进行操作。



## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！




