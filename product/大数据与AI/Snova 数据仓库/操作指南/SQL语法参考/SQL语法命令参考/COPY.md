在一个文件和一个表之间复制数据。

## 概要

```sql
COPY table [(column [, ...])] FROM {'file' | STDIN}
     [ [WITH] 
       [BINARY]
       [OIDS]
       [HEADER]
       [DELIMITER [ AS ] 'delimiter']
       [NULL [ AS ] 'null string']
       [ESCAPE [ AS ] 'escape' | 'OFF']
       [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
       [CSV [QUOTE [ AS ] 'quote'] 
            [FORCE NOT NULL column [, ...]]
       [FILL MISSING FIELDS]
       [[LOG ERRORS]  
       SEGMENT REJECT LIMIT count [ROWS | PERCENT] ]
 
COPY {table [(column [, ...])] | (query)} TO {'file' | STDOUT}
      [ [WITH] 
        [ON SEGMENT]
        [BINARY]
        [OIDS]
        [HEADER]
        [DELIMITER [ AS ] 'delimiter']
        [NULL [ AS ] 'null string']
        [ESCAPE [ AS ] 'escape' | 'OFF']
        [CSV [QUOTE [ AS ] 'quote'] 
             [FORCE QUOTE column [, ...]] ]
      [IGNORE EXTERNAL PARTITIONS ]
```

## 描述
COPY用于数据库表和标准文件系统文件之间移动数据。COPY TO把一个表的内容复制到另一个文件（如果复制，则根据Segment的ID复制多个文件ON SEGMENT），而COPY FROM 则从一个文件复制数据到一个表（把数据追加到表中原有数据）。COPY TO也能复制一个SELECT查询的结果。

>!COPY FROM当前不支持FROM带ON SEGMENT选项的COPY TO产生的Segment文件拷贝数据，但是其他工具可以被用来恢复数据。

如果指定了一个列表，COPY将只把指定列的数据复制到文件或者从文件复制数据到指定列。如果表中有列不在列表中，COPY FROM将会为那些列插入默认值。

带一个文件名的COPY指示数据库服务器直接从一个文件读取或者写入到一个文件。该主机必须可访问该文件，并且必须从主机的角度指定该名称。

当COPY和ON SEGMENT选项一起被使用时，COPY TO导致Segment创建面向Segment的个体文件，这些文件保留在Segment主机上。ON SEGMENT的文件参数是用字符串文字&lt;SEGID&gt;（必须）并使用绝对路径或&lt;SEG_DATA_DIR&gt;字符串文字。 当运行COPY操作时，Segment的ID和Segment数据目录的路径被替换为字符串文字值。

ON SEGMENT选项允许用户将表数据复制到Segment上的文件，以用于诸如在集群之间迁移数据或执行备份等操作。通过ON SEGMENT选项创建的Segment数据可以通过gpfdist等工具进行恢复，这对于高速数据加载是有用的。

当指定STDIN或STDOUT时，通过客户端和主机之间的连接传输数据。STDOUT不能与ON SEGMENT选项一起使用。

如果使用了SEGMENT REJECT LIMIT，则COPY FROM操作将在单行错误隔离模式下运行。在此版本中，单行错误隔离模式仅适用于具有格式错误的输入文件中的行， 例如额外或缺少属性，错误数据类型的属性或无效的客户端编码序列。诸如违反了NOT NULL、CHECK或UNIQUE约束的约束错误仍将以 'all-or-nothing' 输入模式进行处理。
用户可以指定可接受的错误行数（以每个Segment为单位），之后整个COPY FROM操作将被终止，并且不再加载任何行。错误行的计数以每个Segment而不是整个加载操作为基础。如果未达到每Segment的拒绝限制，则将加载不包含错误的所有行，并丢弃任何错误行。要保留错误行进一步检查， 请指定LOG ERRORS子句以补货错误日志信息。错误信息和行存储在数据库中。

## 输出
成功完成后， COPY命令将返回表单的命令标签， 其中count是复制的行数：

```sql
COPY count
```

