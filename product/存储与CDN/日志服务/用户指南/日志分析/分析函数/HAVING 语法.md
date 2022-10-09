HAVING 用于对分组聚合后的数据进行过滤，与 [WHERE](https://cloud.tencent.com/document/product/614/44075) 的区别在于其作用于分组（GROUP BY）之后，排序（ORDER BY）之前，而 WHERE 作用于聚合前的原始数据。

## 语法格式

```
* | SELECT 列名, 聚合函数 GROUP BY [ 列名 | 别名 | 序号 ] HAVING 聚合函数 运算符 值
```

运算符可以是`=`、`<>`、`>`、`<`、`>=`、`<=`、`BETWEEN`、`IN`、`LIKE`。

## 语法示例

统计平均响应耗时大于1000ms的 URL，并按耗时倒排：
```
* | 
select 
  avg(responseTime) as time_avg, 
  URL 
group by 
  URL 
having 
  avg(responseTime)> 1000 
order by 
  avg(responseTime) desc 
limit 
  10000
```

由于过滤条件为各个 URL 的平均响应耗时，属于聚合后的结果，因此不能使用 [WHERE](https://cloud.tencent.com/document/product/614/44075) 进行数据过滤。

