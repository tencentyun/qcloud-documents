## LIKE
```
string LIKE pattern [ESCAPE escape-character]
string NOT LIKE pattern [ESCAPE escape-character]
```
如果该 string 匹配了提供的 pattern，那么 LIKE 表达式返回真（和预期的一样，如果 LIKE 返回真，那么 NOT LIKE 表达式返回假，反之亦然。
一个等效的表达式是 NOT (string lIKE pattern)。
示例：
```
postgres=# SELECT 'abc' LIKE 'abc';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' LIKE 'a%';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' LIKE '_b_';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' LIKE 'c';
 ?column? 
----------
 f
(1 row)
```

## SIMILAR TO 正则表达式
```
string SIMILAR TO pattern [ESCAPE escape-character]
string NOT SIMILAR TO pattern [ESCAPE escape-character]
```
SIMILAR TO 操作符根据自己的模式是否匹配给定串而返回真或者假。它和 LIKE 非常类似，只不过它使用 SQL 标准定义的正则表达式理解模式。

SIMILAR 除了从 LIKE 借用的功能外，还支持下面这些从 POSIX 正则表达式借用的模式匹配元字符：
- | 表示选择（两个候选之一）。
- `*` 表示重复前面的项零次或更多次。
- `+` 表示重复前面的项一次或更多次。
- ? 表示重复前面的项零次或一次。
- {m} 表示重复前面的项刚好 m 次。
- {m,} 表示重复前面的项 m 次或更多次。
- {m,n} 表示重复前面的项至少 m 次并且不超过 n 次。
- 可以使用圆括号 () 把多个项组合成一个逻辑项。
- 一个方括号表达式 [...] 声明一个字符类，就像 POSIX 正则表达式一样。
- 注意点号（.）不是 SIMILAR TO 的一个元字符。

示例：
```
postgres=# SELECT 'abc' SIMILAR TO 'abc';
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' SIMILAR TO 'a';
 ?column? 
----------
 f
(1 row)
 
postgres=# SELECT 'abc' SIMILAR TO '%(b|d)%';
 ?column? 
----------
 t
(1 row)
```

## POSIX 正则表达式
POSIX 正则表达式比 LIKE 和 SIMILAR TO 操作符更强大。
POSIX 正则表达式匹配操作符：

| **操作符** | **描述**                       |
| ---------- | ------------------------------ |
| ~          | 匹配正则表达式，大小写敏感     |
| ~*         | 匹配正则表达式，大小写不敏感   |
| !~         | 不匹配正则表达式，大小写敏感   |
| !~*        | 不匹配正则表达式，大小写不敏感 |

示例：
```
postgres=# SELECT 'abc' ~ 'abc' ;
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' ~ '^a' ;
 ?column? 
----------
 t
(1 row)
 
postgres=# SELECT 'abc' ~ '^(b|c)';
 ?column? 
----------
 f
(1 row)
```
