## 描述
- BITMAP 不能作为 key 列使用，建表时配合聚合类型为 BITMAP_UNION。
- 用户不需要指定长度和默认值。长度根据数据的聚合程度系统内控制。并且 BITMAP 列只能通过配套的 bitmap_union_count、bitmap_union、bitmap_hash 等函数进行查询或使用。
- 离线场景下使用 BITMAP 会影响导入速度，在数据量大的情况下查询速度会慢于 HLL，并优于 Count Distinct。
>! 实时场景下 BITMAP 如果不使用全局字典，使用了 bitmap_hash()可能会导致有千分之一左右的误差。

## 示例
1. 创建表时指定字段类型为 bitmap。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mybitmap` bitmap BITMAP_UNION NULL COMMENT ""
) ENGINE=OLAP
AGGREGATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
2. 利用 bitmap 计算 pv 和 uv。
```sql
select hour, BITMAP_UNION_COUNT(pv) over(order by hour) uv from(
   select hour, BITMAP_UNION(device_id) as pv
   from metric_table -- 查询每小时的累计UV
   where datekey=20200622
group by hour order by 1
) final;
```
