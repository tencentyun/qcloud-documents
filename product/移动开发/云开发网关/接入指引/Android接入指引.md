本指引用于协助指导如何调整 Android 应用，使得 Android 应用的网络请求经过网关进行转发。

## 接入说明
Android 应用，需要使用网关提供的 SDK，实现网络通讯，替换应用原有的网络通讯 SDK 或 API。

## 操作步骤
### 步骤1：获取 SDK
[联系我们](https://cloud.tencent.com/document/product/1595/75974) 获取到网关提供的 Android SDK，并在开发机解压。
SDK 包括如下：
- libWXCloudCore.so（动态库）
- WXCloudCore.java（JNI 类）
- WXCloudContainerResp.java（JNI 回包类）
- WXCloudDemo（示例工程）

<img style="width:500px" src="https://7361-saas-imgbox-9gbntzkl1ad561d5-1258016615.tcb.qcloud.la/demand/c462c81061b0a08e013285e539b22ff8/content/7603-image.png"/>

### 步骤2：添加动态库和类
在项目中添加动态库及调用类用于网络调用使用。需要添加的动态库及调用类有 libWXCloudCore.so、WXCloudCore.java、WXCloudContainerResp.java 和 libz（-lz）。
按如下操作添加动态库及调用类：
- 添加 libWXCloudCore.so，并在 `build.gradle` 中指定动态库目录。
``` java
android {
    ...
    sourceSets{
        main{
            jniLibs.srcDirs = ['libs']
        }
    }
  ...
}
```
- 新建 `com.tencent.wxcloud` 包，并添加 `WXCloudCore.java` 和 `WXCloudContainerResp.java`。

### 步骤3：调用 SDK 及调试
通过使用添加的动态库和调用类实现网络发送，按如下代码实例实现网络请求调用。
其中参数说明如下：
- appKeyId，appKey：通过联系我们获取或更新。
- HOST：业务自定义 HOST 名，需要和网关的路由配置中的域名对应，用于网关路由转发匹配。


```java
// 导入JNI类
import com.tencent.wxcloud.WXCloudCore;
import com.tencent.wxcloud.WXCloudContainerResp;

// 加载动态库
static {
        System.loadLibrary("WXCloudCore");
    }

// 定义JNI类对象
private WXCloudCore wxCloudCore;

// 调用
// 根据网关信息填写
String appKeyId = "_ZbyJWXMrSkZb2PlHVZyrA";
String appKey = "iTQR@M5b66SQJZi7";
this.wxCloudCore = new WXCloudCore(appKeyId, appKey);

// 根据业务 HTTP 参数填写
String method = "POST";
String path = "/";
HashMap<String, String> header = new HashMap<>();
header.put("HOST", "bjbench.woyaodaguaishou.cn");
String body = "Hello World";

WXCloudContainerResp resp1 = this.wxCloudCore.callContainer(method, path, header, body);
System.out.printf("wxcloud resp.ret=%d, resp.http_code=%d, resp.body=%s, resp.headers=%s\n", resp1.ret, resp1.httpCode, resp1.body, resp1.headers);

WXCloudContainerResp resp2 = this.wxCloudCore.callContainer(method, path, header, body);
System.out.printf("wxcloud resp.ret=%d, resp.http_code=%d, resp.body=%s, resp.headers=%s\n", resp2.ret, resp2.httpCode, resp2.body, resp2.headers);
```
测试执行返回 ret=0 且 http_code=200 的情况下，表示调用成功。
另外，也可以自行参考 WXCloudDemo 接入。

## Android SDK 使用常见问题
### Android minSDK 版本不支持怎么办？

SDK 目前配置的 minSDK 版本是19，如果宿主工程有更低版本的需求，可 [联系我们](https://cloud.tencent.com/document/product/1595/75974) 进行处理。

### 如何和 okhttp 整合？

目前 SDK 提供 okhttp 的拦截器，可以仍然使用 okhttp 并通过拦截器将链路转为使用网关。更详细的对接技术问题，可 [联系我们](https://cloud.tencent.com/document/product/1595/75974) 进行处理。
