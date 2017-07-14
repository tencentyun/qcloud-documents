## 1 初始化 

初始化需要调用三个接口，分别是QALSDK的initQal，QALHttpSDK的setCacheMaxSize和init 
首先，初始化QALSDK，初始化接口需要填写一个参数，参数sdkAppid为申请app时获得的sdkappid 

```
/*
@Description 初始化QALSDK
@param sdkAppid 在app申请页面上的产品id
*/
-(id)initQal:(int) sdkAppid;
```
调用示例

```
[[QalSDKProxy sharedInstance] initQal:sdkAppid;
```
接下来，设置Http的缓存大小，参数size为缓存大小，单位为字节，填0表示关闭Cache 

```
/*
@Description 设置Http缓存大小，空闲空间不足时将通过LRU淘汰数据
@param size http缓存大小
*/
+(void)setCacheMaxSize:(size_t)size
```
调用示例 

```
[QALHttpRequest setCacheMaxSize:4096000];//设置cache大小,单位字节
```
最后，初始化QALHttpSDK 

```
+ (void)init;
```
调用示例 

```
[QALHttpRequest init];//初始化http sdk
```

## 2 发送Http GET请求 

发送Http GET请求，示例如下，具体参数设置接口可参阅QALHttpRequest.h： 

```
NSString *fullurl = [NSString stringWithFormat:@"http://www.qq.com"];
NSURL* url = [[NSURL alloc] initWithString:fullurl];
QALHttpRequest* request = [[QALHttpRequest alloc] initWithURL:url];
[request setRequestMethod:@"GET"];
[request startAsynchronous:self];
```
实现QALHTTPRequestDelegate的回调方法，处理http响应 

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
处理http响应示例，具体值获取的接口可参阅QALHttpRequest.h： 

```
-(void)requestFinished:(QALHttpRequest *)request
{
	//收到响应包
	NSLog(@"receive response");
   
	//可以通过get接口拿到响应内容，接口参阅QALHttpRequest.h
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

## 3 发送Http POST请求
```
NSURL* url = [[NSURL alloc] initWithString:@"http://stat.m.jd.com/stat/access"];
QALFormDataRequest* request = [[QALFormDataRequest alloc] initWithURL:url];
[request setRequestMethod:@"POST"];
[request setCharSet:@"charset=utf-8"];
[request addPostValue:@"value1" forKey:@"key1"];
[request addPostValue:@"value2" forKey:@"key2"];
[request startAsynchronous:self];
```
实现QALHTTPRequestDelegate的回调方法，处理http响应 

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
处理http响应示例，具体值获取的接口可参阅QALHttpRequest.h： 

```
-(void)requestFinished:(QALHttpRequest *)request
{
	//收到响应包
	NSLog(@"receive response");
   
	//可以通过get接口拿到响应内容，接口参阅QALHttpRequest.h
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

## 4 错误码

<table class="table table-bordered">
<tr><td width="21%">错误码</td><td>含义</td><td width="34%">是否需要app处理</td></tr>
<tr><td>6</td><td>请求没有响应，超时</td><td>否</td></tr>
<tr><td>-21022</td><td>回包包体Protobuf解包失败</td><td>否</td></tr>
<tr><td>-21021</td><td>回包字符串解码失败</td><td>否</td></tr>
<tr><td>-21020</td><td>回包解析Json格式失败</td><td>否</td></tr>
<tr><td>-21017</td><td>回包分片不完整</td><td>否</td></tr>
<tr><td>-21016</td><td>回包包体解压缩失败</td><td>否</td></tr>
</table>