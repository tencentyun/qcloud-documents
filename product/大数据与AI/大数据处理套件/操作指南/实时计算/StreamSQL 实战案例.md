前置条件：sql 使用的所有非临时表必须事先定义好，并且测试通过，否则在任务运行过程会有异常抛出。
## 案例1：星级游戏实时指标统计
### 需求描述
实时统计多款星级游戏的注册人数。每款游戏的日志数据记录在各自的注册流水表，以 1 分钟为单位实时统计每款游戏的注册人数，并将结果数据写入到用户指定结果数据表。 目前对以下 4 款游戏进行计算：御龙在天，英雄联盟。
### 实现方案
首先对每一款游戏的各个指标分别进行统计，然后将每款游戏相同的结果指标通过 UNION 的方式合并并存储结果表。完整的 sql 如下：

```
with(select "ylzt" bname, iUin qqid, dtEventTime agtime from ylzt_dsl_createrole_fht0) ylzt_cr, 
(select "lol" bname, iUin qqid, dtEventTime agtime from lol_dsl_createrole_fht0) lol_cr, 
(select "bns" bname, iUin qqid, dtEventTime agtime from bns_dsl_createrole_fht0) bns_cr, 
(select "nizhan" bname, iUin qqid, dtEventTime agtime from nizhan_dsl_createrole_fht0) nizhan_cr
insert into rtc_idata_createrole_m select from_unixtime(AGGRTIME DIV 1000, 'yyyyMMddHHmm') vdatetime_m, bname vgame, count(qqid) from (select bname, qqid, agtime from ylzt_cr union all select bname, qqid, agtime from lol_cr union all select bname, qqid, agtime from bns_cr union all select bname, qqid, agtime from nizhan_cr) utbl group by bname coordinate by agtime*1000 with aggr interval 60 seconds
```
1. 在上述 sql 中，首先对每个表选出需要使用的字段。对于目前的需求，只用到 iUin 和 dtEventTime 字段，因此将这两个字段选出来。同理，对于收入流水表，选出收入相关字段。
> 要点：这段sql中使用了with语法，将一段子查询逻辑抽象出来作为临时表，以供后面的逻辑使用。

2. 将每款游戏的数据 UNION 到一起，然后进行聚合统计。首先从上一段 sql 中的临时表中把每个游戏的注册信息进行 UNION，然后进行聚合统计计算，最后将数据写入目标表。Group by bname 定义了聚合分组字段为 bname，coordinate by 定义了时间协调坐标，这里要求一个毫秒数，而 agtime 是源数据表中定义的 dtEventTime 字段是一个秒数，所以这里乘以 1000。Aggr interval 60 seconds 表示聚合粒度为 1 分钟。Count(qqid) 以及 sum(m) 就是聚合统计。另外AGGRTIME 是一个系统关键字，表示聚合时间的毫秒数，并且是 aggr interval 的整数倍。这个字段只有在当前查询（子查询）中包含 group by 时才有意义，否则使用这个关键字会报错。

## 案例2：累加聚合和滑动窗口聚合
### 需求描述
假定某款业务需要按照如下规则进行实时统计： 每1分钟进行一次数据统计，输出当前分钟的登录人数，当前小时截止到当前分钟的登录人数，截止到当前分钟的连续30分钟的登录人数。
### 实现方案
使用累加聚合和滑动窗口聚合两种方法来实现。完整的 sql 如下：

```
INSERT INTO dest SELECT appId, count(qq), count(qq ACCU), count(qq SW) 
FROM src 
GROUP BY appId  
COORDINATE BY dTime WITH AGGR INTERVAL 60 SECONDS WITH ACCU INTERVAL 3600 SECONDS WITH SW INTERVAL 1800 SECONDS 
```
说明：在 sql 中通过 WITH AGGR INTERVAL 60 SECONDS 指定聚合窗口为 1 分钟，通过 WITH ACCU INTERVAL 3600 SECONDS 指定累加聚合窗口为 1 小时，通过 WITH SW INTERVAL 1800 SECONDS 指定滑动窗口为 30 分钟。 Count(qq) 表示当前分钟的计数，count（qq ACCU) 表示当前小时截止到当前分钟的计数，count(qq SW) 表示当前分钟及向前 30 分钟的滑动窗口计数。

## 案例3：关联纬表实时指标统计
### 需求描述
1. 实时计算微信在不同国家和地区，不同的设备的连接数和平均连接耗时。微信连接数据中，每条记录包含一个连接 IP，连接设备类型（Android，ios），连接耗时等信息。
2. 存在一张 IP 表，包含 IP 段到地区的映射关系（纬表）。
3. 要求按照 1 分钟的统计粒度计算每个国家每种设备的连接数和平均连接耗时。

### 实现方案
对于每条数据首先针对 IP 通过纬表关联的方式从 IP 表中读取纬表中的国家和地区信息，然后按照国家和设备进行聚合统计。完整的 SQL 如下：

```
INSERT INTO weixin_res_meta 
SELECT from_unixtime(AGGRTIME DIV 1000, 'yyyyMMddHHmm'), ttt.Device_, ip_table.country_id, 
COUNT(1), avg(CostTimeref_) FROM (SELECT Device_, CostTimeref_, CAST ((ClientIP_ - ClientIP_ % 256) AS STRING) AS ipstr 
FROM log_10410 WHERE Funid_='138') ttt LEFT JOIN ip_table ON ttt.ipstr = ip_table.ipint GROUP BY ttt.Device_, ip_table.country_id 
COORDINATE BY TimeStamp_*1000 WITH AGGR INTERVAL 60 SECONDS
```
