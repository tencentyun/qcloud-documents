## 简介
用户可以通过文件存储控制台，查看当前已创建的文件系统，并可以对已创建的文件系统进行管理操作，如查看文件系统状态及用量、文件系统详情及挂载点信息等。

>!当文件系统处于 "创建中"、"创建失败"、"挂载中"、"删除中" 等状态时，将无法查看文件系统详情和执行删除操作。

## 前提条件

登录 [文件存储](https://console.cloud.tencent.com/cfs) 控制台，进入到文件系统列表页面。

## 查看文件系统状态及用量
在文件系统列表页面中，可以查看到当前文件系统使用量及文件系统状态。同时 CFS 支持通过文件系统名称、ID、VPCID 及 IP 对表格内容进行搜索。
![](https://main.qcloudimg.com/raw/f28e1ee1304c770b3340f3b0662433bf.png)


## 查看文件系统信息
在文件系统列表页面，单击文件系统名称，可以进入文件系统详情页面。在文件系统详情页面可以看到文件系统的基本信息和挂载点信息以及已挂载客户端信息。

### 文件系统基本信息
![](https://main.qcloudimg.com/raw/2c024eddd8293fd24a124e4908cf15a5.png)

### 挂载点信息
NFS 文件系统挂载点信息如下：
![](https://main.qcloudimg.com/raw/63f4f76c4f826f673aa009310fdf633c.png)

CIFS/SMB 文件系统挂载点信息如下：
![](https://main.qcloudimg.com/raw/33bfc3d0d7bae66c41fe0aa5cb0b0f16.png)

### 已挂载客户端信息
"已挂载客户端“选项卡下会展示已挂载该文件系统的客户端信息，但需要在客户端上安装 CFS 监控插件，若未安装插件则无法获取客户端信息，安装指引请参阅 [CFS 监控插件使用指引](https://cloud.tencent.com/document/product/582/34307)。
>!客户端信息展示会有1 - 3分钟的延迟。

![](https://main.qcloudimg.com/raw/d57e4ef245dd2745333388c264ca50d4.png)

## 修改文件系统名称
在文件系统列表页面，单击需要修改名称的文件系统，进入文件系统详情页面，单击实例名称右侧的<img src="https://main.qcloudimg.com/raw/a779dd9fce8c531f8ca36cf19c7d4d42.png"  style="margin:0;">，进行修改。
![](https://main.qcloudimg.com/raw/788dde5826205134b61d5524a4f9a1d2.png)


## 删除文件系统
当您不再需要使用某个文件系统时，您可以在文件系统列表中，找到需要删除的文件系统并在其右侧单击【删除】，即可将其删除。
![](https://main.qcloudimg.com/raw/853a695b37f82cf4fcc2c9eaf60933a9.png)

