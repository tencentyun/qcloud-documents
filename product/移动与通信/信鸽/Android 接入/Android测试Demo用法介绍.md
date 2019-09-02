## 下载 Demo
信鸽的 Demo 工程在 SDK 文件内，需要先行 [下载SDK](http://xg.qq.com/ctr_index/download) 。

## 注册测试应用
注册测试应用的名称不限，但是包名必须为 com.qq.xgdemo ，并获取注册完整过后应用对应的 ACCESSID 和 ACCESSKEY 。
>注意 ：
>如果包名不一致推送的时候需要勾选多包名推送。

![](https://main.qcloudimg.com/raw/5953bfa11a6fbf60fb1dddb3c00719e8.png)
## 配置工程

### Android Studio 工程

需要将获取到的测试应用的 ACCESSID 和 ACCESSKEY 配置到 Demo 工程 App 模块下的 build.gradle 文件下的ManifestPlaceholders 节点。如图所示：

![](https://main.qcloudimg.com/raw/ac1dc3a4d212781138c5d4840c6c5bbd.png)

### Eclipse 工程

需要将获取到的测试应用的 ACCESSID 和 ACCESSKEY 配置到 Demo 工程中的 AndroidManifest.xml 文件下的节点下。

![](https://main.qcloudimg.com/raw/eb3b760d5b7c013e0f360d6d0ba6116c.png)

## 运行代码

如果出现如下日志则说明信鸽注册成功。(日志 tag：“ TPush ”)：

```
10-09 20:08:46.922 24290-24303/com.qq.xgdemo I/XINGE: [TPush] get RegisterEntity:RegisterEntity [accessId=2100250470, accessKey=null, token=5874b7465d9eead746bd9374559e010b0d1c0bc4, packageName=com.qq.xgdemo, state=0, timestamp=1507550766, xgSDKVersion=3.11, appVersion=1.0]
10-09 20:08:47.232 24290-24360/com.qq.xgdemo D/TPush: 注册成功，设备token为：5874b7465d9eead746bd9374559e010b0d1c0bc4
```
## 推送测试
获取日志输出的设备token。通过信鸽web端的应用管理中创建推送。如下图所示

![](https://main.qcloudimg.com/raw/039180137ff4776e4dfcaf53e72ee9b8.png)