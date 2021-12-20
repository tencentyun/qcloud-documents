本文介绍逻辑运算的语法和示例。

### 逻辑运算符

| 运算符 | 描述                                     | 示例    |
| ------ | ---------------------------------------- | ------- |
| AND    | 只有左右运算数都是 TRUE 时，结果才为 TRUE。 | a AND b |
| OR     | 左右运算数任一个为 TRUE 时，结果为 TRUE。   | a OR b  |
| NOT    | 右侧运算数为 FALSE 时，结果才为 FALSE。     | NOT a   |

### 与 NULL 相关的逻辑运算
a 和 b 分别取值 TRUE，FALSE 和 NULL 时的真值表如下：

#### AND，OR 的真值表

| a     | b     | a AND b | a OR b |
| ----- | ----- | ------- | ------ |
| TRUE  | TRUE  | TRUE    | TRUE   |
| TRUE  | FALSE | FALSE   | TRUE   |
| TRUE  | NULL  | NULL    | TRUE   |
| FALSE | TRUE  | FALSE   | TRUE   |
| FALSE | FALSE | FALSE   | FALSE  |
| FALSE | NULL  | FALSE   | NULL   |
| NULL  | TRUE  | NULL    | TRUE   |
| NULL  | FALSE | FALSE   | NULL   |
| NULL  | NULL  | NULL    | NULL   |

#### NOT 的真值表

| a     | NOT a |
| ----- | ----- |
| TRUE  | FALSE |
| FALSE | TRUE  |
| NULL  | NULL  |

