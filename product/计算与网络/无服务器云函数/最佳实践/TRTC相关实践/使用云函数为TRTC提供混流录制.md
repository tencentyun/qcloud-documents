## 使用场景

### 案例

####  在线教育

在线教育的场景中，可以实现在上课的过程中将老师的音视频和学生的音视频进行合成录制，并且加入上课过程中的其他素材与人工智能分析，在真实还原上课场景的同时增加一些业务功能，增加回放视频观看效果。

#### 社交直播

在直播过程，可以采取混流录制的方法将多流合成、旁路审核，从而降低审核的成本，并且根据国家的要求将混流之后录制文件存储，应对监管要求。

#### 金融监管

在线开户，金融双录等场景中，以全局视角录制全部交易过程，并进行存档保留，满足后续服务或者监管要求。

#### 其他

客户服务、投诉等场景，可以实时启动录制，录制服务过程与投诉内容，便于优化服务质量，排查投诉合理性，提升投诉处理效率。 

### 业务流程

本文为您介绍如何 [使用 API 网关集成云函数](https://cloud.tencent.com/product/serverless-catalog)，将实时音视频 TRTC 房间的主播音视频进行混流录制，录制完毕后上传到COS存储，提供开箱即用、灵活便捷、可编程的直播录制能力。云函数默认提供 512MB 内存来存储录制文件，如果您需要更大的存储空间，可以选择使用 [CFS 挂载能力](https://cloud.tencent.com/document/product/583/46199)。工作流程如下图所示： 

![img](https://main.qcloudimg.com/raw/271f5d30639ce9042dac3f3916c30722.png)

录制规则如下：

- 最多只会录制6路音视频流。
- 当房间低于6个人时，会自动混流后续加入的用户。当房间超过6个人时，只会录制最先进房的6个人。
- IsReserve 为 true 时，在用户退出房间后，该用户流仍然在混流任务中，混流任务中将以最后一帧画面和静音补全流。IsReserve 为 false 时，在用户退出房间后，该用户流将从混流任务中删除，如果后续有新用户进入，则以新用户的流加入混流中。

API 网关调用涉及的参数如下：

| 参数名称  | 类型      | 必选 | 描述                                                         |
| --------- | --------- | ---- | ------------------------------------------------------------ |
| SdkAppId  | Int       | 是   | 应用 ID，用于区分不同 TRTC 应用。                            |
| RoomId    | Int       | 否   | 整型房间号ID，用于在一个 TRTC 应用中唯一标识一个房间。       |
| StrRoomId | String    | 否   | 字符串房间号 ID，RoomId 与 StrRoomId 必须配置一项，如果 RoomId 与 StrRoomId 同时配置，使用 RoomId。 |
| UserId    | String    | 是   | 录制用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。        |
| UserSig   | String    | 是   | 录制用户签名，用于对一个用户进行登录鉴权认证。               |
| CosConfig | cosConfig | 是   | COS 存储配置。用于存储录制文件。                              |
| Callback  | String    | 否   | 录制结束后的回调地址，并使用 POST 方式进行回调。             |
| Mode      | String    | 否   | <li>10：混流音频，默认模式。输出 MP3 格式。<br><li>11：混流视频。输出 MP4 格式。<br><li>12：混流音视频，输出 MP4 格式。 |
| IsReserve | Boolean   | 否   | <li>false，主播退出房间，自动删除混流中的流。<br><li>true，主播退出房间，混流任务中将以最后一帧画面和静音补全流。默认值为 true。 |

CosConfig 涉及的参数如下：

| 参数名称  | 类型   | 必选 | 描述                                                         |
| --------- | ------ | ---- | ------------------------------------------------------------ |
| SecretId  | String | 否   | 腾讯云账号的 SecretId。详情请参见 [访问管理](https://cloud.tencent.com/document/product/598/40488)。 |
| SecretKey | String | 否   | 腾讯云账号的 SecretKey。详情请参见 [访问管理](https://cloud.tencent.com/document/product/598/40488)。 |
| Region    | String | 是   | COS 所在区。例如 `ap-guangzhou`。                                    |
| Bucket    | String | 是   | 桶名称。例如 `susu-123456789`。                                   |
| Path      | String | 是   | 桶内路径。例如 `/test`，根目录为 `/`。                             |

>? 
>-  UserId 为指定用户 ID， 多次请求 API 网关不保证幂等。 
>- CosConfig 中如果不配置 SecretId 与 SecretKey，函数访问 COS 时将使用运行角色 SCF_ExecuteRole 权限去执行。

停止录制的触发条件：

- TRTC 房间被销毁。当 TRTC 房间超过300s没有主播，房间会自动销毁。
- 主动调用移除用户接口，将录制观众踢出房间。
- 使用 RoomId 的用户停止录制，需要调用 [移除用户](https://cloud.tencent.com/document/api/647/40496) 接口。
- 使用 StrRoomId 的用户停止录制时，需要调用 [移除用户（字符串房间号）](https://cloud.tencent.com/document/product/647/50426)接口。

停止录制后，函数返回数据格式如下：

| 参数名称  | 类型   | 必选 | 描述          |
| :-------- | :----- | :--- | :------------ |
| SdkAppId  | String | 是   | 应用 ID。       |
| RoomId    | String | 是   | 整型房间 ID。    |
| UserId    | String | 是   | 录制用户 ID。   |
| StrRoomId | String | 是   | 字符串房间 ID。  |
| Files     | Array  | 是   | [{},{},{},{}] |

> ? 如果配置了 Callback，停止结束后，云函数将以 POST 方式将返回数据传递给回调地址。

Files 数组中每一项为 JSON Object，如下：

| 参数名称   | 类型   | 必选 | 描述                                                  |
| :--------- | :----- | :--- | :---------------------------------------------------- |
| UserId     | String | 是   | 被录制的用户 ID。                                        |
| RecordFile | String | 是   | 录制文件最后上传到 COS 的 URL。                            |
| Status     | Int    | 是   | <li>0：失败。<br><li>1：成功。                                        |
| Message    | String | 是   | 录制任务的执行结果。例如，录制失败、转码失败、写入 COS 失败等。 |

## 操作步骤

### 创建云函数[](id:step01)

1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择**广州**地域，并单击**新建**进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/41ef23af4980d5cbabb3a4ebbc5a6844.png)
   - **创建方式**：选择**模板创建**。
   - **模糊搜索**：输入“TRTC”进行搜索，选择**混流音视频录制**。
     单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
3. 单击**下一步**，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/2a53656f693218b1365b744cb888b22e.png)
 - **函数名称**：默认填充。
 - **异步执行**：勾选以开启。开启后，函数将以异步执行模式响应事件，事件调用无需阻塞等待处理结果，事件将在被调用后进入异步执行状态。
 - **状态追踪**：勾选以开启。开启后，针对异步执行的事件，将开始记录响应事件的实时状态，并提供事件的统计、查询及终止服务，产生的事件状态数据将为您保留3天。
 - **执行超时时间**：可根据需要自行修改。
 - **运行角色**：默认使用 **SCF_ExecuteRole** 作为运行角色，并授予 **QcloudCOSFullAccess**、**QcloudCFSFullAccess** 访问权限。
4. 配置 API 网关触发器，默认新建 API 服务，不开启集成响应。您也可以选择自定义创建，自定义创建时确保集成响应关闭。如下图所示：
![img](https://main.qcloudimg.com/raw/3a198dac7c94d6712da1f250ef6b074c.png)
5. 单击**完成**即可完成函数创建和 API 网关触发器创建。
6. 如需使用 [CFS 挂载能力](https://cloud.tencent.com/document/product/583/46199)，由于 CFS 只能私有网络访问，因此必须将云函数的 VPC 配置在与 CFS 在同一个私有网络下。如下图所示：
![](https://main.qcloudimg.com/raw/75ad7754e5b2ecb02186118d96c94ffc.png)
> ?启用 CFS，需要将环境变量 CFS_PATH 设置为本地目录，例如 `/mnt/audio/`。



### 创建 TRTC 应用[](id:step02)

1. 登录实时音视频控制台，选择左侧导航栏中的**开发辅助** >  **[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 填写 Demo 名称，单击**创建**完成应用创建。您可以根据自己的客户端选择模板试运行，例如 [跑通Demo(桌面浏览器)](https://cloud.tencent.com/document/product/647/32398)。
    ![](https://main.qcloudimg.com/raw/f5126148ae72c78d761a0be0c94710d3.jpg)



### 测试函数功能[](id:step03)

1. 参考 [跑通Demo(桌面浏览器)](https://cloud.tencent.com/document/product/647/32398)，用户user_00001与user_00002进入一个 TRTC 房间。
2. 使用 Postman 构造 HTTP 请求。其中 roomId 为已创建 TRTC 应用的房间号，userId 为随机另一个用户 ID（必须唯一）。如下图所示：
```
{
      "SdkAppId": 1400000000, 
      "RoomId": 43474, 
      "UserId": "user_55952145", 
      "Mode":"12",
      "UserSig": "eJwtzNEKgkAUBNB-2efQ3e3eUqG3tMCKJJEIIxxxxxxxxxxxxxxxhvmweLWzGlUxj0mLs1GXKVf3mgrq*GFUdUR0UQrAYWDyW6Y15cwTwDm4UkxF36iXpkq1joiSc9xxxxxxxxxxxxx-S*CZeOk9sHfnEhCwlUW*fE4oWusw3dULlJ7HoSJ2e6d9fM8Y98fxUAzWA__",
      "CosConfig": {
        "Region": "ap-shanghai",
        "Bucket": "test-123456789",
        "Path": "/trtc"
    	},
      "IsReserve":false,
      "Callback":"https:xxxxxxxx.com/post/xxx"    	
}
```
如下图所示：    
![](https://main.qcloudimg.com/raw/16eb02ddacdfd704364fad85a2edf7e0.png)
3. 请求发送后会收到异步函数响应 “Async run task submitted”，此函数的 RequestId 会通过 HTTP 头部信息中的 x-scf-reqid 返回。如下图所示：
![](https://main.qcloudimg.com/raw/2659951b64f7bd81fe29bdd700fa6590.png)
4. 在云函数控制台 **[函数服务](https://console.cloud.tencent.com/scf/list)**页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入“函数详情”页面。
5. 在“函数详情”页面中选择**日志查询**页签，可以查看到打印出的录制日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/4cd729825588e0c245f884fc81ecc43c.png)
6. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，在“监控仪表盘”页面单击房间 ID，查看所有在房间中的用户，其中一个观众即为录制观众。如下图所示：
![](https://main.qcloudimg.com/raw/6b1535b24bb97c8eb9517ccd868d467e.png)
7. 如需在录制过程中停止录制，可以调用 [移除用户](https://cloud.tencent.com/document/api/647/40496) 或者 [移除用户（字符串房间号）](https://cloud.tencent.com/document/product/647/50426) 将用户提出房间。



