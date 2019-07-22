更改一个表的定义。

## 概要

```sql
ALTER TABLE [ONLY] name RENAME [COLUMN] column TO new_column
 
ALTER TABLE name RENAME TO new_name
 
ALTER TABLE name SET SCHEMA new_schema
 
ALTER TABLE [ONLY] name SET 
     DISTRIBUTED BY (column, [ ... ] ) 
   | DISTRIBUTED RANDOMLY 
   | WITH (REORGANIZE=true|false)
 
ALTER TABLE [ONLY] name action [, ... ]
 
ALTER TABLE name
   [ ALTER PARTITION { partition_name | FOR (RANK(number)) 
   | FOR (value) } partition_action [...] ] 
   partition_action
```

其中 action 是下列之一：

```sql
  ADD [COLUMN] column_name type
      [column_constraint [ ... ]]
  DROP [COLUMN] column [RESTRICT | CASCADE]
  ALTER [COLUMN] column TYPE type [USING expression]
  ALTER [COLUMN] column SET DEFAULT expression
  ALTER [COLUMN] column DROP DEFAULT
  ALTER [COLUMN] column { SET | DROP } NOT NULL
  ALTER [COLUMN] column SET STATISTICS integer
  ADD table_constraint
  DROP CONSTRAINT constraint_name [RESTRICT | CASCADE]
  DISABLE TRIGGER [trigger_name | ALL | USER]
  ENABLE TRIGGER [trigger_name | ALL | USER]
  CLUSTER ON index_name
  SET WITHOUT CLUSTER
  SET WITHOUT OIDS
  SET (FILLFACTOR = value)
  RESET (FILLFACTOR)
  INHERIT parent_table
  NO INHERIT parent_table
  OWNER TO new_owner
  SET TABLESPACE new_tablespace
```

其中 partition_action 是下列之一：

```sql
  ALTER DEFAULT PARTITION
  DROP DEFAULT PARTITION [IF EXISTS]
  DROP PARTITION [IF EXISTS] { partition_name | 
      FOR (RANK(number)) | FOR (value) } [CASCADE]
  TRUNCATE DEFAULT PARTITION
  TRUNCATE PARTITION { partition_name | FOR (RANK(number)) | 
      FOR (value) }
  RENAME DEFAULT PARTITION TO new_partition_name
  RENAME PARTITION { partition_name | FOR (RANK(number)) | 
      FOR (value) } TO new_partition_name
  ADD DEFAULT PARTITION name [ ( subpartition_spec ) ]
  ADD PARTITION [partition_name] partition_element
     [ ( subpartition_spec ) ]
  EXCHANGE PARTITION { partition_name | FOR (RANK(number)) | 
       FOR (value) } WITH TABLE table_name
        [ WITH | WITHOUT VALIDATION ]
  EXCHANGE DEFAULT PARTITION WITH TABLE table_name
   [ WITH | WITHOUT VALIDATION ]
  SET SUBPARTITION TEMPLATE (subpartition_spec)
  SPLIT DEFAULT PARTITION
    {  AT (list_value)
     | START([datatype] range_value) [INCLUSIVE | EXCLUSIVE] 
        END([datatype] range_value) [INCLUSIVE | EXCLUSIVE] }
    [ INTO ( PARTITION new_partition_name, 
             PARTITION default_partition_name ) ]
  SPLIT PARTITION { partition_name | FOR (RANK(number)) | 
     FOR (value) } AT (value) 
    [ INTO (PARTITION partition_name, PARTITION partition_name)]  
```

其中 partition_element 是：

```sql
    VALUES (list_value [,...] )
  | START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
  | END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
[ WITH ( partition_storage_parameter=value [, ... ] ) ]
[ TABLESPACE tablespace ]
```

其中 subpartition_spec 是：

```sql
subpartition_element [, ...]
```

其中 subpartition_element 是：

```sql
   DEFAULT SUBPARTITION subpartition_name
  | [SUBPARTITION subpartition_name] VALUES (list_value [,...] )
  | [SUBPARTITION subpartition_name] 
     START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ( [number | datatype] 'interval_value') ]
  | [SUBPARTITION subpartition_name] 
     END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ( [number | datatype] 'interval_value') ]
[ WITH ( partition_storage_parameter=value [, ... ] ) ]
[ TABLESPACE tablespace ]
```

其中 storage_parameter 是：

