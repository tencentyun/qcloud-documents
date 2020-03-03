**Preparations before running**:

Use the client phpredis and download it at https://github.com/phpredis/phpredis

**Sample Codes**:

```
<?php
  /**Input your Redis instance's private IP, port number, instance ID and password for the following fields*/
  $host = "192.168.0.2";
  $port = 6379;
  $instanceid = "c532952f-55dc-4c22-a941-63057e560788";
  $pwd = "1234567q";

  $redis = new Redis();
  //Connect to Redis
  if ($redis->connect($host, $port) == false) {
    die($redis->getLastError());
  }
  //Authentication
  if ($redis->auth($instanceid . ":" . $pwd) == false) {
    die($redis->getLastError());
  }
  
  /**Then start to work with the Redis instance by referring to https://github.com/phpredis/phpredis */
  
  //Set the key
  if ($redis->set("redis", "tencent") == false) {
    die($redis->getLastError());
  }
  echo "set key redis suc, value is:tencent\n";
  
  //Get the key
  $value = $redis->get("redis");
  echo "get key redis is:".$value."\n";
?>
```



**Execution results**:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/PHP-1.jpg)
