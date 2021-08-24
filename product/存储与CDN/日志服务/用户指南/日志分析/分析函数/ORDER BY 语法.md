本文介绍 ORDER BY 语法的使用及示例。

ORDER BY 语法用于根据指定的列名对查询和分析结果表示排序。

## 语法格式

```
ORDER BY 列名 [DESC | ASC]
```

>?
> - 您可以指定多个列名，按照不同的排序方式排序。例如 ORDER BY 列名1[DESC | ASC]，列名2[DESC | ASC]。
> - 如果您未配置关键字 DESC 或 ASC，则系统默认对查询和分析结果进行升序排列。
> - 当排序的目标列中存在相同的值时，每次排序结果可能不同。如果您希望每次序列结果相同，可指定多列进行排序。
> 

参数说明如下表所示：

| 参数 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| 列名 | 列名即为日志字段名称或聚合函数计算结果列，即支持按照日志字段名称（KEY）或聚合函数计算结果列进行排序。 |
| DESC | 降序排列。                                                   |
| ASC  | 升序排列。                                                   |


## 示例

- 统计不同请求状态的数量，并按照请求数量降序排列。
```
* | SELECT status, count(*) AS pv GROUP BY status ORDER BY pv DESC
```
- 计算各服务器的平均请求时间，并按照请求时间进行升序排列。
```
* | SELECT remote_addr, avg(request_time) as request_time group by remote_addr order by request_time ASC LIMIT 10
```
![image-20210719000006781](https://main.qcloudimg.com/raw/c1a051779bc0cd4ce801dc8e9f4edeb5.png)























