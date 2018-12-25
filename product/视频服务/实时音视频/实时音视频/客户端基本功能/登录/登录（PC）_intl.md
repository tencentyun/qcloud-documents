This document describes how to log in to Tencent Cloud from your client.
## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_login.zip)

## Prerequisites
You must have activated the service and created an application at the [TRTC official website](https://cloud.tencent.com/product/trtc).

## Concepts
 - [TRTC application](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
 - [Application ID( sdkAppId )](https://cloud.tencent.com/document/product/647/16792#.E5.BA.94.E7.94.A8.E6.A0.87.E8.AF.86.EF.BC.88-sdkappid-.EF.BC.89)
 - [Account type( accountType )](https://cloud.tencent.com/document/product/647/16792#.E5.B8.90.E5.8F.B7.E7.B1.BB.E5.9E.8B.EF.BC.88-accounttype-.EF.BC.89)
 - [User ID( userId )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E6.A0.87.E8.AF.86.EF.BC.88-userId-.EF.BC.89)
 - [User signature( userSig )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)

## Obtaining a userSig
For more information on how to obtain a userSig, see [User Authentication](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89).
You can also use the development tools to generate a userSig.

## Initializing iLiveSDK

Before login, it is recommended to initialize the SDK when you run the application. The sample code is as follows:
```c++
#define SDKAppId		 SDKAppId generated after creation of the application at backend
#define AccountType		AccountType generated after creation of the application at backend

int nRet = GetILive()->init(SDKAppId, AccountType, false);
if (nRet != NO_ERR)
{
	//Initialization failed. nRet is the error code
}
else
{
	//Initialization successful
}
```

## Calling the Login API
You can log in after initialization. The sample code is as follows:
```c++
GetILive()->login(userId, UserSig, [](void* data) {
	//Login successful
}, [](const int code, const char *desc, void* data) {
	//Login failed. "code" is the error code and "desc" is the error description
}, NULL);
```

## Source Code Description
* C++11 is used in the demonstration code
The lambda expression in C++11 is used by the above login API to pass in the successful/failed SDK callback. If you are using vs2010 or an earlier version that is not fully compatible with C++11, the function pointer in C programming language should be passed in for the successful/failed callback, as shown below:
		void OnLoginSuc(void* data)
		{
			//Login successful
		}

		void OnLoginErr(const int code, const char *desc, void* data)
		{
			//Login failed. "code" is the error code and "desc" is the error description
		}

		GetILive()->login(userId, UserSig, OnLoginSuc, OnLoginErr, NULL);
The lambda expression is always used.

* Each asynchronous callback has a parameter void\* data
As the function pointer in C is used for callback, variables outside of the callback function cannot be accessed during callback. During asynchronous callback, pass in the parameter void\*. The parameter will not change when passed out. Pass in the pointer "this" of the class object, forcibly convert it to the pointer of the class object during callback, and then access the class members via this pointer.

* iLiveSDK relies on Windows message loop
The iLiveSDK SDK uses Windows message loop to throw callbacks back to the main thread (GUI thread ) so that users can perform UI operations in callbacks. Therefore, if it is a Win32 console program, there must be a message loop in the program. The code is as follows:
```c++
#include <Windows.h>
MSG msg;
while (GetMessage(&msg, NULL, 0, 0))
{
	TranslateMessage(&msg);
	DispatchMessage(&msg);
}
```

* In this demo, userId and userSig are hard-coded. userSig is valid for 3 months. When it expires, the login will fail. When you run the demo, generate your userSig by following the steps described in this document, and then use your SDKAppId, AccountType, userId and userSig for testing.

## Execution Results
![](https://main.qcloudimg.com/raw/0efdf60c32dd0b52070a7e0392b53246.png)

## Email
If you have any questions, send us an email to trtcfb@qq.com.

