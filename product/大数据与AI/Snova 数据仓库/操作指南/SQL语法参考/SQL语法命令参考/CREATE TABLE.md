
定义一张新表。

注意：引用完整性约束（外键约束）被接受但不被强制执行。

## 概要

```sql
CREATE [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name ( 
[ { column_name data_type [ DEFAULT default_expr ] 
   [column_constraint [ ... ]
[ ENCODING ( storage_directive [,...] ) ]
] 
   | table_constraint
   | LIKE other_table [{INCLUDING | EXCLUDING} 
                      {DEFAULTS | CONSTRAINTS}] ...}
   [, ... ] ]
   )
   [ INHERITS ( parent_table [, ... ] ) ]
   [ WITH ( storage_parameter=value [, ... ] )
   [ ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP} ]
   [ TABLESPACE tablespace ]
   [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
   [ PARTITION BY partition_type (column)
       [ SUBPARTITION BY partition_type (column) ] 
          [ SUBPARTITION TEMPLATE ( template_spec ) ]
       [...]
    ( partition_spec ) 
        | [ SUBPARTITION BY partition_type (column) ]
          [...]
    ( partition_spec
      [ ( subpartition_spec
           [(...)] 
         ) ] 
    )
```

其中 column_constraint 是：

```sql
   [CONSTRAINT constraint_name]
   NOT NULL | NULL 
   | UNIQUE [USING INDEX TABLESPACE tablespace]
            [WITH ( FILLFACTOR = value )]
   | PRIMARY KEY [USING INDEX TABLESPACE tablespace] 
                 [WITH ( FILLFACTOR = value )]
   | CHECK ( expression )
   | REFERENCES table_name [ ( column_name [, ... ] ) ] 
            [ key_match_type ]
            [ key_action ]
```

其中一列的 storage_directive 是：

```sql
   COMPRESSTYPE={ZLIB | QUICKLZ | RLE_TYPE | NONE}
    [COMPRESSLEVEL={0-9} ]
    [BLOCKSIZE={8192-2097152} ]
```

其中一个表的 storage_parameter 是：

```sql
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   CHECKSUM={TRUE|FALSE}
   COMPRESSTYPE={ZLIB|QUICKLZ|RLE_TYPE|NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

table_constraint 是：

```sql
   [CONSTRAINT constraint_name]
   UNIQUE ( column_name [, ... ] )
          [USING INDEX TABLESPACE tablespace] 
          [WITH ( FILLFACTOR=value )] 
   | PRIMARY KEY ( column_name [, ... ] ) 
                 [USING INDEX TABLESPACE tablespace] 
                 [WITH ( FILLFACTOR=value )] 
   | CHECK ( expression )
   | FOREIGN KEY ( column_name [, ... ] )
            REFERENCES table_name [ ( column_name [, ... ] ) ]
            [ key_match_type ]
            [ key_action ]
            [ key_checking_mode ]
```

其中 key_match_type 是：

```sql
    MATCH FULL
  | SIMPLE
```

其中 key_action 是：

```sql
    ON DELETE 
  | ON UPDATE
  | NO ACTION
  | RESTRICT
  | CASCADE
  | SET NULL
  | SET DEFAULT
```

其中 key_checking_mode 是：

```sql
    DEFERRABLE
  | NOT DEFERRABLE
  | INITIALLY DEFERRED
  | INITIALLY IMMEDIATE
```

其中 partition_type 是：

```sql
    LIST
  | RANGE
```

其中 partition_specification 是：

```sql
partition_element [, ...]
```

partition_element 是：

```sql
   DEFAULT PARTITION name
  | [PARTITION name] VALUES (list_value [,...] )
  | [PARTITION name] 
     START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
  | [PARTITION name] 
     END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
[ WITH ( partition_storage_parameter=value [, ... ] ) ]
[ TABLESPACE tablespace ]
```

其中 subpartition_spec 或 template_spec 是：

```sql
subpartition_element [, ...]
```

subpartition_element 是：

```sql
   DEFAULT SUBPARTITION name
  | [SUBPARTITION name] VALUES (list_value [,...] )
  | [SUBPARTITION name] 
     START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
  | [SUBPARTITION name] 
     END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