```sql
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   COMPRESSTYPE={ZLIB|QUICKLZ|RLE_TYPE|NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```


## 描述
ALTER TABLE 更改一个表的定义。下文描述了几种形式：
 
 **ADD COLUMN** 
 向表中增加一个新列，使用和 CREATE TABLE 相同的语义。将列添加到 append 优化的表时，需要一个 DEFAULT 子句。

**DROP COLUMN** 
这种形式从表中删除一个列，请注意，如果将用作数据库分发密钥的表列删除，表的分发策略将更改为随机分配。涉及列的索引和表约束也将自动删除。用户将使用级联删除如果任何外部表依赖于此列（例如视图）。

**ALTER COLUMN TYPE** 
更改表中一列的数据类型。请注意用户不能修改正在用于分配密钥或分区键的列的数据类型。涉及到该列的索引和简单表约束将通过重新解析最初提供的表达式被自动转换为使用新的列类型。可选的 USING 子句指定如何从旧的列值计算新列值，如果被省略，默认的转换和从旧类型到新类型的赋值造型一样。如果没有从旧类型到新类型的隐式或者赋值造型，则必须提供一个 USING 子句。

**SET/DROP DEFAULT** 
这些形式为一列设置或者移除默认值。默认的值只能在随后的 INSERT 语句中生效。它们不会导致已经在表中的行改变。也会为视图创建默认值，在视图的规则被应用之前。也可以为视图创建默认值，在这种情况下，它们被插入到在视图之前查看 ON INSERT 规则被应用。

**SET/DROP NOT NULL** 
允许被标记的列为空值。更改列是否标记为允许空值或拒绝空值。当列不包含空值时，用户只能使用 SET NOT NULL。

**SET STATISTICS** 
设置后续的每列统计收集目标 ANALYZE 操作。目标可以设置在0到1000之间，或者设置为-1，以恢复为使用系统默认的统计目标（default_statistics_target）。

**ADD** table_constraint 
使用与之相同的语法将新的约束添加到表（而不仅仅是分区）。CREATE TABLE

**DROP CONSTRAINT** 
在表上删除指定的约束。

**DISABLE/ENABLE TRIGGER** 
这些形式配置属于该表的触发器的触发设置。系统仍然知道被禁用触发器的存在，但是即使它的触发事件发生也不会执行它。对于一个延迟触发器，会在事件发生时而不是触发器函数真正被执行时检查其启用状态。可以禁用或者启用用名称指定的单个触发器、表上的所有触发器、用户拥有的触发器禁用或者启用内部生成的约束触发器要求超级用户特权。

>!数据库不支持触发器。由于数据库的并行性，触发器通常具有非常有限的功能。

**CLUSTER ON/SET WITHOUT CLUSTER** 
这种形式为未来的 CLUSTER 操作选择默认的索引。它不会真正地对表进行聚簇。注意 CLUSTER 不是建议在数据库中重新排序表的方式，因为它需要很长时间。最好是用 **CREATE TABLE AS** 重新创建表并由索引列排序。

>!CLUSTER ON在append优化的表上不支持。

**SET WITHOUT OIDS** 
这种形式从该表移除 oid 系统列。注意没有 ALTER TABLE 变体情况下，一旦它们被删除，就可以将 OID 恢复到表中。

**SET ( FILLFACTOR =** value**) / RESET (FILLFACTOR)** 
更改表的填充因子。表的填充因子是10到100之间的百分比。默认值为100（完全打包）。当指定较小的填充因子时， INSERT 操作包表页面仅指示百分比; 保留每个页面上的剩余空间用于更新该页面上的行。这给了 UPDATE 有机会将更新的副本放在与原始页面相同的页面上，这比将其放置在不同页面上更有效。对于其表项永远不会更新的表格，完全打包是最佳选择，但是在大量更新的表中，较小的填充因子是适当的。请注意，此命令不会立即修改表内容。用户将需要重写表以获得所需的效果。

**SET DISTRIBUTED** 
设置表的分配策略。对哈希分发策略的更改将导致表数据在物理上重新分布在磁盘上，这可能是资源密集型的。

**INHERIT** parent_table **/ NO INHERIT** parent_table 
将目标表添加或删除为指定父表的子级。对父母的查询将包括其子表的记录。要作为子级添加，目标表必须已经包含与父级相同的所有列（也可能有其他列）。列必须具有匹配的数据类型， 如果他们有 NOTNULL 父母的约束，他们也必须有 NOT NULL 孩子的约束。所有人也必须有匹配的子表约束 CHECK 父母的约束。

