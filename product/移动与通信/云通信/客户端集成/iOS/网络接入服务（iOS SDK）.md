## 初始化 

初始化需要调用三个接口，分别是 `QALSDK` 的 `initQal`，`QALHttpSDK` 的 `setCacheMaxSize` 和 `init`。首先，初始化 `QALSDK`，初始化接口需要填写一个参数，参数 `sdkAppid` 为申请 App 时获得的`sdkappid`。

```
/*
@Description 初始化 QALSDK
@param sdkAppid 在 App 申请页面上的产品 ID
*/
-(id)initQal:(int) sdkAppid;
```

**示例：**

```
[[QalSDKProxy sharedInstance] initQal:sdkAppid;
```

接下来，设置 HTTP 的缓存大小，参数 `size` 为缓存大小，单位为字节，填 0 表示关闭 Cache。

```
/*
@Description 设置 HTTP 缓存大小，空闲空间不足时将通过 LRU 淘汰数据
@param size http缓存大小
*/
+(void)setCacheMaxSize:(size_t)size
```

**示例：** 

```
[QALHttpRequest setCacheMaxSize:4096000];//设置 Cache 大小,单位字节
```

最后，初始化 `QALHttpSDK`。

```
+ (void)init;
```

**示例：** 

```
[QALHttpRequest init];//初始化 HTTP SDK
```

## 发送 HTTP GET 请求 

发送 HTTP GET 请求，示例如下，具体参数设置接口可参阅 `QALHttpRequest.h`。 

```
NSString *fullurl = [NSString stringWithFormat:@"http://www.qq.com"];
NSURL* url = [[NSURL alloc] initWithString:fullurl];
QALHttpRequest* request = [[QALHttpRequest alloc] initWithURL:url];
[request setRequestMethod:@"GET"];
[request startAsynchronous:self];
```

实现 `QALHTTPRequestDelegate` 的回调方法，处理 HTTP 响应。

```
/*
请求完成回调
*/
- (void)requestFinished:(QALHttpRequest *)request;

/*
请求失败回调
*/
- (void)requestFailed:(int)errCode andErrMsg:(NSString*)errMsg;
```

处理 HTTP 响应示例，具体值获取的接口可参阅 `QALHttpRequest.h`。

```
-(void)requestFinished:(QALHttpRequest *)request
{
	//收到响应包
	NSLog(@"receive response");
	//可以通过 GET 接口拿到响应内容，接口参阅 QALHttpRequest.h
	NSLog(@"status code:%i",[request getResp_status_code]);	   
	NSMutableArray* cookies = [request getResp_cookie];
	int num = (int)[cookies count];
	for(unsigned int i = 0 ; i< num; i++)
	{
		NSLog(@"cookie:%@",[cookies objectAtIndex:i]);
	}
	NSData* body = [request getResp_body];
	NSLog(@"resp body size:%i",(int)[body length]);
}
-(void)requestFailed:(int)errCode andErrMsg:(NSString *)errMsg
{
	NSLog(@"request fail,errcode:%i,errmsg:%@",errCode,errMsg);
}
```

## 发送 HTTP POST 请求

```
NSURL* url = [[NSURL alloc] initWithString:@"http://stat.m.jd.com/stat/access"];
QALFormDataRequest* request = [[QALFormDataRequest alloc] initWithURL:url];
[request setRequestMethod:@"POST"];
[request setCharSet:@"charset=utf-8"];
[request addPostValue:@"value1" forKey:@"key1"];
[request addPostValue:@"value2" forKey:@"key2"];
[request startAsynchronous:self];
```

实现 `QALHTTPRequestDelegate` 的回调方法，处理 HTTP 响应。 

```
/*
请求完成回调
*/
- (void)requestFinished:(QALHttpRequest *)request;
/*
请求失败回调
*/
- (void)requestFailed:(int)errCode andErrMsg:(NSString*)errMsg;
```

处理 HTTP 响应示例，具体值获取的接口可参阅 `QALHttpRequest.h`。

```
-(void)requestFinished:(QALHttpRequest *)request
{
	//收到响应包
	NSLog(@"receive response");
	//可以通过 GET 接口拿到响应内容，接口参阅　QALHttpRequest.h
	NSLog(@"status code:%i",[request getResp_status_code]);	   
	NSMutableArray* cookies = [request getResp_cookie];
	int num = (int)[cookies count];
	for(unsigned int i = 0 ; i< num; i++)
	{
		NSLog(@"cookie:%@",[cookies objectAtIndex:i]);
	}
	NSData* body = [request getResp_body];
	NSLog(@"resp body size:%i",(int)[body length]);
}
-(void)requestFailed:(int)errCode andErrMsg:(NSString *)errMsg
{
	NSLog(@"request fail,errcode:%i,errmsg:%@",errCode,errMsg);
}
```

## 错误码

| 错误码 | 含义 | 是否需要 App 处理 |
| --- | --- | --- |
| 6 | 请求没有响应，超时 | 否 |
| -21022 | 回包包体 Protobuf 解包失败 | 否 |
| -21021 | 回包字符串解码失败 | 否 |
| -21020 | 回包解析 JSON 格式失败 | 否 |
| -21017 | 回包分片不完整 | 否 |
| -21016 | 回包包体解压缩失败 | 否 |
