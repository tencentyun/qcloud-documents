## 概述

COS Select 功能仅支持 SELECT SQL 查询指令，以便检索所需的部分数据，减少传输的数据量。这样可以减少成本，同时降低请求延时。以下是 SELECT 查询支持的标准子句：

- SELECT 语句
- FROM 子句
- WHERE 子句
- LIMIT 子句

> !COS Select 当前暂不支持子句查询或者 joins。

## SELECT 语句

SELECT 语句可以实现从 COS 对象中检索到您所希望看到的数据，您可以以列的名称、函数或者表达式等维度进行查询，并以一个列表的形式返回查询结果。SELECT 语句调用格式如下：

```shell
SELECT *
SELECT projection [ AS column_alias | column_alias ] [, ...]
```

第一句 SELECT 语句带有`*`（星号），将返回 COS 对象中的所有列。第二句 SELECT 语句使用用户自定义输出标量表达式，**projection**为每列创建自定义名称的输出列表。

## FROM 子句

COS Select 支持以下形式的 From 子句：

```shell
FROM table_name
FROM table_name alias
FROM table_name AS alias
```

其中，table_name 指的是存储在 COS 的某个对象，该对象可以是标准存储类型，也可以是低频存储类型。它类似于传统关系数据库，可以将 table_name 视为一个数据库结构，其中包含一个表的多个视图。

参照 SQL 的设计标准，FROM 子句将会根据 WHERE 子句设定的筛选条件，从 table_name 中筛选出相应的结果返回。
对于存储在 COS 的 JSON 格式对象，用户可以通过以下形式的 FROM 子句进行查询：

```shell
FROM COSObject[*].path
FROM COSObject[*].path alias
FROM COSObject[*].path AS alias
```

如果采用这种形式的 FROM 子句，用户可以从 JSON 格式的对象中检索相应的数据。您可以通过如下格式定义 path 参数：

- 通过对象的**字段名称** ：`.*name*` 或 `['*name*']`
- 通过对象的**通配符**：`.*`
- 通过数组的**索引**`[*index*]`
- 通过数组的**通配符**： `[*]`

> !
- 此类调用形式仅支持 JSON 格式的对象。
- 通配符至少返回一条记录。如果没有匹配的记录，COS Select 将返回一个 MISSING。如果序列操作执行完毕后，整个检索结果中均无匹配记录，则 COS Select 将会把 MISSING 替换为空记录。
- 聚合函数（AVG，COUNT，MAX，MIN，SUM）将忽略 MISSING 值。
- 如果您在使用通配符时未提供别名，可以引用路径中的最后一个元素。例如，您可以通过`SELECT price FROM COSObject[*].books[*].price`从书籍列表中查询所有价格。如果路径以通配符而不是以字段名结束，可以使用`_1`来引用行。在这种情况下，您可以使用`SELECT _1.price FROM COSObject[*].books[*]`进行查询，而不是`SELECT price FROM COSObject[*].books[*].price`。
- 通常情况下，COS Select将JSON文件视为一个具有根键值的数组。因此，即便您即将查询的JSON对象只有一个根元素，FROM 子句仍旧需要搭配`COSObject[*]`使用。出于兼容性考虑，COS Select允许您在未包含路径的情况下使用通配符。在这种情况下，`FROM COSObject`和`FROM COSObject[*] as COSObject`等效。如果您将路径包含在查询语句中，您必须使用通配符。这种情况下，`FROM COSObject` 和 `FROM COSObject[*].*path*`都是合法查询指令， `FROM COSObject.*path*`则是非法指令。

**Select 案例**
如下为该案例的待查询数据和查询指令：

```shell
{
    "Rules": [
        {"id": "id-1", "condition": "x < 29"},
        {"condition": "y > x"},
        {"id": "id-2", "condition": "z = DEBUG"}
    ]
},
{
    "created": "April 7",
    "modified": "June 6"
}
```

```shell
SELECT id FROM COSObject[*].Rules[*].id
```

```shell
{"id":"id-1"},
{},
{"id":"id-2"},
{}
```

COS Select 将输出以下结果： 

- `{"id":"id-1"}`：JSON 文件中`COSObject[0].Rules[0].id`存在匹配的元素。
- `{}`：JSON 文件中`COSObject[0].Rules[0].id`无匹配元素，返回 MISSING，并在最终输出时替换为空值。
- `{"id":"id-2"}`：JSON 文件中`COSObject[0].Rules[0].id`存在匹配的元素。
- `{}`：JSON 文件中`COSObject[1]`与 Rules 元素不匹配，返回 MISSING，并在最终输出时替换为空值。

如您不希望 COS Select 在找不到匹配项时返回空值，您可以通过 WHERE 子句过滤掉 MISSING 值。如下查询指令是相应的调用方式，返回结果中不包含空值：

```shell
SELECT id FROM COSObject[*].Rules[*].id WHERE id IS NOT MISSING
```

```json
{"id":"id-1"},
{"id":"id-2"}
```

## WHERE 子句

WHERE 子句使用以下语法：

```shell
WHERE condition
```

WHERE 子句通过 **condition** 进行过滤。**condition** 是一种可以返回布尔结果的表达式，只有返回值为 TRUE 的行才会在结果中输出。

