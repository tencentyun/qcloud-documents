## Dataway快速⼊⻔

Dataway 是企业集成服务中⽤于对数据进⾏⾃定义转换与处理的表达式脚本语⾔，集成在企业集成服务运⾏时服务中，是提供企业集成服务可扩展性的关键能⼒。
企业集成服务的许多内置组件中都可以提供基于Dataway脚本的⾃定义能⼒，可以⽤于对企业集成服务事件进⾏动态处理。例如在set-variable组件中，可以通过Dataway表达式来动态地设置变量的值；在 Transform 组件中，可以充
分利⽤ Dataway 的灵活语法进⾏复杂的数据处理与表达式运算，以最终⽣成期望的 payload 产出，⽤于下
游组件的处理。

### 脚本结构

完整的 Dataway 脚本是符合语法定义的 Python3 代码段，其中包含⼊⼝函数定义 def dw_process(msg)，
如：

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

dw_process⼊⼝函数仅接受⼀个参数，该参数代表当前表达式需要处理的企业集成服务消息。dw_process 的返回
值即是表达式的返回值。
内置的config函数可以⽤于为返回值指定序列化参数，如mimetype、encoding等。

### 语法说明

Dataway是基于Python3.4的语法进⾏实现的，出于安全性的考量，在Dataway中，如下的Python语法是
被禁⽌使⽤的：

1. while/for循环
2. try/except/finally语句
3. yield语句
4. class类型定义语句
5. import/from..import语句

### dw_process ⼊⼝函数详解

dw_process是Dataway脚本的主⼊⼝，其作⽤相当于C/C++语⾔中的main函数。
dw_process仅接受⼀个类型为PyMessage的参数，⽽其返回值就是该Dataway表达式最终的输出值。
作为企业集成服务数据处理流程的⼀个环节，dw_process函数的返回值类型是受到严格限制的，其返回的结果中
仅⽀持如下类型，否则会导致运⾏时的序列化错误：

1. str：即字符串
2. None：Python中的空值
3. bool：布尔值
4. float：浮点数
5. int：整数
6. list：列表，序列类型容器
7. dict：字典，kv类型容器
8. PyMessage：即企业集成服务中的消息，在Dataway中以PyMessage进⾏访问；
9. PyMessageObject：即企业集成服务中的消息数据，在Dataway中以PyMessageObject类型进⾏访问，包括
   mimeType、encoding、raw、value等数据；
10. PyMultiMap：多值map，类似于xml⽽与dict不同，该类型可以⽀持重复的key。通常⽤于
    PyMessage的attr属性中
    对于list/dict/PyMultiMap等容器类型，其元素的也只能是上述类型

### PyMessage 中的预定义属性

PyMessage中包含的属性称之为 预定义属性(Predefined Properties) ，这些属性是由系统根据当前运
⾏信息及处理的消息⽣成的，⽤于在Dataway中通过程序化的⽅式获取上下⽂信息。

2. 语法说明
3. dw_process⼊⼝函数详解
4. PyMessage中的预定义属性
   ⽬前PyMessage中包含的属性有 var、payload、attr、id、seq_id、error 等，可以通过msg.var、
   msg.payload、msg.attr、msg.id、msg.seq_id、msg.error的⽅式进⾏访问，具体说明可⻅Dataway语
   ⾔⼿册。

## Dataway 语⾔⼿册

这⾥是Dataway语⾔的技术⼿册，如果需要快速⼊⻔，请参考 Dataway快速⼊⻔



### Dataway类型系统

由于Dataway表达式就是是标准的Python脚本，在Dataway处理过程中，⽤户可以使⽤并构造允许的任
意类型。但是作为企业集成服务数据流转的重要⼊⼝，dw_process的返回值类型是受到严格限制的，其返回的结
果中仅⽀持如下类型，否则(⼀定)会导致运⾏时的序列化错误：

1. str：即字符串
2. None：Python中的空值
3. bool：布尔值
4. float：浮点数
5. int：整数
6. list：列表，序列类型容器
7. dict：字典，kv类型容器
8. PyMessage：即企业集成服务中的消息，在Dataway中以PyMessage进⾏访问；
9. PyMessageObject：即企业集成服务中的消息数据，在Dataway中以PyMessageObject类型进⾏访问，包括
   mimeType、encoding、raw、value等数据；
   可以通过如下⽅式访问PyMessageObject中的内容：
   obj['^blob']：获取该消息对象的负载，返回bytes类型的数据
   obj['^mime_type']：获取该消息对象的encoding，返回str
   obj['^encoding']：获取该消息对象的encoding，返回str
   obj['^value']：根据mime_type和encoding，对负载数据进⾏反序列化，并返回其结果
   obj.get(attr)：根据mimetype/encoding对message的内容进⾏反序列化，并获取其中指定key的值。
   逻辑上相当于 obj['^value'].get(attr)
   对于以下标⽅式访问PyMessageObject的详细定义，可参考 选择器⽂档
10. PyMultiMap：多值map，类似于xml⽽与dict不同，该类型可以⽀持重复的key。通常⽤于
    PyMessage的attr属性中

### Dataway内置变量及函数

#### Dataway预定义属性(Predefined Properties)

PyMessage中包含的属性称之为 预定义属性(Predefined Properties) ，这些属性是由系统根据当
前运⾏信息及处理的消息⽣成的，⽤于在Dataway中通过程序化的⽅式获取上下⽂信息。
Dataway语⾔⼿册

