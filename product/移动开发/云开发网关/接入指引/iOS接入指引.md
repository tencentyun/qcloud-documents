
<dx-alert infotype="explain" title="">
SDK 正在内测中，请 [联系我们](https://cloud.tencent.com/online-service) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取 SDK。
</dx-alert>

## 操作步骤

### 步骤1：获取 SDK

SDK 包括如下：

- WXCloud.h（头文件）
- libWXCloudCore.a（静态库）
- WXCloudSample（示例工程）

![](https://qcloudimg.tencent-cloud.cn/raw/32c525b49ab07fc7f59640b5d7661d5a.png)

### 步骤2：添加头文件和静态库

1. 准备好 WXCloud.h、libWXCloudCore.a 和 libz。
2. SDK 底层依赖系统动态库 libz。

### 步骤3：调用 SDK 及调试

调用代码如下：
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>


执行返回 ret=0 且 http_code=200 表示调用成功。至此，已经成功接入 SDK，也可以自行参见 WXCloudSample 接入。

## 相关说明

**静态库冲突：** SDK 集成了 libcurl、libcrypto、libssl 和 libnghttp2，如果宿主工程也用了相同的库，可能会导致静态库冲突，可 [联系我们](https://cloud.tencent.com/online-service) 进行处理。
