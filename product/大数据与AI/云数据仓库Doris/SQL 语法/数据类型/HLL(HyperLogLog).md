## 描述
- HLL 不能作为 key 列使用，建表时配合聚合类型为 HLL_UNION。
- 用户不需要指定长度和默认值。长度根据数据的聚合程度系统内控制。
- HLL 列只能通过配套的 hll_union_agg、hll_raw_agg、hll_cardinality、hll_hash 进行查询或使用。
- HLL 是模糊去重，在数据量大的情况性能优于 Count Distinct。
- HLL 的误差通常在1%左右，有时会达到2%。

## 示例
```sql
CREATE TABLE `tbl` (
  `mykey` int NULL COMMENT "",
  `myhll` hll HLL_UNION NULL COMMENT ""
) ENGINE=OLAP
AGGREGATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;

select HLL_UNION_AGG(`myhll`) from `tbl`;
```


