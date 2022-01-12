
## 运算符
运算符是进行算术或逻辑运算的操作。

### 算数运算符
- **a + b**：返回 a 与 b 的和。
- **a - b**：返回 a 与 b 的差。
- **a * b**：返回 a 与 b 的积。
- **a / b**：返回 a 与 b 的商。
- **a % b**：返回 a 与 b 的模。该操作符一般仅在 a 与 b 是整数时有效。
- **-a**：返回 a 的相反数。

### 比较运算符
- **a == b**：如果 a 与 b 类型与值都相等则返回 true，否则返回 false。
- **a != b**：与 == 相反。
- **a < b**：如果 a 比 b 小则为 true，否则为 false。
- **a > b**：如果 a 比 b 大则为 true，否则为 false。
- **a <= b**：如果 a 比 b 小或者相等则为 true，否则为 false。
- **a >= b**：如果 a 比 b 大或者相等则为 true，否则为 false。


### 逻辑运算符
- **a || b**：a 或 b 中有至少一个为 true 则为 true，否则为 false。
- **a && b**：a 与 b 都为 true 则为 true，否则为 false。
- **!a**：如果 a 为 true 则为 false，如果 a 为 false 则为 true。


## 条件表达式
条件表达式是判断一个布尔表达式的结果，以便于在后续两个值当中选择一个。例如：
```bash
condition ? one_value : two_value
```


## FOR 表达式
FOR 表达式可用来遍历一组集合，并将一种集合类型映射为另一种类型。例如：
```bash
[for item in items : upper(item)]
```


## 展开表达式
展开表达式是一种类似 for 表达式的简洁表达方式。例如：
```bash
[for o in var.list : o.id]
等价于
var.list[*].id
```

## 函数表达式
Terraform 支持在计算表达式时使用一些内建函数，函数调用表达式类似操作符。例如：
```bash
upper("123")
```
