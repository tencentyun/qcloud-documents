
本文介绍如何将 RTMP 流接入至智能视图计算平台服务。**本文将以 OBS软件推流为例，您可配置到您的设备端或所支持的软件端。**

## 准备工作

1. 开通 [智能视图计算平台](https://console.cloud.tencent.com/iss)。
2. 完成智能视图计算平台**服务配置**，详细请参见[创建服务配置](https://cloud.tencent.com/document/product/1344)。

## 步骤 1：创建设备

1. 登录 [智能视图计算平台控制台](https://console.cloud.tencent.com/iss)。
2. 在左侧导航栏中，单击展开**设备管理**，进入**设备接入**页面。
3. 在**设备组织**下选择需要添加设备的组织。
4. 单击**添加设备**，根据需求可选择**手动添加**或**批量导入**，操作如下。
   ![](https://qcloudimg.tencent-cloud.cn/raw/537839e7172ee66244639cd4953bd89a.png)
5. 以**手动添加**为例在弹出的窗口中，**接入协议**选择**RTMP**并完善设备名称、服务节点等编辑项后单击**确定**，完成设备添加。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a97fd2f8ccbd032aeb208429e5fdfe59.png)

## 步骤 2：获取 RTMP 设备信息

**设备接入**页面，单击设备名称，进入刚创建的设备详情页面，**推流地址**如下。
![](https://qcloudimg.tencent-cloud.cn/raw/7e42aaa6b7090ee8fa69cbff55c9c78b.png)

## 步骤 3：使用 OBS 进行推流

1. 进入 [OBS 官网](https://obsproject.com/download) 下载并安装推流工具。

> ?OBS是一个免费开源的视频录制和视频实时交流软件,其有多种功能并广泛使用在视频采集，直播等领域。

1. 打开 OBS，单击底部工具栏的 **控件** > **设置** 按钮进入设置界面。
   ![](https://qcloudimg.tencent-cloud.cn/raw/827599161fb4295169de06029aaee568.png)
2. 单击 **推流** 进入推流设置页，进行如下设置：
3. 选择服务类型为：自定义。
4. 填写服务器地址：填写在步骤 2 推流地址中的**服务器地址部分**，例如 **rtmp://61...152/live/**。
5. 填写流密钥：填写在步骤 2 推流地址中**流名称及之后的所有内容部分**，例如 **0d9...2S?token=cms_131...37A**。
6. 单击右下角 **确定**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5a384b9432ae28e14250abfd2b7f629a.png)
7. 单击工具栏的 **控件** > **开始推流**，即可进行推流测试。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4c206f81474d3fb8a6bffe7529ffe9e0.png)


## 步骤4：完成注册

1. 切换至智能视图计算平台控制台，此时设备状态显示为**”在线“**，**表示设备注册成功已上线，即此时有流接入。**

2. 点击**实况预览**，查看实时流画面。

   ![rtmp2](/Users/jason/Desktop/新版本配图/设备端配图/rtmp2.png)

