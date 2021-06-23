常用的逻辑操作符有：AND，OR，NOT，结果包括真，假和 null，null 表示“未知”。运算规则如下：

| **a** | **b** | **a AND b** | **a OR b** | **NOT a** |
| ----- | ----- | ----------- | ---------- | --------- |
| TRUE  | TRUE  | TRUE        | TRUE       | FALSE     |
| TRUE  | FALSE | FALSE       | TRUE       | FALSE     |
| TRUE  | NULL  | NULL        | TRUE       | FALSE     |
| FALSE | FALSE | FALSE       | FALSE      | TRUE      |
| FALSE | NULL  | FALSE       | NULL       | TRUE      |
| NULL  | NULL  | NULL        | NULL       | NULL      |
