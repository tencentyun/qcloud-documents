## 准备工作

1. 拥有腾讯云账号；
2. [创建云开发环境](https://cloud.tencent.com/document/product/876/41391)，获得 **环境 ID**；
3. 安装 [Flutter](https://flutter.cn/docs/get-started/install)。

## 第 1 步：创建 Flutter 项目

```shell
flutter create cloudbase_demo
cd cloudbase_demo
```

## 第 2 步：添加 CloudBase 插件依赖

在项目的 `pubspec.yaml` 文件中添加 `dependencies` 。

```yaml
dependencies:
  cloudbase_core: ^0.0.4
  cloudbase_auth: ^0.0.4
```

从 `pub` 安装依赖。

```shell
flutter pub get
```

## 第 3 步：创建移动应用安全来源的凭证

打开[安全设置页面](https://console.cloud.tencent.com/tcb/env/setting?tab=safetyConfig)中，在移动应用安全来源里**添加应用**. 

<img src="https://main.qcloudimg.com/raw/1c088bc3ddb41faad995d2a8c43186e4.png">

>? 因为 Flutter 是跨端开发框架, 所以需要为 Android 和 iOS 各申请一个应用凭证。 应用标识应该是 Android包名 和 iOS Bundle ID。

## 第 4 步：开启匿名登录

在[环境设置页面](https://console.cloud.tencent.com/tcb/env/setting)中，点击“登录方式”，然后**启用匿名登录**：

<img src="https://main.qcloudimg.com/raw/0b6a93991575776761137e9558aed3fc.png">

## 第 5 步：初始化环境并调用匿名登录

在项目的 `lib/main.dart` 文件中初始化环境并进行匿名登录。

```dart
import 'package:cloudbase_core/cloudbase_core.dart';
import 'package:cloudbase_auth/cloudbase_auth.dart';

// 初始化 CloudBase
CloudBaseCore core = CloudBaseCore.init({
    // 填写您的云开发 env
    'env': 'your-env-id',
    // 填写您的移动应用安全来源凭证
    // 这里应该判断平台，来填写对应的凭证
    'appAccess': {
      // 凭证
      'key': 'your-app-access-key',
      // 版本
      'version': 'your-app-access-version'
    }
});

// 获取登录状态
CloudBaseAuth auth = CloudBaseAuth(core);
CloudBaseAuthState authState = await auth.getAuthState();

// 唤起匿名登录
if (authState == null) {
  await auth.signInAnonymously().then((success) {
    // 登录成功
    print(success);
  }).catchError((err) {
    // 登录失败
    print(err);
  });
}
```

登录成功后，便可以访问和使用云开发的各类资源，详情请参看 Flutter SDK 文档

* [初始化](https://docs.cloudbase.net/api-reference/flutter/initialization.html)
* [登录认证](https://docs.cloudbase.net/api-reference/flutter/authentication.html)
* [云函数](https://docs.cloudbase.net/api-reference/flutter/functions.html)
* [数据库](https://docs.cloudbase.net/api-reference/flutter/database.html)
* [文件存储](https://docs.cloudbase.net/api-reference/flutter/storage.html)