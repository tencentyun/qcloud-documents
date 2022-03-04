本文主要介绍如何快速运行腾讯云 IM Demo（Unity）。

## 环境要求

| 平台 | 版本 | 
|---------|---------|
| Unity | 2019.4.15f1 及以上版本。 | 
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤


[](id:step1)
### 步骤1：创建 IM 应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://main.qcloudimg.com/raw/78340e403359fcf4d753ade29ae9aace.png)
3. 左侧导航栏单击 **[辅助工具](https://console.cloud.tencent.com/im-detail/tool-usersig)** > **UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，在 [步骤5](#step5) 中使用。
![](https://qcloudimg.tencent-cloud.cn/raw/aa6c33f0430f87f788f42dcde92f7094.png)

[](id:step2)
### 步骤2：创建 Unity 项目
通过 Unity，创建一个 Unity 项目，并记住项目所在的位置。
![](https://qcloudimg.tencent-cloud.cn/raw/f07ae1bb4db4ca5f43f6acc563aafa8c.png)

[](id:step3)
### 步骤3：修改依赖文件
1. 通过 IDE（如：Visual Studio Code）打开项目：
![](https://qcloudimg.tencent-cloud.cn/raw/4ea52e320700dc37770a5405ac14d1a7.jpg)
2. 根据目录，找到 Packages/manifest.json，并修改依赖如下：
```json
{
	"dependencies":{
    "com.tencent.imsdk.unity":"1.6.4" // 指定到最新版本即可,所有版本：https://www.npmjs.com/package/com.tencent.imsdk.unity
  },
  "registry": "https://registry.npmjs.org"
}
```

[](id:step4)
### 步骤4：加载依赖
在 Unity Editor 中打开项目，等候依赖加载完毕，确认Tencent Cloud IM 已经加载完成。
![](https://qcloudimg.tencent-cloud.cn/raw/d98dfb17bbee6c0319e370de6f2ba9dd.jpg)

[](id:step5)
### 步骤5：测试脚本
1. 您可 [下载测试脚本](https://imgcache.qq.com/operation/dianshi/other/Demo.1fdc6bd474aa3d12f0f3061155d4a5accdf30c7b.zip
)，将文件解压后，放入项目中，并绑定 TestApi.cs 到任意场景上。
![](https://qcloudimg.tencent-cloud.cn/raw/b4d770775523fdd76b75f1d80f07c925.jpg)
2. 选中场景并运行，配置 [步骤1](#step1) 中的 SDKAppID，UserID，UserSig 开始测试。
![](https://qcloudimg.tencent-cloud.cn/raw/940da8044cd80db27d08a7b0dff45b94.png)

## 常见问题

### 支持哪些平台？
目前支持 iOS、Android、Windows 和 Mac。

### Android 单击 Build And Run 报错找不到可用设备？
确保设备没被其他资源占用，或单击 Build 生成 apk 包，再拖动进模拟器里运行。

### iOS 第一次运行报错？
按照上面的 Demo 运行配置后，如果报错，可以单击**Product**>**Clean**，清除产物后重新 Build，或者关闭 Xcode 重新打开再次 Build。
### 2019.04版 Unity，iOS 平台报错？
Library/PackageCache/com.unity.collab-proxy@1.3.9/Editor/UserInterface/Bootstrap.cs(23,20): error CS0117: 'Collab' does not contain a definition for 'ShowChangesWindow'
在 Editor 工具栏单击**Window**>**Package Manager**，将 Unity Collaborate 降级到1.2.16。

### 2019.04版 Unity，iOS 平台报错？
Library/PackageCache/com.unity.textmeshpro@3.0.1/Scripts/Editor/TMP_PackageUtilities.cs(453,84): error CS0103: The name 'VersionControlSettings' does not exist in the current context
打开源码，把`|| VersionControlSettings.mode != "Visible Meta Files"`这部分代码删除即可。
