**����ǰ�ر�**��

ʹ�ÿͻ���phpredis�����غͲο���ַ��https://github.com/phpredis/phpredis

**ʾ������**��

```
<?php
  /**���²����ֱ���д����redisʵ������IP���˿ںţ�ʵ��id������*/
  $host = "192.168.0.2";
  $port = 6379;
  $instanceid = "c532952f-55dc-4c22-a941-63057e560788";
  $pwd = "1234567q";

  $redis = new Redis();
  //����redis
  if ($redis->connect($host, $port) == false) {
    die($redis->getLastError());
  }
  //��Ȩ
  if ($redis->auth($instanceid . ":" . $pwd) == false) {
    die($redis->getLastError());
  }
  
  /**�������������Ŀ�ʼ����redisʵ�������Բο���https://github.com/phpredis/phpredis */
  
  //����key
  if ($redis->set("redis", "tencent") == false) {
    die($redis->getLastError());
  }
  echo "set key redis suc, value is:tencent\n";
  
  //��ȡkey
  $value = $redis->get("redis");
  echo "get key redis is:".$value."\n";
?>
```



**���н��**��
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/PHP-1.jpg)