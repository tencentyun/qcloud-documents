本文将指导您操作客户端将向腾讯云完成登录过程。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_login.zip)

## 前提条件
本课程要求用户在[ 实时音视频官网 ](https://cloud.tencent.com/product/trtc)完成服务开通及应用创建。

## 相关概念
 - [实时音视频应用](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
 - [应用标识( sdkAppId )](https://cloud.tencent.com/document/product/647/16792#.E5.BA.94.E7.94.A8.E6.A0.87.E8.AF.86.EF.BC.88-sdkappid-.EF.BC.89)
 - [帐号类型( accountType )](https://cloud.tencent.com/document/product/647/16792#.E5.B8.90.E5.8F.B7.E7.B1.BB.E5.9E.8B.EF.BC.88-accounttype-.EF.BC.89)
 - [用户标识( userId )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E6.A0.87.E8.AF.86.EF.BC.88-userId-.EF.BC.89)
 - [用户签名( userSig )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)

## userSig的获取
关于 userSig 的获取请参考[ 用户鉴权 ](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)。
在这里您也可以直接开发辅助工具生成 userSig。

## 初始化 iLiveSDK

在登录之前，需要初始化 SDK，建议在程序运行时就初始化，示例代码如下：
```c++
#define SDKAppId		后台创建应用对应的SDKAppId
#define AccountType		后台创建应用对应的AccountType

int nRet = GetILive()->init(SDKAppId, AccountType, false);
if (nRet != NO_ERR)
{
	//初始化失败,nRet为错误码
}
else
{
	//初始化成功
}
```

## 调用登录接口
初始化后，即可进行登录，示例代码如下：
```c++
GetILive()->login(userId, UserSig, [](void* data) {
	//登录成功
}, [](const int code, const char *desc, void* data) {
	//登录失败, code为错误码，desc为错误原因描述
}, NULL);
```

## 源码说明
* 演示代码使用了 C++11
上面登录接口在传入 SDK 成功和失败回调时，使用了 C++11 的 lambda 表达式，如果用户使用的 vs2010 及更低版本( 不支持或不完全支持 C++11 )，成功和失败的回调需要传入 C 语言的函数指针。调用示例如下：
		void OnLoginSuc(void* data)
		{
			//登录成功
		}

		void OnLoginErr(const int code, const char *desc, void* data)
		{
			//登录失败, code为错误码，desc为错误原因描述
		}

		GetILive()->login(userId, UserSig, OnLoginSuc, OnLoginErr, NULL);
后续都使用 lambda 表达式，不再重复说明。

* 异步回调都带一个 void\* data 参数
由于回调是用 C 的函数指针实现的，回调中无法访问回调函数外部的变量，所以，设计了 void\* 参数；异步回调传入的 void\* 参数，会在回调中原封不动地传出；一般是将类对象的 this 指针传入，在回调中强制转换回类对象指针，然后，通过此指针访问类成员。

* iLiveSDK 依赖 Windows 消息循环
iLiveSDK 内部使用 Windows 的消息循环机制将回调抛回主线程（GUI 线程），方便用户在回调中执行 UI 操作。所以，如果是 Win32 控制台程序，在程序中必须要有消息循环，代码如下：
```c++
#include <Windows.h>
MSG msg;
while (GetMessage(&msg, NULL, 0, 0))
{
	TranslateMessage(&msg);
	DispatchMessage(&msg);
}
```

* 本例 Demo 将 userId 和 userSig 写死了，userSig 是有有效期的，一般为三个月；如果过期，将会登录失败；用户在运行 demo 时，需要按照本文所述的方式生成自己的 userSig，然后换成自己的 SDKAppId、AccountType、userId 和 userSig 进行测试。

## 运行结果
![](https://main.qcloudimg.com/raw/0efdf60c32dd0b52070a7e0392b53246.png)
