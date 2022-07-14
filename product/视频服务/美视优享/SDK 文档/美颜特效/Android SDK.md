
## 功能说明
动效贴纸、绿幕等特效功能，是基于优图实验室的 AI 识别技术和天天 P 图的美妆技术为基础开发的特权功能。腾讯云小直播团队通过跟优图和天天 P 图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。
 
## 版本下载
您可以到 [移动直播 SDK 开发包](/doc/product/454/7873) 页面下方下载特权版 SDK 压缩包，压缩包有加密（解压密码与 License 文件可以联系商务获取）, 成功解压后得到一个 `txrtmpsdk.jar` 和 `libtxrtmpsdk.so` 等几个 so 文件，替换您工程中的非特权版 jar 文件和 so 文件即可。

[](id:jump)
## 工程设置

### 1. 添加 SDK
拷贝 SDK 里的 `txrtmpsdk.jar` 和 `libtxrtmpsdk.so` 等文件到工程对应位置，如 libs 下。
>! 特权版只支持 armeabi 架构的 so 文件，请删除 App 里面的其余架构 so 文件，避免 so 文件加载失败。

### 2. 添加资源
将 zip 包中的 `camera` 文件夹拷贝到工程的 assets 目录下。
>!camera 目录包含了切换动效需要的资源等文件，必须正确放到 assets 目录下，否则会发生异常。

### 3. 导入 License 文件
特权版需要 License 验证通过后，相应功能才能生效。您可以联系商务申请一个免费的为期 30 天的调试用的 License。获得 License 后，将其命名为 **YTFaceSDK.license** ，并添加到工程的 assets 目录下。

>?
> - 每个 License 都有绑定具体的 package name，修改 App 的 package name 会导致验证失败。
> - `YTFaceSDK.license` 的文件名固定，不可修改、且必须放在 assets 目录下。
> - iOS 和 Android 不需要重复申请 License，一个 License 可以同时授权一个 iOS 的 Bundle ID 和一个 Android 的 packageName。

## 功能调用

### 动效功能

一个动效模板是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数和文件大小也不尽相同。
小直播中的示例代码是从后台下载动效资源，再统一解压到 Resource 目录。您可以在小直播代码中找到动效资源和动效缩略图的下载地址，格式如下：

```
https://st1.xiangji.qq.com/yunmaterials/{动效id}Android.zip
https://st1.xiangji.qq.com/yunmaterials/{动效id}.png
```

强烈建议您将动效资源放在自己的服务器上，以防小直播变动造成不必要的影响。
当解压完成后，即可通过以下接口开启动效效果：

```java
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```


### 绿幕功能

使用绿幕需要先准备一个用于播放的 MP4 文件，通过调用以下接口即可开启绿幕效果：

```java
/**
 * 设置绿幕文件:目前图片支持jpg/png，视频支持mp4/3gp等Android系统支持的格式
 * API 要求18
 * @param path ：绿幕文件位置，支持两种方式：
 *             1.资源文件放在assets目录，path直接取文件名
 *             2.path取文件绝对路径
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```

