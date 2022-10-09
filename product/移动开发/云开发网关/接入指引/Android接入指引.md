
<dx-alert infotype="explain" title="">
SDK 正在内测中，请 [联系我们](https://cloud.tencent.com/online-service) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取 SDK。
</dx-alert>



## 操作步骤

### 步骤1：获取 SDK

SDK 包括如下：

- libWXCloudCore.so（动态库）
- WXCloudCore.java（JNI 类）
- WXCloudContainerResp.java（JNI 回包类）
- WXCloudDemo（示例工程）

![](https://qcloudimg.tencent-cloud.cn/raw/a3a753995b027e775e45e9f202f30594.png)

### 步骤2：添加动态库和类

1. 准备好 libWXCloudCore.so、WXCloudCore.java、WXCloudContainerResp.java 和 libz（-lz）。
2. 添加 libWXCloudCore.so，并在 `build.gradle` 中指定动态库目录：
<dx-codeblock>
:::  java
android {
    ...
    sourceSets{
        main{
            jniLibs.srcDirs = ['libs']
        }
    }
  ...
}
:::
</dx-codeblock>
3. 新建 `com.tencent.wxcloud` 包，并添加 `WXCloudCore.java` 和  `WXCloudContainerResp.java`。

### 步骤3：调用 SDK 及调试
调用代码如下：
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>

执行返回 ret=0 且 http_code=200 表示调用成功。至此，已经成功接入 SDK，也可以自行参见 WXCloudDemo 接入。

## 相关说明

**Android minSDK 版本不支持：** SDK 目前配置的 minSDK 是19，如果宿主工程有更低版本的需求，可 [联系我们](https://cloud.tencent.com/online-service) 进行处理。
