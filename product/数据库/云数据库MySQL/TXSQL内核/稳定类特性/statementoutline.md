## 功能介绍
SQL 调优是数据库性能优化中非常重要的一环。为了避免优化器无法选择合适的执行计划所带来的影响，TXSQL 提供了 OUTLINE 功能，供用户绑定执行计划。MySQL 数据库有通过 HINT 来人为绑定执行计划的功能，HINT 信息包含 SQL 采用何种优化规则，执行何种算法，数据扫描采用何种索引等。OUTLINE 主要依靠 HINT 来指定查询计划，我们提供系统表 mysql.outline 让用户添加计划绑定规则，通过开关（cdb_opt_outline_enabled）控制是否开启该功能。

## 支持版本
内核版本 MySQL 8.0 20201230 及以上

## 适用场景
当线上执行计划走错，如线上执行计划选错索引，但业务又不想修改 SQL 重新发版本解决的场景。

## 性能影响
- 当 cdb_opt_outline_enabled 开关打开的情况下，不命中 outline 的 SQL 执行效率将不受影响。
- 命中 outline 的 SQL 执行效率将不及正常执行，但是一般 outline 绑定的提升将比之前的计划性能提升数倍。
- 使用此开关时需要咨询运维或者内核人员，防止可能发生的绑定失误，导致性能回退。

## 使用说明
OUTLINE 语法设置采用新的语法形式：
- 设置 OUTLINE 信息：`outline "sql" set outline_info "outline";`
- 清空 OUTLINE 信息：`outline reset ""; outline reset all;`
- 刷新 OUTLINE 信息：`outline flush;`

下面介绍 OUTLINE 的主要使用方法，用以下 schema 为例说明：
```
create table t1(a int, b int, c int, primary key(a));
create table t2(a int, b int, c int, unique key idx2(a));
create table t3(a int, b int, c int, unique key idx3(a));
```

| 参数名                  | 动态 | 类型 | 默认  | 参数值范围 | 说明                |
| ----------------------- | ---- | ---- | ----- | ---------- | ------------------- |
| cdb_opt_outline_enabled | yes  | bool | fasle | true/false | 是否打开 outline 功能 |

### 绑定 OUTLINE
直接绑定 OUTLINE 的方式是将一条 SQL 替换成另一条，SQL 的语义没有改变，仅是加入了一些 HINT 信息告知优化器如何去执行。
语法形式为：`outline "sql" set outline_info "outline";`，注意 outline_info 后的字符串应该以 "OUTLINE:" 开头，"OUTLINE:" 之后为加入 HINT 之后的 SQL。如给 `select *from t1, t2 where t1.a = t2.a` 这条 SQL 的 t2 表加上 a 列上的索引。
```
outline "select* from t1, t2 where t1.a = t2.a" set outline_info "OUTLINE:select * from t1, t2 use index(idx2) where t1.a = t2.a";
```

### 绑定 optimizer hint
为了功能更加灵活，TXSQL 允许向 SQL 中增量添加 optimizer hint，同样的功能也可以通过直接绑定 outline 实现。
语法形式为：`outline "sql" set outline_info "outline";`，注意 outline_info 后的字符串应该以 "OPT:" 开头，"OPT:" 之后为需要加入的 optimizer hint 信息。如给 s`elect *from t1 where t1.a in (select b from t2)` 这条 SQL 指定 MATERIALIZATION/DUPSWEEDOUT 的 SEMIJOIN。
```
outline "select* from t1 where t1.a in (select b from t2)" set outline_info "OPT:2#qb_name(qb2)";
outline "select * from t1 where t1.a in (select b from t2)" set outline_info "OPT:1#SEMIJOIN(@qb2 MATERIALIZATION, DUPSWEEDOUT)";
```

向原始 SQL 语句中添加 OPTIMIZER 的 HINT，仅支持一次添加一个 HINT，语法上需注意三点：
- OPT 关键字应该紧随在"之后。
- 需要绑定的新语句前必须是':'。
- 需要添加两个字段（query block 的号码 #optimizer hint 的字符串），中间必须用#分割（`ie. "OPT:1#max_execution_time(1000)"`）。

