Principle of Online Expansion of Cloud Memcached
1. Cloud Memcached will be automatically expanded to ensure that user instances always have 20% available space. This is to prevent the business from being damaged due to the read-only status of cache instance. Single instance theoretically has no capacity limit.
2. When an instance needs to be expanded, you will first check the remaining space of the storage machines where the instance currently resides in are available for expansion. If so, the operation will be performed directly; otherwise, extra storage machines are required.
![](https://mc.qcloudimg.com/static/img/4692f2ea5543260503f453de0dfa4917/mem.png)
