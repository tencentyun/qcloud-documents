LIMIT 语法用于限制输出结果的行数。

## 语法格式

- 读取前 N 行：
```
limit N
```
- 从第 S 行开始读，读取 N 行：
```
offset S limit N
```


## 语法示例

- 获取10行结果：
```
* | select status, count(*) as pv group by status limit 10
```
- 获取第3行到第42行的结果，共计40行：
```
* | select status, count(*) as pv group by status offset 2 limit 40
```



## 限制说明

<table>
	<tr><th>指标</th><th>限制说明</th><th>	备注</th></tr>
	<tr><td>SQL 结果条数</td><td>SQL 返回结果条数最大10000条</td><td>limit 默认100，最大10000</td></tr>
</table>

