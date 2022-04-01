TCB 提供开发应用所需服务和基础设施。tcb-php-sdk 让您可以在服务端（如腾讯云云函数或 CVM 等）使用 PHP  服务访问 TCB 的的服务。

需要 php7 及以上版本。

<dx-alert infotype="notice" title="">
PHP SDK 目前尚不支持广州地域，请使用上海地域。
</dx-alert>


## 安装

使用 [composer](https://getcomposer.org/) 安装 CloudBase PHP SDK：
<dx-codeblock>
:::  sh
composer require tcb-php-sdk
:::
</dx-codeblock>

<dx-alert infotype="explain" title="">
国内使用时，可切换为国内镜像：
<dx-codeblock>
:::  sh
composer config -g repo.packagist composer https://packagist.phpcomposer.com
:::
</dx-codeblock>
</dx-alert>

## API 文档

- [介绍](https://docs.cloudbase.net/api-reference/server/php/introduction)

- [应用初始化](https://docs.cloudbase.net/api-reference/server/php/initialization)

- [数据库](https://docs.cloudbase.net/api-reference/server/php/database)

- [云函数](https://docs.cloudbase.net/api-reference/server/php/functions)

- [存储](https://docs.cloudbase.net/api-reference/server/php/storage)

- [云函数引入 php-sdk 快速教程](https://docs.cloudbase.net/api-reference/server/php/tutorial)
