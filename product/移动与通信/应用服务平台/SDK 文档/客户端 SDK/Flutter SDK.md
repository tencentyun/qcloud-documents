## Flutter 插件

CloudBase Flutter SDK 提供一系列插件，可以根据场景按需安装。
<table>
<tr>
<th>Plugin</th>
<th>Version</th>
<th>文档</th>
<th>描述</th>
</tr>
<tr>
<td><a href = "https://pub.dartlang.org/packages/cloudbase_core">cloudbase_core</a></td>
<td><img src = "https://main.qcloudimg.com/raw/8764115ed2dc882cf9d45e5b8f331ef8.svg"  data-nonescope="true" style = "width:98%;"></td>
<td><a href = "https://docs.cloudbase.net/api-reference/flutter/initialization">CloudBase Core</a></td>
<td>核心库，初始化环境等</td>
</tr>
<tr>
<td><a href = "https://pub.dartlang.org/packages/cloudbase_auth">cloudbase_auth</a></td>
<td><img src = "https://main.qcloudimg.com/raw/00ce58ec8f140a3b3ca9d786d1b90c2d.svg"  data-nonescope="true" style = "width:98%;"></td>
<td><a href = "https://docs.cloudbase.net/api-reference/flutter/authentication">CloudBase Auth</a></td>
<td>鉴权库，支持微信登录、自定义登录、匿名登录等</td>
</tr>
<tr>
<td><a href = "https://pub.dartlang.org/packages/cloudbase_function">cloudbase_function</a></td>
<td><img src = "https://main.qcloudimg.com/raw/609869527fd1f38401bc42679c7bfa60.svg"  data-nonescope="true" style = "width:98%;"></td>
<td><a href = "https://docs.cloudbase.net/api-reference/flutter/functions">CloudBase Function</a></td>
<td>支持云函数能力</td>
</tr>
<tr>
<td><a href = "https://pub.dartlang.org/packages/cloudbase_storage">cloudbase_storage</a></td>
<td><img src = "https://main.qcloudimg.com/raw/02f620a770ab4dec3dc37d82f14761dd.svg"  data-nonescope="true" style = "width:98%;"></td>
<td><a href = "https://docs.cloudbase.net/api-reference/flutter/storage">CloudBase Storage</a></td>
<td>支持对象存储能力</td>
</tr>
<tr>
<td><a href = "https://pub.dartlang.org/packages/cloudbase_database">cloudbase_database</a></td>
<td><img src = "https://main.qcloudimg.com/raw/01ab88e435b490caccc36c57810bda54.svg"  data-nonescope="true" style = "width:98%;"></td>
<td><a href = "https://docs.cloudbase.net/api-reference/flutter/database">CloudBase Database</a></td>
<td>支持文档型数据库能力</td>
</tr>
</table>


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

* [安装](https://docs.cloudbase.net/api-reference/flutter/install)

* [初始化](https://docs.cloudbase.net/api-reference/flutter/initialization)

* [登录认证](https://docs.cloudbase.net/api-reference/flutter/authentication)

* [云函数](https://docs.cloudbase.net/api-reference/flutter/functions)

* [数据库](https://docs.cloudbase.net/api-reference/flutter/database)

* [文件存储](https://docs.cloudbase.net/api-reference/flutter/storage)

