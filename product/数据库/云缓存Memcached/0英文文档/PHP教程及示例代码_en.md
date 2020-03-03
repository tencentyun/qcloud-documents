## 1. Environment and dependency
Environment: Install [[Apache](http://www.apache.org/dyn/closer.cgi)] and [[PHP](http://php.net/downloads.php)] on Tencent Cloud CVM. It is recommended to use new versions, Apache2.0+ and PHP Version 5.3+.

Dependency  Install [[PHP-Memcache-3.0.6+](http://php.net/manual/zh/book.memcache.php)] or [[PHP-Memcached-1.0.2+](http://php.net/manual/zh/book.memcached.php)] extension.

[[php-memcache GitHub source code](https://github.com/tricky/php-memcache)]
[[php-memcached GitHub source code](https://github.com/php-memcached-dev/php-memcached)]
## 2. Steps

Deploy Apache+PHP environment and install PHP-Memcache or PHP-Memcached extension on Tencent Cloud CVM.

Write the test code and run.

## 3. Sample code: PHP-Memcache

[[GitHub code reference]](https://github.com/tricky/php-memcache/blob/master/example.php)

```
<?php
$cache = new Memcache;//Create a memcache connection instance
$cache->connect('***.***.***.***', ****);//Connect it to the specified cmem server IP and port
$key = "php-key";
$cache->set($key, "value1". time());//Write a key into cmem
$val = $cache->get($key);//Obtain a key from cmem
var_dump ($val);
$cache->close();
?>
```
## 4. Sample code: PHP-Memcached

[[GitHub code reference]](https://github.com/php-memcached-dev/php-memcached/blob/master/server-example/test-server.php)

```
<?php
$memcached = new Memcached;//Create a memcache connection instance
$memcached->setOption(Memcached::OPT_COMPRESSION, false); //Disable the compression feature
$memcached->setOption(Memcached::OPT_BINARY_PROTOCOL, false); //Disable Binary protocol
$memcached->addServer("***.***.***.***", ****);//Add cmem server, and specify cmem server IP and port
$key = "php-key";
$memcached->set($key, "value-1-".time());//Write a key into cmem
$val = $memcached->get($key);//Obtain a key from cmem
var_dump ($val);
$memcached->quit();
?>
```
