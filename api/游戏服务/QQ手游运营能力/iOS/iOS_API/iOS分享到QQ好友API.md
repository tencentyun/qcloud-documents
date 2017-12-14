
## 功能描述

在用户安装了手机 QQ 时通过手机 QQ 进行分享，否则调用浏览器页面进行分享。其中文本消息，图文消息和音频消息的 title 是必须填写的，summary 可以不填，具体调用请参考实际示例。使用分享到 QQ 好友功能需要设置 QQ 业务回调，请参考处理 QQ 业务的回调。

## 方法原型
```
/**
 向手Q发起分享请求
 \param req 分享内容的请求
 \return 请求发送结果码
 */
+ (QQApiSendResultCode)sendReq:(QQBaseReq *)req;
```

## 参数说明

| 参数名 | 必选 | 类型 |参数说明|
|---------|---------|---------|
| req | 必选 | QQBaseReq*|分享内容的请求|

## 实际示例

### 纯文本分享

```
//开发者分享的文本内容
QQApiTextObject *txtObj = [QQApiTextObject objectWithText:@"text"];
SendMessageToQQReq *req = [SendMessageToQQReq reqWithContent:txtObj];
//将内容分享到qq
QQApiSendResultCode sent = [QQApiInterface sendReq:req];
```

### 纯图片分享

```
//开发者分享图片数据
NSData *imgData = [NSData dataWithContentsOfFile:path];
QQApiImageObject *imgObj = [QQApiImageObject objectWithData:imgData
                                           previewImageData:imgData
                                           title:@"title"
                                           description :@"description"];
SendMessageToQQReq *req = [SendMessageToQQReq reqWithContent:imgObj];
//将内容分享到qq
QQApiSendResultCode sent = [QQApiInterface sendReq:req];
```

### 分享文件（仅数据线）（2.8.1）

```
NSString *filePath = [[[NSBundle mainBundle] resourcePath] stringByAppendingPathCo                           mponent:@"test.txt"];
NSData *fileData = [NSData dataWithContentsOfFile:filePath];
QQApiFileObject *fileObj = [QQApiFileObject 
objectWithData:fileData
previewImageData:nil
title:self.binding_title ? : @""
description:self.binding_description ? : @""];
if (self.binding_description != nil && ![self.binding_description isEqualToString:@""])
fileObj.fileName = self.binding_description;
else
fileObj.fileName = @"test.txt";
[fileObj setCflag:kQQAPICtrlFlagQQShareDataline];
SendMessageToQQReq *req = [SendMessageToQQReq reqWithContent:fileObj];
//将内容分享到qq
//QQApiSendResultCode sent = [QQApiInterface sendReq:req];
```
