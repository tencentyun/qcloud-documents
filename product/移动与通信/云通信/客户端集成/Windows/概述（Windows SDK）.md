## 1 ImSDK集成 

本节主要介绍如何创建一个应用，并集成ImSDK。 

### 1.1 下载ImSDK 

从官网下载ImSDK开发包，主要包括include文件夹和lib文件夹。各部分说明如下：
- libs\c_includes C接口头文件
- libs\includes C++接口头文件
- libs 动态C运行时库
- static-rt-libs 静态C运行时库

推荐使用C接口头文件进行接入

### 1.2 集成ImSDK 

建立VC工程或其他IDE工程 

#### 1.2.1 头文件 

引入头文件 `tim_*.h` 

#### 1.2.2 引用库 

库文件 libtim.dll libtim.lib 
注意：原WinSDK 使用编译选项 `/MD &/MDD`，以动态库的形式引用运行时库。调用时需保持一致。另外，运行时依赖VS2010 SP1相关CRT。 

注：从SDK1.3版本后 开始提供依赖静态运行时库的dll。用户可选择一套符合自己生产环境的dll来使用。 打包文件中文件夹名为`static_rt`的就是以`/MT & /MTD`选项生成的。

#### 1.2.3 关于回调等的注意事项 

sdk使用异步回调的方式，在大部分接口中返回调用结果。 
例如：

```
//sdk定义
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
在用户登陆成功以后，sdk调用callback中的函数指针返回结果。其中，如果登陆成功，sdk调用callback中注册的OnSuccess方法，并且将注册的用户数据void* data在接口中传回用户。反之亦然。 

**注意：**WinSDK库使用回调线程调用回调函数。如果阻塞回调线程将影响SDK库功能：例如无法收发包等等。所以建议用户以可靠的方式传递回调数据到主线程或用户自有线程处理，避免阻塞用户回调。
 
#### 1.2.4 关于句柄 

SDK库使用句柄封装资源。用户创建SDK库接口定义的资源前，调用相应的`Create*Handle`接口创建句柄，在句柄使用完毕后，调用相应的`Destroy*Handle`接口销毁接口，避免资源泄露。当句柄是在回调中传递给用户的时候，用户可选择使用`Clone*Handle`接口复制句柄，在句柄使用完毕以后，仍然销毁资源。当然也可以直接操作Handle，需要注意避免阻塞回调线程。
 
### 1.3 功能开发 

根据后续章节的开发指引进行功能的开发。其中函数调用顺序可参见（2.2 调用顺序介绍）。

### 1.4 支持版本 

ImSDK支持winxp及win7系统。 

## 2 ImSDK 基本概念 

会话：ImSDK中会话(Conversation)分为两种，一种是C2C会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成；另一种是群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。
如下图所示，一个会话表示与一个好友的对话： 
![](//mccdn.qcloud.com/static/img/8c96e0282d1f32b7bcf197043eddef6c/image.jpg)
**消息：**ImSDK中消息(Message)表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等；一条消息由若干Elem组合而成，每种Elem可以是文本、图片、表情等等，消息支持多种Elem组合发送。 
![](//mccdn.qcloud.com/static/img/34bf753940ed435ec8f916a419398b75/image.png)
群组Id：群组Id唯一标识一个群，由后台生成，创建群组时返回。 

### 2.1 ImSDK接口简介 

ImSDK 接口主要分为通讯管理器，会话、消息，群管理，具体参见下表： 

头文件 | 介绍 | 功能
---|---|---
tim_c.h | 管理，负责基本的SDK操作 | 初始化登录、注销、创建会话等
tim_conv_c.h | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等
tim_msg_c.h | 消息 | 包括文本、图片等不同类型消息
tim_group_c.h | 群管理器 | 负责创建群，增删成员，以及修改群资料等
tim_friend_c.h | 资料关系链管理 | 负责获取、修改好友资料和关系链信息

### 2.2 调用顺序介绍 

ImSDK调用API需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

步骤 | 对应函数 | 说明
---|---|---
初始化 | TIMSetMessageCallBack | 设置消息回调
初始化 | TIMSetConnCallBack | 设置链接通知回调
初始化 | TIMInit | 初始化SDK
登录 | TIMLogin | 登录
消息收发 | TIMGetConversation | 获取会话
消息收发 | SendMsg | 发送消息
注销 |TIMLogout | 注销（用户可选）
初始化 | TIMUnInit | 反初始化SDK
	
调用流程图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20150928023342_70933.png)