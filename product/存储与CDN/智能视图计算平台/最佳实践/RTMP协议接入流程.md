本文将介绍如何通过 RTMP 协议接入至智能视图计算平台服务。**以 OBS 软件推流为例，您可参考配置您的设备端或所支持的软件端。**


## 1.创建设备

1. 登录 [智能视图计算平台控制台](https://console.cloud.tencent.com/iss)。
2. 在左侧导航栏中，单击展开**设备管理**，进入**设备接入**页面。
3. 在**设备组织**下选择需要添加设备的组织。
4. 单击**添加设备**，根据需求可选择**手动添加**或**批量导入**，操作如下。
   ![](https://qcloudimg.tencent-cloud.cn/raw/537839e7172ee66244639cd4953bd89a.png)
5. 以**手动添加**为例，在弹出的窗口中，**接入协议**选择 **RTMP** 并完善设备名称、服务节点等编辑项后单击**确定**，完成设备添加。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a97fd2f8ccbd032aeb208429e5fdfe59.png)

## 2.获取 RTMP 推流地址

单击设备名称，进入刚创建的设备详情页面，**推流地址**如下。

>?平台生成的推流地址 URL 格式为 rtmp://{domain name}/{appname}/{streamname}，其中 appname 默认为 live，streamname 为平台生成的设备 ID。

![](https://qcloudimg.tencent-cloud.cn/raw/7e42aaa6b7090ee8fa69cbff55c9c78b.png)

>?可使用**导出设备信息**功能,批量导出设备配置信息。

![](https://qcloudimg.tencent-cloud.cn/raw/59a731e393986a1ade096240f2b1bbe8.png)

## 3.使用 OBS 进行推流

1. 进入 [OBS 官网](https://obsproject.com/download) 下载并安装推流工具。

> ?OBS 是一个免费开源的视频录制和视频实时交流软件,其有多种功能并广泛使用在视频采集，直播等领域。

2.打开 OBS，单击底部工具栏的 **控件** > **设置** 按钮进入设置界面。
 ![](https://qcloudimg.tencent-cloud.cn/raw/827599161fb4295169de06029aaee568.png)
3.单击 **推流** 进入推流设置页，进行如下设置。
![](https://qcloudimg.tencent-cloud.cn/raw/5a384b9432ae28e14250abfd2b7f629a.png)

| 配置参数   | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| 服务类型   | 默认自定义                                                   |
| 服务器地址 | 填写步骤 2 推流地址中的服务器地址部分，例如 rtmp://61...152/live/ |
| 流密钥     | 填写步骤 2 推流地址中流名称及之后的所有内容部分，例如0d9...2S?token=cms_131...37A |

4.单击工具栏的控件 > 开始推流，即可进行推流。
![](https://qcloudimg.tencent-cloud.cn/raw/1d132af5578bfa8f983398c96800880b.png)


## 4.完成注册

切换至智能视图计算平台控制台，此时设备状态显示为**在线**，表示设备注册成功已上线，即此时有流上传。 点击**实况预览**可查看实时画面。