## LIMIT 子句

LIMIT 子句使用以下语法：

```shell
LIMIT number
```

LIMIT 子句限制每次查询返回的记录数量，您可以通过 **number** 参数指定这个限制。

## 访问属性

SELECT 和 WHERE 子句可以通过以下任意方式选择查询的字段，您可以根据文件格式是 CSV 还是 JSON 进行选择。

#### CSV

- **列编号**：您可以通过 `_N`指定查询第 N 列的数据。对于任意一份 CSV 文件，列编号从1开始递增。如第一列编号为`_1` ，第二列编号为`_2` 。在 SELECT 和 WHERE 子句中，通过`_N`或者`alias._N`指定需要查询的列均为合法的方式。
- **列表头**：如果待查询的 CSV 文件中有表头， SELECT 和 WHERE 子句中可以通过这些表头指定需要查询的列。在 SQL 语句中，您可以在 SELECT 和 WHERE 子句中通过`alias.column_name` 或者`column_name`的方式指定。

#### JSON 

- **文档（Document）**：您可以通过`alias.name`的方式访问 JSON 文档。嵌套数组则可以通过如`alias.name1.name2.name3`的方式访问。
- **列表（List）**：您可以通过索引访问列表中的元素，索引从0开始编号，并使用`[]`操作符。例如，您可以通过`alias[1]`访问 JSON 列表中的第2个元素。如果您需要访问嵌套数组，也可以通过如`alias.name1.name2[1].name3`这样的方式进行访问。

**示例** 
以下为该示例的数据样本：

```shell
{
	"name": "Leon",
	"org": "Tencent",
	"projects":
		[
		 {"project_name":"project1", "completed":true},
		 {"project_name":"project2", "completed":false}
		]
}
```

- 示例 1：以下为在数据样本中查询 name 的 SQL 语句和查询结果：
  ```shell
  Select s.name from COSObject s
  ```
  ```shell
  {"name":"Leon"}
  ```
- 示例 2：以下为在数据样本中查询 project_name 的 SQL 语句和查询结果：
  ```shell
  Select s.projects[0].project_name from COSObject s
  ```
  ```shell
  {"project_name":"project1"}
  ```

## 表头和属性名称的大小写敏感性

您可以使用双引号来标注 CSV 文件的表头和 JSON 文件的属性名称是否大小写敏感。如果不添加双引号，则说明表头/属性名是大小写不敏感的。在您设定不明确的情况下，COS Select 可能会抛出异常。

- 示例 1：查询表头/属性名称中有"NAME"的对象。
  以下 SQL 示例未使用双引号，表明是大小写不敏感的，由于表中有这个表头，所以最终会成功返回数值。
  ```shell
  SELECT s.name from COSObject s
  ```

  以下 SQL 示例使用双引号，表明是大小写敏感的。由于表中实际上未包含这个表头，所以最终会返回400错误`MissingHeaderName`。
  ```shell
  SELECT s."name" from COSObject s
  ```

- 示例 2：查询表头/属性名称中有"NAME"和"name"的对象。
  以下 SQL 示例未使用双引号，表明是大小写不敏感的，由于表中同时存在"NAME"和"name"两个表头，查询指令设定不明确，会抛出异常 AmbiguousFieldName。
  ```shell
  SELECT s.name from COSObject s
  ```

  以下 SQL 示例使用了双引号，表明是大小写敏感的，由于表中已经存在"NAME"这个表头，会成功返回查询结果。
  ```shell
  SELECT s."NAME" from COSObject s
  ```

## 使用保留字段作为用户自定义字段

COS Select 的 SQL 表达式具有一些保留字段，包含了函数名称，数据类型，操作符等。在某些情况下，用户可能会使用这些保留字段作为 CSV 文件的列表头或者 JSON 文件的属性名称，这时候可能与保留字段存在冲突。在这种情况下，您可以使用双引号来表明您正在使用自定义字段，否则 COS 将返回`400 parse error`。

如您需要查阅完整的保留字段列表，请参见 [保留字段](https://cloud.tencent.com/document/product/436/37638)。

- 示例：待查询的对象的表头/属性名称具有一个保留字段"CAST"。
  以下 SQL 示例使用了双引号表明 CAST 是用户自定义字段，将成功返回查询结果。
  ```shell
  SELECT s."CAST" from COSObject s
  ```
  以下 SQL 示例未使用双引号表明 CAST 是用户自定义字段，COS 将作为保留字段处理，将返回`400 parse error`。
  ```shell
  SELECT s.CAST from COSObject s
  ```

## 标量表达式

在 SELECT 语句和 WHERE 子句中，您可以使用 SQL 标量表达式（返回标量的表达式）。目前 COS Select 支持以下形式：

- **literal**：SQL 文本。
- **column_reference**：column_name 或者 alias.column_name。
- **unary_op** **expression**： SQL 一元运算符。
- **expression** **binary_op** **expression**：SQL 二元运算符。
- **func_name**：被调用的标量函数的名称。
- **expression** [ NOT ] BETWEEN **expression** AND **expression**
- **expression** LIKE **expression** [ ESCAPE **expression** ]
