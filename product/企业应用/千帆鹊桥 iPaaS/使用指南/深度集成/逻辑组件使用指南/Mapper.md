

## 简介
RecordSet Mapper 组件用于操作 RecordSet，可以对输入的 RecordSet 进行转换，并生成一个新的 RecordSet。在转换的过程中，支持从其他数据源查找数据，并参与运算。

## 操作配置
### 参数配置
RecordSet Mapper 的配置界面包含三部分：
- 输入信息：会自动展示输入数据的字段和类型信息。
- 输出信息：需要用户自行配置输出的字段和类型信息。
- 逻辑映射：配置输入和输出字段间的映射关系。
![image-mapper-1](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-1.png)


#### 配置输入信息
默认会自动识别 `msg.payload` 包含的字段以及字段类型进行展示。如果识别的结果不准确，用户也可以主动修改。
![image-mapper-2](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-2.png)

#### 配置输出信息
需要用户自行配置输出数据中要包含的字段和类型。支持用户直接对输出字段进行赋值，支持赋值常量或者表达式：
- 常量：可以设置任意常量值。
- 表达式：在表达式里面可以用 msg.payload 处理所有输入的字段。
![image-mapper-3](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-3.png)
![image-mapper-4](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-4.png)

#### 配置逻辑映射
用户需要指定输入信息和输出信息间的映射关系，支持两种方式：
- 直接赋值：通过连线直接连接输入字段和输出字段，输入和输出字段的类型需要一致。
- 使用映射逻辑节点：用户需要新增映射逻辑节点。对于每个映射逻辑节点，一般可以配置多个输入和输出，类似于一个函数的入参和出参。用户可以将 Mapper 组件输入信息中的字段连线到映射逻辑节点的输入，然后经过映射逻辑节点内部处理后，将映射逻辑节点的输出连线到 Mapper 组件输出信息中的字段进行赋值。映射逻辑配置可参考下文 [映射逻辑配置说明](#introduction)。
![image-mapper-5](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-5.png)
![image-mapper-7](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-7.png)


### 输入 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上一个组件输出 message 中的 payload                         |
| error       | 空                                                           |
| attribute   | 空                                                           |
| variable    | 继承上一个组件输出 message 中的 variable 数据，在 RecordSet Filter 组件中可以操作 Variables，且不会影响输出 message 中的数据 |


### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 转换后的 RecordSet，其包含的字段为用户配置的输出字段          |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 类型为 dict，继承上一个组件的 attribute                        |
| variable    | 继承上一个组件的 variable                                     |


## [映射逻辑配置说明](id:introduction)
映射逻辑节点内部可以使用多种查找功能（从状态存储中查找、通过连接器查找、从其他流中查找）以及表达式处理功能。
<dx-tabs>
::: 从状态存储中查找
可以配置从 mapState、valueState、tableState 中查找数据，然后在映射节点内部进行处理并输出。下文以 mapState 为例进行说明。
![image-mapper-8](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-8.png)
![image-mapper-9](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-9.png)
:::
::: 通过连接器查找
支持通过连接器来查找第三方数据，然后在映射节点内部进行处理并输出。
![image-mapper-10](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-10.png)
![image-mapper-11](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-11.png)
:::
::: 从其他流中查找
支持从其他流来获取数据，然后在映射节点内部进行处理并输出。
![image-mapper-12](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-12.png)
![image-mapper-13](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-13.png)
![image-mapper-14](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-14.png)
:::
::: 通过表达式配置
支持通过表达式来转换数据，即通过 Dataway 表达式来处理输入，然后输出。
![image-mapper-15](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-15.png)
![image-mapper-16](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-16.png)
:::
</dx-tabs>

如果在节点内部使用查找功能，用户还可以配置三种查找策略，合理使用查找策略可以提高执行效率。  

| 查找策略       | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| 每次都重新查找 | 对于输入的数据中的每一行，都重新执行一次新的查找。如果查找的结果随着输入的每行数据而变化，建议采用该策略。 |
| 只查找一次     | 无论输入的数据有多少行，都只执行一次查找，后续查找都继续使用第一次查找的结果。如果查找的结果不随着输入数据变化，建议采用该策略。 |
| 周期性查找     | 可以配置一个查找周期，仅当两次查找的时间间隔超过配置的查找周期时，才会重新执行查找，否则，继续使用上一次查找的结果。如果查找的结果是周期性更新的，建议采用该策略。 |


## 案例
针对一个学生表进行转换，示例图如下：
![image-mapper-17](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-17.png)
1. 用 RecordSet Encoder 组件创建一个学生表，包含 `name, age, address, socre, adult` 字段，然后在 RecordSet Encoder 组件里面添加 SetPayload 组件，用表达式在学生表中添加数据。
   ![image-mapper-18](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-filter-9.png)
   ![image-mapper-19](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-filter-10.png)
2. 用 Mapper 组件进行转换，生成一个新的学生表，包含 `code, name, company, homeAddress, isAdult` 5个字段，Mapper 组件的整体配置视图如下：
![image-mapper-18](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-18.png)
 1. 用表达式转换节点来处理输入信息中的 `name, age, score`，然后赋值给输出信息中的 `code, name`，配置信息如下：
  ![image-mapper-19](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-19.png)
 2. 输出信息中的 `company` 直接设置为常量 gameloft。
 3. 输出信息中的 `homeAddress` 直接设置为表达式 `return "my home: "+msg.payload["address"]`。
 4. 输入信息中的 `adult` 直连输出信息中的 `isAdult`。
3. 在调试模式下进行单元测试，并查看结果。
![image-mapper-20](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Mapper/image-mapper-20.png)
```plaintext
`[
        [
            "张三1099.5",
            "张三",
            "gameloft",
            "my home:陕西省西安市",
            false
        ],
        [
            "张三2061.2",
            "张三",
            "gameloft",
            "my home:湖北省荆州市",
            true
        ],
        [
            "张三2571.1",
            "张三",
            "gameloft",
            "my home:湖北省洪湖市",
            true
        ],
        [
            "张三3030.33",
            "张三",
            "gameloft",
            "my home:湖北省赤壁市",
            true
        ],
        [
            "张三4080.33",
            "张三",
            "gameloft",
            "my home:湖北省襄阳市",
            false
        ],
        [
            "张三8040.33",
            "张三",
            "gameloft",
            "my home:湖北省襄阳市",
            true
        ],
        [
            "张三9030.33",
            "张三",
            "gameloft",
            "my home:湖北省襄阳市",
            false
        ],
        [
            "李四7010.33",
            "李四",
            "gameloft",
            "my home:北京省长江市",
            true
        ],
        [
            "王五8070.33",
            "王五",
            "gameloft",
            "my home:广东省深圳市",
            true
        ],
        [
            "王五3073.33",
            "王五",
            "gameloft",
            "my home:湖南省长沙市",
            true
        ],
        [
            "王五4023.33",
            "王五",
            "gameloft",
            "my home:湖南省长沙市",
            false
        ]
    ]`
```
