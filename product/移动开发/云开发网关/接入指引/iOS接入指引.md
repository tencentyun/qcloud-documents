本指引用于协助指导如何调整 iOS 应用，使得应用的网络请求经过网关进行转发。

## 接入说明
iOS 应用，需要使用网关提供的 SDK，实现网络通讯，替换应用原有的网络通讯 SDK 或 API。

## 操作步骤
### 步骤1：获取 SDK
[联系我们](https://cloud.tencent.com/document/product/1595/75974) 获取到网关提供的 iOS SDK，并在开发机解压。
SDK 包括如下：
- WXCloud.h（头文件）
- libWXCloudCore.a（静态库）
- WXCloudSample（示例工程）

<img style="width:500px" src="https://7361-saas-imgbox-9gbntzkl1ad561d5-1258016615.tcb.qcloud.la/demand/c462c81061b0a08e013285e539b22ff8/content/7662-image.png"/>

### 步骤2：添加头文件和静态库:
在项目中添加静态库及头文件用于网络调用使用。需要添加的内容有 WXCloud.h、libWXCloudCore.a、libz，其中 SDK 底层依赖系统动态库 libz。

### 步骤3：调用 SDK 及调试
通过使用添加的动态库和调用类实现网络发送，按如下代码实例实现网络请求调用。
其中参数说明如下：
- appKeyId，appKey：通过联系我们获取或更新。
- HOST：业务自定义 HOST 名，需要和网关的路由配置中的域名对应，用于网关路由转发匹配。


```java
// 包含头文件
#import "WXCloud.h"

// curl全局初始化，线程不安全
wxcloud::WXCloud::Init();

// 初始化（根据网关信息，填入 appSDKKeyId & appSDKKey）
NSString *appSDKKeyId = @"_ZbyJWXMrSkZb2PlHVZyrA";
NSString *appSDKKey = @"iTQR@M5b66SQJZi7";
wxcloud::WXCloud wxCloud(appSDKKeyId.UTF8String, appSDKKey.UTF8String);

// 调用（根据业务需求，填入 HTTP 参数）
wxcloud::HttpMethod httpMethod = wxcloud::HttpMethod::POST; // HTTP method
NSString *path = @"/"; // HTTP path，无需携带域名
wxcloud::header_type headers; // HTTP header
headers["HOST"] = "bjbench.woyaodaguaishou.cn"; // header 里指定 HOST
NSString *body = @"Hello World!"; // HTTP Body

wxCloud.callContainer(httpMethod, path.UTF8String, 	 
    headers, std::move(body.UTF8String),[](long 
    ret, long http_code, std::map<std::string, 
    std::string>headers, std::string body){
    // 先判断 ret，0表示成功，其他表示失败
    //   0 表示成功
    //   [1 - 98] 表示失败，详见 https://curl.se/libcurl/c/libcurl-errors.html
    //   102002 请求执行时间超过 15s
    //   -601001 系统失败
    //   -608001 请求包超过 1MB
    //   -608002 响应包超过 3MB
    printf("ret: %ld\n", ret);
    // 再判断 http_code
    printf("http_code: %ld\n\n", http_code);
    for (const auto &&header : headers) {
       printf("http header: %s = %s\n", header.first.c_str(), header.second.c_str());
    }
        printf("\nbody: %s\n", body.c_str());
});

```
测试执行返回 ret=0 且 http_code=200 的情况下，表示调用成功。另外，也可以自行参见 WXCloudSample 接入。


## 常见问题
### 静态库冲突怎么处理？
SDK 集成了 libcurl、libcrypto、libssl 和 libnghttp2，如果宿主工程也用了相同的库，可能会导致静态库冲突，可联系云开发进行处理。
