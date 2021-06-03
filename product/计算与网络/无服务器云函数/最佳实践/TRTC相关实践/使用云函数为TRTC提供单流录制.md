## 使用场景

### 案例

#### 在线教育

 在一对一或一对多的小班课中，可以针对不同学生多维度进行录制：

  1、对于单一学生，可以录制学生的单独数据流合成相关数据，实现记录每个学生的精彩瞬间并推送给家长。

  2、对房间内数据进行定向录制，并生成回放，学生可以观看回放重复进行学习。

  3、 为了方便用户反复观看视频、重复学习，录制的过程可以去除冗余数据。

####  客服中心
  1、智能客服场景支持单独录制用户的数据流，和识别相关接口进行合成后，可实现办卡及智能开户过程的信息核实。

  2、支持单独录制客服和用户的声音，自动识别关键字评估服务质量，对智能客服进行迭代训练。

  3、可以将服务过程的数据进行保存与归档。


#### 社交
  1、只录制房间需要录制的视频流，用来做数据的保存，节省存储和混流的成本。

  2、录制房间指定的数据，调用审核接口进行审核，不同的用户设定不同的审核标准。

  3、可以将精彩的直播片段，定向生成片段文件。

### 业务流程

本文为您介绍如何 [使用 API 网关集成云函数](https://cloud.tencent.com/product/serverless-catalog)，将实时音视频 TRTC 房间的主播音视频进行单流录制，录制完毕后上传到COS存储，提供开箱即用、灵活便捷、可编程的直播录制能力。云函数默认提供 512MB 内存来存储录制文件，如果您需要更大的存储空间，可以选择使用 [CFS 挂载能力](https://cloud.tencent.com/document/product/583/46199)。工作流程如下图所示： 

![img](https://main.qcloudimg.com/raw/346f2a424db2d279b0a316077a04d4d9.png)

API 网关调用涉及的参数如下：

| 参数名称  | 类型      | 必选 | 描述                                                         |
| --------- | --------- | ---- | ------------------------------------------------------------ |
| SdkAppId  | Int       | 是   | 应用 ID，用于区分不同 TRTC 应用。                            |
| RoomId    | Int       | 否   | 整型房间号ID，用于在一个 TRTC 应用中唯一标识一个房间。       |
| StrRoomId | String    | 否   | 字符串房间号ID，RoomId与StrRoomId必须配置一项，如果RoomId与StrRoomId同时配置，使用RoomId。 |
| UserId    | String    | 是   | 录制用户 ID，用于在一个 TRTC 应用中唯一标识一个用户。        |
| UserSig   | String    | 是   | 录制用户签名，用于对一个用户进行登录鉴权认证。               |
| CosConfig | cosConfig | 是   | cos存储配置。用于存储录制文件。                              |
| Callback  | String    | 否   | 录制结束后后的回调地址，并使用post方式进行回调。             |
| Mode      | String    | 否   | 00 单流音频，默认模式。输出MP3格式<br />01 单流视频。输出MP4格式<br />02 单流音视频，输出MP4格式 |

CosConfig涉及的参数如下：

| 参数名称  | 类型   | 必选 | 描述                                                         |
| --------- | ------ | ---- | ------------------------------------------------------------ |
| SecretId  | String | 否   | 腾讯云账号的SecretId。参考[访问管理](https://cloud.tencent.com/document/product/598/40488) |
| SecretKey | String | 否   | 腾讯云账号的SecretKey。参考[访问管理](https://cloud.tencent.com/document/product/598/40488) |
| Region    | String | 是   | COS所在区。如ap-guangzhou                                    |
| Bucket    | String | 是   | 桶名称。如：susu-123456789                                   |
| Path      | String | 是   | 桶内路径。如：/test，根目录为/。                             |

>? 
>
>-  UserId 为指定用户 ID， 多次请求 API 网关不保证幂等。 
>- CosConfig 中如果不配置 SecretId 与 SecretKey，函数访问 COS 时将使用运行角色 SCF_ExecuteRole权限去执行。

停止录制的触发条件：

1. trtc房间被销毁。注意：trtc房间超过300s没有主播，房间会自动销毁。
2. 主动调用移除用户接口，将录制观众踢出房间。
3. 使用RoomId的用户停止录制，需要调用[移除用户](https://cloud.tencent.com/document/api/647/40496)接口
4. 使用StrRoomId的用户停止录制时，需要调用[移除用户（字符串房间号）](https://cloud.tencent.com/document/product/647/50426)接口。

停止录制后，函数返回数据格式如下：

| 参数名称  | 类型   | 必选 | 描述          |
| :-------- | :----- | :--- | :------------ |
| SdkAppId  | String | 是   | 应用id        |
| RoomId    | String | 是   | 整型房间id    |
| UserId    | String | 是   | 录制用户id    |
| StrRoomId | String | 是   | 字符串房间id  |
| Files     | Array  | 是   | [{},{},{},{}] |

> ? 如果配置了Callback，停止结束后，云函数会以post方式将返回数据传递给回调地址。

Files数组中每一项为json object，如下：

| 参数名称   | 类型   | 必选 | 描述                                                  |
| :--------- | :----- | :--- | :---------------------------------------------------- |
| UserId     | String | 是   | 被录制的用户Id                                        |
| RecordFile | String | 是   | 录制文件最后上传到cos的url                            |
| Status     | Int    | 是   | 0：失败1：成功                                        |
| Message    | String | 是   | 录制任务的执行结果。如：录制失败，转码失败，写cos失败 |

## 操作步骤

### 创建云函数[](id:step01)

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**广州**地域，并单击【新建】进入新建函数页面，根据页面相关信息提示进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/060d9a8d1e4a0b3f54efa3d1092a4f81.png)
   - **创建方式**：选择【模板创建】。
   - **模糊搜索**：输入“TRTC”进行搜索，选择【单流音视频录制】。
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
   
    ```
    {
    	"SdkAppId": 1400000000,
    	"RoomId": 43474,
    	"UserId": "user_55952145",
    	"Mode":"02",
    	"UserSig": "eJwtzNEKgkAUBNB-2efQ3e3eUqG3tMCKJJEIIxxxxxxxxxxxxxxxhvmweLWzGlUxj0mLs1GXKVf3mgrq*GFUdUR0UQrAYWDyW6Y15cwTwDm4UkxF36iXpkq1joiSc9xxxxxxxxxxxxx-S*CZeOk9sHfnEhCwlUW*fE4oWusw3dULlJ7HoSJ2e6d9fM8Y98fxUAzWA__",
    	"CosConfig": {
    		"region": "ap-shanghai",
    		"bucket": "test-123456789",
    		"path": "/trtc"
    	}
    }
    ```
    
    ![](https://main.qcloudimg.com/raw/9739ca831f19945a666c27142435ca2a.png)
    
3. 请求发送后会收到异步函数响应 “Async run task submitted”，此次函数的 RequstId 会通过 HTTP 头部信息中的 x-scf-reqid 返回。如下图所示：

    ![](https://main.qcloudimg.com/raw/2659951b64f7bd81fe29bdd700fa6590.png)

4. 在云函数控制台【[函数服务](https://console.cloud.tencent.com/scf/list)】页面中，单击上述 [创建云函数](#step01) 步骤中创建的云函数名称，进入“函数详情”页面。

5. 在“函数详情”页面中选择【日志查询】页签，可以查看到打印出的录制日志信息。如下图所示：

    ![](https://main.qcloudimg.com/raw/5dd0744da897f6fb117c10e8e0ed9b7a.jpeg)

6. 切换至 [实时音视频控制台](https://console.cloud.tencent.com/trtc/monitor)，在“监控仪表盘”页面单击房间 ID，查看所有在房间中的用户，其中一个观众就是我们的录制观众。如下图所示：

    ![](https://main.qcloudimg.com/raw/6b1535b24bb97c8eb9517ccd868d467e.png)

7. 如需在录制过程中停止录制，可以调用 [移除用户](https://cloud.tencent.com/document/api/647/40496)或者（[移除用户（字符串房间号）](https://cloud.tencent.com/document/product/647/50426)）将用户提出房间。