1. Dataway类型系统
2. Dataway内置变量及函数
   ⽬前PyMessage中包含的属性及其说明如下：
   a. msg.var：局部消息变量，dict类型，键为string，代表变量名，值为允许的任意类型，代表变
   量值
   var会在⼀条消息处理的所有环节共享，因此可以⽤于在不同的处理节点之间进⾏数据的传递
   b. msg.payload：当前消息负载数据，可以是允许的任意类型
   payload是⼀条消息对象的负载数据，⼀般是由上⼀个组件通过set-payload或者transform组件
   ⽣成的，其可能的数据类型即是上⽂中列举的Dataway中允许的返回值类型。
   listener组件会根据⽤户发送的原始消息来构造payload的内容，因此listener组件处理之后，
   payload都是PyMessageObject类型，除⾮在下游通过set-payload或者transform组件对
   payload进⾏重新赋值；
   c. msg.attr：当前消息的属性数据，包括消息类型、消息的头部信息等。dict类型，键为str，代
   表属性名，值为任意类型，代表属性值
   attr是消息的属性数据
   d. msg.id：当前消息的唯⼀标识id。str类型
   e. msg.seq_id：当前消息的序列号。str类型
   f. msg.error：当前处理上下⽂中的错误信息。dict类型，键为str，值为str。
   包含的内容有：
   msg.error['code']：错误类型
   msg.error['desc']：错误描述字符串

#### config函数

config函数⽤于指定脚本输出值的相关参数，如mime_type等，基本⽤法：

```
config(mime_type="application/json")
```

在同⼀个Dataway表达式中，config可以在任意位置被多次调⽤，最终以最后⼀次执⾏的结果为准

#### 
 Python上下⽂环境中的内置变量及函数，可参考Python官⽅⽂档。⽬前Dataway中⽀持的函数如
下：
a. abs()：求数值绝对值
b. all()：判断序列(集合、列表、元组、dict)中所有元素是否满⾜给定条件
c. dict()：创建字典
d. min()：数值最⼩值
e. any()：判断集合中是否存在元素满⾜给定条件
f. sorted()：排序
g. bool()：构造布尔值
h. int()：构造整数
1 config(mime_type="application/json")
i. str()：构造字符串
j. sum()：数值求和
k. filter()：集合过滤，如filter(lambda x:x>100, [1,3,4,100,102]) -> [100,102]
l. pow()：求指数
m. float()： 构造浮点数
n. tuple()：构造元组
o. len()：获取集合元素个数
p. list()：构造列表
q. max()：获取数值最⼤值
r. round()：截取数值的整数部分

### 其它可⽤的模块

. time，⽤于时间处理的库，可参考Python官⽅⽂档。已内置在Dataway的处理上下⽂中，可以直接
引⽤
⽬前Dataway中⽀持的库函数/类型如下：
a. time()：函数，返回当前时间戳，float类型，单位为秒
b. struct_time：类型，表示⼀个结构化时间对象
c. altzone：当前时区相对于UTC时区的延迟偏移，单位为秒
d. asctime：将⼀个struct_time转换为时间字符串
e. ctime：将⼀个时间戳转换为时间字符串
f. mktime()：将⼀个struct_time转换为时间戳
g. strftime()：将⼀个struct_time进⾏格式化
h. timezone：当前时区
i. tzname：当前时区名称
j. gmtime：将⼀个时间戳转换为struct_time对象
k. localtime：将⼀个时间戳转换为当前时区的本地时间，返回struct_time类型对象

2. json，⽤于处理json数据的库，可参考Python官⽅⽂档。已内置在Dataway的处理上下⽂中，可以
   直接引⽤
   ⽬前Dataway中⽀持的json模块函数：
   a. dumps：将json对象编码为json字符串
   b. loads：将⼀个json串解析为Python对象
3. math，⽤于数学运算的库，可参考Python官⽅⽂档。已内置在Dataway的处理上下⽂中，可以直接
   引⽤
   ⽬前Dataway中⽀持的math模块函数：
4. 其它可⽤的模块
   i. math.ceil(x)：返回 x 的上限，即⼤于或者等于 x 的最⼩整数。如果 x 不是⼀个浮点数，则
   委托 x.ceil(), 返回⼀个 Integral 类的值。
   ii. math.floor(x)：返回 x 的向下取整，⼩于或等于 x 的最⼤整数。如果 x 不是浮点数，则委
   托 x.floor() ，它应返回 Integral 值。
   iii. math.fabs(x)：返回 x 的绝对值。
   iv. math.pow(x,y)：返回 x 的 y 次幂。
   v. math.sqrt(x)：返回 x 的平⽅根。
   ⽀持的常量：
   i. math.pi：数学常数 π = 3.141592...，精确到可⽤精度。
   ii. math.e：数学常数 e = 2.718281...，精确到可⽤精度。
   iii. math.inf：浮点正⽆穷⼤。 （对于负⽆穷⼤，使⽤ -math.inf 。）相当于 float('inf') 的输
   出。
   iv. math.nan：浮点“⾮数字”（NaN）值。 相当于 float('nan') 的输出。

### PyMessageObject选择器

对于PyMessageObject类型的变量，如预定义属性msg.payload，Dataway⽀持通过选择器(selector)的
⽅式进⾏快速访问，⽀持的操作类型如下：

| 下标类型                                 | 描述                                                         | 举例                     |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------ |
| 数字                                     | 访问当前数组的第i个元素                                      | payload[0]               |
| 以^开头的字符串                          | 获取元信息，例如^mimeType、^encoding、^raw（原始⼆进制）、^value（值） | msg.payload["^mimeType"] |
| 普通字符（字⺟、数字、下划线、横杠、点） | 普通字符的key，按key、nodeName、name等⽅式获取当前元素的⼦元素，如果有多个同名的，只返回第⼀个 | msg.payload["list"]      |