**OWNER** 
将表、序列或视图的所有者更改为指定的用户。

**SET TABLESPACE** 
将表的表空间更改为指定的表空间，并将与表关联的数据文件移动到新的表空间。表上的索引（如果有的话）不移动；但他们可以单独移动用额外 SET TABLESPACE 命令。参见 CREATE TABLESPACE。如果更改分区表的表空间，则所有子表分区也将被移动到新的表空间。

**RENAME** 
更改表（或索引，序列或视图）的名称或表中单个列的名称。对存储的数据没有影响。请注意，数据库分发密钥列不能重命名。

**SET SCHEMA** 
将表移动到另一个模式。关联的索引，约束和表列所有的序列也被移动。

**ALTER PARTITION | DROP PARTITION | RENAME PARTITION | TRUNCATE PARTITION | ADD PARTITION | SPLIT PARTITION | EXCHANGE PARTITION | SET SUBPARTITION TEMPLATE** 
更改分区表的结构。在大多数情况下，用户必须通过父表来更改其子表分区之一。
>? 如果将分区添加到具有子分区编码的表中，则新分区将继承子分区的存储指令。有关压缩设置优先级的更多信息，请参见“数据库管理员指南”中的“使用压缩”。

要使用 ALTER TABLE 用户必须拥有该表。要更改一个表的模式或者表空间，用户还必须拥有新模式或表空间上的 CREATE 特权。要把一个表作为一个父表的新子表加入，用户必须也拥有该父表。要更改拥有者，用户还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该表的模式上的 CREATE 特权。超级用户自动拥有这些权限。

>!如果表具有多个分区，如果表具有压缩，或者表的 blocksize 大，则内存使用量会显着增加。如果与表关联的关系数量较大，则此条件可能会迫使表上的操作使用更多内存。例如，如果表是一个 CO 表并且具有大量列，则每一列都是一个关系。 一个操作像 ALTER TABLE ALTER COLUMN 打开表中的所有列分配关联的缓冲区。如果 CO 表有40列和100分区，列被压缩，并且块大小为2MB（系统系数为3），则系统尝试分配24GB，即（40×100）×（2× 3）MB或24GB。

## 参数

ONLY
只对指定的表名进行操作。如果 ONLY 关键字不被使用，将对命名表和与该表相关联的任何子表分区执行操作。

name
要更改的现有表的名称（可能是方案限定的）。如果 ONLY 被指定，只有该表被更改。如果 ONLY 未指定，该表及其所有后代表（如果有）都会被修改。
>!限制只能添加到整个表中，而不能添加到分区。由于这个限制，该 name 参数只能包含一个表名，而不能是一个分区名。

column
新列或现有列的名称。请注意，数据库分发密钥列必须特别小心处理。更改或删除这些列可以更改表的分发策略。

new_column
现有列的新名称。

new_name
表的新名称。

type
新列的数据类型，或现有列的新数据类型。如果更改分发密钥列的数据类型，则只允许将其更改为兼容类型 (例如 text 到 varchar 是可以的，但是 text 到 int 不行)。

table_constraint
表的新表约束。请注意，Database 目前不支持外键限制。还有一个表只允许一个唯一的约束，唯一性必须在数据库分配密钥中。

constraint_name
要删除的现有约束的名称。

CASCADE
自动删除依赖于已删除列或约束的对象（例如：引用该列的视图）。

RESTRICT
如果有任何依赖对象，拒绝删除列或约束。这是默认行为。

trigger_name
要禁用或启用的单个触发器的名称。请注意，数据库不支持触发器。

ALL
禁用或启用属于表的所有触发器，包括与约束相关的触发器。这需要超级用户权限。

USER
禁用或启用属于该表的所有用户创建的触发器。

index_name
表应标记为聚类的索引名称。注意 CLUSTER 不是建议在数据库中重新排序表的方式，因为它需要很长时间。最好用 **CREATE TABLE AS** 重新创建表并由索引列排序。

FILLFACTOR
设置表的 fillfactor 百分比。

value
FILLFACTOR 参数的新值，在10到100之间的百分比。默认值为100。

