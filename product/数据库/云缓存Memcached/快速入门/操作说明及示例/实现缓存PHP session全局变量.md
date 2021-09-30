
## 使用场景
Session 是 Web 程序中常用的功能，默认情况下其数据是以文件方式存储，对大访问量的场景，其处理能力较低。Memcache 是高性能的基于内存的 Key=>Value 存储系统，能大大改善处理 session 的能力。

## 使用 PHP-Memcache 扩展的实现方法
可以使用修改配置文件或者在程序中实现两种方式。

1. 修改 php.ini 配置文件实现。
修改 session 存储方式。
`session.save_handler = memcache`
修改 session 存储地址，`***`号替换为您的 IP:Port，在 [Memcached 控制台](https://console.cloud.tencent.com/memcached) 可以查看系统分配的 IP:Port。
`session.save_path = "tcp://***.***.***.***:****"`
设置一个合理时间，只缓存热点数据。
`session.gc_maxlifetime = 1500`

2. 代码中直接设置，可参考 [memcache](http://cn.php.net/manual/en/memcache.ini.php)。
```
ini_set("session.save_handler","memcache");
ini_set("session.save_path","tcp://***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);
```

## 使用 PHP-Memcached 扩展的实现方法
可以使用修改配置文件或者在程序中实现两种方式，与 memcache 不同在于其 IP 前没有 tcp://。

1. 修改 php.ini 配置文件实现。
修改 session 存储方式。
`session.save_handler = memcached`
修改 session 存储地址，`***`号替换为您的 IP:Port，在 [Memcached 控制台](https://console.cloud.tencent.com/memcached) 可以查看系统分配的 IP:Port。
`session.save_path = "***.***.***.***:****"`
设置一个合理时间，只缓存热点数据。
`session.gc_maxlifetime = 1500`

2. 代码中直接设置，可参考 [memcache](http://cn.php.net/manual/en/memcache.ini.php)。
```
ini_set("session.save_handler","memcached");
ini_set("session.save_path","***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);
```
