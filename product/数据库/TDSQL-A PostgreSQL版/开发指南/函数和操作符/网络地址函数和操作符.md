## cidr 和 inet 操作符
cidr 和 inet 类型支持如下操作符：

| **操作符** | **描述**         |
| ---------- | ---------------- |
| <          | 小于             |
| <=         | 小于等于         |
| =          | 等于             |
| >=         | 大于等于         |
| >          | 大于             |
| <>         | 不等于           |
| <<         | 被包含在内       |
| <<=        | 被包含在内或等于 |
| >>         | 包含             |
| >>=        | 包含或等于       |
| &&         | 包含或被包含     |
| ~          | 按位 NOT          |
| &          | 按位 AND          |
| \|         | 按位 OR           |
| +          | 加               |
| -          | 减               |

示例：
```
postgres=# SELECT inet '192.168.1.5' <= inet '192.168.1.5';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT inet '192.168.1.5' << inet '192.168.1/24';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT inet '192.168.1/24' && inet '192.168.1.80/28';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT inet '192.168.1.6' + 25;
  ?column? 
--------------
 192.168.1.31
(1 row)
 
postgres=# SELECT inet '192.168.1.6' & inet '0.0.0.255';
 ?column? 
----------
 0.0.0.6
(1 row)
```

## cidr 和 inet 函数
| **函数**                         | **返回类型** | **描述**                         |
| -------------------------------- | ------------ | -------------------------------- |
| abbrev(inet)                   | text         | 缩写显示格式文本                 |
| abbrev(cidr)                   | text         | 缩写显示格式文本                 |
| broadcast(inet)                | inet         | 网络广播地址                     |
| family(inet)                   | int          | 抽取地址族：4为 IPv4，6为 IPv6 |
| host(inet)                     | text         | 抽取 IP 地址为文本               |
| hostmask(inet)                 | inet         | 为网络构造主机掩码               |
| masklen(inet)                  | int          | 抽取网络掩码长度                 |
| netmask(inet)                  | inet         | 为网络构造网络掩码               |
| network(inet)                  | cidr         | 抽取地址的网络部分               |
| set_masklen(inet, int)       | inet         | 为 inet 值设置网络掩码长度       |
| set_masklen(cidr, int)       | cidr         | 为 cidr 值设置网络掩码长度       |
| text(inet)                     | text         | 抽取 IP 地址和网络掩码长度为文本 |
| inet_same_family(inet, inet) | bool         | 地址是否来自同一个地址族         |
| inet_merge(inet, inet)       | cidr         | 最小的网络包括给定的两个网络     |

示例：
```
postgres=# SELECT abbrev(inet '10.1.0.0/16');
  abbrev  
-------------
 10.1.0.0/16
(1 row) 

postgres=# SELECT family('::1');
 family 
--------
   6
(1 row)
 
postgres=# SELECT hostmask('192.168.23.20/30');
 hostmask 
----------
 0.0.0.3

(1 row)
 
postgres=# SELECT set_masklen('192.168.1.5/24', 16);
 set_masklen 
----------------
 192.168.1.5/16
(1 row)
 
postgres=# SELECT netmask('192.168.1.5/24');
  netmask  
---------------
 255.255.255.0
(1 row)
```
更多网络地址函数和操作符及示例，可参考 [官网](http://www.postgres.cn/docs/10/functions-net.html)。
