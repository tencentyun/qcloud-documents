## Dataway 快速入门

Dataway 是企业集成服务中用于对数据进行自定义转换与处理的表达式脚本语言，集成在企业集成服务运行时服务中，是提供企业集成服务可扩展性的关键能力。

企业集成服务的许多内置组件中都可以提供基于 Dataway 脚本的自定义能力，可以用于对企业集成服务事件进行动态处理。
例如在 set-variable 组件中，可以通过 Dataway 表达式来动态地设置变量的值；在 Transform 组件中，可以充分利用 Dataway 的灵活语法进行复杂的数据处理与表达式运算，以最终生成期望的 payload 产出，用于下游组件的处理。

### 脚本结构

完整的 Dataway 脚本符合语法定义的 Python3 代码段，其中包含入口函数定义 def dw_process(msg)，例如：
```
#! dataway: v1.0.0
def func(x):
    return x*x
def dw_process(msg):
    config(mime_type='application/json')
    sq = func(3)
    return {
        'square': sq,
        'data': payload['realData']
    }
```

dw_process 入口函数仅接受一个参数，该参数代表当前表达式需要处理的企业集成服务消息。dw_process 的返回值为表达式的返回值。
内置的 config 函数可以用于为返回值指定序列化参数，例如 mimetype、encoding 等。

### 语法说明

Dataway 基于 Python3.4 语法实现，出于安全性的考量，在 Dataway 中，如下的 Python 语法被禁止使用：

- while/for 循环
- try/except/finally 语句
- yield 语句
- class 类型定义语句
- import/from..import 语句

### dw_process 入口函数详解

dw_process 是 Dataway 脚本的主入口，其作用相当于 C/C++ 语言中的 main 函数。

dw_process 仅接受一个类型为 PyMessage 的参数，而其返回值就是该 Dataway 表达式最终的输出值。
作为企业集成服务数据处理流程的一个环节，dw_process 函数的返回值类型受到严格限制，其返回的结果中仅支持如下类型，否则会导致运行时的序列化错误：

- str：即字符串
- None：Python 中的空值
- bool：布尔值
- float：浮点数
- int：整数
- list：列表，序列类型容器
- dict：字典，kv 类型容器
- PyMessage：即企业集成服务中的消息，在 Dataway 中以 PyMessage 进行访问
- PyMessageObject：即企业集成服务中的消息数据，在 Dataway 中以 PyMessageObject 类型进行访问，包括 mimeType、encoding、raw、value 等数据
- PyMultiMap：多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。通常用于 PyMessage 的 attr 属性中
    
对于 list/dict/PyMultiMap 等容器类型，其元素的也只能是上述类型。

### PyMessage 中的预定义属性

PyMessage 中包含的属性称之为预定义属性（Predefined Properties），这些属性由系统根据当前运行信息及处理的消息生成，用于在 Dataway 中通过程序化的方式获取上下文信息。

