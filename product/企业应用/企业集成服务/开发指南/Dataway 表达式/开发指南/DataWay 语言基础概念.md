DataWay 语言是一门在 EIS 中用于对数据进行自定义转换与处理的表达式脚本语言。使用 DataWay 可以编写出强大和复杂的数据转换程序，在此之前需要先了解一下 DataWay 中的核心概念和功能。


## 脚本结构
- 完整的 DataWay 脚本符合语法定义的 Python3 代码段，其中包含入口函数定义 def dw_process(msg) ，例如：

```python
def dw_process(msg):  
    sq = func(3)
    val = {        
        'square': sq,        
        'data': msg.payload['realData'] + 1
    }
    return Entity.from_value(val, mime_type='application/json')

def func(x):
    return x*x
```

- dw_process 入口函数仅接受一个参数 msg，该参数代表当前表达式需要处理的 EIS 消息，dw_process 的返回值即是表达式的返回值。
- 内置的 Entity.from_value 函数用于为构造 Entity 类型的返回值，可以指定序列化参数，例如：mime_type、encoding 等。
- 在 Set Payload 组件中输入上述表达式，假设该组件的输入消息为 json 结构的数据`{"realData": 123}`，经过 DataWay 表达式的计算，得到的输出结果如下：

```json
{    
    "square": 9,
    "data": 124
}
```

## 基本语法说明
DataWay 基于 Python3.7 语法进行实现，本小节将对 DataWay 的基本语法进行说明。

### 关键字
在 DataWay 中，支持的关键字如下表所示。关键字作为 DataWay 中的保留字，不会被当成任何标识符名称。

| 关键字名称   | 说明                                     |
| ------------ | ---------------------------------------- |
| True         | 布尔类型，True 表示真，相对于 False        |
| False        | 布尔类型，False 表示假，相对于 True        |
| None         | 空值类型                                 |
| and          | 逻辑“与”                                |
| or           | 逻辑“或”                             |
| not          | 逻辑“非”                              |
| as           | 自定义命名                               |
| assert       | 断言，用来测试表达式                     |
| break        | 终止循环语句                             |
| continue     | 跳过本次循环                             |
| def          | 函数定义                                 |
| if/else/elif | 判断语句                                 |
| for          | 循环语句                                 |
| global       | 全局变量声明                             |
| in           | 判断是否包含在其中                       |
| is           | 判断两个变量指向是否一致                 |
| lambda       | 匿名函数，可以用一行实现一个函数         |
| nonlocal     | 在嵌套函数中声明，可以修改外部定义的变量 |
| pass         | 空语句，用于占位                         |
| raise        | 抛出异常                                 |
| return       | 函数返回                                 |

### 行和缩进

DataWay 使用缩进来标识代码块，不同的缩进行数代表不同的代码层级，同一层级的缩进行数需保持一致。

### 运算符

DataWay 支持常见的运算符：算数运算符、比较运算符、赋值运算符、逻辑运算符、位运算符等。下表列出了常见的运算符。其中，假设变量 a 为5、b 为3。

