# Android接入指引

## 一、获取SDK

SDK包括如下：

- libWXCloudCore.so（动态库）
- WXCloudCore.java（JNI类）
- WXCloudContainerResp.java（JNI回包类）
- WXCloudDemo（示例工程）

<img style="width:500px" src="https://7361-saas-imgbox-9gbntzkl1ad561d5-1258016615.tcb.qcloud.la/demand/c462c81061b0a08e013285e539b22ff8/content/7603-image.png"/>

## 二、添加动态库和类

- libWXCloudCore.so、WXCloudCore.java、WXCloudContainerResp.java和libz（-lz）

- 添加libWXCloudCore.so，并在 `build.gradle` 中指定动态库目录

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

- 新建 `com.tencent.wxcloud` 包，并添加 `WXCloudCore.java` 和 `WXCloudContainerResp.java`

## 三、调用SDK及调试

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

执行返回ret=0且http_code=200表示调用成功。
至此，已经成功接入SDK，也可以自行参考WXCloudDemo接入。

## 四、常见问题

- **Android minSDK版本不支持：** SDK目前配置的minSDK是19，如果宿主工程有更低版本的需求，可联系我们进行处理。
