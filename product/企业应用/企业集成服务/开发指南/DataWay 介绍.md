DataWay 是 EIS 服务中用于对数据进行自定义转换与处理的表达式脚本语言，集成在 EIS 运行时服务中，是提供 EIS 可扩展性的关键能力。
EIS 的许多内置组件中都可提供基于 DataWay 脚本的自定义能力，可以用于对 EIS 事件进行动态处理。例如在 Set-Variable 组件中，可以通过 DataWay 表达式来动态地设置变量的值；在 Transform 组件中，可以充分利用 DataWay 的灵活语法进行复杂的数据处理与表达式运算，以最终生成期望的 Payload 产出，用于下游组件的处理。

## 1. 脚本结构

完整的 DataWay 脚本符合语法定义的 Python3 代码段，其中包含入口函数定义 def dw_process(msg)，例如：

```python
#! dataway: v1.0.0
def func(x):
    return x*x
def dw_process(msg):
    sq = func(3)
    val = {
        'square': sq,
        'data': msg.payload['realData']
    }
    return Entity.from_value(val, mime_type='application/json')
```

dw_process 入口函数仅接受一个参数，该参数代表当前表达式需要处理的 EIS 消息。dw_process 的返回值即是表达式的返回值。
内置的 Entity.from_value 函数用于为构造 Entity 类型的返回值，可以指定序列化参数，例如 mime_type、encoding 等。

## 2. 语法说明

DataWay 基于 Python3.4 语法进行实现，出于安全性的考量，在 DataWay 中，如下的 Python 语法被禁止使用：

1. while/for 循环
2. try/except/finally 语句
3. yield 语句
4. class 类型定义语句
5. import/from..import 语句

## 3. dw_process 入口函数

dw_process 是 DataWay 脚本的主入口，其作用相当于 C/C++语言中的 main 函数。

dw_process 仅接受一个**类型为 Message 的参数**，而其返回值就是该 DataWay 表达式最终的输出值。

