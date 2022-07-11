
代码模式 Python 对表达式模式进行了扩展，支持更复杂的语法和更强大的功能，另一方面，也提高了用户使用门槛，需要一定的 Python 语言编程基础。

## IDE 使用
### 使用流程
1. 对于任意 Dataway 编辑文本框，将鼠标移至编辑文本框，会自动弹出模式选择按钮，单击**代码**进入代码模式。
![](https://qcloudimg.tencent-cloud.cn/raw/e745a75553bbb8db299a462beea0602e.png)
2. 单击编辑文本框，弹出代码编辑器，默认即为 Python 脚本编辑器，即可进行 Python 脚本编辑。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/3e696074340fa889d059354f0ba8927c.png" alt="Python编辑框" style="zoom:50%;" />
3. 编辑完成后，单击**确定**保存。

### 功能说明
该编辑器提供了语法检查、格式化、脚本调试、自动联想、代码高亮等类 IDE 功能。

- **语法检查**
在 Python 脚本编辑器中，能够实时对 Pyton 脚本进行语法检查，并通过强提示显示在脚本编辑框左侧和出错代码底部。当鼠标移动到错误提醒处，会有详细的错误信息说明。
用户可以根据语法提示来对 Python 脚本进行修改，只有语法检查通过的代码才能够保存成功。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6c03db1d6f2fc6da7bd5fcffee0c6937.png" alt="ide-语法检查" style="zoom:50%;" />


- **格式化**
在 Python 脚本编辑器中，提供有格式化功能按钮。用户可以单击右上角格式化按钮，一键对 Python 脚本格式化，使代码更加简洁规范。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e65819f14899f4468139734717475e5d.png" alt="ide-格式化前" style="zoom:50%;" />
单击右上角格式化按钮后，格式化后的代码如下图。
<img src="https://qcloudimg.tencent-cloud.cn/raw/0a4d7eb0f8e91e8c5dc16ffeb91d82f0.png" alt="ide-格式化后" style="zoom:50%;" />


- **脚本调试**
在 Python 脚本编辑器中，提供有 Debug 调试功能按钮。用户可以点击右上角 Debug 按钮，在线对 Python 脚本进行调试。详细的使用方法可见 [Python 调试](#dataway-debug)。
<img src="https://qcloudimg.tencent-cloud.cn/raw/12ebd05313ba9e32f34e9258a138cde2.png" alt="ide-单元测试" style="zoom:50%;" />


- **自动联想**
    在编辑框中进行输入时，Python 脚本编辑器能够根据当前上下文自动给出语法提示，并展示在当前光标的下方。通常语法提示的范围包括内置函数、关键字和内置第三方模块。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/4cb7fac8514184793ae3dc570473a672.png" alt="ide-自动联想" style="zoom:50%;" />


- **集成流数据面板引用**
表达式模式支持集成流数据面板引用功能，详情请参见 [集成流数据面板](https://cloud.tencent.com/document/product/1270/73950#dataref)。


- **代码高亮**
Python 脚本编辑器默认对 Dataway 代码进行高亮和括号自动匹配。


##  脚本结构

完整的代码模式 Python 脚本需符合 Python3 语法，其中包含入口函数定义 def dw_process(msg) ，例如：
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

dw_process 入口函数仅接受一个参数 msg，该参数代表当前 Dataway 脚本需要处理的数据连接器消息。dw_process 函数的返回值即是脚本的返回值。

在"配置 Payload"组件中输入上述表达式，假设该组件的输入消息为 json 结构的数据`{"realData": 123}`，经过 Python 脚本的计算，得到的输出结果如下：

```json
{
    "square": 9,
    "data": 124
}
```

## Dataway基本语法说明

代码模式 Python 基于 Python3 语法实现，本小节将对代码模式 Python 的基本语法进行说明。

### 关键字

代码模式 Python 支持的关键字如下表所示。关键字作为代码模式 Python 中的保留字，不会被当成任何标识符名称。

| 关键字名称   | 说明                              |
| ------------ | --------------------------------- |
| True         | 布尔类型，True 表示真，相对于False |
| False        | 布尔类型，False 表示真，相对于True |
| None         | 空值类型                          |
| and          | 逻辑“与”                         |
| or           | 逻辑“或”                         |
| not          | 逻辑“非”                        |
| as           | 自定义命名                        |
| assert       | 断言，用来测试表达式              |
| break        | 终止循环语句                      |
| continue     | 跳过本次循环                      |
| def          | 函数定义                          |
| if/else/elif | 判断语句                          |
| for          | 循环语句                          |
| global       | 全局变量声明                      |
| in           | 判断是否包含在其中                |
| is           | 判断两个变量指向是否一致          |
| lambda       | 匿名函数，可以用一行实现一个函数  |
| nonlocal     | 在嵌套函数中声明，可以修改外部定义的变量 |
| pass         | 空语句，用于占位                         |
| raise | 抛出异常 |
| return | 函数返回 |

### 行和缩进

代码模式 Python 使用缩进来标识代码块，不同的缩进行数代表不同的代码层级，同一层级的缩进行数需保持一致。

### 运算符

代码模式 Python 支持常见的运算符：算数运算符、比较运算符、赋值运算符、逻辑运算符、位运算符等。下表列出了常见的运算符。假设变量 a 为5， b 为3，对应的示例如下：

| 运算符名称 | 说明                 | 示例                                     |
| ---------- | -------------------- | ---------------------------------------- |
| =          | 赋值                 | c = 3                                    |
| +          | 加                   | a + b = 3                                |
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

- 代码模式 Python 通过 if / elif / else 语句来进行条件控制。示例如下，通过判断 a 的值，返回不同的字符串：
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
Dataway表达式的运行结果为：`a is between 10 and 100`
  
- 代码模式 Python 通过 for 循环进行循环控制。示例如下，通过 for 循环，得到 a 中元素的乘积：
```python
def dw_process(msg):
    a = [1, 2, 3, 4]
    num = 1
    for i in a:
        num *= i
    return num
```
Dataway 表达式的运行结果为：`24`

### 定义函数

在代码模式 Python 中，可以使用 def 关键词定义函数，后接函数名和参数名列表，以冒号`:`作为定义函数行的结尾，下一行默认缩进；最终以 return 语句结束函数，如果不带 return 相当于返回 None。

定义了一个函数后，可以在另一个函数中调用执行。在代码模式 Python 中，默认的入口函数 dw_process 函数无需手工声明。如果想自定义函数，直接在 dw_process 入口函数下方定义即可。如下示例，定义了一个函数 test() 用于对列表元素求和， 并在 dw_process() 函数中调用，最终使用 return 语句返回结果。
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

代码模式 Python 内置了多个第三方模块，如 time、json、math、base64、hmac、random、 hashlib、Crypto、socket、struct、decimal 和 datetime 等，使用时直接引用模块名即可，无需使用 import关键字。具体的函数说明可参考 [Dataway函数参考](https://cloud.tencent.com/document/product/1270/73961#function-reference)。具体示例如下，接收一个 json 类型字符串，转换成一个字典：
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

代码模式 Python 单行注释以`#`开头，多行注释则可以用多个`#` 号，或者 `'''`和`"""`。举例如下，执行下面代码：
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

>?代码模式 Python 提供了语法检查功能，在编写代码时会进行实时语法检查，并给出错误提示。详细的语法说明可以参考 [Python 官方文档](https://docs.python.org/zh-cn/3.5/reference/index.html)。

## dw_process 入口函数
dw_process 是代码模式 Python 的主入口函数，其作用相当于 C/C++语言中的 main 函数。

dw_process 仅接受一个类型为 [Message](https://cloud.tencent.com/document/product/1270/73950#message-explain) 的参数，而其返回值就是该代码模式 Python 脚本的输出值。

作为数据连接器中数据处理流程的一个环节，dw_process 函数的返回值目前支持 [核心类型](https://cloud.tencent.com/document/product/1270/73950#core-types)。

关于代码模式 Python 中数据类型及返回值的详细介绍，可参考 DataWay 类型系统 [DataWay 数据类型系统](#dataway-types)。


[](id:dataway-types)
## 数据类型系统
| 类型名 | 说明 | 是否 Dataway 特有类型 | 举例 |
| ----- | ---- | --------------- | --- |
| str | 字符串，即 Python 原生的字符串 str | 否 | "abc" |
| None | Python 中的空值 None | 否 | None |
| bool | 布尔值，即 Python 原生布尔值 bool | 否 | True/False |
| float | 浮点数，即 Python 原生浮点数 float | 否 | 123.123 |
| int | 整数，即 Python 原生整型 int | 否 | 123 |
| bytes | 字节数组，即 Python 字节数组类型 bytes | 否 | b'this_is_a_bytes' |
| set | 集合，即 Python 集合类型set | 否 | {1,2,3} |
| list | 列表，序列类型容器，即 Python 原生 list 类型 | 否 | [1,2,3] |
| dict | 字典，kv 类型容器，即 Python 原生 dict 类型 | 否 | {1:1, 'key': 'value'} |
| **Entity** | 即 EIS 中的实体数据，用于代表一个二进制对象，在 Dataway 中以 Entity 类型进行访问，包括blob、mime_type、encoding等信息 | 是 | http-listener构造消息中的 payload，如 msg.payload |
| **MultiMap** | 多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key。 | 是 | application/www-form-urlencoded 格式的数据解析之后得到的对象 |
| **FormDataParts**| 数组+列表的数据结构，类似于 Python 中的 orderDict 结构| 是 | multipart/form-data 格式的数据解析后得到的对象|
| **Message** | 即 eis 中的消息，在 dataway 中以 Message 进行访问 | 是 | dw_process 入口函数中的 msg 参数 |


>!
>- 上述类型可以在代码模式 Python 中使用，但 **dw_process函数的返回值的类型为 [核心类型](https://cloud.tencent.com/document/product/1270/73950#core-types) 之一**。
>- 如果 Dataway 表达式输出的值会作为集成流的最终返回结果，则支持的返回值类型还会受到相应连接器组件的限制。如在以 http listener 组件作为第一个组件的流中，其最终的 payload 也需要是一个 Entity 类型。


[](id:dataway-debug)
## 脚本调试

代码模式 Python 支持脚本调试，以方便问题排查和结果验证。该功能可通过手工定义输入参数 msg， 点击测试后可以直接查看脚本运行结果、调试日志和错误信息。

1. 在脚本编辑框中输入表达式。
Dataway 调试模式下，支持在表达式中通过 print() 函数打印要观察的信息，运行结束后打印消息会显示在界面上。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/5bf051c8ac8496ac816217f29bad0671.png" alt="调试界面" style="zoom:50%;" />

2. 单击脚本编辑框右上角的 Debug 图标，弹出模拟数据填写对话框，在这里可以对 msg 的载荷、属性和变量进行设置。设置完成后单击**开始测试**，系统会自动组装成一个 msg 参数，并作为脚本的输入传递到 dw_process 函数中。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/5a8e4ff1bc6603ac7709638cf1030aa5.png" alt="模拟数据" style="zoom:50%;" />

3. 运行完成 dw_process 函数后，编辑框下方会弹出运行结果和 print 调试日志，如果运行错误会有 error 报错信息。
	- **输出**：代表 Dataway 表达式的运行结果。
	 <img src="https://qcloudimg.tencent-cloud.cn/raw/0e9d2d98a81736f3294f0c121d9b4127.png" alt="单测运行结果" style="zoom:50%;" />
	- **日志**：代表在脚本中使用 print 函数打印的调试日志。
	  <img src="https://qcloudimg.tencent-cloud.cn/raw/80720758e4387f476465acbcdfe1cf3a.png" alt="单测print日志" style="zoom:50%;" />
	- **错误**：代表脚本运行错误，运行正确无错误显示绿色对勾标志。



## 其他支持
代码模式 Python 提供多样的内置函数和第三方模块，用户可以按需选用，快速实现既定功能，详情请参阅[代码模式 Python 附录](https://cloud.tencent.com/document/product/1270/73955)。