如果单行隔离模式下运行COPY FROM命令，如果由于格式错误而未加载任何行，则将返回以下通知消息，其中count是拒绝的行数：

```sql
NOTICE: Rejected count badly formatted rows.
```

## 参数
table
一个现有表的名称（可以是方案限定的）。

column
可选的要被复制的列列表。如果没有指定列列表，则该表的所有列都会被复制。
当以文本格式复制时，默认为一列数据类型bytea最高可达256MB。

query
一个SELECT或VALUES其结果将被复制。请注意，查询需要括号。

file
输入或者输出文件的路径名。

STDIN
指定输入来自客户端应用。

STDOUT
指定输出会去到客户端应用。

ON SEGMENT
拷贝表数据以创建单独的面向Segment的文件，这些文件保留在Segment主机上。COPY FROM该ON SEGMENT 目前不支持输出。COPY TO STDOUT不能用于ON SEGMENT。&lt;SEG_DATA_DIR&gt;和&lt;SEGID&gt;字符串文字用于ON SEGMENT，具有以下语法：

```sql
COPY table TO '<SEG_DATA_DIR>/gpdumpname<SEGID>_suffix' ON SEGMENT; 
```

镜像Segment不会将其数据拷贝到Segment文件中。


&lt;SEG_DATA_DIR&gt;
表示ON SEGMENT拷贝的Segment数据目录的完整路径的字符串文字。支架是用于指定路径的字符串文字的一部分。 COPY运行时，用字符串文字替换段路径。 (可选，可以用绝对路径代替使用&lt;SEG_DATA_DIR&gt;字符串文字。)

&lt;SEGID&gt;
表示复制 ON SEGMENT时要复制的Segment的内容ID号的字符串文字。&lt;SEGID&gt;是 ON SEGMENT选项的必需部分。 支架是用于指定路径的字符串文字的一部分。 COPY运行时， COPY将使用内容ID替换字符串文字。

BINARY
使所有数据以二进制格式存储或读取，而不是文本。用户不能指定DELIMITER、NULL或CSV 二进制模式下的选项。
当以二进制格式复制时，一行数据最多可达1GB。

OIDS
指定复制每行的OID。（如果为没有OID的表指定了OIDS，或者在复制查询的情况下，则会引发错误。）

分隔符
单个ASCII字符，用于分隔文件每行（行）中的列。默认是文本模式下的制表符，逗号在CSV模式。

空字符串
表示空值的字符串。 文本模式中的默认值为\N (反斜杠-N) ， CSV模式中不含引号的空值。 在不想将空值与空字符串区分开的情况下，即使在文本模式下，也可能更喜欢空字符串。 当使用COPY FROM时，与字符串匹配的任何数据项将被转储为空值，因为用户应该确保使用与COPY TO中使用的字符串相同。

escape
指定用于C转义序列的单个字符(如 \n、\t、\100等) 和引用可能被视为行或列分隔符的数据字符。确保选择在实际列数据中的任何地方都不使用的转义字符。默认转义符为\ (反斜杠)用于文本文件或 " (双引号) 用于CSV文件, 但是可以指定任何其他字符来表示转义。还可以通过指定值OFF'作为转义值。这对于诸如Web日志数据之类的数据非常有用，该数据具有许多嵌入式反斜杠，这些反斜杠不是要转义的。

NEWLINE
指定数据文件中使用的换行符— LF（换行，0x0A）、CR（回车，0x0D）或者CRLF（回车加换行，0x0D 0x0A）。如果未指定，数据库的Segment将通过查看其接收的第一行数据并使用遇到的第一个换行符来检测换行类型。

CSV
选择逗号分隔值（CSV）模式。

HEADER
指定一个文件包含一个标题行和文件中每列的名称。在输出时，第一行包含表中的列名，在输入时，第一行将被忽略。

引用
以CSV模式指定引用字符。默认是双引号。

FORCE QUOTE
在CSV COPY TO模式下，强制引用用于每个指定列中的所有非NULL值。 NULL值输出从不引用。

FORCE NOT NULL
在CSV COPY FROM模式下，处理每一个指定的列，就好像它被引用一样， 因此不是NULL值。对于CSV模式默认的字符串（两个分割符之间不存在），这会导致将值作为零长度字符串计算。

