## 使用场景
Session是Web程序中常用的功能，默认情况下其数据是以文件方式存储，对大访问量的场景，其处理能力较低。Memcache是高性能的基于内存的Key=>Value存储系统，能大大改善处理session的能力。

## 使用PHP-Memcache扩展的实现方法
可以使用修改配置文件或者在程序中实现两种方式。

1. 修改php.ini配置文件实现。
修改session存储方式。
`session.save_handler = memcache`
修改session存储地址，`***`号替换为您的IP:Port，在 [Memcached 控制台](https://console.cloud.tencent.com/memcached) 可以查看系统分配的IP:Port。
`session.save_path = "tcp://***.***.***.***:****"`
设置一个合理时间，只缓存热点数据
`session.gc_maxlifetime = 1500`

2. 代码中直接设置，可参考 [memcache](http://cn.php.net/manual/en/memcache.ini.php)。
```
ini_set("session.save_handler","memcache");
ini_set("session.save_path","tcp://***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);
```


## 使用PHP-Memcached扩展的实现方法
可以使用修改配置文件或者在程序中实现两种方式，与memcache不同在于其IP前没有tcp://。

1. 修改php.ini配置文件实现。
修改session存储方式。
`session.save_handler = memcached`
修改session存储地址，`***`号替换为您的IP:Port，在 [Memcached 控制台](https://console.cloud.tencent.com/memcached) 可以查看系统分配的IP:Port。
`session.save_path = "***.***.***.***:****"`
设置一个合理时间，只缓存热点数据。
`session.gc_maxlifetime = 1500`

2. 代码中直接设置，可参考 [memcache](http://cn.php.net/manual/en/memcache.ini.php)。
```
ini_set("session.save_handler","memcached");
ini_set("session.save_path","***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);
```
