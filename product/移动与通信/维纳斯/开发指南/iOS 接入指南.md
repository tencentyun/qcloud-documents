## Sdk 目录结构说明
WnsSDK：包含 WnsSDK4Cloud.framework
WnsSDKDemo：示例工程，演示了如何使用 WnsSDK
Doc：
    WnsSDK 使用说明：本文档
    http 端接入说明：从控制台配置到 sdk 的流程来演示http服务的接入

## 系统环境要求和限制
适用于 iOS 5.0 及以上的系统版本
sdk 接口字符类型参数限制长度为 256 字节
sdk 发送数据限制长度为 512K 字节
sdk 接受数据限制长度为 512K 字节
应用程序工程需要包含以下库(可以参考 demo)：
![](//mccdn.qcloud.com/static/img/dab523fae1934af9d3ad1d5ff872e9e4/image.png)

## SDK 使用说明
### 名词解释
**appID**：为开发商在控制台申请的应用 ID。
**appVersion**：是开发商应用程序的版本号，如"1.0"等。
**appChannel**：是开发商用来区分发布的渠道的，各种下载渠道，如 appstore、应用宝、百度手机助手。 赋值如"appstore"。
**uid**：业务用户的唯一标识。
**wid**：wns 为每个终端分配的唯一标识。
**appVersion** 和 **appChannel** 是使用在上报统计和服务质量监控的。


终端使用 Sdk 主要包括下面几个步骤
### Sdk 初始化
调用接口 initWithAppID 完成系统初始化。

WnsSDK 在初始化后，会和 Wns 后台建立并保持一个长连接，后续的请求会通过此连接发送
    所以最好尽早初始化 sdk， 最好在- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 里进行初始化。
	示例
```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
    gWnsSDK = [[WnsSDK alloc] initWithAppID:1000244
                              andAppVersion:@"1.0"
                              andAppChannel:@"appstore"];
    [gWnsSDK setStatusCallback:^(WnsSDKStatus status) {
        NSLog(@"WnsSDKStatus:%ld", (long)status);
        gWnsSDKStatus = status;
        
    }];
    
    return YES;
}
```

### 数据收发
初始化完 Sdk 后，应用即可通过 Sdk 来发送数据。据发送的数据的类型的不同，们提供了两组接口：发送二进制数据和发送 http 数据，开发商可以根据后端的协议类型(protobuf 类的二进制数据 或 http 协议)选择不同的接口。
#### Http(s)数据收发
对于发送 HTTP(s)数据, 我们提供了两种接口方式，分别如下
**1. 兼容系统接口方案**：
基于 iOS 系统的 URL Loading System 实现的， 只需引入 WnsURLProtocol.h，然后绑定 sdk 实例并向系统注册，代码如下

```
[WnsURLProtocol bindSDKInstance:gWnsSDK];
[NSURLProtocol registerClass:[WnsURLProtocol class]];

//注:使用AFNetworking的AFURLSessionManager时, 需要使用以下方式注册:

NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
NSMutableArray *protocolsArray = [NSMutableArray arrayWithArray:configuration.protocolClasses];
[protocolsArray insertObject:[WnsURLProtocol class] atIndex:0];
configuration.protocolClasses = protocolsArray;
AFURLSessionManager *manager = [[AFURLSessionManager alloc] initWithSessionConfiguration:configuration];
```

然后您在需要用 Wns 发送的请求用 NSURLProtocol 的方法来给这个请求打上标志```[NSURLProtocol setProperty:@(YES) forKey:ShouldUseWns inRequest:req]```, 然后使用系统的 NSURLConnection 或者 AFNetworking 等第三方库来发送请求即可, Wns 会对打上标志的请求使用 Wns 的通道来发送.

注意， 如果使用 NSURLSessionDataTask 或者使用了该类的第三方库(比如 AFNetworking)，需要对 request 做以下设置：

```
// 当请求的方法是POST时, 如果使用NSURLSessionDataTask或者使用了改类的第三方库(比如AFNetworking)时,
// 自定义的NSURLProtocol获取到的NSURLRequest的HTTPBody为nil(系统bug, 对应的radar链接: rdar://15993891 )
// 所以, 在使用相关类发送前, 需要加上以下语句, 这样WnsURLProtocol才能获取到可用的HTTPBody
if (request.HTTPBody)
{
    [NSURLProtocol setProperty:request.HTTPBody forKey:WnsHTTPBody inRequest:request];
}
```
>注意：
>如果使用 NSURLSessionDataTask 或者使用了该类的第三方库(比如 AFNetworking), 还需要对 request 做以下设置

**2. Wns Sdk 接口方案**
调用接口 sendHTTPRequest 来收发 Http(s)数据。

开发商终端需要修改老的接口，替换为 Wns 的收发接口(该接口不支持 http 的 301，302 跳转)
>注意：
**此模式下，sdk 会自动将 url 设置为 cmd，wns 会统计每 个cmd 的成功率等信息，对应的，需要在控制台配置 url 域名对应的路由。路由配置请参考：[控制台说明](https://cloud.tencent.com/document/product/276/3005)。**

```
            NSString *cmd = @"user.qzone.qq.com/xunren";  
            NSMutableURLRequest *req = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:@"http://user.qzone.qq.com/xunren"]
                                          cachePolicy:NSURLRequestReloadIgnoringLocalAndRemoteCacheData
                                      timeoutInterval:120.0];
            [req setHTTPMethod:@"GET"];
            [req setHTTPShouldHandleCookies:NO];
            [req setValue:@"application/x-www-form-urlencoded" forHTTPHeaderField:@"Content-Type"];
            [req setValue:@"gzip" forHTTPHeaderField:@"Content-Encoding"];

            [gWnsSDK sendHTTPRequest:req cmd:cmd timeout:30 completion:^(NSString *cmd, NSURLResponse* response, NSData* data, NSError* wnsError, NSError* wnsSubError) {
                NSLog(@"cmd = %@, data = %@, wnsError = %@, wnsSubError = %@", cmd, data, wnsError, wnsSubError);
                if (wnsError) {
                    self.detailDescriptionLabel.text = [NSString stringWithFormat:@"数据接收失败！\nerror = %@", wnsError];
                } else {
                    self.detailDescriptionLabel.text = @"";
                    self.responseWebView.hidden = NO;
                    [self.responseWebView loadData:data MIMEType:[response MIMEType] textEncodingName:[response textEncodingName] baseURL:[response URL]];
                }
            }];
```


#### 二进制数据收发
调用接口 sendRequest 来收发二进制数据。
发送二进制数据的接口和发送 http 的比较类似，开发商终端需要修改原来的代码，将收发接口替换为 Wns 的 Sdk
```
/*! @brief 发送请求(TCP协议接口)。
 *
 * @param data 第三方应用应用层数据
 * @param cmd 第三方应用应用层请求命令字
 * @param timeout 请求超时时间
 * @param completion 回调Block，参数data表示服务器应答数据，参数bizError表示第三方业务错误，参数wnsError表示Wns内部错误，wnsSubError表示Wns的子类错误
 * @return 成功返回请求序列号，失败返回-1。
 */
- (long)sendRequest:(NSData *)data
                cmd:(NSString *)cmd
            timeout:(unsigned int)timeout
         completion:(void(^)(NSString *cmd, NSData *data, NSError *bizError, NSError *wnsError, NSError *wnsSubError))completion;

//示例 
NSData *data = [NSData dataWithBytes:"abcdefg" length:7];
            [gWnsSDK sendRequest:data cmd:@"wnsdemo/transfer" timeout:30 completion:^(NSString *cmd, NSData *data, NSError *bizError, NSError *wnsError, NSError* wnsSubError) {
                NSLog(@"cmd = %@, data = %@, bizError = %@, wnsError = %@, wnsSubError = %@", cmd, data, bizError, wnsError, wnsSubError);
                if (bizError || wnsError) {
                    self.detailDescriptionLabel.text = [NSString stringWithFormat:@"数据接收失败！\nerror = %@", bizError ?: wnsError];
                } else {
                    self.detailDescriptionLabel.text = [NSString stringWithFormat:@"数据接收成功：cmd = %@， data length = %lu", cmd, (unsigned long)[data length]];
                }
            }];
        }
```
>注意：
>**cmd 必须是细化到接口，wns 会统计每个 cmd 的成功率等信息，对应的，需要在控制台配置域名 user.qzone.qq.com 对应的路由。路由配置请参考：[控制台说明](https://cloud.tencent.com/document/product/276/3005)。**


### 用户绑定和接收 push
#### 用户绑定
Wns 会对每一个设备记录一个设备 ID 来进行标识，以通过后端的 API 对某一个设备进行消息推送(PUSH).。但是应用本身可能也有自己的用户 id(后面简称 uid)，如果需要对某一个 uid 进行消息推送时，客户端就得在用户登录和注销时调用绑定/注销的相应方法。调用后，Wns 后台会记录两者的对应关系，此后就能对该 uid 进行消息推送
```
/*! @brief
 * 第三方应用层可选调用接口。如果第三方应用后台需要通过WNS服务发送针对指定用户的数据，
 * 则第三方应用终端，在用户登录成功后，需要绑定第三方用户ID到WNS服务。
 * 对新uid进行绑定前, 需要使用unbind对旧bid进行解绑
 * 
 * @param uid 第三方应用的用户唯一标识
 * @param completion 回调Block
 */
- (void)bind:(NSString *)uid completion:(void(^)(NSError *error))completion;


/*! @brief 注销绑定。应用的用户注销时请调用该接口.
 *
 * @param uid 第三方应用的用户唯一标识
 * @param completion 回调Block
 */
- (void)unbind:(NSString *)uid completion:(void(^)(NSError *error))completion;

```

#### 接收 Push
```
/*! @brief 设置Wns Push的数据接收block。
 *
 * @param completion 回调Block，参数cmd标识服务推送数据命令字，参数data标识服务器推送数据，参数error标识错误信息
 */
- (void)setPushDataReceiveBlock:(void(^)(NSString *cmd, NSData *data, NSError *error))completion;

/*! @brief 向服务器注册苹果的推送服务所使用的devicetoken
 *
 * @param deviceToken 用户设备Tokon。
 * @param completion 回调Block, error为nil时表示注册成功
 */
- (void)registerRemoteNotification:(NSString *)deviceToken completion:(void(^)(NSError *error))completion;

```


### 调试类接口
在接入 Wns 的过程中，当遇上某些问题需要和 Wns 侧一起定位问题时，可以通过以下接口设置客户端连接到 Wns 的测试环境，Wns 的测试环境也可以连接到开发商的测试服务器环境中，这样便于快速的定位到具体的问题。
要使用测试环境，开发商必须按下面来要求来设置
#### 设置调试环境接入 IP
WNS 提供调试环境给开发商使用，服务端使用控制台可以配置访问。客户端需要指定调试环境的接入 IP。
**开发商必须在 Wns 控制台配置好开发商测试环境服务器路由信息。**
在接入 Wns 的过程中，当遇上某些问题需要和 Wns 的工作人员一起调试时，可以通过以下接口设置客户端连接的 Wns 后台的 IP，方便查找问题。
```
/*! @brief 调试接口：设置调试服务器地址。
 *
 * @paramip 为nil或@"wns.qq.com"时切换回非调试模式
 * @param port 允许为0，即默认80/443/8080/14000轮询
 *
 * @note 会触发重建链接
 */
- (void)setDebugIP:(NSString *)IP port:(unsigned short)port;

```
#### 关键日志
```
/*! @brief 获取wns的关键的日志信息,用于开发中查问题
 *
 */
- (NSString *)keyLog;

```
另外，如果出现 Wns 连接或者收发出错的问题时，可以通过 Sdk 接口 keyLog 拿到提示信息并打印出来，提供给相关工作人员查看，以方便查找问题。
#### Wns 快速验证模式
对于一些还在犹豫是否该使用 Wns 的业务，我们提供了一个自动测试的模式。
在该模式下，sdk 会自动地每隔一段时间就发送一个测试的数据包到后台。您可以到控制台的监控页面看到对应的成功率和延时等情况，作为是否选用 Wns 的参考。
使用方式:初始化后 sdk后，调用下面接口即可。
```
/*! @brief 设置自动测试模式,这种模式下,sdk自身会定时发送测试数据包到后台,您可以从监控报表查看相关统计数据
 *
 * @param isEnable 是否打开自动测试模式
 *
 */
- (void)setAutoTestMode:(BOOL)isEnable;

```
Wns 提供快速验证模式，开发商可以先集成 Wns 的 Sdk，但是通信接口暂时不切换到 Wns 通道，该模式下，Wns Sdk 会自动发一些探测包到 Wns 的接入服务器（探测包不会转发到开发商服务器）。这样开发商可以在控制台上看到探测包的统计数据。可以准确的评估出实际接入 Wns 后的服务质量。如果效果明显，开发商再后续版本才正式将服务切换到 Wns 通道。

使用 Wns 快速验证模式，开发商只需要下面的几个步骤
1. Wns 控制台注册 App 和签名信息
2. 终端集成 Wns Sdk
3. 终端在初始化阶段调用 Sdk 接口 initWithAppID 和 setAutoTestMode
