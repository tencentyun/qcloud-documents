Dataway 使用 Entity 类型可支持多种不同的数据类型，例如：json、csv、xml等。在 Entity.from_value 或 Entity.from_bytes 函数中指定对应的 mime_type 和 encoding 值, 可以得到一个封装不同数据类型的 Entity 对象。通过使用 Entity 选择器，可以读取解析后的结构数据。

不同的 mime_type 在 Entity 中有不同的数据格式，对应关系如下：

| mime_type                         | 数据格式                                   |
| --------------------------------- | ------------------------------------------ |
| application/json                  | [JSON 格式](#json-format)                   |
| application/x-www-form-urlencoded | [HTTP 表单格式](#urlencode-format)          |
| text/plain                        | [文本格式](#textplain-format)              |
| application/xml                   | [XML 格式](#xml-format)                     |
| application/csv                   | [CSV 表单格式](#csv-format)                 |
| multipart/form-data               | [HTTP FORM DATA 表单格式](#formdata-format) |
| 其他mime_type                     | [其他格式](#other-format)                  |

不同的数据格式有不同的编码规则、数据结构以及特定的 Entity 选择器语法。本节将对这些不同的数据格式分别进行说明。

## <span id='json-format'></span> JSON 格式
JSON 格式的数据代表 mimeType 为 application/json 的 Entity 中数据序列化后得到的类型。
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 dict 类型。
- 使用 Entity.from_value 构造方法，支持 list/dict/MultiMap 等多种输入类型，并最终解析成一个 dict 类型数据结构。

以下将通过两个示例来说明如何使用 JSON 格式数据。

### 构造 JSON 格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 JSON 格式的 Entity，并使用 Entity 选择器获取 Entity 的属性和数据。
#### 输入
DataWay 的运行环境依赖于组件的运行，假定在 Set-Payload 组件前已经有一个 Transform 组件，对流的运行消息 msg 的 payload 进行了设置。msg.payload 为一个 dict 类型对象，内部结构如下。
```python
{
    "name": "zhangsan",
    "age": 10,
    "male": True,
    "brothers": ["lisi", "zhaowu"]
}
```
#### DataWay 脚本
以下 DataWay 脚本使用 from_value 函数将 dict 数据类型的 msg.payload 转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素，并返回。
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
#### 输出
DataWay 的脚本输出为一个 dict, 其结果如下：
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
### 复杂的 JSON 结构使用
本示例将对复杂的 JSON 结构进行解析，并运行在 Set-Payload 组件中。
#### 输入
Dataway 的运行环境依赖于组件的运行，假定在 Set-Payload 组件前已经有一个 Transform 组件，对流的运行消息 msg 的 payload 进行设置。msg.payload 为一个 Entity 类型对象，内部结构如下：
```python
{
    'mime_type': 'application/json',
    'encoding': 'utf-8',
    'blob': b'{"name":"zhangsan","age":10,"male":true,"brothers":["lisi","zhaowu"]'
}
```
#### DataWay 脚本
以下 DataWay 脚本将对 msg 进行处理，获取对应的元素，最终返回一个 Entity 对象。
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
#### 输出
DataWay 脚本的输出结果为一个 Entity 类型对象，为方便说明，我们将 Entity 中的 blob 进行反序列化后赋值给 value 属性。
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
>!关于 DataWay 中使用的第三方模块函数，可以参考 [函数参考](./函数参考.md)。

## <span id='urlencode-format'></span> HTTP 表单格式
HTTP 表单格式的数据代表 mimeType 为 application/x-www-form-urlencoded 的 Entity 中数据序列化后得到的类型。
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 dict 类型数据结构。
- 使用 Entity.from_value 构造方法，支持 dict/MultiMap 两种输入类型，并最终解析成一个 MultiMap 类型数据结构。
**对 HTTP 表单格式数据，由于其内部实现为 MultiMap 数据类型，因此除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector | 含义                              |
| -------- | --------------------------------- |
| ['*key'] | 返回字典下面的 key 对应的所有元素 |
| ['key']  | 返回字典下面的 key 对应的第一个元素 |

以下将通过示例来说明如何使用 HTTP 表单格式数据。

### 构造并使用 HTTP 表单格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 HTTP 表单格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
HTTP 表单格式的输入 ```k1=123&k2=helloworld&k3=2&k3=abc``` 将被当做 Dataway 输入参数 msg 的 payload 属性中，实际的输入类型将会转换为 MultiMap 数据类型。
```python
{
    "k1": 123,
    "k2": "helloworld",
    "k3": [2, "abc"]
}
```
#### DataWay 脚本 
以下 DataWay 脚本使用 from_value 函数将 dict 数据类型转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素。
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
#### 输出
Dataway 的脚本输出为一个 dict , 结果如下。
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

## <span id='textplain-format'></span> 文本格式
文本格式的数据代表 mimeType 为 text/plain 的 Entity 中数据序列化后得到的类型。无论是 Entity.from_value 还是 Entity.from_bytes 函数，输入均为 str/bytes 类型，输出为 str 数据类型。
以下将通过示例来说明如何使用文本格式数据。
### 构造文本格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个文本格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
文本格式的输入 "This is a text plain message" 将被当做 Dataway 输入参数 msg 的 payload 属性中，实际的输入类型将会转换为文本数据类型。
#### DataWay 脚本
以下 DataWay 脚本使用 from_value 函数将字符串数据转换成 Entity 对象，然后用选择器获取 Entity 的元数据和元素。
```python
def dw_process(msg):
    entity = Entity.from_value(msg.payload, mime_type='text/plain', encoding='utf-8')
    return entity['^value']
```
#### 输出
DataWay 的脚本输出为一个 str 字符串, 结果为"This is a text plain message"。

## <span id='xml-format'></span> XML 格式
XML 格式的数据代表 mimeType 为 application/xml 的 Entity 中数据序列化后得到的类型。
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 dict 数据类型。
- 使用 Entity.from_value 构造方法，仅支持 dict 输入类型，并最终解析成一个 dict 数据结构。同时，输入的 dict 仅包含一个默认的key "root"，value 则为内置的 MultiMap，在 MultiMap 中可以自由操作 msg 属性。

以下将通过两个示例来说明如何使用 XML 格式数据。
对 XML 格式数据，除了通用的 Entity 选择器语法，还支持特殊的选择器语法。

| Selector  | 含义                                 |
| --------- | ------------------------------------ |
| ['*key']  | 返回 xml 某个节点 key 对应的所有元素   |
| ['key']   | 返回 xml 某个节点 key 对应的第一个元素 |
| ['#text'] | 获取 xml 某个节点的文本值              |
| ['@attr'] | 获取 xml 某个节点的 attr 属性值          |

### 构造 XML 格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 XML 数据格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
DataWay 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个 key 为 "abc" , value 为 "123" 的键值对。
