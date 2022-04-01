Dataway 使用 Entity 类型可支持多种不同的数据类型，例如：json、csv、xml 等。在 Entity.from_value 或 Entity.from_bytes 函数中指定对应的 mime_type 和 encoding 值，可以得到一个封装不同数据类型的 Entity 对象。通过使用 Entity 选择器，可以读取解析后的结构数据。

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
DataWay 的运行环境依赖于组件的运行，假定在 Set-Payload 组件前已经有一个 Transform 组件，对流的运行消息 msg 的 payload 进行了设置。msg.payload 为一个 dict 类型对象，内部结构如下：

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

### JSON 结构使用
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

>!关于 DataWay 中使用的第三方模块函数，可以参考 [函数参考](https://cloud.tencent.com/document/product/1270/55568)。

## <span id='urlencode-format'></span> HTTP 表单格式
HTTP 表单格式的数据代表 mimeType 为 application/x-www-form-urlencoded 的 Entity 中数据序列化后得到的类型。
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 dict 类型数据结构。
- 使用 Entity.from_value 构造方法，支持 dict/MultiMap 两种输入类型，并最终解析成一个 MultiMap 类型数据结构。

**对 HTTP 表单格式数据，由于其内部实现为 MultiMap 数据类型，因此除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector | 含义                              |
| -------- | --------------------------------- |
| ['*key'] | 返回字典下面的 key 对应的所有元素 |
| ['key']  | 返回字典下面的 key 对应的第一个元素 |

以下将通过示例来说明如何使用 HTTP 表单格式数据：

### 构造并使用 HTTP 表单格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 HTTP 表单格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
HTTP 表单格式的输入`k1=123&k2=helloworld&k3=2&k3=abc`将被当做 Dataway 输入参数 msg 的 payload 属性中，实际的输入类型将会转换为 MultiMap 数据类型。

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
Dataway 的脚本输出为一个 dict , 结果如下：

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
以下将通过示例来说明如何使用文本格式数据：
### 构造文本格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个文本格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
文本格式的输入"This is a text plain message"将被当做 Dataway 输入参数 msg 的 payload 属性中，实际的输入类型将会转换为文本数据类型。
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
- 使用 Entity.from_value 构造方法，仅支持 dict 输入类型，并最终解析成一个 dict 数据结构。同时，输入的 dict 仅包含一个默认的 key "root"，value 则为内置的 MultiMap，在 MultiMap 中可以自由操作 msg 属性。

以下将通过两个示例来说明如何使用 XML 格式数据：
**对 XML 格式数据，除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

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

```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

#### DataWay 脚本
以下 DataWay 脚本使用 from_value 函数将 dict 类型转换成 Entity 对象，并返回。

```python
def dw_process(msg):
    a = math.floor(1.4)
    return Entity.from_value({
        'root': {
            'k1': msg.vars['abc'],
            'k2': json.dumps('哈哈', ensure_ascii=False),
            'k3': a + 1,
            '@id': "hello",
            '#text': "<a>dwad</a>",
            'k4': ['abc', 'def', None],
        }
    }, mime_type = 'application/xml')
```

#### 输出
DataWay 脚本的输出结果为一个 Entity 类型对象，其中 blob 为符合 XML 语法的二进制数据，如下所示：

```python
{
    "mime_type": "application/xml",
    "encoding": "utf-8",
    "blob": b'<?xml version="1.0" encoding="utf-8"?>
    <root id="hello"><k1>123</k1><k2>"哈哈"</k2><k3>2</k3><k4>abc</k4><k4>def</k4><k4></k4><a>dwad</a></root>'
}
```

### 使用 XML 特定选择器
本示例将示范如何在 XML 格式数据中使用特定语法的选择器。
#### 输入
DataWay 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个key为 "abc" , value 为 "123" 的键值对。

```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

#### DataWay 脚本
以下 DataWay 脚本使用 from_value 函数将 dict 类型转换成 Entity 对象，然后用选择器获取 Entity 的数据。

```python
def dw_process(msg):
    a = math.floor(1.4)
    entity =  Entity.from_value({
        'root': {
            'k1': msg.vars['abc'],
            'k2': json.dumps('哈哈', ensure_ascii=False),
            'k3': a + 1,
            '@id': "hello",
            '#text': "<a>dwad</a>",
            'k4': ['abc', 'def', None],
        }
    }, mime_type = 'application/xml')
    return {
        'k1': entity['root']['#text'] + entity['root']['@id'],
        'k2': entity['root']['k1'],
        'k3': entity['root']['*k4']['^value'],
        'k4': entity['root']['k4'],
        'k5': entity['^mime_type']
    }
```

#### 输出
DataWay 脚本的输出结果为一个 dict 类型数据，如下所示：

```python
{
  "k1": "<a>dwad</a>hello",
  "k2": "123",
  "k3": ['abc', 'def', None],
  "k4": "abc",
  "k5": "application/xml"
}
```

>!在 XML 格式数据中，root 节点为默认节点，其属性使用`@id=123`的方式指定，文本使用`#text`的方式指定。value为一个 MultiMap 类型，其中 key 为每一个子节点名称，value 为不同的值。
>
## <span id='csv-format'></span> CSV 格式
CSV 格式的数据代表 mimeType 为 application/csv 的 Entity 中数据序列化后得到的类型。
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 list 类型数据结构，其中每一项元素均为一个 dict。
- 使用 Entity.from_value 构造方法，支持 list 输入类型，并最终解析成一个 list 类型数据结构，其中每一项元素均为一个 dict。

以下将通过示例来说明如何使用 CSV 格式数据：
### 构造 CSV 格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 CSV 格式的 Entity，并使用 Entity 选择器语法获取 Entity 的属性和数据。
#### 输入
DataWay 输入参数 msg 的 payload 值为常量1，同时 msg.vars 中包含一个key为 "abc" , value 为 "123" 的键值对。

```python
{
    "payload": 1,
    "vars": {
        "abc": "123"
    }
}
```

#### DataWay 脚本
以下 DataWay 脚本使用 from_value 函数将 dict 类型转换成 Entity 对象，并使用选择器语法获取 Entity 对象的属性值。

```python
def dw_process(msg):
    entity = Entity.from_value([
        {'k1':'abcd','k2':123.0,'k3':True},
        {'k1':'defs','k2':'dwdw,2e','k3':10},
    ], mime_type = 'application/csv')
    return {
        'var1': entity['^blob'],
        'var2': entity['^mime_type'],
        'var3': entity['^encoding'],
        'var4': entity[0]['k2'] + entity[1]['k3'],
        'var5': entity[1]['k2']
    }
```

#### 输出
DataWay 脚本的输出结果为一个 dict 类型数据，如下所示：

```python
{
    "var1": b'k1,k2,k3\r\nabcd,123.0,True\r\ndefs,"dwdw,2e",10\r\n',
    "var2": "application/csv",
    "var3": "utf-8",
    "var4": "133",
    "var5": "dwdw,2e"
}
```

>!对于 CSV 数据格式，接收的 list 每一项元素均为 dict 类型。每一项元素中的 keys 需保持相同，作为 CSV 文本的标题行；每一项元素中的 values 则代表该行的数据值，用逗号分隔。
## <span id='formdata-format'></span> HTTP Form-Data 表单
HTTP Form-Data表单格式的数据代表 mime-type 为 multipart/form-data 的 Entity 中数据序列化后得到的类型。
### 浏览器中的 multipart/form-data
在浏览器发送 Content-Type 为 multipart/form-data 的请求时，实际传输的 byte 数组转换成字符串如下所示：
- 每一项参数由一个 boundary 开头，标识着这一项的开始，例如：--34b21 。
>! -- 为固定开头，34b21 为浏览器随机的一个不超过70位的字符串。
- boundary 开头下是 Content-Disposition 和 Content-Type 的固定 headers，其中：
 - Content-Disposition 包含 name 和 filename 两项，name 为参数名，filename 为文件名。
 - Content-Type 即为输入内容的 Content-Type。
 - 如果 filename 为"*.txt"或者为空，则 Content-Type 默认为 text/plain；如果 filename 为其他，则 Content-Type 会根据后缀名自动判断。同时，也支持其他的扩展 headers。
- 再往下是实际的内容，如果 Content-Type 为 text/plain ，则为普通字符串，例如："Book"；如果 Content-Type 为 application/json ，则为一个 json 类型的字符串，如下方的 file1 对应的 json 结构。
- 最后用--34b21--来标识该段请求的结束。

```
--34b21
Content-Disposition: form-data; name="text"
Content-Type: text/plain

Book
--34b21
Content-Disposition: form-data; name="file1"; filename="a.json"
Content-Type: application/json

{
"title": "Java 8 in Action",
"author": "Mario Fusco",
"year": 2014
}
--34b21
Content-Disposition: form-data; name="file2"; filename="a.html"
Content-Type: text/html

<!DOCTYPE html>
<title>
Available for download!
</title>
--34b21--
```

### Form-Data 的构造和使用
- 使用 Entity.from_bytes 方法，则 Dataway 对输入的 str/bytes 类型最终解析成一个 FormDataParts 数据结构。
- 使用 Entity.from_value 构造方法，支持 Entity、Formdata、list/dict 输入类型，并最终解析成一个 FormDataParts 数据结构。
>! 
>- 如果为 Entity 类型，则会首先判断 Entity['^mime_type'] 是否为 multipart/form-data。如果为是，直接返回该 Entity；否则将报错。
 - 如果为 FormdataParts 类型（即上文提到的 map+ 数组结构），则直接赋值给 Entity。
 - 如果为 list/tuple 类型，则需要保证为以下数据结构：每一项的第一个元素为参数名。第二个元素如果为 list/tuple，则第二个元素的第一项为文件名，第二项为实际的内容，第三项为 Content-Type ，第四项为一个 dict，代表 extra_headers；如果第二个元素类型为 str，则文件名为空，实际内容即为字符串内容，Content-Type 默认为 text/plain。

**对 HTTP Form-Data 格式数据，除了通用的 Entity 选择器语法，还支持特殊的选择器语法。**

| Selector                                            | 含义                                            |
| --------------------------------------------------- | ----------------------------------------------- |
| ['parts']                                           | 返回自定义类型 FormDataParts 类型                 |
| <span>['parts']</span>[0]                           | 返回 FormData 的第0项                             |
| <span>['parts']</span><span>['a']</span>['content'] | 返回 FormDataParts 中 key 为'a'的 value 中的 content 值 |
| ['boundary']                                        | 返回 FormDataParts 的分隔符                       |

### 应用示例
以下将通过两个示例来说明如何使用 HTTP FORM-DATA 表单格式数据。
#### 示例一：构造 HTTP Form-Data 格式的 Entity
本示例将展示如何使用 Entity 的构造函数构造一个 HTTP Form-Data 数据格式的 Entity。
**输入**
Dataway 输入参数 msg 的 vars 中包含一个key为 "abc" , value 为 "123" 的键值对。

```python
{
    "vars": {
        "abc": "123"
    }
}
```

**Dataway 脚本**
以下 Dataway 脚本使用 from_value 函数将 dict 类型转换成 Entity 对象，并返回。

```python
def dw_process(msg):
    a = math.floor(1.4)
    c = Entity.from_value({
        'k1': msg.vars['abc'],
        'k2': json.dumps('哈哈', ensure_ascii=False),
        'k3': a + 1,
    }, mime_type = 'application/json')
    return Entity.from_value(
        [
        ('a', ('test.json', '{"a": a}', 'application/json', {'Test111': 1})),
        ('b', '333'),
        ('c', ('c.json', c, c['^mime_type']))
        ],
        mime_type='multipart/form-data; boundary=123333333'
    )
```

**输出**
Dataway 脚本的输出结果为一个 Entity 类型对象，其中blob 为符合 multipart/form-data 结构的二进制数据，如下所示。

```python
{
    "mime_type": "multipart/form-data; boundary=12345",
    "encoding": "utf-8",
    "blob": b'''--123333333
Content-Disposition: form-data; name="a"; filename="test.json"
Content-Type: application/json
Test111: 1

{"a": a}
--123333333
Content-Disposition: form-data; name="b"

333
--123333333
Content-Disposition: form-data; name="c"; filename="c.json"
Content-Type: application/json

{"k1":"123","k2":"\"哈哈\"","k3":2}
--123333333--
'''
}
```

#### 示例二：使用 FORM-DATA 选择器
本示例将示范如何在 FORM-DATA 格式数据中使用特定语法的选择器。
**输入**
Dataway 输入参数 msg 的 payload 为一个 Entity 类型，其 mime_type 为 multipart/form-data，通过 Entity.from_value 函数创建。

```python
def dw_process(msg):
    return Entity.from_value(
        [('a', ('test', '1233', 'application/json', {'test111':1})),
        ('b', (None, '2333', 'text/plain')),],
        mime_type="multipart/form-data; boundary=123"
    )
```

**Dataway 脚本**
以下 Dataway 脚本将使用 FORM-DATA 选择器对 msg.payload 进行处理，并返回一个 dict。

```python
def dw_process(msg):
    return {
        'k1': str(type(msg.payload)),
        'k2': msg.payload['^mime_type'],
        'k3': msg.payload['^encoding'],
        'k4': msg.payload['^raw'],
        'k5': msg.payload['boundary'],
        'k6': msg.payload['parts']['a']['headers']['Content-Disposition']['name']
            + '-' + msg.payload['parts'][1]['headers']['Content-Type']
    }
```

**输出**
Dataway 脚本的输出结果为一个 dict 类型数据，结果如下。

```pythonn
{
    'k1': 'Entity',
    'k2': 'multipart/form-data;boundary=123',
    'k3': 'utf-8',
    'k4': b'''--123
Content-Disposition: form-data; name="a"; filename="test"
Content-Type: application/json
test111: 1

1233
--123
Content-Disposition: form-data; name="b"
Content-Type: text/plain

2333
--123--
''',
    'k5': '123',
    'k6': 'a-text/plain'
}
```

## <span id='other-format'></span> 其他类型
对其他类型的 mime_type，Dataway 不支持直接用 Entity.from_value 函数构造，但支持从上游读取数据，以及使用 Entity.from_bytes 函数构造一个封装的 Entity。
下面将通过一个示例来说明，假设输入数据为一个二进制 byte 流，我们通过 Set Payload 组件中使用 Dataway 表达式将该二进制 byte 流封装到 msg.payload 中，然后在下游可以使用 [Entity 选择器](https://cloud.tencent.com/document/product/1270/55573) 语法进行操作。
**Dataway 表达式**

```pythonn
def dw_process(msg): 
    b = msg.payload
    return Entity.from_bytes(b, mime_type='application/octet-stream')
```

