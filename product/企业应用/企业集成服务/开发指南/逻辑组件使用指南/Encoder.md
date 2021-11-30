## 简介
RecordSet Encoder 用于将普通的数据类型组装为 RecordSet 数据类型，用于后续的批量数据处理。在 RecordSet Encoder 中可以配置子流，返回一个普通类型的数据列表。同时在组件配置中指定需要构造的 RecordSet 数据的 schema 和分片数，系统会将根据这些配置信息对子流返回的数据列表进行解析，从而得到一个支持多分区的 RecordSet 数据对象。

## 操作配置
### 配置界面
RecordSet Encoder 组件的配置界面如下：
![](https://main.qcloudimg.com/raw/fb2b884ecf7eb0526d405f2888c0aa0f.png)

### 配置参数

**基本配置**  

| 参数       | 数据类型   | 描述                                                         | 是否必填 | 默认值 |
| :--------- | :--------- | :----------------------------------------------------------- | :------- | ------ |
| 输出 schema | 图形化配置 | 需要输出的 RecordSet 数据的字段结构信息，需要指定字段名（必填）、字段类型（必填）以及显示名称（非必填）| 是       | 无     |

**高级配置**  

| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| :--------- | :------- | :----------------------------------------------------------- | :------- | ------ |
| 输出持久化 | bool     | 用于指定是否需要对输出的 RecordSet 进行持久化存储，若选择 true，则会在该 RecordSet 第一次计算后缓存计算结果，后续对该数据的读取将无需重复计算 | 否       | false  |
| 分区数     | int      | 用于指定输出的 RecordSet 的分区数，在实际获取 RecordSet 数据时，有多少个分区则会执行多少次子流，从而为每个分区分别获取数据 | 否       | 1      |

### 输入 message
RecordSet Encoder 是嵌套组件，可以配置子流。子流的输入 message 内容规定如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当前分区的索引，例如：指定3个分区，则分别会以0、1、2作为 payload 来调用子流 |
| error       | 空                                                           |
| attribute   | 空                                                           |
| variable    | 继承主流中的 variable 数据，同时新增两个变量，分别为：计数器和根信息。若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 访问。在子流中操作 Variables 将不会影响主流中的数据 |

### 输出 message
RecordSet Encoder 组件会根据配置的输出 schema，将子流输出的 payload 转换成一个 RecordSet，然后设置为组件输出 message 的 payload，同时 message 中保留了前一个组件的 Variables 和 attributes 信息。


组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 构造得到的 RecordSet 对象                                      |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承前一个组件输出的 attribute 信息                            |
| variable    | 继承前一个组件输出的 variables 信息                            |


## 案例
使用 RecordSet Encoder 组件构造一个具有三个分区的 RecordSet，操作步骤如下：
1. 添加 RecordSet Encoder 组件，设置输出 schema：
![enter image description here](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Encoder/e1bab0a1028b45d4813f3f74b1f4876f.png)
2. 配置子流，将子流的 payload 设置为需要构造的数据内容：
 - 子流配置：
   ![enter image description here](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Encoder/79f82b7a1ac071c17a451a47344d7344.png)
 - set-payload 的配置如下：
```python3
def dw_process(msg):
    return [{
        "Name": "fuz",
        "Gender": '男',
        "Age": 20,
        "BirthDay": datetime.datetime.now().date(),
    }, {
        "Name": "yat",
        "Gender": "女",
        "Age": 20,
        "BirthDay": datetime.datetime.now().date(),
    }]
```
3. 在下游通过 ForEach 或者 Parallel ForEach 组件遍历输出的 RecordSet，并查看结果。
   ![enter image description here](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Encoder/7235156e6a9c9e885f966fe4214eed58.png)
4. 通过 debug 模式运行并查看，可以得到如下结果：
   ![enter image description here](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Encoder/b2a9ddd93e3d1430379de9f730ae38e6.png)
