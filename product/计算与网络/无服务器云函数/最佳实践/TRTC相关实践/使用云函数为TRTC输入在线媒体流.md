## 使用场景 

### 案例

#### AI 互动课堂

通过录播真人教学视频结合 AI 技术进行线上直播互动教学。

上课前，根据教师的课程设置，将知识点讲解、互动提问、问题反馈和解答等信息录制成视频片段，上传到视频库。课堂中，通过云函数将已有的录播视频推送到 TRTC 房间进行直播。学生通过语音、触屏实现互动式学习。服务端通过 AI 技术，智能识别学生的实时语音和作答，并根据学生的表现，无缝切换教学片段，实时给予不同的反馈，从而提供个性化的教学体验。

#### “一起看”房间服务

游戏直播、秀场、体育赛事等直播类内容，可以通过云函数将 RTMP 直播流推送到 TRTC 房间，实时交流，带动热点。电影、音乐等点播类节目，可以通过云函数将媒体文件转换为在线媒体流输入至TRTC房间，增值服务，打造社区圈层。云函数一键触发、免运维、弹性伸缩等特性可以快速支撑实时互动娱乐社交应用的构建。云函数的可编程性，可以快速整合其他云服务及三方服务，扩展业务边界，高效创新玩法。



### 业务流程

本文为您介绍如何 [使用 API 网关集成云函数](https://cloud.tencent.com/product/serverless-catalog)，将已有的录播视频或者 RTMP 直播流推送到实时音视频 TRTC 房间进行直播，提供开箱即用、灵活便捷、可编程的在线媒体流输入能力。如您需开启推流直播的实时记录，可以选择使用 Redis，API 网关会将进度实时写入 Redis。工作流程如下图所示：

![img](https://main.qcloudimg.com/raw/a03fcfbd42bd2e66345b7882ce1bf522.png)

API 网关调用涉及的参数如下：

| 参数名称      | 类型    | 必选 | 描述                                                         |
| ------------- | ------- | ---- | ------------------------------------------------------------ |
| VideoSrc      | String  | 是   | 被推流的视频源，例如 `https://test-123456789.cos.ap-shanghai.myqcloud.com/video/1.mp4`。 |
| SdkAppId      | Int     | 是   | 应用 ID，用于区分不同 TRTC 应用。                            |
| RoomId        | Int     | 否   | 整型房间号 ID，用于在一个 TRTC 应用中唯一标识一个房间。       |
| StrRoomId     | String  | 否   | 字符串房间号 ID，RoomId 与 StrRoomId 必须配置一项，如果 RoomId 与 StrRoomId 同时配置，则使用 RoomId。 |
| Mode          | String  | 否   | <li>vod：点播模式，即推流为某个录制好的文件，默认模式。<br><li>live：直播模式，即推流为 rtmp 直播源。 |
| UserId        | String  | 是   | 推流用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。        |
| UserSig       | String  | 是   | 推流用户签名，用于对一个用户进行登录鉴权认证。               |
| Redis         | Boolean | 否   | 是否使用 Redis，默认为 false。                               |
| RedisHost     | String  | 否   | Redis 为 true 时，redis 的 host 地址。                        |
| RedisPort     | Integer | 否   | Redis 为 true 时，redis 的访问端口号。                       |
| RedisPassword | String  | 否   | Redis 为 true 时，redis 的访问密码。                         |

>? 
>- 如果 Redis 值为 false，从 VideoSrc 视频源拉流进行直播推流，直播流将从最新开始。
>- 如果 Redis 值为 true，对于同一个 VideoSrc 视频源，API 网关将先在 Redis 中查询是否有上一次直播流推流记录：
>  - 若存在记录，则恢复上一次推流。
>  - 若无记录，则重新开始推流。直播推流进度通过回调实时写入 Redis。



## 操作步骤

### 创建云函数[](id:step01)

1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择**北京**地域，并单击**新建**进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/4e1e5468b371f8478992f6fa8ca07746.jpg)
   - **创建方式**：选择**模板创建**。
   - **模糊搜索**：输入“TRTC直播推流”，并进行搜索。
     单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
3. 单击**下一步**，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/71b0c84a634c8aab0ad86b4cdd21c47f.png)
 - **函数名称**：默认填充。
 - **异步执行**：勾选以开启。开启后，函数将以异步执行模式响应事件，事件调用无需阻塞等待处理结果，事件将在被调用后进入异步执行状态。
 - **状态追踪**：勾选以开启。开启后，针对异步执行的事件，将开始记录响应事件的实时状态，并提供事件的统计、查询及终止服务，产生的事件状态数据将为您保留3天。
 - **执行超时时间**：可根据需要自行修改。
