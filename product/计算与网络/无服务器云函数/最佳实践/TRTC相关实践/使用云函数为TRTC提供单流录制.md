## 使用场景

### 案例

#### 在线教育

在一对一或一对多的小班课中，可以针对不同学生多维度进行录制：
- 对于单一学生，可以录制学生的单独数据流合成相关数据，实现记录每个学生的精彩瞬间并推送给家长。
- 对房间内数据进行定向录制，并生成回放，学生可以观看回放重复进行学习。
- 为了方便用户反复观看视频、重复学习，录制的过程可以去除冗余数据。

####  客服中心
- 智能客服场景支持单独录制用户的数据流，和识别相关接口进行合成后，可实现办卡及智能开户过程的信息核实。
- 支持单独录制客服和用户的声音，自动识别关键字评估服务质量，对智能客服进行迭代训练。
- 可以将服务过程的数据进行保存与归档。


#### 社交
- 仅录制房间需要录制的视频流，用做数据保存，以节省存储和混流的成本。
- 录制房间指定的数据，调用审核接口进行审核，可为不同的用户设定不同的审核标准。
- 可以将直播片段定向生成片段文件。

### 业务流程

本文为您介绍如何 [使用 API 网关集成云函数](https://cloud.tencent.com/product/serverless-catalog)，将实时音视频 TRTC 房间的主播音频进行单流录制，录制完毕后上传到 COS 存储，提供开箱即用、灵活便捷、可编程的直播录制能力。云函数默认提供512MB内存来存储录制文件，如果您需要更大的存储空间，可以选择使用 [CFS 挂载](https://cloud.tencent.com/document/product/583/46199)。工作流程如下图所示： 

![img](https://main.qcloudimg.com/raw/7320a87207b34e715f576ee56a3feac0.png)


API 网关调用涉及的参数如下：

| 参数名称  | 类型      | 必选 | 描述                                                        |
| --------- | --------- | ---- | ----------------------------------------------------------- |
| SdkAppId  | Int       | 是   | 应用 ID，用于区分不同 TRTC 应用。                           |
| RoomId    | Int       | 是   | 整型房间号 ID，用于在一个 TRTC 应用中唯一标识一个房间。      |
| StrRoomId | String    | 否   | 字符串房间号 ID，如果 RoomId 与 StrRoomId 同时配置，将使用 RoomId。 |
| UserId    | String    | 是   | 用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。           |
| UserSig   | String    | 是   | 用户签名，用于对一个用户进行登录鉴权认证。                  |
| CosConfig | cosConfig | 是   |  COS 存储配置。用于存储录制文件。                             |
| Callback  | String    | 否   | 录制结束后的回调地址。                                    |

CosConfig 涉及的参数如下：

| 参数名称  | 类型   | 必选 | 描述                                                         |
| --------- | ------ | ---- | ------------------------------------------------------------ |
| SecretId  | String | 否   | 腾讯云账号的 SecretId。详情请参见 [访问管理](https://cloud.tencent.com/document/product/598/40488) |
| SecretKey | String | 否   | 腾讯云账号的 SecretKey。详情请参见 [访问管理](https://cloud.tencent.com/document/product/598/40488) |
| Region    | String | 是   | COS 所在区。例如 `ap-guangzhou`。                                    |
| Bucket    | String | 是   | 桶名称。例如 `susu-123456789`。                                 |
| Path      | String | 是   | 桶内路径。例如 `/test`。                         |

>? 
>-  UserId 为指定用户 ID，多次请求 API 网关不保证幂等。 
>-  CosConfig 中如果不配置 SecretId 与 SecretKey，函数访问 COS 时将使用运行角色  SCF_ExecuteRole 权限去执行。

**停止录制的触发条件**：

- TRTC 房间被销毁。当 TRTC 房间超过300s没有主播，房间会自动销毁。
- 主动调用移除用户接口，将录制观众踢出房间。
- 使用 RoomId 的用户停止录制，需要调用 [移除用户](https://cloud.tencent.com/document/api/647/40496) 接口。
- 使用 StrRoomId 的用户停止录制时，需要调用 [移除用户（字符串房间号）](https://cloud.tencent.com/document/product/647/50426) 接口。

## 操作步骤

### 创建云函数[](id:step01)

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**广州**地域，并单击【新建】进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
   ![](https://main.qcloudimg.com/raw/616ce1e10c0fc66095b41690593ea815.png)
   - **创建方式**：选择【模板创建】。
   - **模糊搜索**：输入“TRTC”进行搜索，选择【单流音频录制】。
     单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
3. 单击【下一步】，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/5194a1c98b0194cfdc15b6bfaa8df3fc.png)
 - **函数名称**：默认填充。
 - **异步执行**：勾选以开启。开启后，函数将以异步执行模式响应事件，事件调用无需阻塞等待处理结果，事件将在被调用后进入异步执行状态。
 - **状态追踪**：勾选以开启。开启后，针对异步执行的事件，将开始记录响应事件的实时状态，并提供事件的统计、查询及终止服务，产生的事件状态数据将为您保留3天。
 - **执行超时时间**：可根据需要自行修改。
 - **运行角色**：默认使用 **SCF_ExecuteRole** 作为运行角色，并授予 **QcloudCOSFullAccess**、**QcloudCFSFullAccess** 访问权限。
4. 配置 API 网关触发器，默认新建 API 服务，不开启集成响应。您也可以选择自定义创建，自定义创建时确保集成响应关闭。如下图所示：
   ![img](https://main.qcloudimg.com/raw/3a198dac7c94d6712da1f250ef6b074c.png)
5. 单击【完成】即可完成函数创建和 API 网关触发器创建。
6. 如需使用 [CFS 挂载能力](https://cloud.tencent.com/document/product/583/46199)，由于 CFS 为私有网络访问，因此必须将云函数的 VPC 配置在与 CFS 在同一个私有网络下。
 >?启用 CFS，需要将环境变量 CFS_PATH 设置为本地目录，例如 /mnt/audio/。



### 创建 TRTC 应用[](id:step02)

1. 登录实时音视频控制台，选择左侧导航栏中的【开发辅助】>【[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 填写 Demo 名称，单击【创建】完成应用创建。您可以根据自己的客户端选择模板试运行。如下图所示：
  ![](https://main.qcloudimg.com/raw/f5126148ae72c78d761a0be0c94710d3.jpg)




### 测试函数功能[](id:step03)

1. [创建 TRTC 应用](#step02) 并进入应用。
2. 使用 Postman 构造 HTTP 请求。其中 roomId 为已创建 TRTC 应用的房间号，userId 为随机用户 id（必须唯一），如下图所示：
![](https://main.qcloudimg.com/raw/853956afb9d49c4dd8a1eed021b9abe8.png)
3. 请求发送后会收到异步函数响应 “Async run task submitted”，此次函数的 RequstId 会通过 HTTP 头部信息中的 x-scf-reqid 返回。如下图所示：
   ![](https://main.qcloudimg.com/raw/2659951b64f7bd81fe29bdd700fa6590.png)
4. 在云函数控制台【[函数服务](https://console.cloud.tencent.com/scf/list)】页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入“函数详情”页面。
5. 在“函数详情”页面中选择【日志查询】页签，可以查看到打印出的录制日志信息。如下图所示：
   ![](https://main.qcloudimg.com/raw/5dd0744da897f6fb117c10e8e0ed9b7a.jpeg)
6. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，在“监控仪表盘”页面单击房间 ID，查看所有在房间中的用户，其中一个观众即为录制观众。如下图所示：
![](https://main.qcloudimg.com/raw/f165e458a7d68a9259c95051a705930c.png)
7. 如需在录制过程中停止录制，可以通过 [移除用户接口](https://cloud.tencent.com/document/api/647/40496) 或者（[移除用户（字符串房间号）接口](https://cloud.tencent.com/document/product/647/50426)）将用户移出房间。



