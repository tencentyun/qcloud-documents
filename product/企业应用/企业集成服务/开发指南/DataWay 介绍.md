## DataWay 快速入门

DataWay 是企业集成服务 EIS 中用于对数据进行自定义转换与处理的表达式脚本语言，集成在 EIS 运行时的服务中，是提供 EIS 可扩展性的关键能力。
EIS 的许多内置组件中都可以提供基于 DataWay 脚本的自定义能力，可以用于对 EIS 事件进行动态处理。例如：在 set-variable 组件中，可以通过 DataWay 表达式来动态地设置变量的值；在 Transform 组件中，可以充分利用 DataWay 的灵活语法进行复杂的数据处理与表达式运算，以最终生成期望的 `payload` 产出，用于下游组件的处理。

### DataWay 脚本结构

完整的 DataWay 脚本是符合语法定义的 Python3 代码段，其中包含入口函数定义 `def dw_process(msg)`，如：

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

- `dw_process` 入口函数仅接受一个参数，该参数代表当前表达式需要处理的 EIS 消息。
- `dw_process` 的返回值即是表达式的返回值。
- 内置的 `Entity.from_value` 函数用于为构造 `Entity` 类型的返回值，可以指定序列化参数，如 `mime_type`、`encoding` 等。

>?有关 `dw_process` 入口函数的详细说明见下文 [dw_process 入口函数详解](#dw_process-.E5.85.A5.E5.8F.A3.E5.87.BD.E6.95.B0.E8.AF.A6.E8.A7.A3)。

### 语法说明

DataWay 基于 Python3.4 的语法进行实现，出于安全性的考量，在 DataWay 中，如下的 Python 语法被禁止使用：

- **while/for 循环**
- **try/except/finally 语句**
- **yield 语句**
- **class 类型定义语句**
- **import/from..import 语句**

### dw_process 入口函数详解

`dw_process` 是 DataWay 脚本的主入口，其作用相当于 C/C++语言中的 `main` 函数，仅接受一个类型为 `Message` 的参数，而其返回值就是该 DataWay 表达式最终的输出值。
作为 EIS 数据处理流程的一个环节，`dw_process` 函数的返回值类型是受到严格限制的，其返回的结果中仅支持如下类型，否则会导致运行时的序列化错误：

- **str**：即字符串
- **None**：Python 中的空值
- **bool**：布尔值
- **float**：浮点数
- **int**：整数
- **list**：列表，序列类型容器
- **dict**：字典，kv 类型容器
- **Message**：即 EIS 中的消息，在 DataWay 中以 `Message` 进行访问
- **Entity**：即 EIS 中的消息数据，在 DataWay 中以 `Entity` 类型进行访问，包括 `mime_type`、`encoding`、`blob`数据
- **MultiMap**：多值 `map`，该类型可以支持重复的 key，通常用于 `Message` 的 `attrs` 属性中

>?对于 `list` , `dict` , `MultiMap`  等容器类型，其元素的也只能是上述类型。更多内容见 [DataWay 语言手册](#dataway-.E8.AF.AD.E8.A8.80.E6.89.8B.E5.86.8C)。

### Message 中的预定义属性

`Message` 中包含的属性称之为 **预定义属性 (Predefined Properties)** ，这些属性是由系统根据当前运行信息及处理的消息生成的，用于在 DataWay 中通过程序化的方式获取上下文信息。
目前 `Message` 中包含的属性有 `vars`、`payload`、`attrs`、`id`、`seq_id`、`error` 等，可以通过 `msg.vars`、`msg.payload`、`msg.attrs`、`msg.id`、`msg.seq_id`、`msg.error` 的方式进行访问。



## DataWay 语言手册



### DataWay 类型系统

由于 DataWay 表达式是标准的 Python 脚本，在 DataWay 处理过程中，用户可以使用并构造允许的任意类型。但是作为 EIS 数据流转的重要入口，`dw_process` 的返回值类型是受到严格限制的，其返回的结果中仅支持如下类型，否则（一定）会导致运行时的序列化错误：

- **str**：字符串，即 Python 原生的字符串 str。
- **None**：Python 中的空值 None。
- **bool**：布尔值，即 Python 原生布尔值 bool。
- **float**：浮点数，即 Python 原生浮点数 float。
- **int**：整数，即 Python 原生整型 int。
- **list**：列表，序列类型容器，即 Python 原生 `list` 类型。
- **dict**：字典，kv 类型容器，即 Python 原生 `dict` 类型。
- **Message**：即 EIS 中的消息，在 DataWay 中以 `Message` 进行访问，该类型为 EIS 独有。
- **Entity**：即 EIS 中的实体数据，用于代表一个结构化的二进制对象，在 DataWay 中以 `Entity` 类型进行访问，包括 `mime_type`、`encoding`、`blob` 等数据，该类型是 EIS 独有的。
  可以通过如下方式访问 `Entity` 中的内容：
  - **obj['^blob']：**获取该消息对象的负载数据，返回 `bytes` 类型的对象。
  - **obj['^mime_type']：**获取该消息对象的 `encoding`，返回 `str` 对象。
  - **obj['^encoding']：**获取该消息对象的 `encoding`，返回 `str` 对象。
  - **obj['^value']：**根据 `mime_type` 和 `encoding`，对负载数据 `blob` 进行反序列化，并返回其结果
  - **obj['xxxx']：**根据 `mimetype` / `encoding`对 `Message` 的内容进行反序列化，并获取其中指定 key 的值，逻辑上相当于 **obj['^value'] ['xxx']**。
  - **obj.get(attr)：**根据 `mimetype` / `encoding`对 `Message` 的内容进行反序列化，并获取其中指定 key 的值，逻辑上相当于 **obj['^value'].get(attr)**。
- **MultiMap**：多值 `map`，类似于 xml 而与 Python 原生 `dict` 类型不同，该类型可以支持重复的 key。通常用于 `Message` 的 `attrs` 属性中，该类型为 EIS 独有的。

### DataWay 内置变量及类型

- DataWay 预定义属性 (Predefined Properties)
  `Message` 中包含的属性称之为**预定义属性 (Predefined Properties)** ，这些属性是由系统根据当前运行信息及处理的消息生成的，用于在 DataWay 中通过程序化的方式获取上下文信息。
  目前 `Message` 中包含的属性及其说明如下：
  - **msg.vars:** 局部消息变量，`dict` 类型，键为 string，代表变量名，值为允许的任意类型，代表变量值`vars` 会在一条消息处理的所有环节共享，因此可以用于在不同的处理节点之间进行数据的传递
  - **msg.payload**：当前消息负载数据，可以是允许的任意类型 `payload` ，是一条消息对象的负载数据，一般是由上一个组件通过 `set-payload` 或者 Transform 组件生成的，其可能的数据类型是上文中列举的 DataWay 中允许的返回值类型。Listener 组件会根据用户发送的原始消息来构造 `payload` 的内容，因此 Listener 组件处理之后，`payload` 都是 Entity 类型，除非在下游通过 `set-payload` 或者 Transform 组件对 `payload` 进行重新赋值
  - **msg.attrs**：当前消息的属性数据，包括消息类型、消息的头部信息等。`dict` 类型，键为 str，代表属性名，值为任意类型，代表属性值 `attrs` 是消息的属性数据。
  - **msg.id**：当前消息的唯一标识 id，str 类型。
  - **msg.seq_id**：当前消息的序列号，str 类型。
  - **msg.error**：当前处理上下文中的错误信息。`dict` 类型，键为 str，值为 str。
    包含的内容有：
    - **msg.error['code']：**错误类型。
    - **msg.error['desc']：**错误描述字符串。
- **Entity 类型构造**
  - **Entity.from_value：**该函数用于将值类型 `data` 封装为 `Entity` 类型，并返回
    ```python
    Entity.from_value(data, mime_type=None, encoding="utf-8")
    ```
   在 `from_value` 函数内部，会先根据给定的 `mime_type` 和 `encoding` 尝试对 `data` 进行序列化得到 bytes 型数据，再封装为`Entity` 类型进行返回，目前支持的 `mime_type` 有 `application/json` 和 `application/x-www-form-urlencoded` 两种，其中`application/json`仅支持 `encoding` 为utf8，`application/x-www-form-urlencoded` 支持任意合法的编码类型。
  - **Entity.from_bytes：**该函数用于将 str 或者 bytes 型数据封装为 `Entity ` 类型
    ```python
    Entity.from_bytes(data, mime_type=None, encoding="utf8")
    ```
    如果传递给 `from_bytes` 的 `data` 参数类型为 bytes，则该函数会直接返回一个以 `data`、`mime_type`、`encoding`作为参数构造的 `Entity` 对象，且不会对 `mime_type` 和 `encoding` 进行合法性校验；如果传递的 `data` 是 str 数据，则会尝试根据 `encoding`参数将其编码为 bytes，并构造 `Entity` 对象，而不会校验 `mime_type` 参数的合法性。
     `Entity` 类型详细说明可参考 [Dataway 类型系统](#dataway-.E7.B1.BB.E5.9E.8B.E7.B3.BB.E7.BB.9F)。
  - **Python 上下文环境中的内置变量及函数，可参考 [Python 官方文档](https://docs.python.org/3.5/library/functions.html#built-in-funcs)。目前 DataWay 中支持的函数如下：**
    - abs()：求数值绝对值
    - all()：判断序列（集合、列表、元组、dict) 中所有元素是否满足给定条件
    - dict()：创建字典
    - min()：数值最小值
    - any()：判断集合中是否存在元素满足给定条件
    - sorted()：排序
    - bool()：构造布尔值
    - int()：构造整数
    - str()：构造字符串
    - sum()：数值求和
    - filter()：集合过滤，如 filter(lambda x:x>100, [1,3,4,100,102]) -> [100,102]
    - pow()：求指数
    - float()： 构造浮点数
    - tuple()：构造元组
    - len()：获取集合元素个数
    - list()：构造列表
    - max()：获取数值最大值
    - round()：截取数值的整数部分

### 其它可用的模块

- **time**：用于时间处理的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/time.html)。已内置在 DataWay 的处理上下文中，可以直接引用。目前 DataWay 中支持的库函数/类型如下：
  - **time()：**函数，返回当前时间戳，float 类型，单位为秒
  - **struct_time：**类型，表示一个结构化时间对象
  - **altzone：**当前时区相对于 UTC 时区的延迟偏移，单位为秒
  - **asctime：**将一个 struct_time 转换为时间字符串
  - **ctime：**将一个时间戳转换为时间字符串
  - **mktime()：**将一个 struct_time 转换为时间戳
  - **strftime()：**将一个 struct_time 进行格式化
  - **strptime()：**按照给定的格式解析事件字符串，并返回一个结构化的 struct_time 对象
  - **timezone：**当前时区
  - **tzname：**当前时区名称
  - **gmtime：**将一个时间戳转换为 struct_time 对象
  - **localtime：**将一个时间戳转换为当前时区的本地时间，返回 struct_time 类型对象
- **json**：用于处理 json 数据的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/json.html)。已内置在 DataWay 的处理上下文中，可以直接引用。目前 DataWay 中支持的 json 模块函数：
  - **dumps：**将 json 对象编码为 json 字符串
  - **loads：**将一个 json 串解析为 Python 对象
- **math**：用于数学运算的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/math.html)。已内置在 DataWay 的处理上下文中，可以直接引用。目前 DataWay 中支持的 math 模块函数：
  - **math.ceil(x)：**返回 x 的上限，即大于或者等于 x 的最小整数。如果 x 不是一个浮点数，则委托 `x.ceil()`， 返回一个 `Integral` 类的值
  - **math.floor(x)：**返回 x 的向下取整，小于或等于 x 的最大整数。如果 x 不是浮点数，则委托 `x.floor() `，返回 `Integral ` 类的值
  - **math.fabs(x)：**返回 x 的绝对值
  - **math.pow(x,y)：**返回 x 的 y 次幂
  - **math.sqrt(x)：**返回 x 的平方根
  支持的常量：
  - **math.pi：**数学常数 π = 3.141592...，精确到可用精度
  - **math.e：**数学常数 e = 2.718281...，精确到可用精度
  - **math.inf：**浮点正无穷大。（对于负无穷大，使用 `-math.inf` ）相当于 `float('inf') ` 的输出
  - **math.nan：**浮点“非数字”（NaN）值，相当于 `float('nan')` 的输出
