## 设备创建
通过控制台或者云 API 创建设备，把设备密钥写入设备，详情可参考 [设备接入准备](https://cloud.tencent.com/document/product/1131/52737)。

## 启动设备
详细使用方法参考设备端 SDK 里的 readme.md 文档。
- device_info.json 里的 productId、deviceName、deviceSecret 分别填入创建设备时返回的 ProductId、DeviceName、DevicePSK。
- 测试前需要把单独下载的 demo_media 文档按文件书名放入测试环境目录下。

## APP 体验
### 版本问题
- 建议使用最新版本的设备端 SDK 和 demo APP 配合进行体验。
- 版本在2.3.0以上的设备端 SDK 需要匹配版本在2.3.0以上的 demo APP 进行使用。
- 版本在2.2.0以上的设备端 SDK 需要匹配版本在2.2.0以上的 demo APP 进行使用。

### 操作指南
#### 登录 APP（以 Android APP 为例）
1. 打开 demo APP，**单击 VIDEO** > **IoT Video（消费版）**进入 IoT Video Demo 界面。
2. Access ID、Access Token 和 Product ID 分别填入腾讯云账号的 Secretid、Secretkey 和对应设备 的productid。（secretid、secretkey 获取方式：登录 [访问管理控制台](https://console.cloud.tencent.com/cam) > **访问密钥** > **API 密钥管理** 获取 secretId 和 secretKey。如果没有密钥则单击**新建密钥**）。
![](https://main.qcloudimg.com/raw/04916abc449741f91e5b3714e4257cc9.png)
3. 单击**登录**进入 demo APP 主页（如果使用子账号测试，需要给子账号配置策略：QcloudIotVideoFullAccess、QcloudIotExplorerFullAccess）。<br>
<img src="https://main.qcloudimg.com/raw/4ae1547b788081c0533737d225f46281.png" width="40%">

#### 直播预览
1. 单击需要预览的设备，选择**预览**。
<img src="https://main.qcloudimg.com/raw/3e23337bfca6eae3700940f29f2da080.png" width="40%">
2. 直播预览成功后，会展示该次预览的 P2P 连接时间和出图时间。 <br>
<img src="https://main.qcloudimg.com/raw/2e4e1a50c66030e221447ae0ec3ad4cd.png" width="40%">

#### 存储回放
>! 使用云端存储回放前需要先 [开通云存服务](https://cloud.tencent.com/document/product/1131/53636)。
>
1. 单击需要预览的设备，选择**回放**。
<img src="https://main.qcloudimg.com/raw/c8e5e01778004285c7995886a4943ed5.png" width="40%">
2. 可以选择有录像的时间进行录像回放。<br>
<img src="https://main.qcloudimg.com/raw/4e12458d2270ddf1e9fff3b93f2ce56a.png" width="40%">

## APP 功能列表

<table>
<thead>
<tr>
<th>
功能模块
</th>
<th>
视频预览
</th>
</tr>
</thead>
<tr>
<td rowspan="5">
直播预览
</td>
<td>
视频预览
</td>
</tr>
<tr>
<td>
语音对讲
</td>
</tr>
<tr>
<td>
直播录像
</td>
</tr>
<tr>
<td>
直播拍照
</td>
</tr>
<tr>
<td>
清晰度切换
</td>
</tr>
<tr>
<td>
录像回放
</td>
<td>
云端录像回放
</td>
</tr>

<table>



