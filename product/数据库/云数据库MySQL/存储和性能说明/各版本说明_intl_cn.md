## 1 高IO版本
### 1.1 购买说明
2015年6月15日，全新高IO版本发布，性能10倍提升。
国内广州地域全量发布，用户新购云数据库默认发货高IO版。
国内上海地域灰度发布，用户可通过白名单方式购买高IO版，白名单申请地址：http://manage.qcloud.com/cdb/apply.php 
香港和北美地域暂不支持高IO版。

高IO云数据库购买页面如下图所示：
![](//mccdn.qcloud.com/img568280339e902.png)

### 1.2 高IO云数据库性能说明

详见： [高IO版性能说明](http://www.qcloud.com/doc/product/236/%E5%90%84%E7%89%88%E6%9C%AC%E6%80%A7%E8%83%BD%E8%AF%B4%E6%98%8E#2-高io版性能说明)

##  2. 高性能版
云数据库高性能版是腾讯云针对MySQL类业务运营的需求，新研发出来的一种高性能和高可靠的MySQL服务平台。
通过分布式存储提高单机存储的IO能力，从而提高单MySQL实例数据库的查询性能；通过多个节点存储多份数据副本的方式来保证数据库数据的安全可靠。高性能版兼容标准版实例管理、统计等功能。在使用上高性能版和标准版保持完全一致。特别适合对单MySQL实例性能要求较高、对数据安全要求较高的应用。

### 2.1 基本架构

高性能版数据存储通过云存储来完成最终数据落地，基本架构如下图所示：
![](//mccdn.qcloud.com/img568281130fbe2.png)

### 2.2 其它功能

双机热备，故障恢复，数据冷备，监控统计等功能，与现有标准版保持一致（详见这里）

### 2.3 限制说明

#### 2.3.1 InnoDB存储格式

对于InnoDB存储引擎，高性能版默认使用DYNAMIC格式。建议用户不要自行修改，以免影响使用。

#### 2.3.2 支持的最大并发事务数

目前支持的最大并发事务数为1000。

#### 2.3.3 InnoDB支持的记录行内最大长度

高性能版InnoDB的支持记录行内最大长度为1982个字节；超过该值，会出现如下错误：

```
ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 1982. You have to change some columns to TEXT or BLOBs 
```

## 3 标准版总体架构说明

### 3.1 双机热备及故障恢复

标准版通过MySQL的Replication特性提供双机热备支持，master和slave各自部署在一台独立的高性能存储机器上，存储机器使用的SAS磁盘阵列提供数据的可靠存储。如下图所示：

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-1.png)

MySQL客户端并不直接连接master和slave，而是通过接入模块转发。因此当master出现故障时，可将请求自动切换到slave。实现故障时的无缝切换。如下图所示：

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-2.png)

当master出现故障，请求切换到slave后，可以自动启动迁移流程，将数据迁移到另外一对master、slave机器上，完成迁移后，通过在中转模块将请求切换到新的master、slave机器，实现迁移对客户端透明。如下图所示：

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-3.png)

### 3.2 数据冷备

云数据库每天会对数据进行备份，保存在后台的冷备中心。冷备数据保留4天，可以帮助业务恢复到前5天的数据。如果用户需要提取冷备数据，详见云数据库冷备数据提取。

### 3.3 全面的监控和统计功能

云数据库提供了磁盘IO、网络流量、CPU使用情况、连接、查询、慢查询、主从同步、数据备份等多个维度的关键数据的监控和统计,详见监控服务。


建议用户尽量减小记录行内的存储长度。比如，尽量将varchar的字段长度声明为256或者以上（这样字段会行外存储），或者使用text/blob代替。且text\blob\varchar字段总共不能超过48个 

### 3.4 InnoDB不支持compressed

高性能版为了提高性能，采用O_DIRECT方式进行IO，同时调整了innodb引擎的页和磁盘扇区的大小，由于系统限制，无法使用compress格式.