- **base64**：用于 base64 编解码的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/base64.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：
  - **base64.b64encode()**
  - **base64.b64decode()**
- **hmac**：用于hmac加解密的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/hmac.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：
  - **hmac.new()**
- **random**：用于随机数生成的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/random.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数有：
  - **random.randint()**
- **hashlib**：用于生成哈希值的库，可参考 [Python官方文档](https://docs.python.org/3.5/library/hashlib.html)。已内置在 DataWay 的处理上下文中，可以直接引用。 支持的函数/属性有：
  - **hashlib.sha256**

### Entity 选择器

对于 `Entity` 类型的变量，如预定义属性 `msg.payload`，DataWay 支持通过选择器 (selector) 的方式进行快速访问，支持的操作类型如下：

| 下标类型                                 | 描述                                                         | 举例                      |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------- |
| 数字                                     | 访问当前数组的第 i 个元素                                    | payload[0]                |
| 以^开头的字符串                          | 获取元信息，例如 ^mime_ype、^encoding、^raw（原始二进制）、^value（值） | msg.payload["^mime_type"] |
| 普通字符（字母、数字、下划线、横杠、点） | 普通字符的 key，按 key、nodeName、name 等方式获取当前元素的子元素，如果有多个同名的，只返回第一个 | msg.payload["list"]       |