FILL MISSING FIELDS
在TEXT和CSV中的COPY FROM中，指定FILL MISSING FIELDS时，当一行数据在行或行的末尾缺少数据字段时，将丢失尾字段值设置为 NULL（而不是报告错误）。空行，具有NOT NULL在TEXT和CSV中的COPY FROM中，指定FILL MISSING FIELDS时，当一行数据在行或行的末尾缺少数据字段时，将丢失尾字段值设置为NULL（而不是报告错误）。 空行，具有NOT NULL约束的字段和行上的尾随分隔符仍然会报告错误。

LOG ERRORS
这是一个可选的子句，可以在SEGMENT REJECT LIMIT之前捕获有关格式错误的行的错误日志信息。
错误日志信息在内部存储，并使用数据库内置SQL函数 gp_read_error_log()访问。

SEGMENT REJECT LIMIT count [ROWS | PERCENT]
在单行模式下运行COPY FROM操作。如果输入行具有格式错误，则它们将被丢弃，前提是在加载操作期间在任何数据库Segment实例上未达到拒绝限制计数。拒绝限制计数可以指定为行数（默认值）或总行数百分比（1-100）。 如果PERCENT被使用，每个Segment只有在处理参数 gp_reject_percent_threshold 所指定的行数之后才开始计算行百分比。
gp_reject_percent_threshold默认值为300行。诸如违反NOT NULL、CHECK或UNIQUE的约束错误仍将以 'all-or-nothing' 输入模式进行处理。如果达到限制，如果没有达到限制，所有好的行将被加载，任何错误将被丢弃。
>!数据库限制了可能包含格式错误的初始行数SEGMENT REJECT LIMIT不是首先被触发或没有被指定。如果前1000行被拒绝，COPY操作停止并回滚。

可以使用Database服务器配置参数更改初始拒绝行数的限制gp_initial_bad_row_limit。 

IGNORE EXTERNAL PARTITIONS
从分区表复制数据时，数据不会从作为外部表的叶子分区复制。当不复制数据时，会将消息添加到日志文件中。
如果未指定此子句，并且数据库尝试从作为外部表的叶子分区复制数据，则会返回错误。
有关指定从作为外部表的叶子分区复制数据的SQL查询的信息，请参阅“注释”。

## 注释
COPY只能与表一起使用，而不能与外部表或视图一起使用。 但是，用户可以写COPY (SELECT * FROM viewname) TO ...

要从具有作为外部表的叶子分区的分区表复制数据，请使用SQL查询来复制数据。例如，如果表my_sales包含一个叶子子分区，这是一个外部表，这个命令COPY my_sales TO stdout返回错误。 此命令将数据发送到：

```sql
COPY (SELECT * from my_sales ) TO stdout
```

该BINARY关键字将所有数据存储/读取为二进制格式而不是文本。它比正常的文本模式要快一点，但二进制格式的文件在机器架构和数据库版本之间的移植性更低。 另外，用户不能运行COPY FROM 在单行错误隔离模式下，如果数据是二进制格式。

用户必须对其值由COPY TO读取的表具有SELECT权限，并在COPY FROM插入的值上插入特权。

在COPY命令中a在COPY命令中命名的文件由数据库服务器直接读取或写入，而不是由客户端应用程序读取或写入。因此，它们必须驻留在数据库主机主机上或可访问，而不是客户端。 它们必须由数据库系统用户（服务器运行的用户ID）而不是客户机可访问和可读写。 COPY命名文件只允许数据库超级用户使用，因为它允许读取或写入服务器具有访问权限的任何文件。

COPY FROM将调用目标表上的任何触发器和检查约束。 但是，它不会调用重写规则。 请注意，在此版本中，不对单行错误隔离模式评估对约束的违规。

COPY的输入输出受DateStyle影响。为了确保对可能使用非默认DateStyle设置的其他数据库安装的可移植性，在使用 COPY TO之前，应将DateStyle设置为ISO。

