## 环境及依赖
环境：在腾讯云 CVM 上安装对应的 [Apache](http://www.apache.org/dyn/closer.cgi)、[PHP](http://php.net/downloads.php)，建议使用较新版本 Apache2.0+、PHP Version 5.3+。

依赖：安装 [PHP-Memcache-3.0.6+](http://php.net/manual/zh/book.memcache.php) 或者 [PHP-Memcached-1.0.2+](http://php.net/manual/zh/book.memcached.php) 扩展。

[PHP-memcache GitHub 源码](https://github.com/tricky/php-memcache)
[PHP-memcached GitHub 源码](https://github.com/php-memcached-dev/php-memcached)

## 使用步骤
在腾讯云 CVM 上部署好 Apache+PHP 环境并安装好 PHP-Memcache 或者 PHP-Memcached 扩展。
编写测试代码并运行。

## 代码示例 PHP-Memcache
[GitHub 代码参考](https://github.com/tricky/php-memcache/blob/master/example.php)

```
<?php
$cache = new Memcache;//新建一个memcache连接实例
$cache->connect('***.***.***.***', ****);//连接到指定的cmem服务器IP和端口
$key = "php-key";
$cache->set($key, "value1". time());//向cmem写入一个key
$val = $cache->get($key);//向cmem获取一个key
var_dump ($val);
$cache->close();
?>
```

## 代码示例 PHP-Memcached
[GitHub 代码参考](https://github.com/php-memcached-dev/php-memcached/blob/master/server-example/test-server.php)

```
<?php
$memcached = new Memcached;//新建一个memcache连接实例
$memcached->setOption(Memcached::OPT_COMPRESSION, false); //关闭压缩功能
$memcached->setOption(Memcached::OPT_BINARY_PROTOCOL, false); //关闭二进制协议
$memcached->addServer("***.***.***.***", ****);//添加cmem服务器，指定cmem服务器IP和端口
$key = "php-key";
$memcached->set($key, "value-1-".time());//向cmem写入一个key
$val = $memcached->get($key);//向cmem获取一个key
var_dump ($val);
$memcached->quit();
?>
```