4. 配置 API 网关触发器，默认新建 API 服务，不开启集成响应。您也可以选择自定义创建，自定义创建时确保集成响应关闭。如下图所示：
![img](https://main.qcloudimg.com/raw/3a198dac7c94d6712da1f250ef6b074c.png)
5. 单击**完成**即可完成函数创建和 API 网关触发器创建。
6. 如需使用 Redis 实时记录推流进度，由于 Redis 只能私有网络访问，因此必须将云函数的 VPC 配置在与 Redis 在同一个私有网络下。如下图所示：
![](https://main.qcloudimg.com/raw/1d81c0ff8aa4eff4ba9f2f6d4e45717f.png)

    



### 创建 TRTC 应用[](id:step02)

1. 登录实时音视频控制台，选择左侧导航栏中的**开发辅助** >  **[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 填写 Demo 名称，单击**创建**完成应用创建。您可以根据自己的客户端选择模板试运行。
![](https://main.qcloudimg.com/raw/f5126148ae72c78d761a0be0c94710d3.jpg)



### 测试函数功能[](id:step03)

1. 使用 Postman 构造 HTTP 请求。示例如下：
```
{
        "SdkAppId": 1400000000, 
        "StrRoomId": "98915abc", 
        "UserId": "user_55952144", 
        "Mode": "vod", 
        "UserSig": "eJwtzN0KgkAQBeB32dtCZqcd-6CbMMRYIrGiu6jcZAhL1NogevdMvxxxxxxxxxxxxxxxxxAIdENM*c27uLV*552dj6iNRQCiVGgdNfjtVFecilApABSg9OTTmXXFtOiciBIBBWy7xxxxxxxxRHbbjo-kFrN0UvOfuRH1tMyiDeLGcPu7ocxxxxxxxxxxx5uL7A0DEMb8_", 
        "Redis": false, 
        "VideoSrc": "https://test-123456789.cos.ap-shanghai.myqcloud.com/video/1.mp4"
}
```
 如下图所示：
 ![](https://main.qcloudimg.com/raw/22f1e55b18e166d0b4ece52284847e09.png)
2. 请求发送后会收到异步函数响应 “Async run task submitted”，此次函数的 RequstId 会通过 HTTP 头部信息中的 x-scf-reqid 返回。如下图所示：
 ![](https://main.qcloudimg.com/raw/2659951b64f7bd81fe29bdd700fa6590.png)
3. 在云函数控制台 **[函数服务](https://console.cloud.tencent.com/scf/list)**页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入“函数详情”页面。
4. 在“函数详情”页面中选择**日志查询**页签，可以查看到打印出的推流日志信息。如下图所示：
    ![](https://main.qcloudimg.com/raw/5dd0744da897f6fb117c10e8e0ed9b7a.jpeg)
5. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，在“监控仪表盘”页面单击房间 ID，查看推流监控详情信息。如下图所示：
    ![](https://main.qcloudimg.com/raw/b69e2c7f19e22bffbd49e0faf824f4ae.png)
6. 如需在推流过程中停止推流，可以调用 [终止异步函数接口](https://cloud.tencent.com/document/api/583/52500) InvokeRequestId 参数停止推流（**必须开启状态追踪**）。
其中 InvokeRequestId 可从上述步骤2的响应头部信息 x-scf-reqid 中获取。