[ WITH ( partition_storage_parameter=value [, ... ] ) ]
[ TABLESPACE tablespace ]
```

其中一个分区的 storage_parameter 是：

```sql
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   CHECKSUM={TRUE|FALSE}
   COMPRESSTYPE={ZLIB|QUICKLZ|RLE_TYPE|NONE}
   COMPRESSLEVEL={1-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

## 描述

CREATE TABLE 在当前数据库中创建一个初始为空的表。发出该命令的人拥有该表。

如果用户指定了一个模式名字，会在特定的模式中创建该表，否则数据库在当前的模式中创建该表。临时表存在于特殊的模式中，所以用户在创建临时表时不能指定一个模式名。在同一个模式中，表必须和其他表，外部表，序列，索引或者视图不同名。

该可选约束子句指定了条件，该新行或者更新的行必须满足该条件才能成功进行插入或更新操作。约束是一个 SQL 对象，该对象以不同的方式在表中帮助定义有效值集合。约束应用于表，而不是分区，用户不能添加一个约束到分区或者子分区。

引用完整性约束（外键）被接受但不强制执行。该信息保持在系统目录表中，否则将被忽略。

有两种定义约束的方式：表约束和列约束。列约束被定义为列定义的一部分。表约束不与特定的列相关联，并且它可以包含多个列，每个列约束也能写成表约束；当表约束仅影响一列时，列约束仅是一种符号方便。

当创建一张表的时候，还有额外的子句来声明数据库分布策略。如果没有提供 DISTRIBUTED BY 或者 DISTRIBUTED RANDOMLY 子句，则使用 PRIMARY KEY（如果表有的话）或者将该表的第一列作为分布键，给表分配一种哈希分布策略。几何或用户定义的数据类型的列不符合分布键列的资格。如果表没有一个符合条件的数据类型的列，那么这些行则是基于循环或随机分布分配的。为了确保用户的数据库系统中的数据均匀分配，用户需要选择对每个记录唯一的分布键，否则，请选择随机分布 DISTRIBUTED RANDOMLY。

该 PARTITION BY 子句允许用户将表划分成多个子表（或部分），他们组合在一起构成父表并共享其模式。尽管子表以独立表的形式存在，但是数据库以重要的方式限制了他们的使用。在内部，分区被实现为一种特殊形式的继承。每个子表分区的创建带有不同 CHECK 约束，该约束根据一些定义标准限制表可以包含的数据。查询优化器也使用 CHECK 约束来确定要扫描的分区，以满足给定的谓词。这些分区约束由数据库自动管理。

## 参数
GLOBAL | LOCAL
这些参数用于 SQL 标准兼容性，但在数据库中不起作用。

TEMPORARY | TEMP
如果指定，则该表被创建成临时表。临时表在会话结束时自动删除，或选择性地在当前事务结束的时候删除（参阅 ON COMMIT）。当临时表存在时当前会话中具有同名的永久表是不可见的，除非他们使用方案限定的名字来引用。任何在临时表中创建的索引也都是临时的。

table_name
所创建表的名字（可选方案限定）。

column_name
新表中所要创建的列名。

data_type
列的数据类型，这可能包含数据说明符。
对于包含文本数据的表列，通过使用 VARCHAR 或 TEXT指定数据类型。不建议指定数据类型 CHAR。在数据库中，该数据类型 VARCHAR 或 TEXT 将添加到数据之后的补充 （最后一个非空格字符之后添加的空格字符）作为有效字符，而数据类型 CHAR 却不会。

DEFAULT default_expr
该 DEFAULT 子句给其列定义出现的列分配一个默认值。该值时任何无变量表达式（不允许对当前表中其他列的子查询或者交叉引用）。该默认表达式的数据类型必须匹配该列的数据类型。该默认表达式将会在任何对该列没有指定值的插入操作中使用。如果对该列没有默认值，则该默认值为 null。

ENCODING ( storage_directive [, ...] )
对于列，可选的 ENCODING 子句指定列数据的压缩类型和块大小。参阅 storage_options 以获取 COMPRESSTYPE， COMPRESSLEVEL 和 BLOCKSIZE 的值。
该子句仅对追加优化，面向列的表有效。
列压缩设置从表级继承到分区级再到子分区级别。最低级设置优先。

INHERITS
该可选 INHERITS 子句指定了新表自动继承所有列的表的列表（list of tables）。使用 INHERITS 在新的子表和其父表之间创建持久的关系。对父表的模式修改通常也传播给子表，默认情况下，子表的数据包含在父表的扫描中。
在数据库中，在创建分区表的时候该 INHERITS 子句是不用的。尽管在分区层次体系中使用了继承的概念，但是分区表的继承结构是由 PARTITION BY 子句所创建的。
如果同样的列名存在于多个父表中，则会报告错误，除非列数据类型在每个父表中都匹配。如果没有冲突，则将重复的列合并在新表中形成单一的列。如果新表的列名列表包含继承的列名称，则数据类型必须与继承的列一致，列定义合并为一。但是，相同名字的继承列和新列的声明不需要指定相同约束：任何声明中提供的所有约束都合并在一起，并且都应用于新表。如果新表为一列明确指定了默认值，则该默认值覆盖该列继承声明中的任何默认值。否则，任何为该列指定默认值的父表都必须指定相同的默认值。否则将报告错误。

LIKE other_table [{INCLUDING | EXCLUDING} {DEFAULTS | CONSTRAINTS}]
该 LIKE 子句指定新表将自动复制所有列名，数据类型，非空约束和分发策略的表。诸如追加优化或分区结构之类的存储属性不被复制。与 INHERITS 不同，新表创建完成之后，新表和原始表完全解耦。
复制的列定义的默认表达式仅在指定了 INCLUDING DEFAULTS 时才会被复制。默认行为是排除默认表达式，该操作导致复制的列在新表中使用null的默认值。
Not-null 约束总是会被复制到新表中。仅当指定了 INCLUDING CONSTRAINTS 时，才会复制 CHECK 约束。其他类型的约束将永远不会被复制。此外，当请求约束时，列约束和表约束之间不作区分，所有的检查约束都将会被复制。
还要注意，不像 INHERITS，复制的列和约束不会与命名相似的列和约束合并。如果明确指定相同的名字，或在另一个 LIKE 子句中，则会提示错误。

CONSTRAINT constraint_name
列或表约束的可选名称。如果违反该约束，则该约束名称会出现在错误消息中，因此诸如该列必须为正数的约束名称，可以用来向客户端应用传达有用的约束信息（需要用双引号来指定包含空格的约束名称）。如果没有指定约束名称，则该系统将生成一个名称。
注意：该指定的 constraint_name 用于约束，但是系统生成的唯一名字是用于索引名称。在先前的版本中，提供的名称用于约束名称和索引名称（both）。

NULL | NOT NULL
指明该列是否允许包含 null。值默认值是 NULL。

UNIQUE ( column constraint )
UNIQUE ( column_name [, ... ] ) ( table constraint )
该 UNIQUE 约束指定表中一列或多列的组合只包含唯一值。该唯一表约束的行为和列约束相同，具有跨多个列的附加功能。为了唯一约束的目的，空值不被认为是相等的。该唯一列必须包含分布键的所有列。此外，如果表被分区，该 &lt;key&gt; 必须包含分区键中的所有列。请注意，分区表中的 &lt;key&gt; 约束和简单的 simple UNIQUE INDEX 不同。

PRIMARY KEY ( column constraint )
PRIMARY KEY ( column_name [, ... ] ) ( table constraint )
该主键约束指定表的一列或多列只能包含唯一（非重复）非空值。技术上，PRIMARY KEY 仅仅是 UNIQUE 和 NOT NULL 的组合，但是将一组列标识为主键还提供了关于设计模式的元数据，因为主键意味着其他表可能依赖这组列作为行的唯一标识符。要使表具有主键，它必须是哈希分布（不是随机分布），唯一的主键列必须包含分布键的所有列。另外，如果表被分区，则 &lt;key&gt; 必须包含分区键的所有列。请注意，分区表中的 &lt;key&gt; 约束和简单的 UNIQUE INDEX 不同。

CHECK ( expression )
该 CHECK 指定了一个表达式，该表达式产生布尔结果，新的或更新行必须满足该表达式才能成功插入或更新操作。 被评估为 TRUE 或者 UNKNOWN 的表达式算是成功。 
如果插入或更新的任何行产生 FALSE 结果，则会引发错误异常，并且插入或更新不会更改数据库。指定为列约束的检查约束应仅引用该列的值，而表约束中出现的表达式可能会引用多个列。CHECK 表达式不能包含子查询也不能引用当前行以外的值。

REFERENCES table_name [ ( column_name [, ... ] ) ]
[ key_match_type ] [ key_action ]
FOREIGN KEY ( column_name [, ... ] )
REFERENCES table_name [ ( column_name [, ... ] )
[ key_match_type ] [ key_action [ key_checking_mode ]
该 REFERENCES 和 FOREIGN KEY 子句指定引用完整性约束（外键约束）。数据库接受 PostgreSQL 语法中指定的引用完整性约束，但是不执行他们。有关引用完整性约束的信息请参考 PostgreSQL 文档。

WITH ( storage_option=value )
该 WITH 子句可以用来为表或索引设置存储选项。注意用户也能在分区说明中，通过声明 WITH 来在特定的分区或子分区上设置存储参数。最低级设置优先。
某些表存储选项的默认值可以使用服务器配置参数 gp_default_storage_options 来指定。
有以下存储选项：
- **APPENDONLY**：设置为 TRUE 来创建一个表作为追加优化表。如果设置为 FALSE 或者没有指定，则该表将会被创建为常规的堆存储表。
- **BLOCKSIZE**：对表中的每个块设置大小。该 BLOCKSIZE 必须在8192和2097152字节之间，且必须是8192字节的倍数。该默认值是32768。
- **ORIENTATION** ：设置为 column 是面向列存储，或设置为 row（默认值）是面向行存储。该选项仅当 APPENDONLY=TRUE时才有效。堆存储表只能是面向行的。
- **CHECKSUM** ：该存储表仅对追加优化表（append-optimized tables）才是有效的，即（APPENDONLY=TRUE）。该值 TRUE 时默认的并且为追加优化表启用 CRC 校验和验证。该校验在块创建期间计算并存储在磁盘上。校验验证在块读取期间执行。如果读取期间计算的校验和存储的校验不匹配，则事务终止。如果用户设置该值为 FALSE 来禁用校验验证，则会启动检查表数据防止磁盘损坏。
- **COMPRESSTYPE**：设置为 ZLIB（默认值），RLE-TYPE 或 QUICKLZ1 来指明使用的压缩类型。该值 NONE 禁用压缩。QuickLZ 比 zlib 使用更少量的 CPU 功率，具有更低的压缩比和更快的数据压缩。zlib 提供了在低压缩速度下高压缩比。该选项仅当 APPENDONLY=TRUE 时才有效。
注意： 1QuickLZ 压缩仅在 Pivotal 公司的数据库的商业发型版中可用。
该值 RLE_TYPE 仅在指定 ORIENTATION =column 的时候才支持。数据库使用运行长度编码（RLE）压缩算法。当同样的数据出现在连续的行中，RLE比zlib 和 QuickLZ 压缩算法能更好压缩数据。
对于类型为 BIGINT， INTEGER，DATE，TIME 或 TIMESTAMP 的列，如果 COMPRESSTYPE 选项设置为 RLE-TYPE压缩，同样会应用增量压缩。该增量压缩算法是基于连续的行中列值之间的增量，并且设计为当加载的数据是有序或者要压缩的列数据是有序时，能提高压缩性能。
有关使用表压缩的信息，请参阅“数据库管理员指南”的“选择表的存储模式”。
- **COMPRESSLEVEL**：对于追加优化表的zlib压缩，设置为1（最快压缩）到 9（最高压缩比）之间的整数。QuickLZ压缩等级只能设置为1，如果没有指定，则默认为1。对于 RLE_TYPE，该压缩比能设置在1 （最快压缩）到 4（最高压缩比）之间的整数。
该选项仅当 APPENDONLY=TRUE 时才有效。
- **FILLFACTOR** ：参阅 CREATE INDEX 获取更多关于该索引存储参数的信息。
- **OIDS** ：设置为 OIDS=FALSE （默认值），以便行没有分配对象表示符。强烈推荐用户在创建表时不启用 OIDs。
在大型表中（如典型的数据库系统中的表），对表行使用 OIDs 会导致32位 OID 计数器环绕。一旦计数器环绕，OID 就不能被认为是唯一的，这不仅会导致他们对用户程序无用，而且还可能在数据库系统目录中引起问题。
此外，从表中排出 OID 会减少表在磁盘所需存储的空间，每行4字节，这会稍微提升性能。OIDs 不允许在分区表或者追加优化表面向列的表中使用。

ON COMMIT
在事务块结束时临时表的行为可以通过使用 ON COMMIT 来控制。该三个选项如下：
- **PRESERVE ROWS** - 在事务结束时候没有对临时表特别的操作，这是默认的行为。
- **DELETE ROWS** - 在每个事务块结束时，临时表的所有行都将被删除。本质上，在每次提交时，执行了自动删除 TRUNCATE。
- **DROP** - 在当前事务结束时，会删除临时表。

TABLESPACE tablespace
要创建的新表所在的表空间的名字，如果没有指定，使用数据库的默认空间。

USING INDEX TABLESPACE tablespace
该子句允许表空间的选择，在该表空间中和 UNIQUE 或 PRIMARY KEY 相联系的索引将会被创建。如果没有指定，则使用数据库默认表空间。

DISTRIBUTED BY (column, [ ... ] )
DISTRIBUTED RANDOMLY
使用来声明数据库中表的分布策略。 DISTIBUTED BY 使用在分布键中声明的一行或者多行做哈希分布。对于最均匀的数据分布，该分布键应当是表的主键或者一个唯一列（或者唯一多列）。如果这是不可能的，则用户可能会选择 DISTRIBUTED RANDOMLY，该策略会循环发送数据到 Segment 实例。
该数据库服务器配置参数 gp_create_table_random_default_distribution 控制默认表分布策略，如果当用户创建表的时没有指定 DISTRIBUTED BY 子句。遵循以下规则来创建表，当没有指定分布策略时。
如果参数的值时 off（也是默认值），数据库基于命令选择表分布键。如果在表的创建命令中指定了该 LIKE 或 INHERITS 子句，则该创建的表使用同源表或者父级表的分布键相同的分布键。
如果该参数设置成了 on，则数据库遵循以下规则：
- 如果没有指定 PRIMARY KEY 或 UNIQUE 列，则该表分布式随机的（DISTRIBUTED RANDOMLY）。即使表的创建命令包含 LIKE 或者 INHERITS 子句，该表的分布还是随机的。
- 如果指定了 PRIMARY KEY 或 UNIQUE 列，则DISTRIBUTED BY 子句必须也要指定。如果没有指定 DISTRIBUTED BY 子句作为表创建命令的一部分，则命令失败。
关于该参数的信息，参阅“服务器配置参数”。

PARTITION BY
声明一列或多列，根据该列来将表分区。
当创建一个分区表，数据库使用指定的表名创建根分区表（该根分区）。数据库也会根据用户指定的分区选项创建子分区包括里面表的层次结构，子表。该数据库 *pg_partition* 系统视图包含子分区表的信息。
对于每个分区级别（每个表的层次结构），分区表做多可以有32,767 个分区。
注意： 数据库将分区表数据存储在叶子表中，子表的层次结构中的最低级表用于分区表。

partition_type
声明分区类型：LIST（值列表）或者 RANGE（数字或日期范围）。

partition_specification
声明要创建各个分区，每个分区可以被单独定义或者为范围分区，用户可以使用 EVERY 子句（用一个 START 和可选的 END 子句）来定义用于创建各个分区的增量模式。
- **DEFAULT PARTITION** **name**：声明一个默认分区，当数据不匹配存在的分区时，则被插入到默认分区中。没有默认分区的设计将拒绝与现有分区不匹配的新的数据行的插入。
- **PARTITION** **name**：声明要用于分区的名字，使用以下命名约定创建分区：parentname_level#_prt_givenname。
- **VALUES** ：对于列表分区，定义分区会包含的值。
- **START** ：对于范围分区，定义分区的开始范围值。默认的是，开始值为 INCLUSIVE。 例如，如果用户声明了 '2016-01-01'的开始日期，则该分区会包含所有大于等于 '2016-01-01'的日期。通常， START 表达式的数据类型和分区键列的数据类型是一样的。如果不是这样，用户必须显式地转换为预期的数据类型。
- **END** ：对于范围分区，定义分区的结束范围值。默认的是，结束值是 EXCLUSIVE。 例如，如果用户定义了 '2016-02-01'的结束日期，则该分区将会包含所有小于该 '2016-02-01'的日期。通常， END 表达式的数据类型和分区键列的数据类型是一样的。如果不是这样，用户必须显式地转换为预期的数据类型。
- **EVERY** ：对于范围分区，定义如何将值从 START 增加到 END 以创建单个分区。通常，EVERY 表达式的数据类型和分区键列的数据类型相同。如果不是这样，则用户必须显式的准换为预期的数据类型。
- **WITH** ：设置分区的存储选项，例如，用户可能希望老分区是追加优化表，而较新的分区则为常规的堆表。
- **TABLESPACE** ：要创建的分区所在的表空间的名字。

SUBPARTITION BY
声明一列或多列来对表的第一级分区进行子分区。子分区规范的格式与上述分区规范的格式相似。

SUBPARTITION TEMPLATE
用户可以选择在声明一个用于创建自分区（较低级字表）的子分区模板，而不是为每个分区单独声明每个子分区定义。然后，此子分区规范将应用于所有父分区。

## 注意

- 在数据库中（一个基于 Postgres 的系统）数据类型 VARCHAR 或 TEXT 处理添加到文本数据后的补充（添加到最后一个非空格字符后面的空格）作为有效的字符。而数据类型 CHAR 则不会。
数据库中，CHAR(n) 类型的值被填充尾部空格来达到指定的宽度 n。该值存储并显示空格。然而，该添加的空格被视为语义不重要的。当值分布时，尾部的空格被忽略。当比较 CHAR 类型的值时，尾部的空格也被视为语义不重要的，并且将字符值转化为其他字符串类型之一时，尾部空格被删除。

- 不建议在新的应用中使用 OIDs：在可能的情况下，使用 SERIAL 或其他序列生成器作为表的主键的首选。但是如果用户的应用确实使用 OID 来标识表的特定行，则推荐在该 OID 列上创建唯一的约束，以确保表中的 OID 确实唯一标识行，即使在计数器轮回之后。避免假设 OID 在多表之间（across）是唯一的；如果用户需要数据库范围内的唯一标识符号，则可以使用表 OID 和行 OID 的组合。

- 数据库对主键和涉及表中*分布键* 的列的唯一约束有一些特殊的条件。对数据库中强制执行的唯一约束，表必须是哈希分布的（不是 DISTRIBUTED RANDOMLY），约束列必须表的分布键列（或超集）相同。此外，分布键必须是列约束的左子集并且列的顺序是正确的。例如，如果主键是（a，b，c），该分布键只能是以下集合之一：（a），（a，b），或（a，b，c）。
主键约束仅仅是唯一约束和非空约束的组合。
数据库自动创建 UNIQUE 索引为每个 UNIQUE 或 PRIMARY KEY 约束来强制执行唯一性。因此，无需为主键列显式创建索引。在追加优化表上不允许使用UNIQUE 和 PRIMARY KEY 约束，因为由约束创建的 UNIQUE 索引在追加优化表上不允许。数据库不支持外键约束。
对于继承的表，唯一约束，主键约束，索引和表权限在当前实现中不会继承。
- 对于追加优化表，UPDATE 和 DELETE 在序列化事务中不被允许，并且会导致事务中断。CLUSTER，DECLARE...FORUPDATE 和 触发器在追加优化表中不支持。

- 要将数据插入到分区表中，请指定根分区表，即用 CREATE TABLE 命令创建的表。用户也可以在 INSERT 命令中指定分区表的叶子表。如果数据不符合指定的叶子表，则会返回错误。不支持在 INSERT 命令中指定不是叶子表的子表。不支持在分区表任何子表上执行 DML 命令，如 UPDATE 和 DELETE。这些命令必须在根分布表上执行，即用 CREATE TABLE 命令创建的表。

- 这些表存储选项的默认值可以通过服务器配置参数 gp_default_storage_option 指定。
 - APPENDONLY
 - BLOCKSIZE
 - CHECKSUM
 - COMPRESSTYPE
 - COMPRESSLEVEL
 - ORIENTATION
 
该默认值可以设置于数据库，模式和用户。关于设置存储选项的信息，请参阅服务器配置参数 gp_default_storage_options。

重要：当前数据库遗传优化器允许具有多列（复合）分区键的列表分区。GPORCA 不支持复合键，所以不建议使用复合分区键。

## 示例

创建一个名为 rank 的表在名为 baby 的模式中并且使用 rank，gender 和 year来分布数据：

```sql
CREATE TABLE baby.rank (id int, rank int, year smallint, 
gender char(1), count int ) DISTRIBUTED BY (rank, gender, 
year);
```

创建表 films 和表 distributors（默认会使用主键作为的分布键）：

```sql
CREATE TABLE films (
code        char(5) CONSTRAINT firstkey PRIMARY KEY,
title       varchar(40) NOT NULL,
did         integer NOT NULL,
date_prod   date,
kind        varchar(10),
len         interval hour to minute
);
 
CREATE TABLE distributors (
did    integer PRIMARY KEY DEFAULT nextval('serial'),
name   varchar(40) NOT NULL CHECK (name <> '')
);
```

创建 gzip-压缩的追加优化表：

```sql
CREATE TABLE sales (txn_id int, qty int, date date) 
WITH (appendonly=true, compresslevel=5) 
DISTRIBUTED BY (txn_id);
```

创建3级分区表使用，使用子分区模板和每级的默认分区：

```sql
CREATE TABLE sales (id int, year int, month int, day int, 
region text)
DISTRIBUTED BY (id)
PARTITION BY RANGE (year)
 
  SUBPARTITION BY RANGE (month)
    SUBPARTITION TEMPLATE (
       START (1) END (13) EVERY (1), 
       DEFAULT SUBPARTITION other_months )
 
  SUBPARTITION BY LIST (region)
    SUBPARTITION TEMPLATE (
       SUBPARTITION usa VALUES ('usa'),
       SUBPARTITION europe VALUES ('europe'),
       SUBPARTITION asia VALUES ('asia'),
       DEFAULT SUBPARTITION other_regions)
 
( START (2008) END (2016) EVERY (1),
  DEFAULT PARTITION outlying_years);
```

## 兼容性

CREATE TABLE 命令服从 SQL 标准，还有以下的例外：
- **临时表**：在 SQL 标准中，在需要他们的每个会话中，临时表只定义一次并自动存在（从空的内容开始）。数据库需要每个会话为每个要使用的临时表发出自己的 CREATE TEMPORARY TABLE 命令。这允许不同的会话为不同目的使用相同的临时表名称，而标准的方法限制给定临时表名的实例具有相同的表结构
在全局和本地临时表之间的标准区别不存在于数据库中。数据库会在临时表的声明中接收 GLOBAL 和 LOCAL 关键字，但是他们没有影响。
如果 ON COMMIT 子句被省略，该 SQL 标准指定默认行为为 ON COMMIT DELETE ROWS。而然，数据库中的默认行为为 ON COMMIT PRESERVE ROWS。该 ON COMMIT DROP 选项不存在与 SQL 标准中。

- **列检查约束**：该 SQL 标准说 CHECK 列约束可能仅指所应用到的列；只有 CHECK 表约束可能指定到多列。数据不强制执行该约束，它对待列和表的约束一样。

- **NULL 约束**：该 NULL 是数据库对SQL标准的扩展，为了是和其他数据库系统的兼容（为了和 NOT NULL 约束的对称）。因为它是任何列的默认值，因此不需要它的存在。

- **继承**：多重继承通过 INHERITS 子句是数据库语言的扩展。SQL:1999 和更高的版本使用不同的语法和语义来定义单个继承。数据库不支持 SQL：1999 版的继承。

- **分区**：表分区通过使用 PARTITION BY 子句是数据库语言扩展。

- **零列表**：数据库允许0列表的创建（例如：CREATE TABLE foo();）。这是从不支持0列表的 SQL 标准来的扩展。0列表本身不是非常有用，但是不允许他们对 ALTER TABLE DROP COLUMN 语句会创建奇怪的特殊情况的表，所以决定忽视此规范限制。

- **WITH 子句** ：该 WITH 子句是数据库扩展；存储参数和 OID 都不是 SQL 标准中的。

- **表空间**：该表空间的概念 SQL 标准的一部分。 该子句 TABLESPACE 和 USING INDEX TABLESPACE 是扩展。

- **数据分布**：该数据库并行和分布数据库的概念不是 SQL 标准的一部分。该 DISTRIBUTED 子句是扩展。

## 另见
ALTER TABLE、DROP TABLE、CREATE EXTERNAL TABLE、CREATE TABLE AS
