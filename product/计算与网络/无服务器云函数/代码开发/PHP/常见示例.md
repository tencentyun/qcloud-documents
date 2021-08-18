常见示例中包含了 PHP 环境下可以试用的相关代码片段，您可以根据需要选择尝试。示例均基于 PHP 7.2 环境提供。

您可以从 GitHub 项目 [scf-php-code-snippet](https://github.com/awesome-scf/scf-php-code-snippet) 中获取相关代码片段并直接部署。

## 环境变量读取

本示例提供了获取全部环境变量列表，或单一环境变量值的方法。示例如下：

```php
<?php
function main_handler($event, $context) {
    print_r($_ENV);
    echo getenv('SCF_RUNTIME');
    return "hello world";
}
?> 
```

## 本地时间格式化输出

本示例提供了时间格式化输出方法，按指定格式进行日期和时间输出。

SCF 环境默认是 UTC 时间，如果期望按北京时间输出，可以为函数添加 `TZ=Asia/Shanghai` 环境变量，并在函数代码中通过`date_default_timezone_set(getenv('TZ'));` 设置需要使用的时区。示例如下：

```php
<?php
function main_handler($event, $context) {
    date_default_timezone_set(getenv('TZ'));
    echo date("Y-m-d H:i:s",time()); 
    return "hello world";
}
?> 
```

## 函数内发起网络连接

```php
<?php
function main_handler($event, $context) {
    $url = 'https://cloud.tencent.com';
    echo file_get_contents($url);
    return "hello world";
}
?> 
```
