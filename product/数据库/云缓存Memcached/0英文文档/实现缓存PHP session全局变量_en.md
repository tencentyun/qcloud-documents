## 1. Usage Scenarios

Session is commonly used in WEB programs, whose data is stored in the form of a file. It has a limited processing capacity in scenarios with large access volume. Memcache is a memory-based Key=>Value storage system with high performance, which can significantly improve the capacity of session processing.

## 2. Use PHP-Memcache extension

You can modify configuration file or cache data in the program.

1. Modify php.ini configuration file.
Modify the storage method of session
session.save_handler = memcache
Modify the storage address of session. Replace *** in the code with your IP:Port. In the console, click "Cloud Memcached", and you can see IP:Port assigned by the system in "Management View".
session.save_path = "tcp://***.***.***.***:****"
Set a reasonable length of time and cache hotspot data only
session.gc_maxlifetime = 1500

2. Directly make configurations in the code. For more information, please see [[here](http://cn.php.net/manual/en/memcache.ini.php)].
ini_set("session.save_handler","memcache");
ini_set("session.save_path","tcp://***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);

## 3. Use PHP-Memcached extension

You can modify configuration file or cache data in the program. Unlike memcache, tcp:// is not appended to the beginning of IP.
1. Modify php.ini configuration file.
Modify the storage method of session
session.save_handler = memcached
Modify the storage address of session. Replace *** in the code with your IP:Port. In the console, click "Cloud Memcached", and you can see IP:Port assigned by the system in "Management View".
session.save_path = "***.***.***.***:****"
Set a reasonable length of time and cache hotspot data only
session.gc_maxlifetime = 1500
2. Directly make configurations in the code. For more information, please see [[here](http://cn.php.net/manual/en/memcache.ini.php)].
ini_set("session.save_handler","memcached");
ini_set("session.save_path","***.***.***.***:****");
ini_set("session.gc_maxlifetime",1500);
