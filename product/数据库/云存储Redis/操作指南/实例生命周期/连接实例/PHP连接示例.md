**运行前必备**：

下载客户端 [phpredis](https://github.com/phpredis/phpredis)。

**示例代码**：

```
<?php
  /**以下参数分别填写您的Redis实例内网IP，端口号，实例ID和密码*/
  $host = "192.168.0.2";
  $port = 6379;
  $instanceid = "c532952f-55dc-4c22-a941-63057e560788";
  $pwd = "1234567q";

  $redis = new Redis();
  //连接Redis
  if ($redis->connect($host, $port) == false) {
    die($redis->getLastError());
  }
  //鉴权
  if ($redis->auth($instanceid . ":" . $pwd) == false) {
    die($redis->getLastError());
  }
  
  /**接下来可以开始操作Redis实例，可以参考：https://github.com/phpredis/phpredis */
  
  //设置Key
  if ($redis->set("redis", "tencent") == false) {
    die($redis->getLastError());
  }
  echo "set key redis suc, value is:tencent\n";
  
  //获取Key
  $value = $redis->get("redis");
  echo "get key redis is:".$value."\n";
?>
```



**运行结果**：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/PHP-1.jpg)
