本文主要介绍如何从零开始创建一个 Flutter 项目并初始化环境。

### 准备工作
1. 注册 [腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Flvb)，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 参考 [开通环境](https://cloud.tencent.com/document/product/876/41391) 创建云开发环境，获得 环境 ID。
3. 参考 [Flutter 官网](https://flutter.cn/docs/get-started/install) 开发文档安装 Flutter。

### 步骤1： 开启匿名登录
在腾讯云控制台 - 云开发 - [环境设置页面](https://console.cloud.tencent.com/tcb/env/setting) 中，单击“登录方式”，然后启用匿名登录：
![](https://main.qcloudimg.com/raw/00fc7e367e87a28f488c8b2e247cac90.png)

### 步骤2： 创建 Flutter 项目
```
$ flutter create cloudbase_demo
$ cd cloudbase_demo
```

### 步骤3： 添加 CloudBase 插件依赖
在项目的 pubspec.yaml 文件中添加 dependencies。
```
dependencies:
  cloudbase_core: ^0.0.4
  cloudbase_auth: ^0.0.4
```

从 pub 安装依赖。
```
$ flutter pub get
```

### 步骤4： 初始化环境并调用匿名登录
在项目的 `lib/main.dart` 文件中初始化环境并进行匿名登录。
```
import 'package:cloudbase_core/cloudbase_core.dart';
import 'package:cloudbase_auth/cloudbase_auth.dart';

// 初始化 CloudBase
CloudBaseCore core = CloudBaseCore.init({
    // 填写您的云开发 env
    'env': 'your-env-id'
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

登录成功后，便可以访问和使用云开发的各类资源，详情请参阅 Flutter SDK 文档：

- [登录授权](https://cloud.tencent.com/document/product/876/41618)。
- [云函数](https://cloud.tencent.com/document/product/876/41619)。
- [数据库](https://cloud.tencent.com/document/product/876/43487)。
- [文件存储](https://cloud.tencent.com/document/product/876/41620)。