### 绑定 index hint
为了功能更加灵活，TXSQL 允许向 SQL 中增量添加 index hint，同样的功能也可以通过直接绑定 outline 实现。
语法形式为：`outline "sql" set outline_info "outline";`，注意 outline_info 后的字符串应该以 "INDEX:" 开头，"INDEX:" 之后为需要加入的 index hint 信息。
下面举个例子：给 `select *from t1 where t1.a in (select t1.a from t1 where t1.b in (select t1.a from t1 left join t2 on t1.a = t2.a))` 这条 SQL 的 query block 3 上数据库 test 下 t1 表增加 USE INDEX 的索引 idx1，类型为 FOR JOIN。
```
outline "select* from t1 where t1.a in (select t1.a from t1 where t1.b in (select t1.a from t1 left join t2 on t1.a = t2.a))" set outline_info "INDEX:3#test#t1#idx1#1#0";
```

向原始 SQL 语句中添加 INDEX 的 HINT，仅支持一次添加一个 HINT，语法上注意四点：
- INDEX 关键字应该紧随"之后。
- 需要绑定的新语句前必须是':'。
- 需要添加五个字段（query block 的号码 #db_name#table_name#index_name#index_type#clause）。
- 其中 index_type 还有三个值（0为 INDEX_HINT_IGNORE、1为 INDEX_HINT_USE、2为 INDEX_HINT_FORCE），其中 clause 有三个值（1为 FOR JOIN、2为 FOR ORDER BY、3为 FOR GROUP BY），中间必须用#分割（`ie. "INDEX:2#test#t2#idx2#1#0"` 表示将第2个 query block 中的 test.t2 表中绑定类型为 USE INDEX FOR JOIN 的 idx1 索引）。

### 删除某条 SQL 对应的 OUTLINE 信息
TXSQL 允许用户删除某一条 SQL 语句的 OUTLINE 绑定信息。
语法为：`outline reset "sql";`，如将 `select *from t1, t2 where t1.a = t2.a` 的 outline 信息删除：`outline reset "select* from t1, t2 where t1.a = t2.a";`。

### 清空所有 OUTLINE 信息
TXSQL 允许用户删除内核中所有 OUTLINE 绑定信息。语法为：`outline reset all`，执行语句为：`outline reset all;`。

线上业务中有时候会有一些非常特定的问题，需要强制绑定索引，这里可以直接设置 OUTLINE 去绑定。
需要分析设置 OUTLINE 后可能导致的性能回退，在可接受的性能回退范围下做绑定，必要时和内核人员商议。

## 相关参数状态说明
TXSQL 提供多种方式可以查看用户 SQL 的 OUTLINE 绑定，首先可以通过 mysql.outline 表来查看用户设置 OUTLINE 的情况。然后可以通过 show cdb_outline_info 和 select * from information_schema.cdb_outline_info 两个接口查看内存中的 OUTLINE 信息，输入 SQL 是否能被改变，取决于内存中是否有 OUTLINE 信息，所以用户可以用以上两个接口调试。

新增 mysql.outline 系统表，用户设置的 OUTLINE 信息记录存放于此表中，该表字段如下：

| 字段名       | 说明                                   |
| ------------ | -------------------------------------- |
| Id                | OUTLINE 设置信息编号                    |
| Digest         | 原始 SQL 语句的哈希值                    |
| Digest_text  | 原始 SQL 语句的指纹信息文本              |
| Outline_text | 绑定 OUTLINE 之后的 SQL 语句的指纹信息文本 |

通过 show cdb_outline_info 或者 select * from information_schema.cdb_outline_info 也可以查看内存中的记录，执行 SQL 会命中其中的 OUTLINE 记录绑定计划，参数如下：

| 字段名  | 说明                         |
| ------- | ---------------------------- |
| origin  | 原始 SQL 语句指纹              |
| outline | 绑定 OUTLINE 之后的 SQL 语句指纹 |

