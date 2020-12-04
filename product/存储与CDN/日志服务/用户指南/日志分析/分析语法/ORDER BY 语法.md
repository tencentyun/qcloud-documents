

`ORDER BY`语句用于根据指定的 KEY 对结果集进行排序。
`ORDER BY`语句默认按照升序对记录进行排序。
如果您希望按照降序对记录进行排序，可以使用`DESC`关键字。

## ORDER BY 语法格式

```plaintext
ORDER BY  列名（KEY） [ DESC | ASC ]
```

## ORDER BY 语法样例

统计不同访问状态并降序排列：

```plaintext
*|SELECT status, COUNT(status) AS c GROUP BY status ORDER BY c DESC
```