DISTRIBUTED BY (column) | DISTRIBUTED RANDOMLY
指定表的分发策略。更改哈希分发策略将导致表数据在物理上重新分配到磁盘上，这可能是资源密集型的。如果用户声明相同的哈希散布策略或从哈希更改为随机分布，除非用户声明了 SET WITH(REORGANIZE=true)否则不会重新分发数据。

REORGANIZE=true|false
使用 REORGANIZE=true 当哈希分发策略没有改变或者当用户从一个哈希更改为一个随机分布，并且用户想重新分发数据。

parent_table
与该表关联或取消关联的父表。

new_owner
表的新所有者的角色名称。

new_tablespace
要移动表的表空间的名称。

new_schema
要移动表的模式的名称。

parent_table_name
更改分区表时，该顶级父表的名称。

ALTER [DEFAULT] PARTITION
如果更改分区比第一级分区更深，那么 ALTER PARTITION 子句用于指定要更改的层次结构中的哪个子分区。

DROP [DEFAULT] PARTITION
删除指定的分区。如果分区具有子分区，子分区也将自动删除。

TRUNCATE [DEFAULT] PARTITION
截断指定的分区。如果分区具有子分区，则子分区也将自动截断。

RENAME [DEFAULT] PARTITION
更改分区的分区名称（而不是关系名称）。使用命名约定创建分区表：<parentname>_<level>_prt_<partition_name>。

ADD DEFAULT PARTITION
将默认分区添加到现有分区设计。当数据与现有分区不匹配时，它将被插入到默认分区中。没有默认分区的分区设计将拒绝与现有分区不匹配的传入行。必须给默认分区一个名称。

ADD PARTITION

partition_element
使用表（范围或列表）的现有分区类型，定义要添加的新分区的边界。

name
此新分区的名称。

**VALUES** 
对于列表分区，定义分区将包含的值。

**START** 
对于范围分区，定义分区的起始范围值。默认情况下，起始值为 INCLUSIVE。例如，如果用户宣布开始日期为'2016-01-01'，那么分区将包含大于或等于'2016-01-01'。通常数据类型为 START 表达式与分区键列类型相同。如果不是这样，那么用户必须显式地转换为预期的数据类型。

**END** 
对于范围分区，定义分区的结束范围值。默认情况下，结束值为 EXCLUSIVE。例如如果用户宣布结束日期为'2016-02-01'，那么分区将包含所有日期小于但不等于'2016-02-01'。通常数据类型为 END 表达式与分区键列类型相同。如果不是这样，那么用户必须显式地转换为预期的数据类型。

**WITH** 
设置分区的表存储选项。例如用户可能希望较旧的分区是追加优化的表和较新的分区为常规堆表。参考 CREATE TABLE 有关存储选项的说明。

**TABLESPACE** 
要在其中创建分区的表空间的名称。

subpartition_spec 
只允许在没有子分区模板的情况下创建的分区设计。声明要添加的新分区的子分区规范。如果最初使用子分区模板定义了分区表，那么将使用该模板自动生成子分区。

EXCHANGE [DEFAULT] PARTITION
将另一个表交换到分区层次结构到现有分区的位置。在多级别分区设计中，只能交换最低级别的分区（包含数据的分区）。

数据库服务器配置参数 gp_enable_exchange_default_partition 控制可用 EXCHANGE DEFAULT PARTITION 子句。参数的默认值为 off。该子句不可用并且如果在 ALTER TABLE 命令中指定了子句数据库将返回错误。

警告：在交换默认分区之前，用户必须确保要被交换的表（新的默认分区）中的数据对于默认分区是有效的。例如新默认分区中的数据不能含有对该分区表其他叶子子分区中有效的数据。否则，针对被交换默认分区所在分区表的查询在被GPORCA执行时可能返回不正确的结果。

**WITH TABLE** table_name
用户正在换入到分区设计中的表名。用户可以交换一个表数据被存储在数据库中的表。例如该表由 CREATE TABLE 命令创建。

通过 EXCHANGE PARTITION 子句，用户还可以交换一个可读外部表（由 CREATE EXTERNAL TABLE 命令创建）到分区层次中替换一个现有的叶子子分区。如果用户指定一个可读外部表，用户还必须指定 WITHOUT VALIDATION 子句以跳过针对正在交换的分区上 CHECK 约束的表验证。

