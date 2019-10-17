
云开发 tcb-manager-php SDK 支持开发者通过接口形式对云开发提供的云函数、数据库、文件存储资源进行创建、管理、配置等操作。更多源码内容请参见 [tcb-manager-php SDK](https://github.com/TencentCloudBase/tcb-manager-php)。

### 安装

云开发 tcb-manager-php SDK 的安装方式有两种，通过 composer 安装和手动安装源码包。

- 通过 composer 安装（推荐使用）：
  具体安装步骤请参见 [官方说明文档](https://getcomposer.org/doc/00-intro.md)。

```bash
composer require tencentcloudbase/tcb-manager-php
```

- 手动安装源码包：
    1. 前往 [源码仓库](https://github.com/TencentCloudBase/tcb-manager-php) 下载源码包。
    2. 将源码包放到项目合适的目录。

### 引入

如果项目使用 composer 管理依赖，则会自动引入，可跳过此步骤。

```php
require_once "/path/to/tcb-manager-php/autoload.php"
```

引用 SDK 后即可使用，SDK 命名空间为 TcbManager。
