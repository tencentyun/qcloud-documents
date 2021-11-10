列出命名表的表属性。
## 语法
```
SHOW TBLPROPERTIES table_name [('property_name')]
```
## 参数 
`[('property_name')]`：如果包含，则只列出属性 name 和 value 值。

## 示例
```
SHOW TBLPROPERTIES tb1;
```
```
SHOW TBLPROPERTIES orders('tb1');
```
