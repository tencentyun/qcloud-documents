
**运行前必备**：
下载客户端 [phpredis](https://github.com/phpredis/phpredis)。

**示例代码**：
```
<?php
  /**以下参数分别填写您的 Tendis 实例内网 IP、端口号、实例 ID 和密码*/
  $host = "192.xx.xx.2";
  $port = 6379;
  $pwd = "123tj6na";

  $redis = new Redis();
  //连接 Tendis
  if ($redis->connect($host, $port) == false) {
    die($redis->getLastError());
  }
  //鉴权
  if ($redis->auth($pwd) == false) {
    die($redis->getLastError());
  }

  /**接下来可以开始操作 Tendis 实例，可以参考 https://github.com/phpredis/phpredis */

  //设置 Key
  if ($redis->set("redis", "tencent") == false) {
    die($redis->getLastError());
  }
  echo "set key redis suc, value is:tencent\n";

  //获取 Key
  $value = $redis->get("redis");
  echo "get key redis is:".$value."\n";
?>
```

**运行结果**：
![](https://main.qcloudimg.com/raw/62e281a52fd9e18178866e70236c6755.jpg)
