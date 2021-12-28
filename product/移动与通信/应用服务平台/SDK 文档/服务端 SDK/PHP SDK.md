TCB 提供开发应用所需服务和基础设施。tcb-php-sdk 让你可以在服务端（如腾讯云云函数或 CVM 等）使用 php 服务访问 TCB 的的服务。

需要 php7 及以上版本。

:::caution
PHP SDK 目前尚不支持广州地域，请使用上海地域。
:::

## 安装

使用 [composer](https://getcomposer.org/) 安装 CloudBase PHP SDK：

```sh
composer require tcb-php-sdk
```

> ? 国内使用时，可切换为国内镜像:
>
> ```sh
> composer config -g repo.packagist composer https://packagist.phpcomposer.com
> ```

## API 文档

- [介绍](https://docs.cloudbase.net/api-reference/server/php/introduction.html)

- [应用初始化](https://docs.cloudbase.net/api-reference/server/php/initialization.html)

- [数据库](https://docs.cloudbase.net/api-reference/server/php/database.html)

- [云函数](https://docs.cloudbase.net/api-reference/server/php/functions.html)

- [存储](https://docs.cloudbase.net/api-reference/server/php/storage.html)

- [云函数引入 php-sdk 快速教程](https://docs.cloudbase.net/api-reference/server/php/tutorial.html)
