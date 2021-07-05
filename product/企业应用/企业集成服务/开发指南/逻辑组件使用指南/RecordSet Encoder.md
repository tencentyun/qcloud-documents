## 简介
RecordSet Encoder 用于将普通的数据类型组装为 RecordSet 数据类型，用于后续的批量数据处理。在 RecordSet Encoder 中可以配置子流，返回一个普通类型的数据列表。同时在组件配置中指定需要构造的 RecordSet 数据的 schema 和分片数，系统会将根据这些配置信息对子流返回的数据列表进行解析，从而得到一个支持多分区的 RecordSet 数据对象。

## 操作说明
### 参数配置
RecordSet Encoder 组件的配置界面如下：
![配置界面](https://main.qcloudimg.com/raw/d14d5a30885959254a537d86866cdb63.png)

配置参数说明：

| 参数   | 数据类型                | 描述                                                         | 是否必填 | 默认值      |
| :----- | :---------------------- | :----------------------------------------------------------- | :------- | ----------- |
| 输出 schema | 图形化配置 | 需要输出的 RecordSet 数据的字段结构信息，需要指定字段名（必填）、字段类型（必填）、显示名称（非必填） | 是       | 无          |
| 输出持久化 | bool                  | 用于指定是否需要对输出的 RecordSet 进行持久化存储，若选择 true，则会在该 RecordSet 第一次计算后缓存计算结果，后续对该数据的读取将无需重复计算 | 否       | false     |
| 分区数 | int                  | 用于指定输出的 RecordSet 的分区数，在实际获取 RecordSet 数据时，有多少个分区则会执行多少次子流，从而为每个分区分别获取数据 | 否       | 1 |

### 子流中的输入 message
RecordSet Encoder 是嵌套组件，可以指定子流程，子流程的输入 message 内容规定如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当前分区的索引，例如：指定3个分区，则分别会以0、1、2作为 payload 来调用子流 |
| error       | 空                                                           |
| attribute   | 空                                                           |
| variable    | 继承主流中的 variable 数据，同时新增两个变量，分别为：计数器、根信息，若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 访问。在子流中操作 Variables 将不会影响主流中的数据  |

### 输出
RecordSet Encoder 组件输出的 message 中，保留前一个组件的 Variables 和 attributes 信息，只有 payload 会被设置为输出的 RecordSet 数据对象。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 构造得到的 RecordSet 对象                          |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承前一个组件输出的 attribute 信息                  |
| variable    | 继承前一个组件输出的 variables 信息 |

## 执行原理
### 分区数
RecordSet 中的数据分区是为了充分利用系统的并行计算能力而设计的，在计算时，不同的分区之间可以进行并行计算。在 RecordSet Encoder 中，可以设置分区数为[1,100]范围中的任意整数值，系统将会输出具有指定分区数的 RecordSet 对象。

### 延迟计算
由于 RecordSet 数据类型本身具有的延迟计算的特性，RecordSet Encoder 组件中的子流会在后续流程尝试获取其输出的 RecordSet 的内容时才会真正开始执行，如下集成流：
![enter image description here](https://main.qcloudimg.com/raw/fcf6222f369c2e196af0d853e0385583.png)
在开始执行 Parallel ForEach 节点时，才会开始触发 RecordSet Encoder 中的子流程的执行。

### 持久化缓存
在设计上，RecordSet 中的数据是可重复读取的，其实现的机制是每次都会触发 RecordSet 中计算逻辑，得到新的输出。在 RecordSet 的计算复杂度较高的情况下，重复发起计算流程可能会导致性能低下。持久化缓存主要就是为解决这一问题而设计的。
若开启持久化缓存选项，系统将会在 RecordSet 第一次计算后将结果持久化到对象存储上，后续的读取将会直接从存储中加载而不会触发重复计算，因此能很大程度降低系统性能负载。

## 使用案例
使用 RecordSet Encoder 组件构造一个具有三个分区的 RecordSet。
1. 添加 RecordSet Encoder 组件，设置输出 schema。
![enter image description here](https://main.qcloudimg.com/raw/e1bab0a1028b45d4813f3f74b1f4876f.png)
2. 配置子流，将子流的 payload 设置为需要构造的数据内容，子流配置：
![enter image description here](https://main.qcloudimg.com/raw/79f82b7a1ac071c17a451a47344d7344.png)
 - 其中 set-payload 的配置如下：
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
![enter image description here](https://main.qcloudimg.com/raw/7235156e6a9c9e885f966fe4214eed58.png)
4. 通过 debug 模式运行并查看，可以得到如下结果。
![enter image description here](https://main.qcloudimg.com/raw/b2a9ddd93e3d1430379de9f730ae38e6.png)