在文本模式下从文件复制XML数据时，服务器配置参数xmloption影响复制的XML数据的验证。如果值为content（默认），XML数据被验证为XML内容片段。如果参数值为 ocument，XML数据被验证为XML文档。如果XML数据无效，COPY返回错误。

默认情况下，COPY在第一个错误时停止运行。在COPY TO的情况下，这不应该导致问题但是目标表已经在COPY FROM中接受了较早的行。这些行将不可见或可访问，但他们仍占用磁盘空间，如果故障发生在大的COPY FROM操作中这可能会相当大量的浪费磁盘空间。用户可能希望VACUUM来恢复浪费的空间。另一个选择时使用单行错误隔离模式来过滤错误行，同时仍然加载好的行。

当用户指定LOG ERRORS子句时，数据库捕获读取外部表数据时发生的错误。用户可以查看和管理捕获的错误日志数据。

- 使用内置的SQL函数 gp_read_error_log('table_name')。需要在table_name上有SELECT特权。 此示例显示使用 COPY命令加载到表ext_expenses中的数据错误日志信息：
```
SELECT * from gp_read_error_log('ext_expenses');
```
该函数返回FALSE如果table_name表不存在。
- 如果指定的表存在错误日志数据，新的错误日志数据将附加到现有的错误日志数据。错误日志信息不会复制到镜像Segment。
- 使用内置的SQL函数gp_truncate_error_log('table_name') 删除table_name中的错误日志数据。它需要表所有者权限此示例删除将数据移动到表中时捕获的错误日志信息ext_expenses:
```
SELECT gp_truncate_error_log('ext_expenses'); 
```
函数返回FALSE if table_name表不存在。

指定 * 通配符删除当前数据库中现有表的错误日志信息。指定字符串 *.*删除所有数据库错误日志信息，包括由于以前的数据库问题而未被删除的错误日志信息。如果 * 没被指定， 则需要数据库所有者权限。如果*.* 被指定，需要操作系统超级用户权限。

当不是超级用户的数据库用户运行时COPY命令时，命令可以由资源队列控制。必须配置资源队列ACTIVE_STATEMENTS参数，指定分配给该队列的角色可以执行的查询数量的最大限制。数据库不会将消耗值或内存值应用于COPY命令， 只有消耗或内存限制的资源队列不影响运行COPY 命令。

非超级用户只能运行这些类型COPY 命令：
- COPY FROM 命令，其中源为stdin。
- COPY TO 命令，其中源为 stdout。

有关资源队列的信息，请参阅“数据库管理员指南”中的“具有资源队列的工作负载管理”。

## 文件格式

文件格式支持COPY。

**文本格式**
当使用的COPY不带BINARY或CSV选项时，读取或写入的数据是每个表行一行的文本文件。一行中的列由分隔符字符（默认选项卡）分割。列值本身是由每个属性的数据类型的输出函数生成的或输入函数可接受的字符串。使用指定的空字符串代替为空的列。如果输入文件的任何行包含比预期的更多或更少的列，COPY FROM将引发错误。如果OIDS被指定，OID作为被读取或写入第一列，位于用户数据列之前。

数据文件有两个具有COPY特殊含义的保留字符：
- 指定的分隔符（默认为tab），用于分隔数据文件中的字段。
- UNIX样式换行符（\n或 0x0a），用于指定数据文件中的新行。强烈建议应用程序生成COPY数据的应用程序将数据换行符转换为UNIX样式的换行符，而不是Microsoft Windows样式回车换行（\r\n 或0x0a 0x0d）。

如果用户的数据包含这些字符，用户必须转义该字符，因此COPY将其视为数据而不是字段分隔符或新行。

默认情况下，转义字符是文本格式文件的\（反斜杠）和 " (双引号) 为csv格式的文件。如果要使用不同的转义字符，可以使用ESCAPE AS子句。确保选择一个在数据文件中的任何位置不被用作实际数据值的转义字符。用户还可以通过使用禁用文本格式文件中的转义 ESCAPE 'OFF'。

例如，假设用户有一个具有三列的表，并且用户想使用COPY加载以下三个字段。
- 百分比 = %
- 垂直条 = |
- 反斜杠 = \

