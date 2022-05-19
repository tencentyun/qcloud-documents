# Dataway 语言基础概念
Dataway 是腾讯云数据连接器服务中用于对数据进行自定义转换与处理的脚本引擎，使用 Dataway 可以编写和执行强大而复杂的数据转换脚本，在此之前需要先了解一下 Dataway 的核心概念和功能。

##  Dataway 工具箱
Dataway 提供文本模式、表达式模式和代码模式三套脚本工具集，支持各具特色的语义和语法，以应对不同的使用场景和数据需求。Dataway 编辑文本框可同时提供至多三套工具集用于数据输入（具体情况视所在组件功能设计而定），用户可根据应用需求和自身喜好，自由选用其中一套工具集。

- **文本模式**：用于数据流转，提供数据创建和传递功能。用户可以跟随可视化交互界面的指引生成所需数据或引用集成流上下文数据。
- **表达式模式**：用于简单数据转换和处理，提供轻量脚本执行功能。用户可以通过填写表达式获取所需数据。
- **代码模式**：用于复杂数据转换和处理，提供复杂脚本执行、格式化和调试等功能。用户可以通过编写脚本获取所需数据。目前支持 python3 脚本和 Java JDK8 脚本。

**集成流数据面板**同时嵌入三种模式，提供集成流上下文数据引用功能。用户均可通过可视化点选的方式，快速引用前置组件的数据。

## <span id="core-types"></span> Dataway 类型系统

 Dataway 核心类型如下，可作为 Dataway 脚本的输出结果：

