## 描述
- QUANTILE_STATE 不能作为 key 列使用，建表时配合聚合类型为 QUANTILE_UNION。
- 用户不需要指定长度和默认值。长度根据数据的聚合程度系统内控制。
- QUANTILE_STATE 列只能通过配套的 QUANTILE_PERCENT、QUANTILE_UNION、TO_QUANTILE_STATE 等函数进行查询或使用。
- QUANTILE_STATE 是一种计算分位数近似值的类型，在导入时会对相同的 key，不同 value 进行预聚合，当 value 数量不超过2048时采用明细记录所有数据，当 value 数量大于2048时采用 [TDigest](https://github.com/tdunning/t-digest/blob/main/docs/t-digest-paper/histo.pdf) 算法，对数据进行聚合（聚类）保存聚类后的质心点。

## 相关函数
#### QUANTILE_UNION(QUANTILE_STATE)
此函数为聚合函数，用于将不同的分位数计算中间结果进行聚合操作。此函数返回的结果仍是QUANTILE_STATE

#### TO_QUANTILE_STATE(INT/FLOAT/DOUBLE raw_data [,FLOAT compression])
此函数将数值类型转化成 QUANTILE_STATE 类型。
- compression参数是可选项，可设置范围是[2048, 10000]，值越大，后续分位数近似计算的精度越高，内存消耗越大，计算耗时越长。 
- compression参数未指定或设置的值在[2048, 10000]范围外，以2048的默认值运行

#### QUANTILE_PERCENT(QUANTILE_STATE)
此函数将分位数计算的中间结果变量（QUANTILE_STATE）转化为具体的分位数数值

## 示例
```sql
select QUANTILE_PERCENT(QUANTILE_UNION(v1)) from test_table group by k1, k2, k3;
```
    