指定的分隔符是 | (管道字符)，用户指定的转义字符是* (星号)。数据文件中格式化的行将如下所示：

```sql
percentage sign = % | vertical bar = *| | backslash = \
```

请注意，使用星号（*）转义数据的一部分的管道字符。 还要注意，由于我们使用替代转义字符，我们不需要转义反斜杠。

以下字符必须在转义字符前面，如果它们显示为列值的一部分：转义字符本身，换行符，回车符和当前分隔符字符。用户可以使用ESCAPE AS子句指定其他转义符。

**CSV Format**
此格式用于导入和导出许多其他程序（如电子表格）使用的逗号分隔值（CSV）文件格式。而不是Database标准文本模式使用的转义，它会生成并识别常用的CSV转义机制。

每个记录的值由DELIMITER字符分隔。如果值包含分隔符字符，则QUOTE字符，ESCAPE 字符（默认为双引号）， NULL字符串，回车符或换行字符，则整个值为前缀，后缀为QUOTE字符。用户可以使用FORCE QUOTE强制引用在特定列中输出非NULL 。

CSV格式没有标准的方法来区分NULL值和空字符串。数据库通过COPY引用来处理 。一个NULL作为NULL字符串输出，不引用，而与NULL 字符串匹配的数据值被引用。因此，使用 默认设置，NULL写为无引号的空字符串，而空字符串用双引号（“”）写入。阅读值遵循相似的规则。用户可以使用FORCE NOT NULL来阻止特定列的NULL输出比较。

因为反斜杠不是一个特殊的字符CSV 格式，出现在行上的单个条目的数据值在输出上自动引用，并且在输入时（如果引用）不会被解释为数据结尾标记。如果用户正在加载另一个应用程序创建的文件，该应用程序具有单个未引用的列，并且值可能为\.， 用户可能需要在输入文件中引用该值。

注解： 在CSV 模式，所有字符都很重要。由空格或DELIMITER以外的任何字符包围的引用值将包含这些字符。如果用户从系统中将数据从白色空间填充到某些固定宽度的系统中，则可能会导致错误。如果出现这种情况，则在将数据导入到数据库之前，用户可能需要预处理CSV文件以删除尾随的空格。

CSV模式将会识别并生成包含嵌入回车符和换行符的引用值的CSV文件。因此，文件不是每个表行严格一行，如文本模式文件。

注解： 许多程序产生奇怪且偶然的CSV文件，因此文件格式比标准更为常规。因此，用户可能会遇到一些无法使用此机制导入的文件，COPY 可能会生成 其他程序无法处理的文件。

**二进制格式**
该 BINARY 格式由文件头，包含行数据的零个或多个元组和文件预告片组成。标题和数据是网络字节顺序

- **文件头** ：文件头由15个字节的固定字段组成，后面是可变长度的标题扩展区。固定字段是：
 - **签名** ：11字节序列PGCOPY \ n \ 377 \ r \ n \ 0 - 请注意，零字节是签名的必需部分。（签名被设计为容易地识别由非8位清理传输所掩盖的文件，该签名将通过行尾转换过滤器，丢弃的零字节，丢弃的高位或奇偶变化。）
 - **标志字段**：32位整数位掩码，用于表示文件格式的重要方面。位从0（LSB）到31（MSB）编号。请注意，该字段以网络字节顺序（最高有效字节优先）存储，以及文件格式中使用的所有整数字段。位16-31保留以表示关键文件格式问题；如果发现在此范围内设置了意外的位，读取器将中止。bit 0-15被保留以表示向后兼容的格式问题；读者应该简单地忽略在此范围内设置的任何意外的位。目前只定义了一个标志，其余的标志位必须为零（如果数据有OID，则为16：1，否则为0）。
 - **标题扩展区长度**：32位整数，标题剩余字节长度，不包括自身。目前，这是零，第一个元组立即跟随。格式的未来更改可能允许在标题中存在附加数据。读者应该默默地跳过任何不知道该怎么做的标题扩展名数据。标题扩展区域被设想为包含一系列自识别块。标志字段不是要告诉读者扩展区域是什么。标题扩展内容的具体设计留待以后发布。
