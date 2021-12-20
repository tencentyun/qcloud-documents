

## 类型
- 在 DataWay 中， 用 Entity 类型来表示 EIS 中的实体数据，表示二进制数据的封装对象，其主要组成部分包括 blob、mime_type 以及 encoding。
 - blob：原始的二进制数据。
 - mime_type：表示二进制数据的内容格式，例如：application/json、application/www-form-urlencoded、multipart/form-data 等。
 - encoding：表示二进制数据的字符编码格式，例如：utf8、gbk 等。
- 可以通过如下方式访问 Entity 中的内容：
 - entity['^blob']：获取该消息对象的负载数据，返回 bytes 类型的对象。
 - entity['^mime_type']：获取该消息对象的 mime_type，返回 str 对象。
 - entity['^encoding']：获取该消息对象的 encoding，返回 str 对象。
 - entity['^value']：根据 mime_type 和 encoding，对负载数据 blob 进行反序列化，并返回其结果，该类型为 [DataWay类型系统](https://cloud.tencent.com/document/product/1270/55572) 中定义的类型之一。
- entity['xxxx']：根据 mimetype/encoding 对 message 的内容进行反序列化，并获取其中指定 key 的值，逻辑上相当于 obj<span>['^value']</span>['xxx']。
- entity.get(attr, default=None)：根据 mimetype/encoding 对 message 的内容进行反序列化，并获取其中指定 key 的值，如果获取不到则返回默认值 None，逻辑上相当于 obj['^value'].get(attr, default=None)。

## 选择器
对于 Entity 类型的变量，如预定义属性 msg.payload，DataWay 支持通过选择器 (selector) 的方式进行快速访问，支持的操作类型如下：

| 下标类型                                 | 描述                                                         | 举例                      |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------- |
| 数字                                     | 访问当前数组的第 i 个元素                                    | msg.payload[0]            |
| 以'^'开头的字符串                        | 获取元信息，例如：^mime_type、^encoding、^raw（原始二进制）、^value（值） | msg.payload['^mime_type'] |
| 普通字符（字母、数字、下划线、横杠、点） | 普通字符的 key，按名称的方式获取当前元素的子元素，如果有多个同名的，只返回第一个 | msg.payload['list']       |

下面将对这几种选择器类型举例说明。假设输入消息的 payload 值为一个 Entity 类型，其代表的负载数据 blob 反序列化后为一个 json 数组`[{"a1":1},{"b1":1,"b2":2,"b3":3},{"c1":[1,2,3]}]`，对应的 mime_type 为 application/json，编码为默认的 utf-8。

### 使用数字下标获取数据
使用数字下标可以获取输入 payload 中的元素。如下所示，Dataway 表达式为：
```python
def dw_process(msg):
    return msg.payload[1]
```
则表达式的输出为 dict 类型的结果：`{"b1":1,"b2":2,"b3":3}`
### 使用'^'符号获取元数据
要获取 Entity 类型的 payload 元数据，可以使用'^'符号。如下所示，DataWay 表达式为：
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
### 使用普通字符获取元素
我们假设输入消息的 payload 值仍为 Entity 类型，其代表的负载数据 blob 反序列化后变成`{"a1":1,"b1":1,"b2":2,"b3":3,"c1":[1,2,3]}`，对应的 mime_type 仍为 application/json，编码为默认的 utf-8。如下所示，DataWay 表达式为：
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
>!在 DataWay 表达式中，字符串可以用`''`或`""`的方式表示，其作用一致。

## 类型对象构造
### Entity.from_value 函数
用于将值类型 data 封装为 Entity 类型，并返回。如下所示：
```python
Entity.from_value(data, mime_type=None, encoding="utf-8")
```
在 from_value 函数内部，会先根据给定的 mime_type 和 encoding 尝试对 data 进行序列化得到 bytes 类型的数据，然后再封装为 Entity 类型进行返回。
- mime_type 参数必传，且目前支持的 mime_type 参数有 text/plain、application/json、application/x-www-form-urlencoded、application/csv、 application/xml 和 multipart/form-data 六种。
- encoding 参数则支持任意合法的编码类型，若为空则默认为 utf-8 编码。

### Entity.from_bytes 函数
用于将 str 或者 bytes 类型数据封装为 Entity 类型，并返回。如下所示：
```python
Entity.from_bytes(data, mime_type=None, encoding="utf-8")
```
from_bytes 函数中的 mime_type 和 encoding 参数校验规则与 from_value 函数相似，不同的是不会对 mime_type 的参数值进行限制，可以为任意的 mime_type 类型。
- 如果传递给 from_bytes 函数的 data 参数类型为 bytes 类型，该函数会直接返回一个以 data、mime_type、encoding 作为参数构造的 Entity 对象。
- 如果传递的 data 是 str 数据，则会尝试根据 encoding 参数将其编码为 bytes 类型，并构造成 Entity 对象。

## 使用对象限制
Entity 对象在本质上是一个对二进制数据的封装对象，为方便使用，也提供例如：Entity.get(attr, default=None) 等对象方法以及基于下标的选择器语法（详见[ Entity 选择器](#selectors)） 等快速访问功能。
在使用这些功能时，需要注意的是，有些特殊操作下系统会尝试先对 Entity 中的二进制数据进行解析，如果解析失败则会导致运行时错误。这些特殊操作包括：
- 用 Entity['^value'] 来获取解析后的结构化结果；
- 用 Entity.get('attrName', default=None) 或 Entity['attrName'] 来获取结构化结果中的某个属性值；
- 用 Entity['*key'] 来执行选择器语法（只在 mime_type 为 application/x-www-form-urlencoded 的 Entity 中使用）。

在不符合条件的 Entity 对象上执行上述特殊操作，将会导致运行时错误。
