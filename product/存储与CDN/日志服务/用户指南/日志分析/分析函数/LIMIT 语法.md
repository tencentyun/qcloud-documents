本文介绍 LIMIT 语法的使用及示例。

LIMIT 语法用于限制输出结果的行数。

>? 当前 CLS 函数仅支持重庆地域使用。其他地域如有需要，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。
>

## 语法格式

日志服务支持以下一种 LIMIT 语法格式。

- 只读取前 N 行：
```
limit N
```
- 从第 S 行开始读，读取 N 行：
```
offset S limit N
```
>?
> - limit 翻页读取时，只用于获取最终的结果，不可用于获取 SQL 中间的结果。
> - 不支持将 limit 语法用于子查询内部。例如：
>```
* | select sum(pv) from 
(
select count(1) as pv from log group by status 
)
```
> 

## 示例

- 只获取10行结果：
```
* | select status, count(*) as pv group by status limit 10
```
- 获取第2行到第42行的结果，共计41行：
```
* | select * from log order by ip offset 2 limit 40
```

