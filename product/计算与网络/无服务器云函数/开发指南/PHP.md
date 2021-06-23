目前支持的 PHP 开发语言包括如下版本：
- PHP 5.6
- PHP 7.2

## 函数形态

PHP 函数形态一般如下所示：
```
<?php

function main_handler($event, $context) {
    echo("hello world");
    print_r($event);
    return "hello world";
}

?>
```

## 执行方法

在创建 SCF 云函数时，均需要指定执行方法。使用 PHP 开发语言时，执行方法类似 `index.main_handler`，此处 `index`表示执行的入口文件为 `index.php` ，`main_handler` 表示执行的入口函数为 `main_handler` 函数。在使用 本地 zip 文件上传、COS 上传等方法提交代码 zip 包时，请确认 zip 包的根目录下包含有指定的入口文件，文件内有定义指定的入口函数，文件名和函数名和执行方法处填写的能够对应，避免因为无法查找到入口文件和入口函数导致的执行失败。

## 入参

PHP 环境下的入参包括 $event 、$context。
- $event：使用此参数传递触发事件数据。
- $context：使用此参数向您的处理程序传递运行时信息。

## 返回和异常

您的处理程序可以使用 `return` 来返回值，根据调用函数时的调用类型不同，返回值会有不同的处理方式。
- 同步调用：使用同步调用时，返回值会序列化后以 JSON 的格式返回给调用方，调用方可以获取返回值来进行后续处理。例如通过控制台进行的函数调试的调用方法就是同步调用，能够在调用完成后捕捉到函数返回值并显示。
- 异步调用：异步调用时，由于调用方法仅触发函数就返回，不会等待函数完成执行，因此函数返回值会被丢弃。

同时，无论同步调用还是异步调用，返回值均会在函数日志中 `ret_msg` 位置显示。
在函数中，可以通过调用 die() 退出函数。此时函数会被标记为执行失败，同时日志中也会记录使用 die() 退出时的输出。

## 日志
您可以在程序中使用如下语句来完成日志输出：
- echo 或 echo()
- print 或 print()
- print_r()
- var_dump()

输出内容您可以在函数日志中的 `log` 位置查看。

## 已安装扩展

如下列出目前已安装的 PHP 扩展：
- date
- libxml
- openssl
- pcre
- sqlite3
- zlib
- bcmath
- bz2
- calendar
- ctype
- curl
- dom
- hash
- fileinfo
- filter
- ftp
- SPL
- iconv
- json
- mbstring
- session
- standard
- mysqlnd
- PDO
- pdo_mysql
- pdo_sqlite
- Phar
- posix
- Reflection
- mysqli
- SimpleXML
- soap
- sockets
- exif
- tidy
- tokenizer
- xml
- xmlreader
- xmlwriter
- zip
- eio
- protobuf
- Zend OPcache
- mongodb
- memcached 
- redis 
- gd2 
- ImageMagick 
- imagick
- swoole (PHP7)

您也可以随时在函数中通过 `print_r(get_loaded_extensions());` 代码打印查看已安装的扩展。

## 更多指引
您可参考以下文档，使用相关功能：
- [使用 SCF 连接数据库](<https://cloud.tencent.com/document/product/583/38012>)
- [网络配置管理](<https://cloud.tencent.com/document/product/583/38202>)
- [角色与授权](<https://cloud.tencent.com/document/product/583/32389>)
