## 简介
[Neo4j](https://neo4j.com/) 数据库是开源的高性能 NOSQL 图形数据库，图数据库用来解决现有关系数据库的局限性，图模型明确地列出数据节点之间的依赖关系，可以简单快速地检索难以在关系系统中建模的复杂层次结构。Neo4j 数据库适合处理复杂关系，应用在欺诈检测、推荐系统、社交网络图、身份和访问管理等领域。

Neo4j 设计 CQL（Cypher Query Language）查询语言，Neo4j 通过 CQL 可以进行 Neo4j 数据库的增删改查等相关操作，[CQL](https://neo4j.com/docs/cypher-manual/current/introduction/quering-updating-administering/) 的语法类似于 SQL，简单易读。

iPaaS Neo4j 连接器可连接第三方 Neo4j 数据库系统并执行节点的增删改查和 CQL 操作。用户通过连接器配置来配置数据库的连接参数，配置成功后便可执行对应的数据库操作。

## 连接器配置
### 配置参数

| 参数         | 数据类型 | 描述                                           | **是否必填** | **默认值** |
| ------------ | -------- | ---------------------------------------------- | ------------ | ---------- |
| 连接URL      | string   | 用于连接 Neo4j 数据库的 URL                       | 是           |    -        |
| 用户名       | string   | 用于连接验证的用户名                           | 否           |      -      |
| 密码         | string   | 用于连接验证的用户密码                         | 否           |      -      |
| 数据库       | string   | 连接的数据库名称                               | 否           |     -       |
| 连接超时时间 | int      | 连接超时时间（单位秒），最长超时时间为30秒 | 否           | 5          |

### 配置界面
![image-20210520153224585](https://main.qcloudimg.com/raw/b739c11e72991bd4911b6d9eefe5ff85.png)

## 操作说明
Neo4j 连接器目前支持创建节点、查询节点、删除节点、更新节点、执行 CQL 语句等操作。
<dx-tabs>
::: 创建节点
#### 参数配置

| 参数         | 数据类型 | 描述                                           | **是否必填** | **默认值** |
| ------------ | -------- | ---------------------------------------------- | ------------ | ---------- |
| 节点标签名称 | string   | 待创建节点的标签名称                           | 是           |       -     |
| 节点属性     | dict     | 待创建节点的属性，key 为属性名称，value 为属性值 | 否           |        -    |

![image-20210520171116857](https://main.qcloudimg.com/raw/05639b0884b6c145029027fdb30ed2fe.png)

####  输出
查询操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 int 类型，返回创建成功的节点数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Neo4j 连接器组件，选择创建节点操作。
![image-20210520171439537](https://main.qcloudimg.com/raw/8137c4e098a4206bbe571f80898166e1.png)
2. 新建连接器配置，填写配置参数，单击**测试连接**，测试连接器配置是否正确。
![image-20210520171520885](https://main.qcloudimg.com/raw/01592bb58a39687226fed9c6bd5944c3/neo4j4.png)
3. 在通用配置中，填写节点标签名称和节点属性信息。例如：标签名称填写为 person、节点属性 item_1 的 key 为 name、value 为 'xiaoming'、item_2 的 key 为 age、value 为18。
![image-20210520171945127](https://main.qcloudimg.com/raw/9dbe1c7a719f40acb773e71f0075bb45/neo4.png)
 - 节点属性：
![image-20210520172021477](https://main.qcloudimg.com/raw/2785ce892988d8a3287f2a102da43778/neo5.png)
![image-20210520172041721](https://main.qcloudimg.com/raw/1eee02092692d6e2a900d5dc20ccac30/neo6.png)
4. 创建成功后，message payload 返回创建节点的数量。
![image-20210323113311938](https://main.qcloudimg.com/raw/d53859516c51a156b44d4287f721a88a.png)
5. 若执行过程中出现错误，message error中会包含错误信息。
![image-20210322192839811](https://main.qcloudimg.com/raw/6deb24f5373066f0d10bcab0cc418cff.png)
:::
::: 查询节点
#### 参数配置

| 参数         | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ------------ | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 节点标签名称 | string   | 待查询的节点标签名称                                         | 是           |    -        |
| 节点属性     | dict     | 节点属性，根据节点属性作为查询过滤条件，不填则返回标签下所有节点 | 否           |   -         |

![image-20210520184724126](https://main.qcloudimg.com/raw/3ccc57371a547bd39be14d6c0a59815b/neo7.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，表示节点的属性信息；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：查询操作执行成功后，查询返回两个节点的属性信息，message payload 值如下：
```json
[
    {
        "age": 18,
        "name": "xiaohua"
    },
    {
        "age": 18,
        "name": "xiaoming"
    }
]
```

#### 案例
1. 添加 Neo4j 连接器组件，选择查询节点操作。
![image-20210521095822998](https://main.qcloudimg.com/raw/fd4be8ca36cf8dc2462a606e8d9f5289/neo10.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入节点标签名称和节点属性。例如：标签名称填写为 person、节点属性 item_1 的 key 值为 age、value 值为18，即可筛选出 age 属性值为18的节点。
 ![image-20210521100202113](https://main.qcloudimg.com/raw/5283e71c8185e65101eb3a382621be01/neo11.png)
4. 查询成功后，message payload 中包含执行结果，返回 age 属性为18的两个节点信息。
![image-20210521100419381](https://main.qcloudimg.com/raw/ed84547eddde4078a51a3594b72fe6f4/neo12.png)
:::
::: 更新节点
#### 参数配置

| 参数             | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ---------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 节点标签名称     | string   | 待删除的节点标签名称                                         | 是           |     -       |
| 节点属性         | dict     | 节点属性，根据节点属性作为删除条件，不填则更新标签下所有节点 | 否           |     -       |
| 更新后的节点属性 | dict     | 更新后的节点属性                                             | 是           |    -        |

![image-20210521101343734](https://main.qcloudimg.com/raw/bd9255a1e3c23384e681853a2aa00f11/neo15.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 Bool 类型，更新成功为 true，更新失败为 false；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Neo4j 连接器组件，选择更新节点操作。
  ![image-20210521101205675](https://main.qcloudimg.com/raw/8a333334f032c1f2772a0467830f4567/neo14.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入所需参数。例如：节点标签填写为 person、节点属性 item_1 的 key 值为 age、value 值为18，更新后的节点属性采用 Dataway 表达式输入。
```python
def dw_process(msg):
    return {
        'name': 'abc',
        'age': 30
    }
```
4. 执行成功后，message payload 中包含执行结果，true 表示更新成功。
![image-20210521105858364](https://main.qcloudimg.com/raw/cfcd5ce3353664f0f61d82844d474790/neo20.png)
 - 再执行查询节点操作，可以看到两个节点已经完成更新。
![image-20210521105957969](https://main.qcloudimg.com/raw/4ff130e3574b0a5b2832138b446486a0/neo21.png)
:::
::: 删除节点
#### 参数配置

| 参数             | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ---------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 节点标签名称     | string   | 待删除的节点标签名称                                         | 是           |     -       |
| 是否删除节点关系 | bool     | 是否删除节点间的关系信息                                     | 否           | true       |
| 节点属性         | dict     | 节点属性，根据节点属性作为删除条件，不填则删除标签下所有节点 | 否           |        -    |

![image-20210521104644913](https://main.qcloudimg.com/raw/a989c83a9ad8721e59e87a0dd5b29d00/neo17.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 int 类型，代表删除的节点数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Neo4j 连接器组件，选择删除节点操作。
   ![image-20210521100615438](https://main.qcloudimg.com/raw/99f7c29fd1d5c733246a3ff6e3369bb7/neo13.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：节点标签填写为 person、节点属性采用 Dataway 表达式输入，输入如下：
```python
def dw_process(msg):
    return {
        'age': 30
    }
```
4. 删除成功后，message payload 中包含成功删除的节点数量。
![image-20210521110242528](https://main.qcloudimg.com/raw/b12aeeb32ddca750a62b46e36b0f36ed/neo22.png)

:::
::: 执行CQL语句
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| CQL语句  | string   | 待执行的 CQL 语句，遵循 Cypher Query Language 标准的语句，支持原生 CQL 及参数化输入。参数化使用($+参数名称)输入 |      -        |        -    |
| 输入参数 | string   | CQL 语句的输入参数，key 为参数名称，参数名称需要和 input 参数名称一致，value 为参数值 | 是           |        -    |

![image-20210521104754750](https://main.qcloudimg.com/raw/ff5908cf83a12170d8eaa0720903db8a/neo18.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 dict 类型，包含4个字段：selectResult、createCount、deleteCount、containsUpdates。<br><li>selectResult 字段代表查询结果，对应的值为 list 类型，list 成员为 dict 类型，为节点的属性信息<br><li> createCount 代表创建的节点数量，对应的值为 int 类型<br><li>deleteCount 代表删除的节点数量，对应的值为 int 类型<br><li>containsUpdates 代表是否执行更新，对应的值为 bool 类型；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Neo4j 连接器组件，选择执行 CQL 操作。
![image-20210521104542626](https://main.qcloudimg.com/raw/5c93f8bbc2c1acbdb1ff1cd6e8b3499c/neo16.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入相关信息。例如：”CQL 语句“为`MATCH(n:person {age:$age}) RETURN n`，CQL 语句中包含 age 参数变量，输入参数采用 Dataway 表达式输入，如下：
```python
def dw_process(msg):
    return {
        'age': 18
    }
```
 - 界面如图：
![image-20210521111606338](https://main.qcloudimg.com/raw/3c288803e615c50ef78233b0ea1a7035/neo23.png)
4. 执行成功后，message payload 中包含执行结果，由于执行的是查询命令，“selectResult”字段包含查询结果。
![image-20210521111640518](https://main.qcloudimg.com/raw/9fcfdbc9590716331fb29309753a479e/neo24.png)

:::
</dx-tabs>
