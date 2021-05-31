## 使用场景

### 案例

#### 在线教育

  在1v1 1v多的小班课中，针对不同学生的角度进行录制：

  1、单一学生的角度，录制每个学生的单独数据流，进行相关数据的合成，实现每个学生对应的精彩瞬间，推送给家长。

  2、对房间里面的数据进行定向录制，生成回放，错过上课的学生也可以观看回放进行学习。

  3、方便用户反复观看视频，重复学习，录制的过程可以去除一些不必要的数据。

####  客服中心
  1、智能客服场景，可以单独录制客户的数据流，和识别相关接口进行合成。实现只能办卡，智能开户过程的信息核实。

  2、单独录制客服和用户的声音，自动识别关键字，评估服务质量，用于对智能客服的训练，效果的提升迭代。

  3、服务过程的苏剧保存，归档。


#### 社交
  1、只录制房间需要录制的视频流，用来做数据的保存，节省存储和混流的成本

  2、录制房间指定的数据，调用审核接口进行审核，不同的用户设定不同的审核标准。

  3、精彩的直播片段，定向生成，形成片段文件。

### 业务流程

本文为您介绍如何 [使用 API 网关集成云函数](https://cloud.tencent.com/product/serverless-catalog)，将实时音视频 TRTC 房间的主播音频进行单流录制，录制完毕后上传到COS存储，提供开箱即用、灵活便捷、可编程的直播录制能力。云函数默认提供 512MB 内存来存储录制文件，如果您需要更大的存储空间，可以选择使用 [CFS 挂载能力](https://cloud.tencent.com/document/product/583/46199)。工作流程如下图所示： 

![img](https://main.qcloudimg.com/raw/7320a87207b34e715f576ee56a3feac0.png)

API 网关调用涉及的参数如下：

| 参数名称  | 类型      | 必选 | 描述                                              |
| --------- | --------- | ---- | ------------------------------------------------- |
| sdkAppId  | Int       | 是   | 应用 ID，用于区分不同 TRTC 应用。                 |
| roomId    | Int       | 是   | 房间 ID，用于在一个 TRTC 应用中唯一标识一个房间。 |
| userId    | String    | 是   | 用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。 |
| userSig   | String    | 是   | 用户签名，用于对一个用户进行登录鉴权认证。        |
| cosConfig | cosConfig | 是   | cos存储配置。用于存储录制文件。                   |
| callback  | String    | 否   | 录制结束后后的回调地址。                          |

cosConfig涉及的参数如下：

| 参数名称  | 类型   | 必选 | 描述                                                         |
| --------- | ------ | ---- | ------------------------------------------------------------ |
| secretId  | String | 否   | 腾讯云账号的SecretId。参考[访问管理](https://cloud.tencent.com/document/product/598/40488) |
| secretKey | String | 否   | 腾讯云账号的SecretKey。参考[访问管理](https://cloud.tencent.com/document/product/598/40488) |
| region    | String | 是   | COS所在区。如ap-guangzhou                                    |
| bucket    | String | 是   | 桶名称。如：susu-123456789                                   |
| path      | String | 是   | 桶内路径。如：/test                                          |

>? 
>
>-  userId 为指定用户 ID， 多次请求 API 网关不保证幂等。 
>- cosConfig 中如果不配置 secretId 与 secretKey，函数访问 COS 时将使用运行角色 SCF_ExecuteRole权限去执行。

停止录制的触发条件：

1. trtc房间被销毁。注意：trtc房间超过300s没有主播，房间会自动销毁。
2. 主动调用移除用户接口，将录制观众踢出房间。

## 操作步骤

### 创建云函数[](id:step01)

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**广州**地域，并单击【新建】进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/616ce1e10c0fc66095b41690593ea815.png)
   - **创建方式**：选择【模板创建】。
   - **模糊搜索**：输入“TRTC”进行搜索，选择【单流音频录制】。
     单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
3. 单击【下一步】，根据页面相关信息提示进行配置。如下图所示：
![img](https://main.qcloudimg.com/raw/4751dadf884d51dcd69c417f53b098f4.png)
 - **函数名称**：默认填充。
 - **异步执行**：勾选以开启。开启后，函数将以异步执行模式响应事件，事件调用无需阻塞等待处理结果，事件将在被调用后进入异步执行状态。
 - **状态追踪**：勾选以开启。开启后，针对异步执行的事件，将开始记录响应事件的实时状态，并提供事件的统计、查询及终止服务，产生的事件状态数据将为您保留3天。
 - **执行超时时间**：可根据需要自行修改。
 - **运行角色**：默认使用 **SCF_ExecuteRole** 作为运行角色，并授予**QcloudCOSFullAccess**、**QcloudCFSFullAccess**访问权限。
4. 配置 API 网关触发器，默认新建 API 服务，不开启集成响应。您也可以选择自定义创建，自定义创建时确保集成响应关闭。如下图所示：
![img](https://main.qcloudimg.com/raw/3a198dac7c94d6712da1f250ef6b074c.png)
5. 单击【完成】即可完成函数创建和 API 网关触发器创建。
6. 如需使用 [CFS挂载能力](https://cloud.tencent.com/document/product/583/46199)，由于 CFS只能私有网络访问，因此必须将云函数的 VPC 配置在与 CFS 在同一个私有网络下。如下图所示：
![](https://main.qcloudimg.com/raw/75ad7754e5b2ecb02186118d96c94ffc.png)

   > ? 
   >
   > 启用CFS，需要将环境变量CFS_PATH设置为本地目录，如：/mnt/audio/。



### 创建 TRTC 应用[](id:step02)

1. 登录实时音视频控制台，选择左侧导航栏中的【开发辅助】>【[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)】。

2. 填写 Demo 名称，单击【创建】完成应用创建。您可以根据自己的客户端选择模板试运行，例如：[跑通Demo(桌面浏览器)](https://cloud.tencent.com/document/product/647/32398)

  ![](https://main.qcloudimg.com/raw/f5126148ae72c78d761a0be0c94710d3.jpg)




### 测试函数功能[](id:step03)

1. 参考[跑通Demo(桌面浏览器)](https://cloud.tencent.com/document/product/647/32398)，主播user_00001进入一个trtc房间，
2. 使用 Postman 构造 HTTP 请求。其中roomId 为步骤1中的trtc房间号，userId为随机另一个用户id（必须唯一），如下图所示：
    ![](https://main.qcloudimg.com/raw/40893b9066bec3040078e61b3459fc0f.png)
3. 请求发送后会收到异步函数响应 “Async run task submitted”，此次函数的 RequstId 会通过 HTTP 头部信息中的 x-scf-reqid 返回。如下图所示：
    ![](https://main.qcloudimg.com/raw/2659951b64f7bd81fe29bdd700fa6590.png)
4. 在云函数控制台【[函数服务](https://console.cloud.tencent.com/scf/list)】页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入“函数详情”页面。
5. 在“函数详情”页面中选择【日志查询】页签，可以查看到打印出的录制日志信息。如下图所示：
    ![](https://main.qcloudimg.com/raw/5dd0744da897f6fb117c10e8e0ed9b7a.jpeg)
6. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，在“监控仪表盘”页面单击房间 ID，查看所有在房间中的用户，其中一个观众就是我们的录制观众。如下图所示：
    ![](https://main.qcloudimg.com/raw/6b1535b24bb97c8eb9517ccd868d467e.png)
7. 如需在录制过程中停止录制，可以调用 [移除用户接口](https://cloud.tencent.com/document/api/647/40496)将用户提出房间。



