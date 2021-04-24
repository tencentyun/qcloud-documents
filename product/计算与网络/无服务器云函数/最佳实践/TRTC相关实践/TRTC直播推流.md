## 操作场景

本文为您介绍如何利用云函数，通过 API 网关调用，将已有的录播视频或者 RTMP 直播流推送到 TRTC 房间进行直播。如果您想要开启推流直播的实时记录，可以选择使用 redis，则会将进度实时写入 redis。
![img](https://main.qcloudimg.com/raw/3c3ad59015712158e08342f80d8a8cde.png)

API 网关调用涉及的参数如下：

| 参数名称      | 类型    | 必选 | 描述                                             |
| ------------- | ------- | ---- | ------------------------------------------------ |
| videoSrc      | String  | 是   | 被推流的视频源。                                 |
| sdkAppId      | String  | 是   | 应用 ID，用于区分不同 TRTC 应用。                 |
| roomId        | String  | 是   | 房间 ID，用于在一个 TRTC 应用中唯一标识一个房间。 |
| userId        | String  | 是   | 用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。 |
| userSig       | String  | 是   | 用户签名，用于对一个用户进行登录鉴权认证。       |
| clientRole    | String  | 否   | 角色名称，默认为 anchor（主播）                   |
| redis         | Boolean | 否   | 是否使用 redis，默认为false。                     |
| redisHost     | String  | 否   | redis 为 true 时，redis 的 host 地址。                 |
| redisPort     | Integer | 否   | redis 为 true 时，redis 的访问端口号。               |
| redisPassword | String  | 否   | redis 为 true 时，redis 的访问密码。                 |

>? 如果 redis 的值为 false，直接从 videoSrc 视频源拉流下来做直播推流，直播流永远都是从最新开始；如果为 true，对于同一个 videoSrc 视频源，先去 redis 中查询是否有上一次直播流推流记录。如果有，则恢复上一次推流；如果没有，则从新开始推流。直播推流进度通过回调实时写入redis。



## 操作步骤

[](id:step01)
### 创建云函数

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
	![img](https://main.qcloudimg.com/raw/3d1e48528307d1ef693603c330d7f025.png)
	- **创建方式**：选择【模板创建】。
	- **模糊搜索**：输入“TRTC直播推流”，并进行搜索。
    单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
3. 单击【下一步】，函数名称默认填充，开启异步执行与状态追踪能力，执行超时时间可根据需要自行修改。
![img](https://main.qcloudimg.com/raw/c3dce45f0f08e6ed314ca24c82a02e8e.png)
4. 配置 API 网关触发器，默认新建 API 服务，不开启集成响应。你也可以选择自定义创建，自定义创建时确保集成响应关闭。
![img](https://main.qcloudimg.com/raw/3a198dac7c94d6712da1f250ef6b074c.png)
5. 单击【完成】即可完成函数创建和 API 网关触发器创建。
6. 如果要使用 redis 实时记录推流进度，由于 redis 只能私有网络访问，因此必须将云函数的 vpc 配置在与 redis 在同一个私有网络下。如下图所示：
![1618907406496](https://main.qcloudimg.com/raw/80916249822c4b1417f873f843c37390.png)

   
[](id:step02)
### 创建 TRTC 应用

1. 登录实时音视频控制台，选择左侧导航栏中的【[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
![img](https://main.qcloudimg.com/raw/7a7f16dc4c84bf5549a42b8d45820b7c.png)
2. 填写 Demo 名称，完成应用创建。你可以根据自己的客户端选择模板试运行。

[](id:step03)
### 测试函数功能

1. 使用 Postman 构造 http 请求。
![postman](https://main.qcloudimg.com/raw/0ed1230050967174b133ab7163ae0f6c.png)
2. 请求发送后会收到异步函数响应 “Async run task submitted”，此次函数的 RequstId 会在 http 头部信息中 x-scf-reqid 返回。
![postman](https://main.qcloudimg.com/raw/8b3a343e8850fe98f39ba712fee11617.png)
3. 在云函数控制台【[函数服务](https://console.cloud.tencent.com/scf/list)】页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入函数详情页面。
4. 在函数详情页面中选择【日志查询】页签，可以查看到打印出的推流日志信息。如下图所示
![推流进度](https://main.qcloudimg.com/raw/26c5baad44747f1929c102d16c6f50d9.png)
5. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，查看推流监控。
![监控](https://main.qcloudimg.com/raw/9724de9c1407dde5a188dd4eb87ce8f3.png)
![监控视角](https://main.qcloudimg.com/raw/4382a38640060de7e2883cae5ceadd4d.png)
6. 如果在推流过程中想要停止推流，可以调用 [终止异步函数接口](https://cloud.tencent.com/document/api/583/52500)（**必须开启状态追踪**）：
![监控](https://main.qcloudimg.com/raw/adb37bacb25ce8d0529b7a00386f0c1a.png)
其中 InvokeRequestId 可以从第2步的响应头部信息x-scf-reqid中获取。

   

   
