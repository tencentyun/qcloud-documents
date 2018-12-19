>Note: Before accessing Cloud Memcached, be sure to read [Cloud Memcached (Originally Called NoSQL Fast Storage) Use Limits](/doc/product/241/限制说明).

## 1 About the Client

1. Use open-source synchronous client to access Cloud Memcached service
Cloud Memcached is a distributed system and does not support asynchronous client.

(1) If you need to use PHP based client, it is recommended to use the memcache extension 2.2.6: ([memcache-2.2.6](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/memcache-2.2.6.zip)), which is proved to be realized by using synchronous I/O model.

(2) If you need to use Java based client, it is recommended to use this one: [memcached-java-2.5.1](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/memcached-java-2.5.1.zip).

(3) If you need to use clients based on other languages, refer to [This](https://code.google.com/archive/p/memcached/downloads).

2 Socket connection timeout Limits for Cloud Memcached

If the client does not have any access requests for 180 seconds since the last access, the connection is automatically terminated. Therefore, the client should send at least one access request every 180 seconds. Current open-source clients don't check connection liveness so users need to handle this on their own.

## 2 Accessing Cloud Memcached Service

1. Acquire the IP:Port of the Cloud Memcached you wish to access

Log in to Tencent Cloud and go to Management Center, click "Cloud Memcached" and view the IP:Port assigned by the system in the "Management View" of Cloud Memcached.
This IP:Port is used to access the Cloud Memcached service.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Nosql_access_2.png)

2. Implement code to achieve Cloud Memcached service access

For code implementation, see [Development Manual](http://www.php.net/manual/zh/book.memcache.php) (example is based on PHP).
