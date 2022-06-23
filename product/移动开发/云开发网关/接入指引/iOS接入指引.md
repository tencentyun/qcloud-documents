# iOS接入指引

## 一、获取SDK

SDK包括如下：

- WXCloud.h（头文件）
- libWXCloudCore.a（静态库）
- WXCloudSample（示例工程）

<img style="width:500px" src="https://7361-saas-imgbox-9gbntzkl1ad561d5-1258016615.tcb.qcloud.la/demand/c462c81061b0a08e013285e539b22ff8/content/7662-image.png"/>

## 二、添加头文件和静态库

WXCloud.h、libWXCloudCore.a和libz

SDK底层依赖系统动态库libz。

## 三、调用SDK及调试

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

执行返回ret=0且http_code=200表示调用成功。
至此，已经成功接入SDK，也可以自行参考WXCloudSample接入。

## 四、常见问题

- **静态库冲突：** SDK集成了libcurl、libcrypto、libssl和libnghttp2，如果宿主工程也用了相同的库，可能会导致静态库冲突，可联系云开发进行处理。