| 运算符名称 | 说明                 | 示例                                     |
| ---------- | -------------------- | ---------------------------------------- |
| =          | 赋值                 | c = 3                                    |
| +          | 加                   | a + b = 8                                |
| -          | 减                   | a - b = 2                                |
| *          | 乘                   | a * b = 15                               |
| /          | 除                   | 15 / a = b                               |
| %          | 取模，返回除法的余数 | 16 % b = 1                               |
| **         | 幂                   | a ** b = 125                             |
| //         | 向下取整             | a // b = 1                               |
| +=         | 加法赋值             | c += a等效于 c = c + a                   |
| -=         | 减法赋值             | c -= a 等效于 c = c - a                  |
| *=         | 乘法赋值             | c *= a 等效于 c = c * a                  |
| /=         | 除法赋值             | c /= a 等效于 c = c / a                  |
| ==         | 是否相等             | a == b 返回 False                        |
| !=         | 是否不等             | a != b 返回 True                         |
| >          | 大于比较             | a > b 返回 True                          |
| <          | 小于比较             | a  < b 返回 False                        |
| >=         | 大于等于比较         | a >= b 返回 True                         |
| <=         | 小于等于比较         | a <= b 返回 False                        |
| &          | 按位与               | a & b = 1(0101 & 0011 = 0001)            |
| \|         | 按位或               | a \| b = 7 (0101 & 0011 = 0111)          |
| ^          | 按位异或             | a ^ b = 6 (0101 ^ 0011 = 0110)           |
| ~          | 按位取反             | ~a = -6                                  |
| <<         | 左移运算符           | a << 3 = 20 (0000 0101 << 3 = 0001 0100) |
| <<         | 右移运算符           | a >> 1 = 2 (0101 >> 1 = 0010)            |

### 条件及循环控制语句
- DataWay 通过 if/elif/else 语句来进行条件控制。示例如下：通过判断 a 的值，返回不同的字符串：
 
```python
def dw_process(msg):  
    a = 100
    if a < 10:
        return 'a is lower than 10'
    elif a <= 100 and a >= 10:
        return 'a is between 10 and 100'
    else:
        return 'a is bigger than 100'
```
DataWay 表达式的运行结果为：`a is between 10 and 100`
- DataWay 通过 for 循环进行循环控制。示例如下：通过 for 循环，得到 a 中元素的乘积：
 
```python
def dw_process(msg): 
    a = [1, 2, 3, 4]
    num = 1
    for i in a:
        num *= i
    return num
```
DataWay 表达式的运行结果为：`24`

### 定义函数

- 在 DataWay 中，可以使用 def 关键词定义函数，后接函数名和参数名列表，以冒号“：”作为定义函数行的结尾，下一行默认缩进；最终以 return 语句结束函数，如果不带 return 则相当于返回 None。
- 定义一个函数后，可以在另一个函数中调用执行。在 DataWay 中，默认的入口函数 dw_process 函数无需手工声明。如果想自定义函数，直接在 dw_process 入口函数下方定义即可。如下示例，定义一个函数 test() 用于对列表元素求和，并在 dw_process() 函数中调用，最终使用 return 语句返回结果。

```python
def dw_process(msg): 
    a = [1, 2, 3, 4]
    return add_list(a)

def add_list(alist):
    sum = 0
    for i in reversed(alist):
        sum += i
    return sum
```

最终的输出结果为：`10`

### 模块调用