目前 PyMessage 中包含的属性有 **var**、**payload**、**attr**、**id**、**seq_id**、**error** 等，可以通过msg.var、msg.payload、msg.attr、msg.id、msg.seq_id、msg.error 的方式进行访问，具体说明可见下文 [Dataway 语言手册](#dataway-.E8.AF.AD.E8.A8.80.E6.89.8B.E5.86.8C)。



## Dataway 语言手册

### Dataway 类型系统

由于 Dataway 表达式是标准的 Python 脚本，在 Dataway 处理过程中，用户可以使用并构造允许的任意类型。但是作为企业集成服务数据流转的重要入口，dw_process 的返回值类型是受到严格限制的，其返回的结果中仅支持如下类型，否则（一定）将导致运行时的序列化错误：

- str：即字符串
- None：Python 中的空值
- bool：布尔值
- float：浮点数
- int：整数
- list：列表，序列类型容器
- dict：字典，kv 类型容器
- PyMessage：即企业集成服务中的消息，在 Dataway 中以 PyMessage 进行访问；
- PyMessageObject：即企业集成服务中的消息数据，在 Dataway 中以 PyMessageObject 类型进行访问，包括mimeType、encoding、raw、value 等数据；可以通过如下方式访问 PyMessageObject中 的内容：
   - obj['blob']：获取该消息对象的负载，返回 bytes 类型的数据
   - obj['mime_type']：获取该消息对象的 encoding，返回 str
   - obj['encoding']：获取该消息对象的 encoding，返回 str
   - obj['value']：根据 mime_type 和 encoding，对负载数据进行反序列化，并返回其结果
   - obj.get(attr)：根据 mimetype/encoding 对 message 的内容进行反序列化，并获取其中指定 key 的值。逻辑上相当于 obj['^value'].get(attr)
   对于以下标方式访问 PyMessageObject 的详细定义，可参考 [选择器](#pymessageobject-.E9.80.89.E6.8B.A9.E5.99.A8)
- PyMultiMap：多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。通常用于 PyMessage 的 attr 属性中

### Dataway 内置变量及函数

#### Dataway 预定义属性（Predefined Properties） 

PyMessage 中包含的属性称之为预定义属性（Predefined Properties），这些属性是由系统根据当前运行信息及处理的消息生成的，用于在 Dataway 中通过程序化的方式获取上下文信息。 
   目前 PyMessage 中包含的属性及其说明如下： 
- msg.var：局部消息变量，dict 类型，键为 string，代表变量名，值为允许的任意类型，代表变量值
   var 会在一条消息处理的所有环节共享，因此可以用于在不同的处理节点之间进行数据的传递
- msg.payload：当前消息负载数据，可以是允许的任意类型
   payload 是一条消息对象的负载数据，一般是由上一个组件通过 set-payload 或者 transform 组件生成的，其可能的数据类型即是上文中列举的 Dataway 中允许的返回值类型
   listener 组件会根据用户发送的原始消息来构造 payload 的内容，因此 listener 组件处理之后，payload 都是 PyMessageObject 类型，除非在下游通过 set-payload 或者 transform 组件对 payload 进行重新赋值
- msg.attr：当前消息的属性数据，包括消息类型、消息的头部信息等。dict 类型，键为 str，代表属性名，值为任意类型，代表属性值，attr 是消息的属性数据
- msg.id：当前消息的唯一标识 id，str 类型
- msg.seq_id：当前消息的序列号，str 类型
- msg.error：当前处理上下文中的错误信息。dict 类型，键为 str，值为 str
   包含的内容有：
   msg.error['code']：错误类型
   msg.error['desc']：错误描述字符串

#### config 函数
config 函数用于指定脚本输出值的相关参数，例如 mime_type 等，基本用法：
```
config(mime_type="application/json")
```
在同一个 Dataway 表达式中，config 可以在任意位置被多次调用，最终以最后一次执行的结果为准。


####  Python 上下文环境中的内置变量及函数
可参考 [Python 官方文档](https://docs.python.org/3.5/library/functions.html#built-in-funcs)。目前 Dataway 中支持的函数如下： 

- abs()：求数值绝对值
- all()：判断序列（集合、列表、元组、dict）中所有元素是否满足给定条件
- dict()：创建字典
- min()：数值最小值
- any()：判断集合中是否存在元素满足给定条件
- sorted()：排序
- bool()：构造布尔值
- int()：构造整数
- str()：构造字符串
- sum()：数值求和
- filter()：集合过滤，例如 filter(lambda x:x>100, [1,3,4,100,102]) -> [100,102]
- pow()：求指数
- float()： 构造浮点数
- tuple()：构造元组
- len()：获取集合元素个数
- list()：构造列表
- max()：获取数值最大值
- round()：截取数值的整数部分

### 其它可用的模块

- **time**，用于时间处理的库，可参考 Python 官方文档。已内置在 Dataway 的处理上下文中，可以直接引用
   目前 Dataway 中支持的库函数/类型如下： 
	- time()：函数，返回当前时间戳，float 类型，单位为秒
	- struct_time：类型，表示一个结构化时间对象
	- altzone：当前时区相对于 UTC 时区的延迟偏移，单位为秒
	- asctime：将一个 struct_time 转换为时间字符串
	- ctime：将一个时间戳转换为时间字符串
	- mktime()：将一个 struct_time 转换为时间戳
	- strftime()：将一个 struct_time 进行格式化
	- timezone：当前时区
	- tzname：当前时区名称
	- gmtime：将一个时间戳转换为 struct_time 对象
	- localtime：将一个时间戳转换为当前时区的本地时间，返回 struct_time 类型对象
- **json**，用于处理 json 数据的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/json.html)。已内置在 Dataway 的处理上下文中，可以直接引用
    目前 Datawa y中支持的 json 模块函数： 
	- dumps：将 json 对象编码为 json 字符串
	- loads：将一个 json 串解析为 Python 对象
- **math**，用于数学运算的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/math.html)。已内置在 Dataway 的处理上下文中，可以直接引用 
    - 目前 Dataway 中支持的 math 模块函数： 
		- math.ceil(x)：返回 x 的上限，即大于或者等于 x 的最小整数。如果 x 不是一个浮点数，则委托 x.ceil(), 返回一个 Integral 类的值
		- math.floor(x)：返回 x 的向下取整，小于或等于 x 的最大整数。如果 x 不是浮点数，则委托 x.floor() ，它应返回 Integral 值
		- math.fabs(x)：返回 x 的绝对值
		- math.pow(x,y)：返回 x 的 y 次幂
		- math.sqrt(x)：返回 x 的平方根
    - 支持的常量： 
		- math.pi：数学常数 π = 3.141592...，精确到可用精度
		- math.e：数学常数 e = 2.718281...，精确到可用精度
		- math.inf：浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出
		- math.nan：浮点“非数字”（NaN）值。 相当于 float('nan') 的输出

### PyMessageObject 选择器

对于 PyMessageObject 类型的变量，例如预定义属性 msg.payload，Dataway 支持通过选择器（selector）的方式进行快速访问，支持的操作类型如下：

| 下标类型                                 | 描述                                                         | 举例                     |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------ |
| 数字                                     | 访问当前数组的第 i 个元素                                      | payload[0]               |
| 以^开头的字符串                          | 获取元信息，例如 ^mimeType、^encoding、^raw（原始⼆进制）、^value（值） | msg.payload["^mimeType"] |
| 普通字符（字⺟、数字、下划线、横杠、点） | 普通字符的 key，按 key、nodeName、name 等⽅式获取当前元素的⼦元素，如果有多个同名的，只返回第⼀个 | msg.payload["list"]      |
