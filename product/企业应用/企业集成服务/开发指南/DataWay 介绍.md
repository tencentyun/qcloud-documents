## 简介

DataWay 是企业基础服务服务中用于对数据进行自定义转换与处理的表达式脚本语言，集成在企业基础服务运行时服务中，是提供企业基础服务可扩展性的关键能力。

企业基础服务的许多内置组件中都可以提供基于 DataWay 脚本的自定义能力，可以用于对企业基础服务事件进行动态处理。例如在 set-variable 组件中，可以通过 DataWay 表达式来动态地设置变量的值；在 Transform 组件中，可以充分利用 DataWay 的灵活语法进行复杂的数据处理与表达式运算，以最终生成期望的 payload 产出，用于下游组件的处理。

## 脚本结构

完整的 DataWay 脚本是符合语法定义的 Python 代码段，被以三个以上的连续#符号开头的注释行分为 Header 和 Body 两个部分，例如：

```
#! dataway: v1.0.0
def func(x):
    return x*x
sq = func(3)
output(mime_type='application/json')
####
{
    'square': sq,
    'data': payload['realData']
}
```

其中 Header 部分可以是任意符合语法规范的代码，Body 部分则必须是标准的 Python 表达式 。在内联表达式的场景下，若不指定`###`分隔符，则整个脚本会被解析为 Body 部分 。
从概念上，可以把 Header 理解为数据的预处理步骤，Body 则是最终需要输出的数据。
Header 和 Body 在运行时共享所有的局部变量，因此在 Header 定义的所有变量都在 Body 部分可用。

## 语法说明

DataWay 基于 Python3.4 语法进行实现，Header 部分是 Python 代码块，Body 则是标准的Python表达式
出于安全性的考量，在 DataWay 中，如下的 Python 语法被禁止使用：
- while/for 循环
- try/except/finally 语句
- yield 语句
- class类型定义 语句
- import/from..import 语句



## Header 部分详解

Header 部分是 DataWay 脚本的预处理阶段，可以用于定义局部变量或函数、导入库函数、执行复杂的处理逻辑、或者指定输出相关的参数等。
Header 中的操作必须是符合 Python3.4 语法的代码块，以下是几种可以在 Header 部分进行的常用操作：
- output 配置：output 函数用于指定输出消息的相关参数，例如 mime_type 等
- 函数定义及函数调用
- 变量定义及数据处理
- 其它操作：除上述语法说明中被禁止之外的其它 Python 操作都可以在 Header 部分进行

## Body 部分详解

Body 部分为 DataWay 脚本最终产出的数据，因此需要以标准的 Python 表达式（expression，可以理解为有值的语句）的方式提供。
由于 Body 的产出最终会通过序列化进行输出，因此 __Body表达式的值必须是以下类型及其组合类型__，否则将导致运行时的序列化错误：
- str
- None
- bool
- float
- int
- list
- dict
- PyMessage：即企业基础服务中的消息，在 DataWay 中以 PyMessage 进行访问。
- PyMessageObject：即企业基础服务中的消息数据，在 DataWay 中以 PyMessageObject 类型进行访问，包括 mimeType、encoding、raw 等数据。
- PyMultiMap：多值 map，通常用于 attr 预定义变量中。

>?对于 list/dict/PyMultiMap 等容器类型，其元素的也只能是上述类型。


## 预定义变量