DataWay 内置多个第三方模块，例如：time、json、math、base64、hmac、random、 hashlib、Crypto、socket、struct、decimal 和 datetime 等，使用时直接引用模块名即可，无需使用 import 关键字。具体的函数说明可参考 [DataWay 函数参考](https://cloud.tencent.com/document/product/1270/55568)。具体示例如下，接收一个 json 类型字符串，转换成一个 dict 字典：

```python
def dw_process(msg):
    jsonStr = '{"a": 1, "b": 2, "c": 3}'
    jsonDict = json.loads(jsonStr)  # 转换成一个dict
    num = 1
    for k, v in jsonDict.items():   # 对dict进行遍历
        num += math.pow(v, 2)
    return num
```

最终的输入结果为: `15.0`

### 注释
DataWay 单行注释以`#`开头，多行注释则可以用多个`#` 号，或者`'''`和`"""`。举例如下，执行下面代码：

```python
# Dataway 注释

'''
Dataway 注释
Dataway 注释
'''
 
"""
Dataway 注释
Dataway 注释
"""
def dw_process(msg):
    return 'Dataway Hello World!'
```

输出结果为：

```python
Dataway Hello World!
```

>!DataWay 提供语法检查功能，在编写代码时会进行实时语法检查，并给出错误提示。详细的 Python 语法说明可以参考 [Python 官方文档](https://docs.python.org/zh-cn/3.5/reference/index.html)。

## dw_process 入口函数
- dw_process 是 DataWay 的主入口函数，其作用相当于 C/C++语言中的 main 函数。
- dw_process 仅接受一个类型为 [Message](#message-explain) 的参数，而其返回值就是该 DataWay 表达式最终的输出值。
- 作为 EIS 数据处理流程的一个环节，dw_process 函数的返回值目前支持的类型有：str/None/bool/float/int/list/dict/Entity/MultiMap/FormDataParts/Message 等。
- 关于 DataWay 中数据类型及返回值的详细介绍，可参考 [DataWay 数据类型系统](#dataway-types)。

## DataWay 数据类型系统

| 类型名            | 说明                                                         | 是否 DataWay 特有类型       | 举例                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------ |
| str               | 字符串，即 Python 原生的字符串 str                           | 否                        | "abc"                                                        |
| None              | Python 中的空值 None                                         | 否                        | None                                                         |
| bool              | 布尔值，即 Python 原生布尔值 bool                            | 否                        | True/False                                                   |
| float             | 浮点数，即 Python 原生浮点数 float                           | 否                        | 123.123                                                      |
| int               | 整数，即 Python 原生整型 int                                 | 否                        | 123                                                          |
| bytes             | 字节数组，即 Python 字节数组类型 bytes                       | 否                        | b'this_is_a_bytes'                                           |
| set               | 集合，即 Python 集合类型set                                  | 否                        | {1,2,3}                                                      |
| list              | 列表，序列类型容器，即 Python 原生 list 类型                 | 否                        | [1,2,3]                                                      |
| dict              | 字典，kv 类型容器，即 Python 原生 dict 类型                  | 否                        | {1:1, 'key': 'value'}                                        |
| Entity      | 即 EIS 中的实体数据，用于代表一个二进制对象，在 DataWay 中以 Entity 类型进行访问，包括blob、mime_type、encoding 等信息 | 是 | HTTP-listener 构造消息中的 payload，如 msg.payload            |
| MultiMap      | 多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。 |是| application/www-form-urlencoded 格式的数据解析之后得到的对象 |
|FormDataParts | 数组+列表的数据结构，类似于 Python 中的 orderDict 结构       | 是 | multipart/form-data 格式的数据解析后得到的对象               |
| Message       | 即 eis 中的消息，在 dataWay 中以 Message 进行访问            |是| dw_process 入口函数中的 msg 参数                             |

>!1. 上述类型可以在 DataWay 表达式中使用，但 **dw_process 函数的返回值的类型为其中的 str/None/ bool/float/int/list/ dict/Entity/MultiMap/FormDataParts/Message 之一**。
>2. 需要注意的是，如果 DataWay 表达式输出的值会作为集成流的最终返回结果，则支持的返回值类型还会受到相应连接器组件的限制。如在以 HTTP listener 组件作为第一个组件的流中，其最终的 payload 也需要是一个 Entity 类型。

## Message 类型及预定义属性

Message 类型是 DataWay 用于表示一条 EIS 消息的数据类型，其中包含 payload、vars、attrs 等属性，称之为**预定义属性（Predefined Properties）**。这些属性是由系统根据当前运行信息及处理的消息生成的，用于在 DataWay 中通过程序化的方式获取上下文信息。

**目前 Message 中包含的属性及其说明如下：**

| 属性        | 作用                                             | 属性类型                                                     | 属性说明                                                     |
| ----------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| msg.vars    | 当前消息上下文中的变量                           | dict 类型，键为 str 类型，代表变量名，值为允许的任意类型，代表变量值 | vars 会在消息处理的所有环节共享，因此可用于在不同的处理节点之间进行数据的传递 |
| msg.payload | 当前消息的载荷数据                               | 任意类型                                                     | payload 是一条消息对象的负载数据，一般是由上一个组件通过 Set-Payload 或者 Transform 组件生成的，其可能的数据类型即是上文中列举的 DataWay 中支持的返回值类型。HTTP listener 组件会根据用户发送的原始消息来构造 payload 的内容，因此 listener 组件处理之后，payload 都是 Entity 类型，除非在下游通过 set-payload 或者 transform 组件对 payload 进行重新赋值 |
| msg.attrs   | 当前消息的属性数据，如消息来源、消息的头部信息等 | dict 类型，键为 str，代表属性名，值为任意类型，代表属性值    | 如果 trigger 组件为 HTTP listener，则请求的 headers 将会被设置到 msg.attrs 中 |
| msg.id      | 当前消息的唯一标识 id                            | str 类型                                                     | 经过一个逻辑组件，msg.id 可能会变化                           |
| msg.seq_id  | 当前消息的序列号                                 | str 类型                                                     | 消息在流中流转时，msg.seq_id 保持不变                         |
| msg.error   | 当前处理上下文中的错误信息                       | dict 类型，键为 str，代表错误属性名；值为 str，代表属性值    | 包含的内容有：msg.error['code']：错误类型；msg.error['desc']：错误描述字符串 |

## DataWay IDE 使用
在 EIS 系统新建一个 Set Variable 组件，单击变量值文本框进入 DataWay 脚本编辑器，该编辑器提供语法检查、格式化、脚本调试、自动联想、代码高亮等类 IDE 功能。
<img src="https://main.qcloudimg.com/raw/27cb6a575cbd1bdac914981679ff2bc2/ide-%E6%95%B4%E4%BD%93%E9%A1%B5%E9%9D%A2.png" alt="ide-整体页面" style="zoom: 50%;" />

### 语法检查
在 DataWay IDE 中，能够实时对 DataWay 表达式进行语法检查，并通过强提示显示在 IDE 左侧和出错代码底部。当鼠标移动到错误提醒处，会有详细的错误信息说明。用户可以根据语法提示来对 DataWay 脚本进行修改，只有语法检查通过的代码才能够保存成功。
<img src="https://main.qcloudimg.com/raw/46bc25019af93bcb6b73dba766468444/ide-%E8%AF%AD%E6%B3%95%E6%A3%80%E6%9F%A5.png" alt="ide-语法检查" style="zoom:50%;" />

### 格式化
在 Dataway IDE 中，提供有格式化功能按钮。用户可以单击右上角格式化按钮，一键对 DataWay 代码格式化，以使代码更加简洁规范。
<img src="https://main.qcloudimg.com/raw/4373c5f877489eb9d67f27d1247a0dc3/ide-%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%89%8D.png" alt="ide-格式化前" style="zoom:50%;" />
 - 单击右上角格式化按钮后，格式化后的代码如下图：
![](https://main.qcloudimg.com/raw/f46937560a73d88ab0c32cd6d0823582/ide-%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%90%8E.png)

### 脚本调试
在 DataWay IDE 中，提供有 Debug 调试功能按钮。用户可以单击右上角“Debug”图标，在线对 DataWay 脚本进行调试。详细的使用方法可见 [DataWay 脚本调试](https://cloud.tencent.com/document/product/1270/55618)。
![](https://main.qcloudimg.com/raw/d59d57534cc3616ddc1a994530bf1d61/ide-%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95.png)

### 自动联想
DataWay IDE 能够自动对流中已配置的 payload、vars、attrs 中的变量名进行联想，并展示在 IDE 右侧栏。例如：在 Set Variable 组件前已经创建了一个 Set Payload 和一个 Set Variable 组件，则右侧栏会展示出来，单击对应的联想值会自动加入到左侧编辑框中。
![](https://main.qcloudimg.com/raw/ae9a1410a37e2a9144e0f3520918c12f/ide-%E8%87%AA%E5%8A%A8%E8%81%94%E6%83%B3.png)

### 代码高亮
Dataway IDE 默认对 Dataway 代码进行高亮和括号自动匹配。
