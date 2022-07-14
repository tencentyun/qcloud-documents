
运算符是一个保留字或字符，主要用于指定 SQL语句中的条件，并在语句中连接多个条件。

- [算术运算符](#.E7.AE.97.E6.9C.AF.E8.BF.90.E7.AE.97.E7.AC.A6)
- [比较运算符](#.E6.AF.94.E8.BE.83.E8.BF.90.E7.AE.97.E7.AC.A6)
- [逻辑运算符](#.E9.80.BB.E8.BE.91.E8.BF.90.E7.AE.97.E7.AC.A6)

## 算术运算符

算术运算符是用来处理四则运算的符号，是最简单最常用的符号，尤其是数字的处理，几乎都会使用到算术运算符号。

假设变量 a=1，变量 b=2，则：

| 运算符 | 描述                                          | 示例  |
| ------ | --------------------------------------------- | ----- |
| +      | 加法：运算符两边的值相加                      | a + b |
| -      | 减法：运算符左边减去运算符右边                | a - b |
| *      | 乘法 - 把运算符两边的值相乘                   | a * b |
| /      | 除法 -   运算符左边除以运算符右边             | b / a |
| %      | 取模 -   运算符左边除以运算符右边后得到的余数 | b % a |

## 比较运算符

比较运算符用于判断值的大小关系，支持任何可比较的类型，例如 int、long、double 和 text 等。

假设变量 a=1，变量 b=2，则：

| 运算符 | 描述                                                         | 示例              |
| :----- | :----------------------------------------------------------- | :---------------- |
| =      | 判断运算符两边的值是否相等，如果相等则条件为真。             | a = b             |
| !=     | 判断运算符两边的值是否相等，如果不相等则条件为真。           | a != b            |
| <>     | 判断运算符两边的值是否相等，如果不相等则条件为真。           | a <> b            |
| >      | 判断运算符左边的值是否大于运算符右边的值，如果是则条件为真。 | a > b |
| <      | 判断运算符左边的值是否小于运算符右边的值，如果是则条件为真。 | a < b   |
| >=     | 判断运算符左边的值是否大于等于运算符右边的值，如果是则条件为真。 | a >= b |
| <=     | 判断运算符左边的值是否小于等于运算符右边的值，如果是则条件为真。 | a <= b   |
| IN      | IN 运算符用于把某个值与一系列指定列表的值进行比较。          |  status IN (200,206,404) |
| NOT IN  | IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。 | status NOT IN (200,206,404)  |
| BETWEEN AND | BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。 | status between 200 AND 400 |
| LIKE    | LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。%代表零个、一个或者多个字；\_代表单个数字或者字符。  | url LIKE '%.mp4' |
| IS NULL | NULL 运算符用于把某个值与 NULL 值进行比较，为空为真。 | status IS NULL |
| IS NOT NULL | NULL 运算符用于把某个值与 NULL 值进行比较，不为空为真。 | status IS NOT NULL |
| DISTINCT   | 语法：`x IS DISTINCT FROM y` 或 `x IS NOT DISTINCT FROM y`。</br>用于对比 x 和 y 是否相等，与&lt;&gt;的差异在于 DISTINCT 可用于对 null 的比较，详见 [<> 与 DISTINCT 运算符差异](#DISTINCT)。    | NULL IS NOT DISTINCT FROM NULL   |
| LEAST   | 语法：`LEAST(x, y...)`  </br>返回 x,y...中的最小值。    | LEAST(1,2,3)   |
| GREATEST   | 语法：`GREATEST(x, y...)`  </br>返回 x,y...中的最大值。   | 	GREATEST(1,2,3)   |
| ALL   |  语法：`x expression operator ALL ( subquery ) `  </br>x 满足所有条件时，返回 true，operator 支持`<、>、<=、>=、=、<>、!=`。   | 示例1：21 < ALL (VALUES 19, 20, 21) </br>示例2：* \| SELECT 200 = ALL(SELECT status)   |
| ANY / SOME   | 	语法：`x expression operator ANY ( subquery )` 或 `x expression operator SOME ( subquery )`  </br>x 满足任意一个条件时，返回 true，operator 支持`<、>、<=、>=、=、<>、!=`。    | 示例1：'hello' = ANY (VALUES 'hello', 'world') </br>示例2：* \| SELECT 200 = ANY(SELECT status)   |


<span id="DISTINCT"></span>
&lt;&gt; 与 DISTINCT 运算符差异：

| x | y | 	x = y | x <> y | x IS DISTINCT FROM y | x IS NOT DISTINCT FROM y |
|---------|---------|---------|---------|---------|---------|
| 1 | 1 | true | false | false | true |
| 1 | 2 | false | true | true | false |
| 1 | null | null | null | true | false |
| null | null | null | null | false | true |


## 逻辑运算符

| 运算符  | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| AND     | AND 运算符要求运算符两边条件同时存在为真。                   |
| OR      | OR 运算符要求运算符两边任一条件存在即为真。                  |
| NOT     | NOT 运算符是所用的逻辑运算符的对立面。例如 NOT EXISTS、NOT BETWEEN、NOT IN 等。 |
