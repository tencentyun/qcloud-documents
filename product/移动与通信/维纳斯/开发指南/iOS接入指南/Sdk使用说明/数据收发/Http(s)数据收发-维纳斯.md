
对于发送 HTTP(s)数据, 我们提供了两种接口方式，分别如下
**1、兼容系统接口方案：**
基于 iOS 系统的 URL Loading System 实现的, 只需引 入WnsURLProtocol.h, 然后绑定 sdk 实例并向系统注册，代码如下

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

然后你在需要用Wns发送的请求用NSURLProtocol的方法来给这个请求打上标志```[NSURLProtocol setProperty:@(YES) forKey:ShouldUseWns inRequest:req]```, 然后使用系统的NSURLConnection或者AFNetworking等第三方库来发送请求即可, Wns会对打上标志的请求使用Wns的通道来发送.

注意, 如果使用NSURLSessionDataTask或者使用了该类的第三方库(比如AFNetworking), 还需要对request做以下设置:

```
// 当请求的方法是POST时, 如果使用NSURLSessionDataTask或者使用了改类的第三方库(比如AFNetworking)时,
// 自定义的NSURLProtocol获取到的NSURLRequest的HTTPBody为nil(系统bug, 对应的radar链接: rdar://15993891 )
// 所以, 在使用相关类发送前, 需要加上以下语句, 这样WnsURLProtocol才能获取到可用的HTTPBody
if (request.HTTPBody)
{
    [NSURLProtocol setProperty:request.HTTPBody forKey:WnsHTTPBody inRequest:request];
}
```
**[注意]此模式下，sdk 会自动将 url 设置为 cmd，wns 会统计每 个cmd 的成功率等信息，对应的，需要在控制台配置 url 域名对应的路由。路由配置请参考：[控制台说明](http://cloud.tencent.com/doc/product/276/%E6%8E%A7%E5%88%B6%E5%8F%B0%E8%AF%B4%E6%98%8E)**

** 2、Wns Sdk 接口方案**
调用接口 sendHTTPRequest 来收发 Http(s)数据。

开发商终端需要修改老的接口，替换为 Wns 的收发接口(该接口不支持http的301, 302跳转)

**[注意]cmd 必须是细化到接口，wns 会统计每个 cmd 的成功率等信息，对应的，需要在控制台配置域名 user.qzone.qq.com 对应的路由。路由配置请参考：[控制台说明](http://cloud.tencent.com/doc/product/276/%E6%8E%A7%E5%88%B6%E5%8F%B0%E8%AF%B4%E6%98%8E)**
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