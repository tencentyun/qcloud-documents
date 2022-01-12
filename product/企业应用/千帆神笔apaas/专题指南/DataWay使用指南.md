## 操作场景
千帆神笔 aPaaS 中可通过 DataWay 语言对数据进行自定义转换与处理。通过 DataWay 可以编写出强大和复杂的数据转换程序。 

>?**私有化部署**租户需联系 aPaaS 服务商，提供租户ID，开通该功能。用户通过设计的自定义函数可使用在“流程编排/表达式”节点中。

## 前提条件
1. 已 [创建应用](https://cloud.tencent.com/document/product/1365/51314)。
2. 已登录 [千帆神笔 aPaaS 控制台](https://apaas.cloud.tencent.com/)，单击应用名称，进入设计态首页。

## 操作步骤
### 函数列表

1. 在千帆神笔 aPaaS 设计态首页，单击**应用设置** > **自定义函数**。
2. 根据页面提示完成授权后即可查看函数列表页面。
![](https://qcloudimg.tencent-cloud.cn/raw/c48066021cb56e79a6a0ea42a46cc035.png) 


### 创建函数

1. 在千帆神笔 aPaaS 设计态首页，单击**应用设置** > **自定义函数**。
2. 在自定义函数管理页面，单击**新建**，在弹出的新建函数表单中填写函数的配置信息。
![](https://qcloudimg.tencent-cloud.cn/raw/70b50908e44474aeee0b63305a136674.png)
	- 函数名称：要求在同一个应用中不能重复。 
	- 语言：目前支持 Python3.7、Nodejs12.16。       
	- 函数描述（选填）：函数的说明信息。
3. 单击**确认**，即可创建一个函数，并自动跳转至**函数代码**页。

>?此时创建的函数为初始创建阶段，并不能在其他组件中直接使用，还需进行函数的参数设置及代码的编写。


### 函数基本信息修改

1. 在千帆神笔 aPaaS 设计态首页，单击**应用设置** > **自定义函数**。
2. 在自定义函数管理页面，单击函数列表中的“函数名称”，进入函数基本信息页面。
![](https://qcloudimg.tencent-cloud.cn/raw/e4dc66020d1a2b4c6418355b746e162c.png)
3. 单击右上角**编辑**，弹出编辑函数弹窗。
![](https://qcloudimg.tencent-cloud.cn/raw/53ad7961da16c03e70ccf5f5200dd37c.png)
4. 修改函数描述信息，并单击**确认**，完成函数基本信息修改。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8b73cffa4d674b0b2b3f1d0d5ae9b543.png" width="60%">

>?函数基本信息修改目前仅支持对函数描述的修改。

### 函数代码管理

1. 在千帆神笔 aPaaS 设计态首页，单击**应用设置** > **自定义函数**。
2. 在自定义函数管理页面，单击操作列的**代码管理**，进入函数代码页。
在函数代码页中，区域1为函数入参设置区域，区域2为函数返回值类型设置区域，区域3为编辑函数代码的在线 IDE。
![](https://qcloudimg.tencent-cloud.cn/raw/e4e91386dec132db40cbee9dc5e30d35.png)
3. 设置函数参数：如需设置函数的请求参数，只要在区域 1 单击右上角的**编辑**即可弹出参数设置弹窗，依次设置所需参数信息即可，后续可对参数进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/3d3586c79abd0f6e3a64727f492807da.png)
**属性说明**
<table>
<thead>
<tr>
<th>属性</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>参数</td>
<td>必填属性，作为函数的输入变量，可以在自定义函数中直接使用</td>
</tr>
<tr>
<td>类型</td>
<td>必填属性，目前执行类型如下：<br><ul><li>number：数值类型，可以是整数也可以是实数</li><li>object：对象类型</li><li>boolean：布尔类型</li><li>dateTime：日期时间类型</li><li>collection：集合类型</li><li>stringLiteral：文本类型</li></ul></td>
</tr>
<tr>
<td>说明</td>
<td>非必填属性，对于参数的解释说明</td>
</tr>
</tbody></table>
>?参数名称及类型请谨慎设置，参数类型会在函数调用方进行校验，参数名称会在函数代码内引用。

4. 设置函数返回值类型。
   + object：对象类型
   + collection：集合类型
   + string：文本类型
   + number：数值类型，可以是整数也可以是实数
   + boolean：布尔类型
	 ![](https://qcloudimg.tencent-cloud.cn/raw/e46e3e0a8c633521932911060f185a55.png)

5. 编写函数内容。
![](https://qcloudimg.tencent-cloud.cn/raw/fad95c23f45761e19976f1c0fcb61ddb.png)

6. 单击右上方 Dubag，设置测试变量值，测试函数功能，功能测试无误后，即可使用此函数。
![](https://qcloudimg.tencent-cloud.cn/raw/e853eed0f8fee4c9b615fc594860d16e.png)
设置测试变量：
<img src="https://qcloudimg.tencent-cloud.cn/raw/a3512e5d5a6d3d3f24ab67fcabaa96fd.png" width="70%"/><br>
测试结果：
![](https://qcloudimg.tencent-cloud.cn/raw/6245a77db34911f9979d626e3057f88d.png)

### 函数删除
1. 在千帆神笔 aPaaS 设计态首页，单击**应用设置** > **自定义函数**。
2. 在自定义函数管理页面，单击操作列的**删除**。
![](https://qcloudimg.tencent-cloud.cn/raw/4cb2660adf0f55711ea9f1960bf66091.png)


## 代码开发

DataWay 基于 Python3.7 语法进行实现。

### 函数结构

Python 函数形态一般如下所示：

```plaintext
def dw_process(msg):
    level = msg.vars.get("level")
    leader = {}
    leader["name"] = str(level) + "级领导：aiden"
    leader["mobile"] = "15200000002"
    return leader
```

**入参**

 入口函数定义 def dw_process(msg)  ，输入参数为msg，该参数代表当前表达式需要处理数据。

**返回**

您的处理程序可以使用 return 来返回值。在 Python 环境下，您可以直接返回一个可序列化的对象。例如：返回一个 leader 对象。

**行和缩进**

DataWay 使用缩进来标识代码块，不同的缩进行数代表不同的代码层级，同一层级的缩进行数需保持一致。

### 基本语法
<dx-tabs>
::: 关键字
在 DataWay 中，支持的关键字如下表所示。关键字作为 DataWay 中的保留字，不会被当成任何标识符名称。

| 关键字名称   | 说明                                     |
| :----------- | :--------------------------------------- |
| True         | 布尔类型，True 表示真，相对于 False      |
| False        | 布尔类型，False 表示假，相对于 True      |
| None         | 空值类型                                 |
| and          | 逻辑“与”                                 |
| or           | 逻辑“或”                                 |
| not          | 逻辑“非”                                 |
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
:::
::: 运算符
DataWay 支持常见的运算符：算数运算符、比较运算符、赋值运算符、逻辑运算符、位运算符等。下表列出了常见的运算符。其中，假设变量 a 为5、b 为3。

| 运算符名称 | 说明                 | 示例                                     |
| :--------- | :------------------- | :--------------------------------------- |
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
| <          | 小于比较             | a < b 返回 False                         |
| >=         | 大于等于比较         | a >= b 返回 True                         |
| <=         | 小于等于比较         | a <= b 返回 False                        |
| &          | 按位与               | a & b = 1(0101 & 0011 = 0001)            |
| \|         | 按位或               | a \| b = 7 (0101 & 0011 = 0111)          |
| ^          | 按位异或             | a ^ b = 6 (0101 ^ 0011 = 0110)           |
| ~          | 按位取反             | ~a = -6                                  |
| <<         | 左移运算符           | a << 3 = 20 (0000 0101 << 3 = 0001 0100) |
| <<         | 右移运算符           | a >> 1 = 2 (0101 >> 1 = 0010)            |
:::
::: 注释
DataWay 单行注释以`#`开头，多行注释则可以用多个`#` 号，或者`'''`和`"""`。举例如下，执行下面代码： ![img](https://qcloudimg.tencent-cloud.cn/raw/e83933328eba29e8871899b45da00954.png)

输出结果为：![img](https://qcloudimg.tencent-cloud.cn/raw/8ec6d3511a514c376fa3f9fd962aa2a6.png)

:::
</dx-tabs>



### 内置函数

目前 DataWay 中支持的内置函数如下：
 
| 函数名 | 函数功能 | 
|---------|---------|
| abs()  |  求数值绝对值
|  all()  |  判断序列（集合、列表、元组、dict) 中所有元素是否满足给定条件
| any()  |  判断集合中是否存在元素满足给定条件
| bool()  |  构造布尔值
| bytearray()  |  构造字节数组
| bytes()  |  构造空字节
| chr()  |  0~256的整数对应的 ASCII 码
| dict()  |  创建字典
| enumerate()  |  将一个可遍历的数据对象组合列出数据和数据下标，一般用于 for 循环中
| filter()  |  集合过滤，例如：list(filter(lambda x:x>=100, [1,3,4,100,102])) -> [100,102]
| float()  |  构造浮点数
| getattr()  |  求一个对象的属性值
| hasattr()  |  判断一个对象是否有某个属性
| hash()  |  求哈希值
| id()  |  求对象的唯一标识
| int()  |  构造整数
| isinstance()  |  判断对象是否属于某种类型
| iter()  |  生成一个迭代器
| len()  |  获取集合元素个数
| list()  |  构造列表
| map()  |  根据函数对指定序列做映射，例如：list(map(lambda x: x * 2, [1, 2, 3, 4, 5])) -> [2, 4, 6, 8, 10]
| max()  |  获取数值最大值
| min()  |  数值最小值
| next()  |  返回迭代器的下一个项目，和 iter() 一起使用
| object()  |  返回空对象
| ord()  |  单个 ASCII 码字符的整数值
| pow()  |  求指数
| print()  |  DataWay 调试时可以打印相关信息（仅在 DataWay 表达式编辑时使用 Debug 功能生效）
| range()  |  创建可迭代对象，例如：list(range(5)) -> [0, 1, 2, 3, 4]
| reversed()  |  创建反转的迭代器，例如：list(reversed('abcdefg')) -> ['g', 'f', 'e', 'd', 'c', 'b', 'a']
| round()  |  截取数值的整数部分
| set()  |  创建一个集合
| slice()  |  设置截取元素的切片
| sorted()  |  排序
| str()  |  构造字符串
| sum()  |  数值求和
| tuple()  |  构造元组
| type()  |  返回对象类型
| zip()  |  打包可迭代对象中元素成多个 tuple。例如：list(zip([1,2,3], [4,5,6])) -> [(1, 4), (2, 5), (3, 6)]

### 脚本调试

在开发 Dataway 时，对脚本进行调试和测试，以方便问题排查和结果验证，该功能可通过手工定义输入参数 ，测试后可以直接查看脚本运行结果、调试日志和错误信息。 

**操作步骤：**

1. 创建一个自定义函数，设置输入参数并输入表达式脚本。
![img](https://qcloudimg.tencent-cloud.cn/raw/e97f4e884a22fbe927682eb8df36db2e.png)
2. 单击 Dataway 表达式编辑框右上角“Debug”，弹出参数设置页面，填写变量名称、取值类型、测试参数值后，点击**确定**开始测试，系统会自动组装成一个 msg 参数，并作为脚本的输入传递到 dw_process 函数中。 ![img](https://qcloudimg.tencent-cloud.cn/raw/b9d3f4534c08e6fe478e73d0becad60c.png)
参数设置：
![img](https://qcloudimg.tencent-cloud.cn/raw/60555a60257245f0930a006418cc6d32.png)
3. 运行完成 dw_process 函数后，编辑框下方会弹出输出结果和调试日志，如果运行错误会有 error 报错信息。
![img](https://qcloudimg.tencent-cloud.cn/raw/ab8a9166c6aa1b5302f2b18d1f153d87.png)

## 案列说明

这里通过设置员工公司个人邮箱，来说明在 apaas 应用中如何使用云函数。

### 创建函数

**操作步骤**： 

1. aPaaS 设计态应用中，点击应用设置 \>左侧导航栏中“自定义函数”>自定义函数管理页，点击**新建**，创建自定义函数。![img](https://qcloudimg.tencent-cloud.cn/raw/54647706b99dd1b33fdf7dc0f8a45c5e.png)
2. 弹出框中，填写函数名称、选择编程语言，点击**确定**创建函数。 ![img](https://qcloudimg.tencent-cloud.cn/raw/341e4f327447eb3caf92d9a18acee0f1.png)
函数创建成功后，跳转到代码管理页面，区域1 为函数入参设置区域，区域 2 为函数返回值类型设置区域，区域 3 为编辑函数代码的在线 IDE，如下图所示： ![img](https://qcloudimg.tencent-cloud.cn/raw/47fa68b745fe4006ee5d3217254cf8e4.png)

### 编写代码并测试验证

1. 设置函数入参。该步骤可选，如果该函数不需要使用入参，则无需设置。
 ![img](https://qcloudimg.tencent-cloud.cn/raw/d1fff6b966f82bdf711d958e1625d16e.png)
2. 设置返回值类型。
 ![img](https://qcloudimg.tencent-cloud.cn/raw/976750e7fb79974b99e173d878cb543d.png)
3. 编写函数内容。
 ![img](https://qcloudimg.tencent-cloud.cn/raw/fd69a67c881f28431a8200dd3a5ffca5.png)
4. 设置函数变量，测试代码功能。
![img](https://qcloudimg.tencent-cloud.cn/raw/79ffa9c9337257a815ef3eb501a79369.png)
测试结果如下：
![img](https://qcloudimg.tencent-cloud.cn/raw/5e402a559e67078974a8a13ef86ad30e.png)

### 在流程中使用函数

1. aPaaS 设计态应用中，点击流程编排，右上方点击**新建流程**，创建流程。
![img](https://qcloudimg.tencent-cloud.cn/raw/9c93b2b6a16d67a8426adf959526b052.png)
2. 流程开始节点，设置"员工"输入变量。
![img](https://qcloudimg.tencent-cloud.cn/raw/3beaf6d3c4cb1d8e036a057008f268d4.png)
3. 添加“表达式”节点，引用自定义函数、流程输入的员工变量，完成表达式设置。
通过以下语法调用自定义函数：
```javascript
cloud.staff()
```
可通过以下语法引用流程中变量及变量字段：
```
#staff.name
```
![img](https://qcloudimg.tencent-cloud.cn/raw/b849facf6356c344ee1b4f2c1c5b468f.png)
4. 添加“更新变量节点，并设置赋值，选择上一节点表达式输出变量，更新员工邮箱信息。
![img](https://qcloudimg.tencent-cloud.cn/raw/129f6a63285d9d9ecf3ef094bbef5eab.png)
设置赋值：
![img](https://qcloudimg.tencent-cloud.cn/raw/c33feb631bb648dcfc9db95cd9f07006.png)
5. 流程应用：对象创建时，触发流程，设置员工邮箱信息。
aPaaS设计态应用中，点击“对象建模”，勾选定位对象，设置员工对象事件处理。
![img](https://qcloudimg.tencent-cloud.cn/raw/e04378a0617a50424c3f0fb34c3bb5b8.png)
添加事件，并设置触发时机、选择流程等，点击**确定**完成流程应用。如下图所示：
![img](https://qcloudimg.tencent-cloud.cn/raw/33365599bda35186c90de86f18e46bfc.png)

### 功能测试

1. aPaaS 设计态应用中，右上方点击"预览"，测试表达式功能。
![img](https://qcloudimg.tencent-cloud.cn/raw/9450728d604e89248f3116ceb10ae1ee.png)
2. 点击进入新增员工信息页面，填写员工信息，创建对象。
![img](https://qcloudimg.tencent-cloud.cn/raw/089f583ba30d59179996d6f46dcede8e.png)
3. 员工信息列表页即可测试查看到表达式设置的个人邮箱信息。
![img](https://qcloudimg.tencent-cloud.cn/raw/089b02014cdf6adf45f0b11aaf3b95e3.png)