- **元组**：每个元组从元组中的字段数的16位整数开始。（目前，表中的所有元组都将具有相同的计数，但可能并不总是如此）。然后，对于元组中的每个字段重复，都有一个32位长度的字， 后跟多个字段的字段数据。（长度字不包括本身，可以为零）。作为特殊情况，-1表示NULL字段值。在NULL的情况下没有值字节。
字段之间没有对齐填充或任何其他额外的数据。
目前，COPY BINARY文件中的所有数据值都被假定为二进制格式（格式代码一）。预计未来的扩展可能会添加一个头域，允许指定每列格式代码。
如果OID包含在文件中，则OID字段紧跟在字段计数字之后。 这是一个正常的字段，除了它不包括在字段计数中。 特别是它有一个长度字 - 这将允许处理4字节与8字节OID没有太多的痛苦，并将允许OID显示为null，如果有证明是可取的。
- **File Trailer**：file trailer由包含-1的16位整数组成。这很容易与元组的字段计数字区分开。如果字段计数字不是-1 -1也不是预期的列数，读者应该报告错误。 这提供额外的检查，以防止与数据不同步。

## 示例
使用垂直条（|）作为字段分隔符将表复制到客户端：

```sql
COPY country TO STDOUT WITH DELIMITER '|';
```

从文件中复制数据到country表中：

```sql
COPY country FROM '/home/usr1/sql/country_data';
```

复制到名称以'A'开头的国家/地区的文件：

```sql
COPY (SELECT * FROM country WHERE country_name LIKE 'A%') TO 
'/home/usr1/sql/a_list_countries.copy';
```

将数据从文件复制到sales表使用单行错误隔离模式和日志错误：

```sql
COPY sales FROM '/home/usr1/sql/sales_data' LOG ERRORS 
   SEGMENT REJECT LIMIT 10 ROWS;
```

要拷贝Segment数据供以后使用，使用ON SEGMENT语句。 使用 ON SEGMENT 语句的形式为:

COPY table TO '&lt;SEG_DATA_DIR&gt;/gpdumpname&lt;SEGID&gt;_suffix' ON SEGMENT;

该&lt;SEGID&gt;是必须的。 但是，用户可以替换绝对路径&lt;SEG_DATA_DIR&gt;字符串文字在路径中。

当用户传递字符串文字&lt;SEG_DATA_DIR&gt;和&lt;SEGID&gt;到 COPY，COPY将在运行操作时填写适当的值。

例如, 如果用户有表mytable以及如下所示的Segment和镜像Segment：

```sql
contentid | dbid | file segment location 
    0     |  1   |/home/usr1/data1/gpsegdir0
 
    0     |  3   | /home/usr1/data_mirror1/gpsegdir0 
 
    1     |  4   | /home/usr1/data2/gpsegdir1
 
    1     |  2   | /home/usr1/data_mirror2/gpsegdir1 
```

运行命令:

```sql
COPY mytable TO '<SEG_DATA_DIR>/gpbackup<SEGID>.txt' ON SEGMENT;
```

将导致以下文件：

```sql
/home/usr1/data1/gpsegdir0/gpbackup0.txt
/home/usr1/data2/gpsegdir1/gpbackup1.txt
```

第一列中的内容ID是插入到文件路径中的标识符 (例如：gpsegdir0/gpbackup0.txt above) 文件是在Segment主机上创建的，而不是在主服务器上，因为它们将在标准中COPY操作。使用时，不会为镜像Segment创建任何数据文件ON SEGMENT复制。

如果指定绝对路径，而不是&lt;SEG_DATA_DIR&gt;，如在声明中

```sql
COPY mytable TO '/tmp/gpdir/gpbackup_<SEGID>.txt' ON SEGMENT;
```

文件将被放置在每个段上的/tmp/gpdir中。

注解：该COPY FROM操作目前还不支持ON SEGMENT语句。像gpfdist这样的工具可以恢复数据。

## 兼容性
在SQL标准中没有COPY语句。

## 另见
CREATE EXTERNAL TABLE
