

AS 子句用于为列名称（KEY）指定别名。

## AS 语法格式

```sql
*|SELECT 列名（KEY） AS  别名
```

## AS 语法样例

#### 创建中文别名：
```sql
*|SELECT remote_addr AS "客户端IP", request_time AS "请求时间(单位：秒)" 
```
>!如果别名中包含中文或其他特殊字符，需要使用双引号。


#### 统计访问次数：
```sql
*|SELECT COUNT(*) AS PV
```