这些情况中不支持用外部表交换叶子子分区：
- 分区表通过 SUBPARTITION 子句创建，或者如果分区具有子分区。
- 分区表含有一个带有检查约束或者 NOT NULL 约束的列。

**WITH** | **WITHOUT VALIDATION** 
验证表中的数据匹配正在交换的分区的 CHECK 约束。默认是针对 CHECK 约束验证数据。

警告：如果用户指定 WITHOUT VALIDATION 子句，用户必须确保正在交换一个现有叶子子分区的表中的数据对于该分区上的 CHECK 约束有效。否则针对分区表的查询可能返回不正确的结果。

SET SUBPARTITION TEMPLATE
为一个现有分区修改子分区模板。在设置了一个新的子分区模板后，所有增加的新分区都将具有新的子分区设计（现有分区不会被修改）。

SPLIT DEFAULT PARTITION
分裂一个默认分区。在一种多级分区设计中，用户只能分裂最底层的默认分区（它们包含数据）。分裂默认分区会创建包含指定值的新分区并且让默认分区包含不匹配现有分区的任何值。

**AT** 
对于列表分区表，指定应该被用作分裂条件的单个列表值。

**START** 
对于范围分区表，为新分区指定一个开始值。

**END** 
对于范围分区表，为新分区指定一个结束值。

**INTO** 
允许用户为新分区指定一个名字。在使用 INTO 子句分裂默认分区时，被指定的第二个分区名应该总是现有的默认分区。如果用户不知道默认分区的名称，用户可以使用 pg_partitions 视图找到它。

SPLIT PARTITION
将一个现有分区分裂成两个分区。在多层分区设计中，用户只能分裂最底层的分区（包含着数据）。

**AT** 
指定应该被用作分裂条件的单个值。分区将被划分成两个新分区，指定的分裂值会成为后一个分区的开始范围。

**INTO** 
允许用户为分裂创建两个新分区指定名字。

partition_name
给定的分区名称。

FOR (RANK(number))
对于范围分区，分区在范围中的排名。

FOR ('value')
通过声明一个落在分区边界说明中的值来指定一个分区。如果用 FOR 声明的值匹配一个分区和它的一个子分区（例如如果值是一个日期并且表先按月分区然后按日分区），那么 FOR 将在第一个找到匹配的层次上操作（例如每月的分区）。如果用户的目的是在子分区上操作，则必须按如下的方式声明：ALTER TABLE name ALTER PARTITION FOR ('2016-10-01') DROP PARTITION FOR ('2016-10-01');

## 注解

ALTER TABLE 命令中指定的表名不能是一个表中的分区名。

在修改或者删除作为数据库分布键一部分的列时要特别小心，因为这可能会改变表的分布策略。

数据库当前不支持外键约束。对于要在数据库中实施的唯一约束，表必须被哈希分布（不能用 DISTRIBUTED RANDOMLY），并且所有的分布键列必须和唯一约束列中前部的列相同。

增加 CHECK 或者 NOT NULL 约束要求扫描表以验证现有的行是否符合约束。

在用 ADD COLUMN 增加列时，表中所有的现有行都用该列的默认值初始化，如果没有指定 DEFAULT 子句则初始化为 NULL（注意不允许在追加优化表中增加不指定默认值的列）。增加一个非空默认值的列或者更改现有列的类型要求重写整个表。对于大型表这可能需要大量的时间，并且会临时要求两倍的磁盘空间。

用户可以在单个 ALTER TABLE 命令中指定多个更改，它们将在对表的一趟扫描中完成。

DROP COLUMN 形式不会物理上移除列，而是简单地将它变成对 SQL 操作不可见。后续在表中的插入和更新操作将为该列存储一个空值。因此，删除一列很快，但是不会立即减少表的磁盘尺寸，因为被删除列所占据的空间没有被回收。这些空间将随着现有行被更新而逐渐被回收。

ALTER TYPE 要求重写整个表的做法有时候是一种优点，因为重写过程会消除表中的任何死亡空间。例如，要立即回收被删除列占据的空间，最快的方法是：ALTER TABLE table ALTER COLUMN anycol TYPE sametype;，其中*anycol*是任何现有表列而*sametype*是该列现有的数据类型。这不会对表产生任何语义可见的变化，但是该命令强制进行了重写，这就会去除无用的数据。

如果表被分区或者由任意后代表，就不允许对父表增加列、重命名列或者更改列类型而不对其后代表做同样的事情。这确保了后代总是具有和父辈相匹配的列。

