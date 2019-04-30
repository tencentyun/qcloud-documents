## ImSDK 集成 

本节主要介绍如何创建一个应用，并集成 ImSDK。 

### 下载 ImSDK 

从 [官网](https://cloud.tencent.com/product/im/developer) 下载 ImSDK 开发包，主要包括 `include` 文件夹和 `lib` 文件夹，推荐使用 C 接口头文件进行接入。各部分说明如下：

- libs\c_includes C 接口头文件
- libs\includes C++ 接口头文件
- libs 动态 C 运行时库
- static-rt-libs 静态 C 运行时库

### 集成 ImSDK 

建立 VC 工程或其他 IDE 工程。

#### 头文件 

引入头文件 `tim_*.h`。

#### 引用库 

库文件 `libtim.dll libtim.lib`，从 SDK 1.3 版本后开始提供依赖静态运行时库的 dll。用户可选择一套符合自己生产环境的 dll 来使用。打包文件中文件夹名为 `static_rt` 的就是以 `/MT & /MTD` 选项生成的。

> **注意：**
> 原 WinSDK 使用编译选项 `/MD &/MDD`，以动态库的形式引用运行时库。调用时需保持一致。另外，运行时依赖 VS2010 SP1 相关 CRT。

#### 关于回调等的注意事项 

SDK 使用异步回调的方式，在大部分接口中返回调用结果。在用户登录成功以后，SDK 调用 `callback` 中的函数指针返回结果。其中，如果登录成功，SDK 调用 `callback` 中注册的 `OnSuccess` 方法，并且将注册的用户数据 `void* data` 在接口中传回用户。反之亦然。 

**示例：**

```
//SDK 定义
typedef void (*CBOnSuccess) (void* data);
typedef void (*CBOnError) (int code, const char* desc, void* data);
typedef struct _TIMCallBack_c
{
   CBOnSuccess OnSuccess;
   CBOnError	OnError;
   void*		data;
}TIMCommCB;
TIMCommCB callback;
callback.OnSuccess = CBCommOnSuccessImp;
callback.OnError = CBCommOnErrorImp;
TIMLogin(sdk_app_id, &user, user_sig, &callback);
SLEEP(1);
```

> **注意：**
> WinSDK 库使用回调线程调用回调函数。如果阻塞回调线程将影响 SDK 库功能：例如无法收发包等等。所以建议用户以可靠的方式传递回调数据到主线程或用户自有线程处理，避免阻塞用户回调。
 
#### 关于句柄 

SDK 库使用句柄封装资源。用户创建 SDK 库接口定义的资源前，调用相应的 `Create*Handle` 接口创建句柄，在句柄使用完毕后，调用相应的 `Destroy*Handle` 接口销毁接口，避免资源泄露。当句柄是在回调中传递给用户的时候，用户可选择使用 `Clone*Handle` 接口复制句柄，在句柄使用完毕以后，仍然销毁资源。当然也可以直接操作 Handle，需要注意避免阻塞回调线程。
 
### 功能开发 

根据后续章节的开发指引进行功能的开发。其中函数调用顺序可参见 [调用顺序介绍](#.E8.B0.83.E7.94.A8.E9.A1.BA.E5.BA.8F.E4.BB.8B.E7.BB.8D)。

### 支持版本 

ImSDK 支持 Windows XP 及 Windows 7 系统。 

## ImSDK 基本概念 

**会话：**ImSDK 中会话（Conversation）分为两种，一种是 C2C 会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成；另一种是群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。

如下图所示，一个会话表示与一个好友的对话： 

![](//mccdn.qcloud.com/static/img/8c96e0282d1f32b7bcf197043eddef6c/image.jpg)

**消息：**ImSDK 中消息（Message）表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等；一条消息由若干 `Elem` 组合而成，每种 `Elem` 可以是文本、图片、表情等等，消息支持多种 `Elem` 组合发送。 

![](//mccdn.qcloud.com/static/img/34bf753940ed435ec8f916a419398b75/image.png)

**群组 ID**：群组 ID 唯一标识一个群，由后台生成，创建群组时返回。 

### ImSDK 接口简介 

ImSDK 接口主要分为通讯管理器，会话、消息，群管理，具体参见下表： 

头文件 | 介绍 | 功能
---|---|---
tim_c.h | 管理，负责基本的 SDK 操作 | 初始化登录、注销、创建会话等
tim_conv_c.h | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等
tim_msg_c.h | 消息 | 包括文本、图片等不同类型消息
tim_group_c.h | 群管理器 | 负责创建群，增删成员，以及修改群资料等
tim_friend_c.h | 资料关系链管理 | 负责获取、修改好友资料和关系链信息

### 调用顺序介绍 

ImSDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

步骤 | 对应函数 | 说明
---|---|---
初始化 | TIMSetMessageCallBack | 设置消息回调
初始化 | TIMSetConnCallBack | 设置链接通知回调
初始化 | TIMInit | 初始化 SDK
登录 | TIMLogin | 登录
消息收发 | TIMGetConversation | 获取会话
消息收发 | SendMsg | 发送消息
注销 |TIMLogout | 注销（用户可选）
初始化 | TIMUnInit | 反初始化 SDK
	
**调用流程图：**

![](//avc.qcloud.com/wiki2.0/im/imgs/20150928023342_70933.png)