在 DataWay 的处理上下文中，系统会根据当前处理的消息，预置一些环境变量，用于在 DataWay 中通过程序化的方式获取上下文信息。这些变量被称之为`__预定义变量（Predefined Variables）__`。目前支持的预定义变量有 `var__`、`__payload__`、`__attr__`、`__id__`、`__seq_id__`、`__error__`等，具体说明可参见本文 [DataWay 语言手册](#dataway-.E8.AF.AD.E8.A8.80.E6.89.8B.E5.86.8C)。


## 字面量与表达式

企业基础服务中的大部分组件都具备对 DataWay 表达式的求值能力。目前，除了在 Transform 组件中可以编写完整的 DataWay 脚本（最终存储为 json/xml 配置时，需用`#[]`进行包裹）之外，其它组件的表达式是以内嵌表达式（inline expression）的形式作为property 使用。

内嵌表达式有两种形式：
- 字面量：即任意的常量字符串。
- 当 property 的值被`#[]`包裹时，`#[]`内部的字符串将被解析为 DataWay 脚本表达式，用户可以在其中包含完整的 Header、Body等。

## 选择器

对于 PyMessageObject 类型的变量，例如上游直接传递的 payload、variable 等，DataWay 支持通过选择器（selector）的方式进行快速访问，支持的操作类型如下：

| 下标类型                                                 | 描述                                                     | 举例           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------- |
| 数字                                                         | 访问当前数组的第 i 个元素                                      | payload[0]          |
| 以`^`开头的字符串                                            | 获取元信息，例如 ^mimeType、^encoding、^raw（原始二进制）、^value（值） | payload["^mimeType"]     |
| 普通字符（字母、数字、下划线、横杠、点）                     | 普通字符的 key，按 key、nodeName、name 等方式获取当前元素的子元素，如果有多个同名的，只返回第一个 | payload["list"]     |

## DataWay 语言手册
### DataWay 内置变量及函数

#### DataWay 预定义变量
在 DataWay 的处理上下文中，系统会根据当前处理的消息，预置一些环境变量，用于在 DataWay 中通过程序化的方式获取上下文信息。这些变量被称之为 预定义变量(Predefined Variables) 。目前支持的预定义变量有： 
- `var__`：局部消息变量，dict类 型，键为 string，代表变量名，值为任意类型，代表变量值。
   var会在一条消息处理的所有环节共享，因此可以用于在不同的处理节点之间进行数据的传递。
- `__payload`：当前消息负载数据，可以是允许的任意类型。payload 是一条消息对象的负载数据。
- `__attr__`：当前消息的属性数据，包括消息类型、消息的头部信息等。dict 类型，键为 str，代表属性名，值为任意类型，代表属性值
   attr 是消息的属性数据。
-  `__id__`：当前消息的唯一标识 ID。str 类型。
-  `__seq_id__`：当前消息的序列号。str 类型。
- `__error__`：当前处理上下文中的错误信息。dict 类型，键为 str，值为 str。



#### output 函数
output 函数用于指定脚本输出值的相关参数，例如 mime_type 等，基本用法：
```
output(mime_type="application/json")
```


Python 上下文环境中的内置变量及函数，可参考 [Python 官方文档](https://docs.python.org/3.5/library/functions.html#built-in-funcs)。目前 DataWay 中支持的函数如下：

-  abs()：求数值绝对值
- all()：判断序列(集合、列表、元组、dict)中所有元素是否满足给定条件
-  dict()：创建字典
-  min()：数值最小值
-  any()：判断集合中是否存在元素满足给定条件
-  sorted()：排序
- bool()：构造布尔值
- int()：构造整数
- str()：构造字符串
- sum()：数值求和
- filter()：集合过滤，例如 filter(lambda x:x>100, [1,3,4,100,102]) -> [100,102]
- pow()：求指数
- float()： 构造浮点数
- tuple()：构造元组
-  len()：获取集合元素个数
-  list()：构造列表
-  max()：获取数值最大值
- round()：截取数值的整数部分

### 其它可用的模块

- ` __time__`，用于时间处理的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/time.html)。目前 DataWay 中支持的库函数/类型如下： 
	-  time()：函数，返回当前时间戳，float 类型，单位为秒
	-  struct_time：类型，表示一个结构化时间对象
	- altzone：当前时区相对于 UTC 时区的延迟偏移，单位为秒
	- asctime：将一个 struct_time 转换为时间字符串
	- ctime：将一个时间戳转换为时间字符串
	- mktime()：将一个 struct_time 转换为时间戳
	- strftime()：将一个 struct_time 进行格式化
	- timezone：当前时区
	- tzname：当前时区名称
	- gmtime：将一个时间戳转换为 struct_time 对象
	- localtime：将一个时间戳转换为当前时区的本地时间，返回 struct_time 类型对象
-  `__json__`，用于处理 JSON 数据的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/json.html)。目前 DataWay 中支持的函数： 
	- dumps：将 JSON 对象编码为 JSON 字符串
	- loads：将一个 JSON 串解析为 Python 对象
- `__math__`，用于数学运算的库，可参考 [Python 官方文档](https://docs.python.org/3.5/library/math.html)。目前 DataWay 中支持的函数： 
	- acos
	- acosh
	- asin
	- asinh
	- atan
	- atan2
	- atanh
	- ceil
	- copysign
	- cos
	- cosh
	- degrees
	- e
	- exp
	- fabs
	- factorial
	- floor
	- fmod
	- frexp
	- fsum
	- hypot
	- isinf
	- isnan
	- ldexp
	- log
	- log10
	- log1p
	- modf
	- pi
	- pow
	- radians
	- sin
	- sinh
	- sqrt
	- tan
	- tanh
	- trunc