作为 EIS 数据处理流程的一个环节，dw_process 函数的返回值类型是受到严格限制的，目前支持的类型有：str/None/bool/float/int/list/dict/Entity/MultiMap/Message 等。
- 关于 DataWay 中数据类型的详细介绍，可参考 [DataWay 类型系统](#4.-dataway-.E7.B1.BB.E5.9E.8B.E7.B3.BB.E7.BB.9F)。
- 关于返回值类型限制的说明，可参考 [返回值类型的限制](#7.4-.E8.BF.94.E5.9B.9E.E5.80.BC.E7.B1.BB.E5.9E.8B.E9.99.90.E5.88.B6)。

## 4. DataWay 类型系统

由于 DataWay 表达式为标准的 Python 脚本，在 DataWay 处理过程中，用户可以使用并构造 Python 允许的任意类型。
其中比较常用的数据类型如下：

| 类型名       | 说明                                                         | 是否 DataWay 特有类型       | 举例                                                        |
| ------------ | ------------------------------------------------------------ | ------------------------- | ----------------------------------------------------------- |
| str          | 字符串，即 Python 原生的字符串 str                           | 否                        | "abc"                                                       |
| None         | Python 中的空值 None                                         | 否                        | None                                                        |
| bool         | 布尔值，即 Python 原生布尔值 bool                            | 否                        | True/False                                                  |
| float        | 浮点数，即 Python 原生浮点数 float                           | 否                        | 123.123                                                     |
| int          | 整数，即 Python 原生整型 int                                 | 否                        | 123                                                         |
| bytes        | 字节数组，即 Python 字节数组类型 bytes                       | 否                        | b'this_is_a_bytes'                                          |
| set          | 集合，即 Python 集合类型set                                  | 否                        | {1,2,3}                                                     |
| list         | 列表，序列类型容器，即 Python 原生 list 类型                 | 否                        | [1,2,3]                                                     |
| dict         | 字典，kv 类型容器，即 Python 原生 dict 类型                  | 否                        | {1:1, 'key': 'value'}                                       |
| **Entity**   | 即 EIS 中的实体数据，用于代表一个二进制对象，在 DataWay 中以 Entity 类型进行访问，包括 blob、mime_type、encoding 等信息 | **是** | http-listener 构造消息中的 payload，msg.payload               |
| **MultiMap** | 多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。 | **是** | application/www-form-urlencoded 格式的数据解析之后得到的对象 |
| **Message**  | 即 EIS 中的消息，在 DataWay 中以 Message 进行访问            | **是** | dw_process 入口函数中的msg 参数                               |

>!上述类型可以在 DataWay 表达式中使用，但是 dw_process 函数**返回值的类型受到严格限制**，详情可参考 [返回值类型限制](#7.4-.E8.BF.94.E5.9B.9E.E5.80.BC.E7.B1.BB.E5.9E.8B.E9.99.90.E5.88.B6)。


### 4.1 Entity 类型

Entity 类型在 DataWay 中用于表示一个二进制数据的封装对象，其主要组成部分包括 blob、mime_type 以及 encoding。
- blob：原始的二进制数据。
- mime_type：表示二进制数据的内容格式，例如 application/json、application/www-form-urlencoded 等。
- encoding：表示二进制数据的字符编码格式，例如 utf8、gbk 等。

可以通过如下方式访问 Entity 中的内容：
- entity['^blob']：获取该消息对象的负载数据，返回 bytes 类型的对象
- entity['^mime_type']：获取该消息对象的 mime_type，返回 str 对象
- entity['^encoding']：获取该消息对象的 encoding，返回 str 对象
- entity['^value']：根据 mime_type 和 encoding，对负载数据 blob 进行反序列化，并返回其结果
- entity['xxxx']：根据 mimetype/encoding 对 message 的内容进行反序列化，并获取其中指定 key 的值。逻辑上相当于 obj['^value']['xxx']
- entity.get(attr)：根据 mimetype/encoding 对 message 的内容进行反序列化，并获取其中指定 key 的值。逻辑上相当于 obj['^value'].get(attr)


>?
>- 对于以下标方式访问 Entity 的详细定义，可参考 [选择器](#4.2-entity-.E9.80.89.E6.8B.A9.E5.99.A8)。
>- 对于如何手动构造 Entity 类型的对象，可参考 [Entity 对象构造](#4.3-entity-.E5.AF.B9.E8.B1.A1.E6.9E.84.E9.80.A0)。
>- 对于使用 Entity 类型时的相关限制，可参考 [Entity 类型 mime_type 与 encoding 支持情况](#7.5-entity-.E7.B1.BB.E5.9E.8B-mime_type-.E4.B8.8E-encoding-.E6.94.AF.E6.8C.81.E6.83.85.E5.86.B5)。

### 4.2 Entity 选择器

对于 Entity 类型的变量，如预定义属性 msg.payload，DataWay 支持通过选择器 (selector) 的方式进行快速访问，支持的操作类型如下：

| 下标类型                                 | 描述                                                         | 举例                      |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------- |
| 数字                                     | 访问当前数组的第 i 个元素                                    | msg.payload[0]            |
| 以^开头的字符串                          | 获取元信息，例如^mime_type、^encoding、^raw（原始二进制）、^value（值） | msg.payload["^mime_type"] |
| 普通字符（字母、数字、下划线、横杠、点） | 普通字符的 key，按 key、nodeName、name 等方式获取当前元素的子元素，如果有多个同名的，只返回第一个 | msg.payload["list"]       |

### 4.3 Entity 对象构造

1. Entity.from_value 函数用于将值类型 data 封装为 Entity 类型，并返回如下：
   ```python
   Entity.from_value(data, mime_type=None, encoding="utf-8")
   ```
   在 from_value 函数内部，会先根据给定的 mime_type 和 encoding 尝试对 data 进行序列化得到 bytes 型数据，再封装为 Entity 类型进行返回。
   目前支持的 mime_type 有 application/json、application/x-www-form-urlencoded 两种，其中 application/json 仅支持 encoding 为 utf8，application/x-www-form-urlencoded 支持任意合法的编码类型。
	 
2. Entity.from_bytes 函数用于将 str 或者bytes 型数据封装为 Entity 类型。
   ```python
   Entity.from_bytes(data, mime_type=None, encoding="utf8")
   ```
   - 如果传递给 from_bytes 的 data 参数类型为 bytes，则该函数会直接返回一个以 data、mime_type、encoding 作为参数构造的 Entity 对象，且不会对 mime_type 和 encoding 进行合法性校验。
   - 如果传递的 data 是 str 数据，则会尝试根据 encoding 参数将其编码为 bytes，并构造 Entity 对象，而不会校验 mime_type 参数的合法性


### 4.4 Message 类型与预定义属性

Message 类型是 DataWay 用于表示一条 EIS 消息的数据类型，其中包含 payload、vars、attrs 等属性，称之为**预定义属性（Predefined Properties）**。这些属性由系统根据当前运行信息及处理的消息生成，用于在 DataWay 中通过程序化的方式获取上下文信息。

目前 Message 中包含的属性及其说明如下：

| 属性        | 作用                                             | 属性类型                                                     | 属性说明                                                     |
| ----------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| msg.vars    | 当前消息上下文中的变量                           | dict，键为 str类型，代表变量名，值为允许的任意类型，代表变量值 | vars 会在一条消息处理的所有环节共享，因此可以用于在不同的处理节点之间进行数据的传递 |
| msg.payload | 当前消息的载荷数据                               | 任意类型。在listener中为Entity类型                           | payload 是一条消息对象的负载数据，一般是由上一个组件通过 set-payload 或者 transform 组件生成的，其可能的数据类型即是上文中列举的 DataWay 中允许的返回值类型。 listener 组件会根据用户发送的原始消息来构造 payload 的内容，因此 listener 组件处理之后，payload 都是 Entity 类型，除非在下游通过 set-payload 或者 transform 组件对 payload 进行重新赋值 |
| msg.attrs   | 当前消息的属性数据，如消息来源、消息的头部信息等 | dict 类型，键为 str，代表属性名，值为任意类型，代表属性值    |       -                                                       |
| msg.id      | 当前消息的唯一标识 id                            | str 类型                                                     |          -                                                    |
| msg.seq_id  | 当前消息的序列号                                 | str 类型                                                     |           -                                                   |
| msg.error   | 当前处理上下文中的错误信息                       | dict 类型，键为 str，代表错误属性名；值为 str，代表属性值    | 包含的内容有： msg.error['code'] 错误类型；msg.error['desc']：错误描述字符串 |



## 5. DataWay 内置函数

1. Python 上下文环境中的内置变量及函数，可参考 [Python 官方文档](https://docs.python.org/3.5/library/functions.html#built-in-funcs)。目前 DataWay 中支持的函数如下：
   1. abs()：求数值绝对值
   2. all()：判断序列（集合、列表、元组、dict) 中所有元素是否满足给定条件
   3. dict()：创建字典
   4. min()：数值最小值
   5. any()：判断集合中是否存在元素满足给定条件
   6. sorted()：排序
   7. bool()：构造布尔值
   8. int()：构造整数
   9. str()：构造字符串
   10. sum()：数值求和
   11. filter()：集合过滤，如 filter(lambda x:x>100, [1,3,4,100,102]) -> [100,102]
   12. pow()：求指数
   13. float()： 构造浮点数
   14. tuple()：构造元组
   15. len()：获取集合元素个数
   16. list()：构造列表
   17. max()：获取数值最大值
   18. round()：截取数值的整数部分


## 6. 其它可用的模块

1. __time__，用于时间处理的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/time.html)。已内置在 DataWay 的处理上下文中，可以直接引用
   目前 DataWay 中支持的库函数/类型如下：
   1. time()：函数，返回当前时间戳，float 类型，单位为秒
   2. struct_time：类型，表示一个结构化时间对象
   3. altzone：当前时区相对于 UTC 时区的延迟偏移，单位为秒
   4. asctime：将一个 struct_time 转换为时间字符串
   5. ctime：将一个时间戳转换为时间字符串
   6. mktime()：将一个 struct_time 转换为时间戳
   7. strftime()：将一个 struct_time 进行格式化
   8. strptime()：按照给定的格式解析事件字符串，并返回一个结构化的struct_time对象
   9. timezone：当前时区
   10. tzname：当前时区名称
   11. gmtime：将一个时间戳转换为 struct_time 对象
   12. localtime：将一个时间戳转换为当前时区的本地时间，返回 struct_time 类型对象
2. __json__，用于处理 json 数据的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/json.html)。已内置在 DataWay 的处理上下文中，可以直接引用
   目前 DataWay 中支持的 json 模块函数：
   1. dumps：将 json 对象编码为 json 字符串
   2. loads：将一个 json 串解析为 Python 对象
3. __math__，用于数学运算的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/math.html)。已内置在 DataWay 的处理上下文中，可以直接引用：
   - 目前 DataWay 中支持的 math 模块函数：  
     1. math.ceil(x)：返回 x 的上限，即大于或者等于 x 的最小整数。如果 x 不是一个浮点数，则委托 x.__ceil__(), 返回一个 Integral 类的值。
     2. math.floor(x)：返回 x 的向下取整，小于或等于 x 的最大整数。如果 x 不是浮点数，则委托 x.__floor__() ，它应返回 Integral 值。
     3. math.fabs(x)：返回 x 的绝对值。
     4. math.pow(x,y)：返回 x 的 y 次幂。
     5. math.sqrt(x)：返回 x 的平方根。
   - 支持的常量：
     1. math.pi：数学常数 π = 3.141592...，精确到可用精度。
     2. math.e：数学常数 e = 2.718281...，精确到可用精度。
     3. math.inf：浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出。
     4. math.nan：浮点“非数字”（NaN）值。 相当于 float('nan') 的输出。
4. __base64__：用于base64编解码的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/base64.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：
   1. base64.b64encode()
   2. base64.b64decode()
5. __hmac__：用于hmac加解密的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/hmac.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：hmac.new()
7. __random__：用于随机数生成的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/random.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：random.randint()
9. __hashlib__：用于生成哈希值的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/hashlib.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数/属性有： hashlib.sha256

## 7. 系统限制

### 7.1 语法限制

如 [语法说明](#2.-.E8.AF.AD.E6.B3.95.E8.AF.B4.E6.98.8E) 所述，在 DataWay 表达式中编写 Python 语句时，需要注意如下语句被禁止使用。在表达式中使用这些语句将导致运行时错误：
1. while/for 循环
2. try/except/finally 语句
3. yield 语句
4. class 类型定义语句
5. import/from..import 语句

### 7.2 库函数限制

在 DataWay 表达式中使用除上述 [内置函数/属性](#5.-dataway-.E5.86.85.E7.BD.AE.E5.87.BD.E6.95.B0) 以及 [其它可用的模块](#6.-.E5.85.B6.E5.AE.83.E5.8F.AF.E7.94.A8.E7.9A.84.E6.A8.A1.E5.9D.97) 之外的其它 Python 函数或者三方库，将导致运行时错误。

### 7.3 内存控制与执行超时限制

为防止恶意代码对 EIS 运行时造成损害，DataWay 表达式的执行环境会受到内存与执行时间的限制。
目前单条 DataWay 表达式所能使用的内存上限是100MB，超过此上限将导致运行时 MemoryError 错误；
同时执行时间不能超过1000毫秒，超过此限制将导致 TimeoutError 错误；

### 7.4 返回值类型限制

虽然在 DataWay 表达式中可以构造并使用任意的 Python 对象，但是其最终的返回值的数据类型是受到限制的。目前仅支持如下类型：

| 类型名       | 说明                                                         | 是否 DataWay 特有类型       | 举例                                                        |
| ------------ | ------------------------------------------------------------ | ------------------------- | ----------------------------------------------------------- |
| str          | 字符串，即 Python 原生的字符串 str                           | 否                        | "abc"                                                       |
| None         | Python 中的空值 None                                         | 否                        | None                                                        |
| bool         | 布尔值，即 Python 原生布尔值 bool                            | 否                        | True/False                                                  |
| float        | 浮点数，即 Python 原生浮点数 float                           | 否                        | 123.123                                                     |
| int          | 整数，即 Python 原生整型 int                                 | 否                        | 123                                                         |
| list         | 列表，序列类型容器，即 Python 原生 list 类型                 | 否                        | [1,2,3]                                                     |
| dict         | 字典，kv 类型容器，即 Python 原生 dict 类型                  | 否                        | {1:1, 'key': 'value'}                                       |
| **Entity**   | 即 EIS 中的实体数据，用于代表一个二进制对象，在 DataWay 中以 Entity 类型进行访问，包括 blob、mime_type、encoding 等信息 |** 是** | http-listener 构造消息中的 payload，msg.payload               |
| **MultiMap** | 多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。 | **是** | application/www-form-urlencoded 格式的数据解析之后得到的对象 |
| **Message**  | 即 EIS 中的消息，在 DataWay 中以 Message 进行访问            | **是** | dw_process 入口函数中的 msg 参数                               |

对于 list、dict、MultiMap 以及 Message 等容器类型，其容器元素也必须符合上述类型限制。

>!如果 DataWay 表达式输出的值会作为集成流的最终返回结果，则其允许的类型还会受到相应连接器组件的限制。
> 例如，在以 http listener 组件作为第一个组件的流中，其最终的 payload 必须是一个 Entity 类型，否则会导致 RESPONSE_TYPE_ERROR 错误。

### 7.5  Entity 类型 mime_type 与 encoding 支持情况

#### 构造 Entity 对象时的限制

若使用 **Entity.from_value(obj, mime_type, encoding)** 函数来构造 Entity 对象，则其支持的 mime_type 及其转换逻辑为：

| mime_type                         | 格式说明     | 编码规则                                                     | 支持的 obj 类型                                |
| --------------------------------- | ------------ | ------------------------------------------------------------ | -------------------------------------------- |
| application/json                  | json 内容格式 | 先用标准 utf8 编码为 json 字符串，再转换为其它编码：json.dumps(obj).decode('utf8').encode(encoding) | str/bool/None/int/float/list/dict/MultiMap等 |
| application/x-www-form-urlencoded | http 表单格式 | 先序列化为 http 表单格式，再转换为其它编码：urllib.parse.urlencode(obj).encode(encoding) | MultiMap、dict                               |

如果使用 **Entity.from_bytes(data, mime_type=None, encoding="utf8")**，则按照如下方式进行处理：

1. 如果 data 类型为 bytes，则直接构造并返回。
2. 如果 data 类型为 str，则先将其根据 encoding 进行编码转换为 bytes，再构造 Entity 对象并返回，若转换出错则报错。

#### 使用 Entity 对象的限制

Entity 对象在本质上是一个对二进制数据的封装对象，但是为了方便使用，也提供了 Entity.get(attr) 等对象方法以及基于下标的选择器语法（详见 [Entity 选择器](#4.2-entity-.E9.80.89.E6.8B.A9.E5.99.A8)）等快速访问功能。
在使用这些功能时，需要注意的是，有些特殊操作下系统会尝试先对 Entity 中的二进制数据进行解析，如果解析失败则会导致运行时错误。这些特殊操作包括：

1. 用 Entity['^value'] 来获取解析后的结构化结果。
2. 用 Entity.get('attrName') 或 Entity['attrName'] 来获取结构化结果中的某个属性值。
3. 用 Entity['*key'] 来执行选择器语法。

目前仅支持符合如下条件的 Entity 解析：

| mime_type 类型                     | 备注         | 支持的 encoding 类型          | 解析到的结果类型 |
| --------------------------------- | ------------ | --------------------------- | ---------------- |
| application/json                  | json 内容格式 | utf8、gbk 等 Python 支持的编码 | dict             |
| application/x-www-form-urlencoded | http 表单格式 | utf8、gbk 等 Python 支持的编码 | MultiMap         |

在不符合条件的 Entity 对象上执行上述特殊操作，会导致运行时错误。

## 8. 常见问题

#### 8.1 DataWay 表达式与 Python 脚本是什么关系？

目前 DataWay 表达式基于 Python 语言进行封装，主要是在 Python 的基础上进行了功能的裁剪，以及要求必须定义合法的入口函数 dw_process(msg)。因此，所有的 DataWay 表达式正常执行结束之后都会有最终的返回值，但 “Python脚本” 却可以没有明确返回值。

#### 8.2 DataWay 表达式在什么场景下使用？

目前几乎所有的 EIS 核心组件都具有表达式求值的能力，DataWay 是 EIS 具有动态求值能力的关键所在。
