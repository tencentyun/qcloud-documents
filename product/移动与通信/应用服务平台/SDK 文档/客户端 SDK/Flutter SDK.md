## Flutter 插件

CloudBase Flutter SDK 提供一系列插件，可以根据场景按需安装。

| Plugin                             | Version                        | 文档                               | 描述
| ---------------------------------- | ------------------------------ | ---------------------------------- | ----------------------
| [cloudbase_core][core_pub]         | ![pub package][core_badge]     | [CloudBase Core][core_doc]         | 核心库，初始化环境等
| [cloudbase_auth][auth_pub]         | ![pub package][auth_badge]     | [CloudBase Auth][auth_doc]         | 鉴权库，支持微信登录、自定义登录、匿名登录等
| [cloudbase_function][function_pub] | ![pub package][function_badge] | [CloudBase Function][function_doc] | 支持云函数能力
| [cloudbase_storage][storage_pub]   | ![pub package][storage_badge]  | [CloudBase Storage][storage_doc]   | 支持对象存储能力
| [cloudbase_database][database_pub]   | ![pub package][database_badge]  | [CloudBase Database][database_doc]   | 支持文档型数据库能力

[core_pub]: https://pub.dartlang.org/packages/cloudbase_core
[auth_pub]: https://pub.dartlang.org/packages/cloudbase_auth
[function_pub]: https://pub.dartlang.org/packages/cloudbase_function
[storage_pub]: https://pub.dartlang.org/packages/cloudbase_storage
[database_pub]: https://pub.dartlang.org/packages/cloudbase_database
[core_badge]: https://main.qcloudimg.com/raw/8764115ed2dc882cf9d45e5b8f331ef8.svg
[auth_badge]: https://main.qcloudimg.com/raw/00ce58ec8f140a3b3ca9d786d1b90c2d.svg
[function_badge]: https://main.qcloudimg.com/raw/609869527fd1f38401bc42679c7bfa60.svg
[storage_badge]: https://main.qcloudimg.com/raw/02f620a770ab4dec3dc37d82f14761dd.svg
[database_badge]: https://main.qcloudimg.com/raw/01ab88e435b490caccc36c57810bda54.svg
[core_doc]: https://docs.cloudbase.net/api-reference/flutter/initialization.html
[auth_doc]: https://docs.cloudbase.net/api-reference/flutter/authentication.html
[function_doc]: https://docs.cloudbase.net/api-reference/flutter/functions.html
[storage_doc]: https://docs.cloudbase.net/api-reference/flutter/storage.html
[database_doc]: https://docs.cloudbase.net/api-reference/flutter/database.html

## 安装

在 flutter 项目的 `pubspec.yaml` 文件的 `dependencies` 中添加需要的插件，例如：

```yaml
dependencies:
  cloudbase_core: ^0.0.9
  cloudbase_auth: ^0.0.11
  cloudbase_function: ^0.0.2
  cloudbase_storage: ^0.0.3
  cloudbase_database: ^0.0.10
```

然后在命令行中运行。

```bash
flutter pub get
```

## 开发文档

* [安装](https://docs.cloudbase.net/api-reference/flutter/install.html)

* [初始化](https://docs.cloudbase.net/api-reference/flutter/initialization.html)

* [登录认证](https://docs.cloudbase.net/api-reference/flutter/authentication.html)

* [云函数](https://docs.cloudbase.net/api-reference/flutter/functions.html)

* [数据库](https://docs.cloudbase.net/api-reference/flutter/database.html)

* [文件存储](https://docs.cloudbase.net/api-reference/flutter/storage.html)