| 类型名 | 中文名 | 描述 | 是否 Dataway 特有类型 |举例 |
| ----- | ---- | --------------- | --- | --------------------------------- | 
| None |  空值 | 空值类型 | 否 | <font color=red>Python</font>: None / <font color=red>Java</font>: null |
| string | 字符串 | 字符串类型 | 否 | "abc" |
| bool | 布尔值 | 布尔类型 | 否 | <font color=red>Python</font>: True/False / <font color=red>Java</font>: true/false |
| float | 浮点数 | 浮点类型 | 否 | 123.456 |
| int/Long | 整数 | 整型 | 否 | <font color=red>Python</font>: 123 / <font color=red>Java</font>: 123L | 
| list | 列表 | 序列类型容器 | 否 | <font color=red>Python</font>: [1,2,3] / <font color=red>Java</font>: new java.util.ArrayList<>() |
| dict/Map | 字典 | 键值类型容器 | 否 | <font color=red>Python</font>: {1:1, 'key': 'value'} / <font color=red>Java</font>: new java.util.HashMap<>() | 
| decimal | 十进制 | 用于精确十进制数值计算 | 否 | <font color=red>Python</font>: decimal.Decimal(1) / <font color=red>Java</font>: new java.math.BigDecimal("1") |
| datetime | 时刻 | 时刻，包括日期和时钟 | 否 | <font color=red>Python</font>: datetime.datetime.now() / <font color=red>Java</font>: java.time.OffsetDateTime.now() |
| date | 日期 | 日期 | 否 | <font color=red>Python</font>: datetime.date.today() / <font color=red>Java</font>: java.time.LocalDate.now() |
| time | 时间 | 时间 | 否 | <font color=red>Python</font>: datetime.datetime.now().time() / <font color=red>Java</font>: java.time.OffsetTime.now() |
| [**Entity**](#entity-explain) | 二进制实体 |数据连接器中的实体数据，用于代表一个二进制对象，包括 blob、mime_type、encoding 等信息 | <font color=red>是</font> | http-listener 构造消息中的 payload |
| **MultiMap** | 多值字典 | 类似于 xml 而与 dict 不同，该类型可以支持重复的 key | <font color=red>是</font> | application/www-form-urlencoded 格式的数据解析之后得到的对象 |
| **FormDataParts** | 表单数据 | 数组+列表的数据结构，类似于 Python 中的 orderDict 结构 | <font color=red>是</font> | multipart/form-data 格式的数据解析后得到的对象|
| [**Message**](#message-explain)  | 消息 |数据连接器中的消息，承载了集成流数据，包括 payload、variables、attributes 等信息 | <font color=red>是</font> | 代码模式 python 脚本 dw_process 入口函数中的 msg 参数 |
| **DataSet** | 数据集 | 数据集成中数据集，通过数据集成组件操作 |  <font color=red>是</font> | Builder 组件的输出 |
| **Record** | 单条数据 | 数据集成中的单条数据，附有 Schema | <font color=red>是</font> | 可通过 Foreach 组件遍历 DataSet 获取 |

> Dataway 核心类型在不同模式或不同语言脚本工具集中均存在对应实现，且同一类型的不同实现间可以自动映射。
> 用户可以在集成流的不同组件不同 Dataway 编辑文本框中使用不同的 Dataway 脚本工具集，不会影响核心类型的数据处理过程的连贯和精确。

> 需要注意的是，如果 Dataway 脚本的输出结果作为集成流的最终返回结果，则支持的返回值类型还会受到相应集成流组件的限制。如在以 http listener 组件作为触发器的集成流中，其最终返回结果必须是一个 Entity 类型。

除了核心类型外，不同模式或不同语言的脚本工具集额外支持部分特异类型，以贴合使用场景并提高可用性，但<font color=red>特异类型的数据无法作为 Dataway 脚本的输出结果</font>，详情请查阅文本模式、表达式模式、代码模式 Python、代码模式 Java。

##  <span id="message-explain"></span>Message 类型

在 Dataway 中，Message 类型承载了腾讯云数据连接器消息，而消息伴随集成流的执行过程传递和更新。Message 类型包含**载荷（payload）**、**变量（vars）**、**属性（attrs）**等属性，称之为**预定义属性(Predefined Properties)**，这些属性是由系统根据当前运行信息及处理的数据生成的，用于在 Dataway 脚本中获取集成流的当前上下文信息。

> Dataway 脚本以 msg 变量作为输入，该变量即 Message 类型，承载了集成流执行至当前组件节点前夕的上下文信息。

Message 类型中包含的属性及其说明如下：

| 属性名 | 获取方法（以代码模式 Python 为例） | 描述 | 属性类型 | 属性说明 |
| ----- | --- | ------- | -------- | ----- |
| 变量集 | msg.vars | 当前消息上下文中的变量集合 | 字典类型：键为字符串类型，代表变量名；值为任意[核心类型](#core-types)，代表变量值 | 已设置变量在集成流的所有后置组件节点共享，因此可用于在不同的组件节点之间进行数据整合 |
| 载荷 | msg.payload | 当前消息的载荷数据 | 任意[核心类型](#core-types) | 载荷是腾讯云数据连接器消息的负载数据，反映了组件节点的执行结果，由组件节点执行后更新，也可以通过特定组件（如"配置 payload"等）进行配置。 比如，http listener 组件会根据接收到的网络请求来构造载荷的内容，因此 listener 组件处理之后，载荷为 Entity 类型 |
| 属性集 | msg.attrs | 当前消息的属性数据集合，如消息来源、消息的头部信息等 | 字典类型：键为字符串类型，代表属性名；值为任意[核心类型](#core-types)，代表属性值 | 如果集成流触发器为 http listener，则网络请求的 headers 将会存储在 msg.attrs |
| 唯一标志 | msg.id | 当前消息的唯一标识 id | 字符串类型 | 经过一个逻辑组件，唯一标志可能会变化 |
| 序列号 | msg.seq_id | 当前消息的序列号 | 字符串类型 | 消息在集成流中流转时，序列号保持不变 |
| 错误信息 | msg.error | 当前处理上下文中的错误信息 | 字典类型：键为字符串类型，代表错误属性名；值为字符串类型，代表属性值 | 包含的内容有：'code': 错误类型；'desc'：错误描述字符串 |

##   <span id="entity-explain"></span>Entity 类型

###  Entity 类型简介

在 Dataway 中，Entity 类型承载了腾讯云数据连接器实体数据，是二进制数据的封装对象，其主要组成部分包括**原始数据（blob）**、**MIME 类型（mime_type）** 以及**编码类型 encoding**。

- **原始数据（blob）**：原始的二进制数据。
- **MIME 类型（mime_type）**：二进制数据的内容格式，例如 application/json、application/www-form-urlencoded、multipart/form-data 等。
- **编码类型（encoding）**：二进制数据的字符编码格式，例如 utf8、gbk 等。

可以通过如下方式访问 Entity 中的内容（以代码模式 Python 为例）：

- entity['^blob']：获取该二进制对象的负载数据，返回 bytes 类型的对象;
- entity['^mime_type']：获取该消息对象的 MIME 类型，返回字符串对象;
- entity['^encoding']：获取该消息对象的编码类型，返回字符串对象;


为了方便使用，Dataway 还提供了如 entity.get(attr, default=None) 等对象方法以及基于下标的选择器语法（详见[ Entity 选择器](#selectors)） 以实现快速访问功能：
- entity\['^value'\]：根据 MIME 类型和编码类型，解析负载数据，并返回解析结果，类型为[核心类型](#core-types)之一;
- entity\['xxxx'\]：根据 MIME 类型和编码类型，解析负载数据，并获取其中指定键对应值，相当于 entity\['^value'\]['xxx'];
- entity.get(attr, default=None)：根据 MIME 类型和编码类型， 解析负载数据，并获取其中指定键对应值，如果获取不到则返回默认值（默认为 None），相当于 entity['^value'].get(attr, default=None)。

在使用快速访问功能时，系统会尝试解析 Entity 中的二进制负载数据，如果解析失败会导致运行时错误。（详见[MIME 类型支持](#mime-type)）

### <span id='selectors'></span>Entity 选择器

对于常用 MIME 类型和编码类型，Dataway 支持通过选择器 (selector) 快速访问 Entity 对象内容，支持的操作类型如下：

| 下标类型                                 | 描述                                                                             | 举例                      |
| ---------------------------------------- | -------------------------------------------------------------------------------- | ------------------------- |
| 数字                                     | 访问当前数组的第 i 个元素                                                        | entity[0]            |
| 以'^'开头的字符串                | 获取元信息，例如 ^mime_type 、 ^encoding 、 ^blob（原始二进制） 、 ^value（值）   | entity['^mime_type'] |
| 普通字符（字母、数字、下划线、横杠、点） | 普通字符的 key，按名称的方式获取当前元素的子元素，如果有多个同名的，只返回第一个 | entity['list']     |

下面将对这几种选择器类型举例说明。假设输入消息的载荷 msg.payload 是一个 Entity 对象，其原始数据 blob 解析后是一个 json 数组，MIME 类型为 "application/json"，编码类型为 "utf-8"：
```json
 [{"a1":1},{"b1":1,"b2":2,"b3":3},{"c1":[1,2,3]}] 
```


1. __使用数字下标获取数据__
   
    使用数字下标可以获取 msg.payload 中的元素。如下所示，Dataway 表达式为：
```python
def dw_process(msg):
    return msg.payload[1]
```
    则表达式的输出为 dict 类型的结果： `{"b1":1,"b2":2,"b3":3}`

2. __使用'^'符号获取元数据__
   
    要获取 msg.payload 的元数据，可以使用'^'符号。如下所示，Dataway 表达式为：
```python
def dw_process(msg):
    return {
        "mimeType" : msg.payload["^mime_type"],
        "encoding": msg.payload["^encoding"],
        "blob": msg.payload["^blob"],
        "value": msg.payload["^value"],
    }
```

    则表达式的输出为 dict 类型的结果：
```python
{
    "mimeType" : "application/json",
    "encoding": "utf-8",
    "blob": b'[{"a1":1},{"b1":1,"b2":2,"b3":3},{"c1":[1,2,3]}]',
    "value": [{"a1":1},{"b1":1,"b2":2,"b3":3},{"c1":[1,2,3]}]
}
```


3. __使用普通字符获取元素__
   
    现在我们假设 msg.payload 值仍为 Entity 类型，其 MIME 类型仍为 "application/json"，编码类型仍为 "utf-8"，但负载数据 blob 解析后变成了：
```json
{"a1":1,"b1":1,"b2":2,"b3":3,"c1":[1,2,3]}
```
		
 如下所示，Dataway 表达式为：
```python
def dw_process(msg):
    return {
        "a1" : msg.payload["a1"],
        "b2": msg.payload["b2"],
        "c1": msg.payload['c1'],
    }
```

    则表达式的输出为 dict 类型的结果：
```python
{
    "a1" : 1,
    "b2": 2,
    "c1": [1,2,3]
}
```


###  Entity 类型对象构造（以代码模式 Python 为例）

1. <span id="from-value"></span> **值构造方法（Entity.from_value）**：将数据 data 封装为 Entity 类型并返回。如下所示：
```python
Entity.from_value(data, mime_type=None, encoding="utf-8")
```
 值构造方法根据给定的 MIME 类型和编码类型对 data 进行序列化得到 bytes 类型的原始数据，然后再封装为 Entity 类型返回。
    
    其中 mime_type 参数必传，目前支持的 MIME 类型有 text/plain、application/json（别名 text/json）、application/x-www-form-urlencoded、application/csv、application/xml（别名 text/xml）和 multipart/form-data 六种；encoding 参数则支持任意合法的编码类型，若为空则默认为 utf-8 编码。

2. <span id="from-bytes"></span>**原始数据构造方法（Entity.from_bytes）** ：将字符串或者 bytes 类型数据封装为 Entity 类型并返回。如下所示：
```python
Entity.from_bytes(data, mime_type=None, encoding="utf-8")
```
  原始数据构造方法中的 mime_type 和 encoding 参数校验规则与值构造方法相似，不同的是不会对 mime_type 参数值进行限制，可以为任意的 MIME 类型。
    
  如果传递给原始数据构造方法的 data 参数类型为 bytes 类型，该方法会直接返回一个原始数据为 data，MIME 类型为 mime_type，编码类型为 encoding 的 Entity 对象。
  如果传递的 data 参数是字符串数据，则会尝试根据 encoding 参数将其编码为 bytes 类型，并构造成 Entity 对象。


##  <span id="mime-type"></span>MIME 类型支持

Dataway 使用 Entity 类型可支持多种不同的数据类型，如 json、csv、xml等。在值构造方法或原始数据构造方法中指定对应的 MIME 类型和编码类型, 可以得到一个封装不同数据类型的 Entity 对象。通过使用 Entity 选择器，可以读取解析后的结构数据。

不同的 MIME 类型在 Entity 中有不同的数据格式，对应关系如下：

| MIME 类型                         | 数据格式                                   |
| --------------------------------- | --------------------------------------- |
| application/json                  | [JSON格式](#json-format)                   |
| application/x-www-form-urlencoded | [HTTP表单格式](#urlencode-format)          |
| text/plain                        | [文本格式](#textplain-format)              |
| application/xml                   | [XML格式](#xml-format)                     |
| application/csv                   | [CSV表单格式](#csv-format)                 |
| multipart/form-data               | [HTTP FORM DATA表单格式](#formdata-format) |
| 其他 MIME 类型 | [其他格式](#other-format) |

不同的数据格式有不同的编码规则、数据结构以及特定的 Entity 选择器语法。本节将对这些不同的数据格式分别进行说明

###  <span id='json-format'></span> JSON格式

JSON 格式的数据代表 MIME 类型为 application/json 的 Entity 中数据序列化后得到的类型。
- 使用[原始数据构造方法](#from-bytes)，则 Dataway 对输入的 str/bytes 类型最终解析成一个字典类型数据。
- 使用[值构造方法](#from-value)，支持列表、字典、多值字典等多种输入类型，并最终解析成一个字典类型数据。

以下将通过两个示例来说明如何使用 JSON 格式数据。

1.  **构造 JSON 格式的 Entity**
   
    本示例将展示如何使用 Entity 的构造函数构造一个 JSON 格式的 Entity，并使用 Entity 选择器获取 Entity 的属性和数据。
		
　*__输入__*

　Dataway 的运行环境依赖于组件的运行，假定在"配置 Payload"组件前已经有一个"Transform"组件，对流的运行消息 msg 的 payload 进行了设置。msg.payload 为一个字典类型对象，内部结构如下。
```python
{
    "name": "zhangsan",
    "age": 10,
    "male": True,
    "brothers": ["lisi", "zhaowu"]
}
```


　*__Dataway 脚本__*

　以下 Dataway 脚本使用值构造方法将字典数据类型的 msg.payload 转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素，并返回。
```python
def dw_process(msg):
    entity = Entity.from_value(msg.payload, mime_type='application/json', encoding='utf-8')
    return {
        'blob': entity['^blob'],
        'mimeType': entity['^mime_type'],
        'name': entity['name'],
        'brother': entity['brothers'][0],
        'male': entity['^value']['age'],
        'other': entity.get('other', 'other_default')
    }
```
		
　*__输出__*

　Dataway 的脚本输出为一个字典, 其结果如下。
```python
{
    "blob": b'{"name":"zhangsan","age":10,"male":true,"brothers":["lisi","zhaowu"]}',
    "mimeType": "application/json",
    "name": "zhangsan",
    "brother": "lisi",
    "male": 10,
    "other": "other_default"
}
```

２. **复杂的 JSON 结构使用**

　本示例将对复杂的 JSON 结构进行解析，并运行在”配置 Payload"组件中。

　*__输入__*

　Dataway 的运行环境依赖于组件的运行，假定在”配置 Payload"组件前已经有一个"Transform"组件，对流的运行消息 msg 的 payload 进行了设置。msg.payload 为一个 Entity 类型对象，内部结构如下：
```python
{
    'mime_type': 'application/json',
    'encoding': 'utf-8',
    'blob': b'{"name":"zhangsan","age":10,"male":true,"brothers":["lisi","zhaowu"]'
}
```

　*__Dataway 脚本__*

　以下 Dataway 脚本将对 msg 进行处理，获取对应的元素，最终返回一个 Entity 对象。
```python
def dw_process(msg):
    val = {
        "k0": msg.payload['^blob'].decode(msg.payload['^encoding']),
        "k1": {
            "str": "str",
            "list": [123, "abc", 12.34],
            "dict": {
                "k1": "v1"
            }
        },
        "k2": math.sqrt(10),
        "k3": json.dumps({"a": 1, "b": [1, "d"]}),
        "k4": time.strftime('%Y-%m-%d %H:%M:%S'),
        "k5": "hello" + "world",
        "k6": ["12", 3] + [[1, 2], 4.5],
        "k8": msg.payload['^mime_type'],
    }
    if val['k8'] == 'application/json':
        val['k7'] = msg.payload.get('gbk')
        val['k9'] = time.time()
    return Entity.from_value(val, mime_type='application/json', encoding='utf-8')
```

　*__输出__*

　Dataway 脚本的输出结果为一个 Entity 类型对象，为方便说明，我们将 Entity 中的原始数据进行解析后赋值给 value 属性。
```python
 {
    "mime_type": "application/json",
    "encoding": "utf-8",
    "value": {
        "k0": "{\"name\":\"zhangsan\",\"age\":10,\"male\":true,\"brothers\":[\"lisi\",\"zhaowu\"]}",
        "k1": {
            "str": "str",
            "list": [
                123,
                "abc",
                12.34
            ],
            "dict": {
                "k1": "v1"
            }
        },
        "k2": 3.1622776601683795,
        "k3": "{\"a\": 1, \"b\": [1, \"d\"]}",
        "k4": "2021-04-27 10:49:54",
        "k5": "helloworld",
        "k6": [
            "12",
            3,
            [
                1,
                2
            ],
            4.5
        ],
        "k8": "application/json",
        "k7": None,
        "k9": 1619491794.670995
    }
}
```
   
### <span id='urlencode-format'></span> HTTP 表单格式

HTTP 表单格式的数据代表 MIME 类型为 application/x-www-form-urlencoded 的 Entity 中数据解析后得到的类型。
- 使用[原始数据构造方法](#from-bytes)，，则 Dataway 对输入的字符串或 bytes 类型最终解析成一个字典类型数据。
- 使用[值构造方法](#from-value)，支持字典或多值字典两种输入类型，并最终解析成一个多值字典类型数据。

**对 HTTP 表单格式数据，由于其内部实现为多值字典数据类型，因此除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector | 含义                              |
| -------- | --------------------------------- |
| ['*key'] | 返回字典下面的 key 对应的所有元素 |
| ['key']  | 返回字典下面的 key 对应的第一个元素 |


以下将通过示例来说明如何使用 HTTP 表单格式数据。

 **构造并使用 HTTP 表单格式的 Entity**

　本示例将展示如何使用 Entity 的构造函数构造一个 HTTP 表单格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。

　*__输入__*
		
　msg.payload 存储了 HTTP 表单格式的数据：k1=123&k2=helloworld&k3=2&k3=abc，在 Dataway 中以多值字典类型呈现，可转化为字典类型数据： 
```python
{
    "k1": 123,
    "k2": "helloworld",
    "k3": [2, "abc"]
}
```

　*__Dataway 脚本__*

　以下 Dataway 脚本使用值构造方法将字典类型数据转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素。

```python
def dw_process(msg):
    entity = Entity.from_value(msg.payload, mime_type='application/x-www-form-urlencoded', encoding='utf-8')
    return {
        'blob': entity['^blob'],
        'mimeType': entity['^mime_type'],
        'k1': entity['k1'],
        'k3': entity['^value']['k3'],
        'k3multi_selector': entity['^value']['*k3'],
        'k5': entity.get('k5', 'default_value')
    }
```

　*__输出__*

　Dataway 的脚本输出为一个字典类型数据 , 结果如下。

```python
{
    "blob": b'k1=123&k2=helloworld&k3=2&k3=abc',
    "mimeType": "application/x-www-form-urlencoded",
    "k1": 123,
    "k3": 2,
    "k3multi_selector": [2, "abc"],
    "k5": "default_value"
}
```

###  <span id='textplain-format'></span> 文本格式

文本格式的数据代表 MIME 类型为 text/plain 的 Entity 中数据解析后得到的类型。无论是[值构造方法](#from-bytes)还是[原始数据构造方法](#from-bytes)，data 参数均为字符串或 bytes 类型，entity 内容均为字符串数据类型。

以下将通过示例来说明如何使用文本格式数据。

**构造文本格式的 Entity**

　本示例将展示如何使用 Entity 的构造函数构造一个文本格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。

　*__输入__*

　msg. payload 存储了文本格式的数据： "This is a text plain message"。

　*__Dataway脚本__*

　以下 Dataway 脚本使用值构造方法将字符串数据转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素。

```python
def dw_process(msg):
    entity = Entity.from_value(msg.payload, mime_type='text/plain', encoding='utf-8')
    return entity['^value']
```

　*__输出__*

　Dataway 的脚本输出为一个字符串, 结果为"This is a text plain message"。

###  <span id='xml-format'></span> XML 格式

XML 格式的数据代表 MIME 类型为 application/xml 的 Entity 中数据序列化后得到的类型。
- 使用[原始数据构造方法](#from-bytes)方法，则 Dataway 对输入的字符串或 bytes 类型最终解析成一个字典数据类型。
- 使用[值构造方法](#from-value)，仅支持字典输入类型，并最终解析成一个字典数据结构。同时，输入的字典仅包含一个默认的键"root"，值则为内置的 MultiMap，在 MultiMap 中可以自由操作 msg 属性。

以下将通过两个示例来说明如何使用 XML 格式数据。

**对 XML 格式数据，除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector  | 含义                                 |
| --------- | ------------------------------------ |
| ['*key']  | 返回xml某个节点 key 对应的所有元素   |
| ['key']   | 返回xml某个节点 key 对应的第一个元素 |
| ['#text'] | 获取xml某个节点的文本值              |
| ['@attr'] | 获取xml某个节点的attr属性值          |

1. **构造 XML 格式的 Entity**

　本示例将展示如何使用 Entity 的构造函数构造一个 XML 数据格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。

　*__输入__*

　Dataway 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个键为 "abc" ,值为 "123" 的键值对。
```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

　*__Dataway脚本__*

　以下 Dataway 脚本使用[值构造方法](#from-value)将字典类型转换成 Entity 对象，并返回。

```python
def dw_process(msg):
    a = math.floor(1.4)
    return Entity.from_value({
        'root': {
            'k1': msg.vars['abc'],
            'k2': json.dumps('哈哈', ensure_ascii=False),
            'k3': a + 1,
            '@id': "hello",
            '#text': "<a>dwad</a>",
            'k4': ['abc', 'def', None],
        }
    }, mime_type = 'application/xml')
```

　*__输出__*

　Dataway 脚本的输出结果为一个 Entity 类型对象，其中原始数据（blob）为符合 XML 语法的二进制数据，如下所示。
    
```python
{
    "mime_type": "application/xml",
    "encoding": "utf-8",
    "blob": b'<?xml version="1.0" encoding="utf-8"?>
    <root id="hello"><k1>123</k1><k2>"哈哈"</k2><k3>2</k3><k4>abc</k4><k4>def</k4><k4></k4><a>dwad</a></root>'
}
```

2. **使用 XML 特定选择器**

    本示例将示范如何在 XML 格式数据中使用特定语法的选择器。

    *__输入__*

　Dataway 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个键为 "abc" ,值为 "123" 的键值对。

```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

　*__Dataway脚本__*

　以下 Dataway 脚本使用[值构造方法](#from-value)将字典类型转换成 Entity 对象，然后用选择器获取 Entity 的数据。

```python
def dw_process(msg):
    a = math.floor(1.4)
    entity =  Entity.from_value({
        'root': {
            'k1': msg.vars['abc'],
            'k2': json.dumps('哈哈', ensure_ascii=False),
            'k3': a + 1,
            '@id': "hello",
            '#text': "<a>dwad</a>",
            'k4': ['abc', 'def', None],
        }
    }, mime_type = 'application/xml')
    return {
        'k1': entity['root']['#text'] + entity['root']['@id'],
        'k2': entity['root']['k1'],
        'k3': entity['root']['*k4']['^value'],
        'k4': entity['root']['k4'],
        'k5': entity['^mime_type']
    }
```
   
　*__输出__*

　Dataway 脚本的输出结果为一个字典类型数据，如下所示。 
    
```python
{
    "k1": "<a>dwad</a>hello",
    "k2": "123",
    "k3": ['abc', 'def', None],
    "k4": "abc",
    "k5": "application/xml"
}
```

> 在 XML 格式数据中，root 节点为默认节点，其属性使用 `@id=123` 的方式指定，文本使用 `#text` 的方式指定。root 节点值为一个 MultiMap 类型，其中键为每一个子节点名称, 值为相应子节点的值。


###  <span id='csv-format'></span> CSV 格式

CSV 格式的数据代表 MIME 类型为 application/csv 的 Entity 中数据序列化后得到的类型。
- 使用[原始数据构造方法](#from-bytes)，则 Dataway 对输入的字符串或 bytes 类型最终解析成一个列表类型数据结构，其中每一项元素均为一个字典。
- 使用[值构造方法](#from-value)，支持列表类型输入，并最终解析成一个列表类型数据结构，其中每一项元素均为一个字典。


以下将通过示例来说明如何使用 CSV 格式数据。

1. **构造 CSV 格式的 Entity**

　本示例将展示如何使用 Entity 的构造函数构造一个 CSV 格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。

　*__输入__*

　Dataway 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个键为 "abc" , 值为 "123" 的键值对。

```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

　*__Dataway脚本__*

　以下 Dataway 脚本使用[值构造方法](#from-value)将字典类型转换成 Entity 对象，并使用选择器语法获取 Entity 对象的属性值。

```python
def dw_process(msg):
    entity = Entity.from_value([
        {'k1':'abcd','k2':123.0,'k3':True},
        {'k1':'defs','k2':'dwdw,2e','k3':10},
    ], mime_type = 'application/csv')
    return {
        'var1': entity['^blob'],
        'var2': entity['^mime_type'],
        'var3': entity['^encoding'],
        'var4': entity[0]['k2'] + entity[1]['k3'],
        'var5': entity[1]['k2']
    }
```
    
　*__输出__*
    
　Dataway 脚本的输出结果为一个字典类型数据，如下所示。
    
```python
{
    "var1": b'k1,k2,k3\r\nabcd,123.0,True\r\ndefs,"dwdw,2e",10\r\n',
    "var2": "application/csv",
    "var3": "utf-8",
    "var4": "133",
    "var5": "dwdw,2e"
}
```

> 对于 CSV 数据格式，接收的列表每一项元素均为字典类型。每一项元素中的键需保持相同，作为 CSV 文本的标题行；每一项元素中的值则代表该行的数据值，用逗号分隔。

###  <span id='formdata-format'></span> HTTP Form-Data表单

HTTP Form-Data表单格式的数据代表 mime-type 为 multipart/form-data 的 Entity 中数据序列化后得到的类型。

1. **浏览器中的multipart/form-data**

    在浏览器发送 Content-Type 为 multipart/form-data 的请求时，实际传输的 byte 数组转换成字符串如下所示。

    每一项参数由一个 boundary 开头，标识着这一项的开始，如 --34b21 。注意 -- 为固定开头，34b21 为浏览器随机的一个不超过70位的字符串。

    下面两行分别是 Content-Disposition 和 Content-Type 的固定 headers。其中 Content-Disposition 包含 name 和filename 两项，Content-Type 即为输入内容的Content-Type。name 为参数名，filename 为文件名。如果filename 为"*.txt"或者为空，则 Content-Type 默认为 text/plain；如果 filename 为其他，则 Content-Type 会根据后缀名自动判断。同时，也支持其他的扩展 headers。

    再往下是实际的内容，如果 Content-Type 为 text/plain ，则为普通字符串，如"Book"; 如果 Content-Type 为application/json ，则为一个 json 类型的字符串，如下方的file1 对应的 json 结构。

    最后，会用--34b21--来标识这段请求的结束。
    
```
--34b21
Content-Disposition: form-data; name="text"
Content-Type: text/plain

Book
--34b21
Content-Disposition: form-data; name="file1"; filename="a.json"
Content-Type: application/json

{
    "title": "Java 8 in Action",
    "author": "Mario Fusco",
    "year": 2014
}
--34b21
Content-Disposition: form-data; name="file2"; filename="a.html"
Content-Type: text/html

<!DOCTYPE html>
<title>
Available for download!
</title>
--34b21--
```


2. **Form-Data 的构造和使用**


- 使用[原始数据构造方法](#from-bytes)，则 Dataway 对输入的字符串或 bytes 类型最终解析成一个 [FormDataParts](#formdataparts) 数据结构。
- 使用[值构造方法](#from-value)，支持 Entity、Formdata、列表/字典输入类型，并最终解析成一个 [FormDataParts](#formdataparts) 数据结构。

> 如果为 Entity 类型，则会首先判断 MIME 类型是否为 multipart/form-data 。
> 如果为是，直接返回这个 Entity ；否则将报错。
>
> 如果为 FormdataParts 类型（即上文提到的列表/字典结构），则直接赋值给 Entity。
>
> 如果为列表类型，则需要保证为以下数据结构：每一项的第一个元素为参数名。第二个元素如果为列表，则第二个元素的第一项为文件名，第二项为实际的内容，第三项为 Content-Type ，第四项为一个字典，代表 extra_headers；如果第二个元素类型为字符串， 则文件名为空，实际内容即为字符串内容，Content-Type默认为 text/plain。

**对 HTTP Form-Data 格式数据，除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector                                            | 含义                                            |
| --------------------------------------------------- | ----------------------------------------------- |
| ['parts']                                           | 返回自定义类型 FormDataParts 类型                 |
| <span>['parts']</span>[0]                           | 返回 FormData 的第0项                             |
| <span>['parts']</span><span>['a']</span>['content'] | 返回 FormDataParts 中键为'a'的值中的 content 值 |
| ['boundary']                                        | 返回 FormDataParts 的分隔符                       |

3. **应用示例**

    以下将通过两个示例来说明如何使用 HTTP FORM-DATA 表单格式数据。


- **构造 HTTP Form-Data 格式的 Entity**

    本示例将展示如何使用 Entity 的构造函数构造一个 HTTP Form-Data 数据格式的 Entity。

　*__输入__*

　Dataway 输入参数 msg 的变量（vars）中包含一个键为 "abc" , 值为 "123" 的键值对。

```python
{
    "vars": {
        "abc": "123"
    }
}
```

　*__Dataway脚本__*

　以下 Dataway 脚本使用[值构造方法](#from-value)将字典类型转换成 Entity 对象，并返回。

```python
def dw_process(msg):
    a = math.floor(1.4)
    c = Entity.from_value({
        'k1': msg.vars['abc'],
        'k2': json.dumps('哈哈', ensure_ascii=False),
        'k3': a + 1,
    }, mime_type = 'application/json')
    return Entity.from_value(
        [
            ('a', ('test.json', '{"a": a}', 'application/json', {'Test111': 1})),
            ('b', '333'),
            ('c', ('c.json', c, c['^mime_type']))
        ],
        mime_type='multipart/form-data; boundary=123333333'
    )
```

　*__输出__*

　Dataway 脚本的输出结果为一个 Entity 类型对象，其中原始数据（blob）为符合 multipart/form-data 结构的二进制数据，如下所示。

```python
{
    "mime_type": "multipart/form-data; boundary=12345",
    "encoding": "utf-8",
    "blob": b'''--123333333
Content-Disposition: form-data; name="a"; filename="test.json"
Content-Type: application/json
Test111: 1

{"a": a}
--123333333
Content-Disposition: form-data; name="b"

333
--123333333
Content-Disposition: form-data; name="c"; filename="c.json"
Content-Type: application/json

{"k1":"123","k2":"\"哈哈\"","k3":2}
--123333333--
'''
}
```

- **使用 FORM-DATA 选择器**

　本示例将示范如何在 FORM-DATA 格式数据中使用特定语法的选择器。

　*__输入__*

　Dataway 输入参数 msg 的 payload 为一个 Entity 类型，其 MIME 类型为 multipart/form-data，通过[值构造方法](#from-value)创建。

```python
def dw_process(msg):
    return Entity.from_value(
        [('a', ('test', '1233', 'application/json', {'test111':1})),
        ('b', (None, '2333', 'text/plain')),],
        mime_type="multipart/form-data; boundary=ce560532019a77d83195f9e9873e16a1"
    )
```

　*__Dataway脚本__*

　以下 Dataway 脚本将使用 FORM-DATA 选择器对 msg.payload 进行处理，并返回一个字典。

```python
def dw_process(msg):
    return {
        'k1': str(type(msg.payload)),
        'k2': msg.payload['^mime_type'],
        'k3': msg.payload['^encoding'],
        'k4': msg.payload['^blob'],
        'k5': msg.payload['boundary'],
        'k6': msg.payload['parts']['a']['headers']['Content-Disposition']['name']
						+ '-' + msg.payload['parts'][1]['headers']['Content-Type']
    }
```

　*__输出__*

　Dataway 脚本的输出结果为一个字典类型数据，结果如下。

```python
{
    'k1': 'Entity',
    'k2': 'multipart/form-data;boundary=ce560532019a77d83195f9e9873e16a1',
    'k3': 'utf-8',
    'k4': b'''--ce560532019a77d83195f9e9873e16a1
Content-Disposition: form-data; name="a"; filename="test"
Content-Type: application/json
test111: 1

1233
--ce560532019a77d83195f9e9873e16a1
Content-Disposition: form-data; name="b"
Content-Type: text/plain

2333
--ce560532019a77d83195f9e9873e16a1--
''',
		'k5': 'ce560532019a77d83195f9e9873e16a1',
		'k6': 'a-text/plain'
}
```

### <span id='other-format'></span> 其他类型

　对其他类型的 MIME 类型，Dataway 不支持直接用[值构造方法](#from-value)构造，但支持从上游读取数据，以及使用[原始数据构造方法](#from-bytes)构造一个封装的 Entity。

　下面将通过一个示例来说明，假设输入数据为一个二进制 bytes 流，我们通过"配置 Payload"组件中使用 Dataway 表达式将该二进制 bytes 流封装到 msg.payload 中。

　*__Dataway表达式__*

```python
def dw_process(msg):
    b = msg.payload
    return Entity.from_bytes(b, mime_type='application/octet-stream')
```

　然后在下游可以使用 [Entity 选择器](#selectors) 语法进行操作。

###  六. <span id='dataref'></span>集成流数据面板

Dataway 支持可视化数据引用，在**"集成流数据面板"**点击数据标签即可引用集成流上下文中的相应数据（包括变量、前置组件输出等），打通组件间的数据高速路，提升用户体验。当前 Dataway 所有模式均支持可视化数据引用功能，包括[文本](../Dataway文档/文本模式.md)模式、[表达式](../Dataway文档/表达式模式.md)模式、[代码模式 Python ](../Dataway文档/代码模式Python.md)和[代码模式 Java ](../Dataway文档/代码模式Java.md)。

1. 点击 Dataway 输入文本框时自动弹出**"集成流数据面板"**。

2. 点选**"集成流数据面板"**中的数据标签，Dataway 编辑文本框中会自动引用集成流上下文数据，并在当前光标位置插入对应的数据标签。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b8690a07abe2c2f57c3aa686d59de4e9.png" alt="集成流数据面板" style="zoom:50%;" />