要查看一个分区表的结构，用户可以使用视图 pg_partitions。这个视图可以帮助确定用户想要修改的特定分区。

只有当后代表没有从任何其他父表继承某一列并且也没有对该列的独立定义时，递归的 DROP COLUMN 操作才会移除后代表的这个列。非递归的 DROP COLUMN（ALTER TABLE ONLY ... DROP COLUMN）不会移除任何后代列，而是将它们标记为独立定义而不是继承而来。

TRIGGER、CLUSTER、OWNER 以及 TABLESPACE 动作不会递归到后代表，也就是说它们的动作总是好像在指定了 ONLY 的情况下执行。增加约束的动作中只有 CHECK 约束可以递归。

如果在包含已经被交换为使用外部表的叶子子分区的分区表上没有数据被更改，则支持这些 ALTER PARTITION 操作。否则会返回错误。
- 添加或删除列。
- 更改列的数据类型。

这些 ALTER PARTITION 对于已经交换为使用外部表的叶子分区的分区表，不支持以下操作：

- 设置子分区模板。
- 更改分区属性。
- 创建一个默认分区。
- 制定分销政策。
- 设置或删除 NOT NULL 列的约束。
- 添加或删除约束。
- 拆分外部分区。

不允许更改系统目录表的任何部分。

## 示例

向列中添加列：

```sql
ALTER TABLE distributors ADD COLUMN address varchar(30);
```

重命名现有列：

```sql
ALTER TABLE distributors RENAME COLUMN address TO city;
```

重命名现有表：

```sql
ALTER TABLE distributors RENAME TO suppliers;
```

向列添加非空约束：

```sql
ALTER TABLE distributors ALTER COLUMN street SET NOT NULL;
```

向表中添加检查约束：

```sql
ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK 
(char_length(zipcode) = 5);
 
--增加约束，c1列的值必须大于5
alter table table1 ADD CONSTRAINT xxcheck2 check (c1 > 5);
ALTER TABLE
Time: 50.201 ms
--插入数据，当插入列的值小于5，则报错。
INSERT INTO table1 VALUES(20190117,'test', 4);
ERROR:  new row for relation "table1" violates check constraint "xxcheck2"  (seg0 10.0.15.16:40000 pid=11071)
 
INSERT INTO table1 VALUES(20190117,'test', 6);
INSERT 0 1
Time: 71.215 ms
 
```

将表移动到不同的模式：

```sql
ALTER TABLE myschema.distributors SET SCHEMA yourschema;
```

将新分区添加到分区表中：

```sql
ALTER TABLE sales ADD PARTITION 
            START (date '2017-02-01') INCLUSIVE 
            END (date '2017-03-01') EXCLUSIVE;
```

将默认分区添加到现有分区设计中：

```sql
ALTER TABLE sales ADD DEFAULT PARTITION other;
```

重命名分区：

```sql
ALTER TABLE sales RENAME PARTITION FOR ('2016-01-01') TO 
jan08;
```

删除范围序列中的第一个（最旧的）分区：

```sql
ALTER TABLE sales DROP PARTITION FOR (RANK(1));
```

将表交换到用户的分区设计中：

```sql
ALTER TABLE sales EXCHANGE PARTITION FOR ('2016-01-01') WITH 
TABLE jan08;
```

拆分默认分区（现有的默认分区名称 other）为2017年1月添加新的每月分区：

```sql
ALTER TABLE sales SPLIT DEFAULT PARTITION 
START ('2017-01-01') INCLUSIVE 
END ('2017-02-01') EXCLUSIVE 
INTO (PARTITION jan09, PARTITION other);
```

第一个分区包含日期为1月1日至15日，第二个分区包含日期1月16日至31日：

```sql
ALTER TABLE sales SPLIT PARTITION FOR ('2016-01-01')
AT ('2016-01-16')
INTO (PARTITION jan081to15, PARTITION jan0816to31);
```

## 兼容性

ADD、DROP、SET DEFAULT 项符合 SQL 标准。其他形式是 SQL 标准的数据库扩展。另外，在一个单一的指定多个操作的能力 ALTER TABLE 命令是一个扩展。

ALTER TABLE DROP COLUMN 可用于删除表的唯一列，留下零列表。这是 SQL 的扩展，它不允许零列表。

## 另见

CREATE TABLE、DROP TABLE
