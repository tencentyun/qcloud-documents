## 准备工作

1. 拥有腾讯云账号；
2. [创建云开发环境](https://cloud.tencent.com/document/product/876/41391)，获得 **环境 ID**（目前仅支持上海地域环境）；
3. 安装 [Flutter](https://flutter.cn/docs/get-started/install)。

## 步骤1：创建 Flutter 项目

```sh
flutter create cloudbase_demo
cd cloudbase_demo
```

## 步骤2：添加 CloudBase 插件依赖

在项目的 `pubspec.yaml` 文件中添加 `dependencies` 。

```yaml
dependencies:
  cloudbase_core: ^0.0.9
  cloudbase_auth: ^0.0.11
```

从 `pub` 安装依赖。

```sh
flutter pub get
```

## 步骤3：创建移动应用安全来源的凭证

打开 [安全设置页面](https://console.cloud.tencent.com/tcb/env/safety) 中，在移动应用安全来源里**添加应用**。

<img src="https://main.qcloudimg.com/raw/1c088bc3ddb41faad995d2a8c43186e4.png">

>? 因为 Flutter 是跨端开发框架, 所以需要为 Android 和 iOS 各申请一个应用凭证。 应用标识应该是 Android 包名 和 iOS Bundle ID。

## 步骤4：开启匿名登录

在 [环境设置页面](https://console.cloud.tencent.com/tcb/env/setting) 中，单击“登录方式”，然后**启用匿名登录**：

<img src="https://main.qcloudimg.com/raw/0b6a93991575776761137e9558aed3fc.png">

## 步骤5：初始化环境并调用匿名登录

在项目的 `lib/main.dart` 文件中初始化环境并进行匿名登录。

```dart
import 'package:cloudbase_core/cloudbase_core.dart';
import 'package:cloudbase_auth/cloudbase_auth.dart';

void main() async {
  // 初始化 CloudBase
  CloudBaseCore core = CloudBaseCore.init({
      // 填写您的云开发 env
      'env': 'your-env-id',
      // 填写您的移动应用安全来源凭证
      // 生成凭证的应用标识必须是 Android 包名或者 iOS BundleID
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
}
```

>? 初始化 CloudBase 时用到的 `appAccess` 参数可以从控制台的安全来源凭证模块中获取。
> 
> <img src="https://main.qcloudimg.com/raw/434baba046148be1d2a0effc444ec0f8.png">

登录成功后，便可以访问和使用云开发的各类资源，详情请参见 Flutter SDK 文档。

- [初始化](https://docs.cloudbase.net/api-reference/flutter/initialization)
- [登录认证](https://docs.cloudbase.net/api-reference/flutter/authentication)
- [云函数](https://docs.cloudbase.net/api-reference/flutter/functions)
- [数据库](https://docs.cloudbase.net/api-reference/flutter/database)
- [文件存储](https://docs.cloudbase.net/api-reference/flutter/storage)
