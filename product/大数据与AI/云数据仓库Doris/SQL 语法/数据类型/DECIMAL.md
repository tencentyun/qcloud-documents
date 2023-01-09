## 描述
DECIMAL(M[,D])：
- 高精度定点数，M 代表一共有多少个有效数字(precision)，D 代表小数位有多少数字(scale)。
- 有效数字 M 的范围是 [1, 27]，小数位数字数量 D 的范围是 [0, 9]，整数位数字数量的范围是 [1, 18]，M 必须要大于等于 D 的取值。
- 默认值为 DECIMAL(9, 0)。

## 示例
创建表时指定字段类型为 DECIMAL。
```sql
CREATE TABLE `tbl` (
  `mykey` int(11) NULL COMMENT "",
  `mydecimal` decimal(10, 4) NOT NULL DEFAULT "0.0" COMMENT ""
) ENGINE=OLAP
DUPLICATE KEY(`mykey`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`mykey`) BUCKETS 3;
```
