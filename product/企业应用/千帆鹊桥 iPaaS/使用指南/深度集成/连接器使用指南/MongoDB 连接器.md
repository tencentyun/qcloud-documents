

## 简介

MongoDB 是[面向文档](https://zh.wikipedia.org/wiki/面向文檔的數據庫) 的数据库管理系统，MongoDB 将数据存储为一个文档，数据结构由键值对（key/value）组成。MongoDB 文档类似于 JSON 对象，字段值可以包含其他文档，数组及文档数组。
iPaaS MongoDB 连接器可连接第三方 MongoDB 数据库并执行操作。用户通过连接器配置来配置 MongoDB 的连接参数，配置成功后便可执行 MongoDB 操作。

## 连接器配置
iPaaS MongoDB 连接器支持两种连接形式：
- 自定义配置方式，用户根据连接器参数进行参数配置。
- URI字符串方式，用户输入 MongoDB 连接 URI，例如："mongodb://localhost:27017"。

<dx-tabs>
::: 通用标签页-连接配置
| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值  |
| ---------- | -------- | ------------------------------------------------------------ | ------------ | ----------- |
| 连接方式   | enum     | MongoDB 连接模式，支持自定义配置方式和 URI 字符串方式           | 是           |             |
| URI 字符串  | string   | URI 字符串方式参数，MongoDB 数据库连接 URI，例如："mongodb://localhost:27017" | 是           |             |
| 服务器地址 | string   | 自定义配置方式参数，MongoDB 地址，格式为 host:port，以逗号相隔 | 是           |             |
| 数据库     | string   | 自定义配置方式参数，待连接数据库                             | 是           |             |
| 用户名     | string   | 自定义配置方式参数，用于验证的用户名                         | 否           |             |
| 密码       | string   | 自定义配置方式参数，用于验证的密码                           | 否           |             |
| 认证方式   | string   | 自定义配置方式参数，连接 MongoDB 数据的认证方式，支持 SCRAM-SHA-1、SCRAM-SHA-256、PLAIN | 否           | SCRAM-SHA-1 |
| 认证源     | string   | 自定义配置方式参数，MongoDB 数据认证的授权来源                | 否           |             |
| 副本集名称 | string   | 自定义配置方式参数，MongoDB 复制集名称                        | 否           |             |

![image-20210425102005682](https://main.qcloudimg.com/raw/c61a52897b51ec9960d95c3f1afa5fd4/mongo1.png)
:::
:::高级标签页-连接配置
| 参数                     | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------------------ | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 读写超时时间（毫秒）     | int      | 自定义配置方式参数，读写网络超时时间，默认时间单位为毫秒     | 否           | 30000      |
| 连接超时时间（毫秒）     | int      | 自定义配置方式参数，连接 MongoDB 数据库的超时时间，默认时间单位为毫秒 | 否           | 30000      |
| 启用可重试写入           | bool     | 自定义配置方式参数，是否可重试写入，默认为 false，不启用可重试写入 | 否           | false      |
| 连接池最小连接数         | int      | 自定义配置方式参数，连接池最小连接数                         | 否           | 0          |
| 连接池最大连接数         | int      | 自定义配置方式参数，连接池最大连接数                         | 否           | 100        |
| 连接最大空闲时间（毫秒） | int      | 自定义配置方式参数，连接最大空闲时间，默认时间单位为毫秒     | 否           | 0          |

![image-20210425102832288](https://main.qcloudimg.com/raw/12e80cf04f36a896dbb479b8a8888ff5/mongo2.png)
:::
::: 高级标签页-服务路由配置
| 参数                          | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ----------------------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 服务器选择RTT参考阈值（毫秒） | int      | 自定义配置方式参数，MongoDB 数据库服务器选择 RTT 参考阈值，默认时间单位为毫秒 | 否           | 15         |
| 服务器选择超时时间（毫秒）    | int      | 自定义配置方式参数，MongoDB 数据库服务器选择超时时间，默认时间单位为毫秒 | 否           | 30000      |

![image-20210428164058088](https://main.qcloudimg.com/raw/ec5feb9a2030c5917b0c5147bb4e1731/mongo32.png)

:::
::: 高级标签页-读策略
| 参数            | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| --------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| Read Concern    | enum     | 自定义配置方式参数，读关注类型设置，支持 LOCAL、AVAILABLE、MAJORITY、LINEARIZABLE、SNAPSHOT | 否           | MAJORITY   |
| Read Preference | enum     | 自定义配置方式参数，读偏好类型设置，支持 PRIMARY、PRIMARYPREFERRED、SECONDARY、SECONDARYPREFERRED、NEAREST | 否           | PRIMARY    |

![image-20210330144102285](https://main.qcloudimg.com/raw/13a67a4fcc9d4dd041da6479b54b2103/mongo3.png)
:::
::: 高级标签页-写策略
| 参数                   | 数据类型 | 描述                                                         | 是否必填 | 默认值|
| ---------------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| Write Concern          | enum     | 自定义配置方式参数，写操作确认等级，对应 MongoDB 数据库 writeConcern 参数 | 否           | majority   |
| 写确认超时时间（毫秒） | int      | 自定义配置方式参数，写操作超时时间，默认时间单位为毫秒       | 否           | 1000       |

![image-20210428164151321](https://main.qcloudimg.com/raw/22db0cabc03ea5a2205804ece5baff53/mongo4.png)

:::
</dx-tabs>



## 操作说明

MongoDB 连接器的操作分为集合操作、文档操作、索引操作。
![image-20210330144606250](https://main.qcloudimg.com/raw/eaaaddf58befa187d3a171154d3732e1/mongo5.png)

### 集合操作
<dx-tabs>
::: 判断集合存在
#### 参数配置

| 参数     | 数据类型 | 描述     | **是否必填** | **默认值** |
| -------- | -------- | -------- | ------------ | ---------- |
| 集合名称 | string   | 集合名称 | 是           |            |

#### 输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示集合存在，false 表示集合不存在；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
![image-20210330144809170](https://main.qcloudimg.com/raw/af43d4d200ad684360a3bed27ea5f9a7/mongo6.png)
2. 新建连接器配置，填写配置参数，单击**测试连接**，测试连接器配置是否正确。
![image-20210425103813367](https://main.qcloudimg.com/raw/5877b9e034ec92b687893944b8037b90/mongo7.png)
3. 在通用配置中，填入集合名称。
  ![image-20210330145017036](https://main.qcloudimg.com/raw/4bb0b61cbab40d5212b3473a4e6b943d/mongo8.png)
4. 执行成功后，message payload 中包含查询结果。
  ![image-20210330145044079](https://main.qcloudimg.com/raw/f04513852a5dda72b4ce8bba71bfdfdd/mongo9.png)

::: 
::: 创建集合
#### 参数配置

| 参数           | 数据类型 | 描述                     | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------ | ------------ | ---------- |
| 集合名称       | string   | 集合名称                 | 是           |            |
| 集合最大文档数 | int      | 集合最大文档数           | 否           |            |
| 集合最大容量   | int      | 集合最大容量，单位为 Byte | 否           |            |

#### 输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示集合创建成功；若集合已存在或执行失败后，则 payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入待删除的键。
   ![image-20210330145535335](https://main.qcloudimg.com/raw/038e9cc860671894e988e22bb33ec1c4/mongo10.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，则 Message error 保存报错信息。
 - 执行成功：
   ![image-20210330150018584](https://main.qcloudimg.com/raw/0e2cc5c55f9f3e85a96de8522cc43cc3/mongo11.png)
 - 集合已存在，则会报错：
   ![image-20210330150048009](https://main.qcloudimg.com/raw/ecb5dcbd3dea60d06ac7cd726699303c/mongo12.png)
:::
::: 删除集合
#### 参数配置

| 参数     | 数据类型 | 描述     | **是否必填** | **默认值** |
| -------- | -------- | -------- | ------------ | ---------- |
| 集合名称 | string   | 集合名称 | 是           |            |

#### 输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示集合删除成功；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。
4. 执行成功后，message payload 中保存执行结果；执行失败后，Message error 保存报错信息。
:::
::: 列出数据库所有集合
#### 参数配置
不需要填写输入参数。

#### 输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。操作执行成功，返回保存集合名称的 list 数组信息。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 list 类型，成员为 dict 类型，保存集合信息；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：操作执行成功，message payload 如下：
```json
[
	"test_coll2",
  "test_coll",
  "test_coll3"    
]
```

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 执行成功后，message payload 中保存执行结果；执行失败后，Message error 则保存报错信息。上例执行成功，返回 list 数组信息：
   ![image-20210330151557345](https://main.qcloudimg.com/raw/78349185bdce88441abe321025883b26/mongo13.png)

:::
</dx-tabs>


### 文档操作
<dx-tabs>
::: 插入文档
插入文档，支持批量插入文档。

#### 参数配置

| 参数               | 数据类型 | 描述                                     | 是否必填 | 默认值 |
| ------------------ | -------- | ---------------------------------------- | ------------ | ---------- |
| 集合名称           | string   | 集合名称                                 | 是           |            |
| 文档信息           | list     | 文档信息，list 类型，元素为 JSON 字符串格式 | 是           |            |
| 是否按集合顺序插入 | bool     | 是否按集合顺序插入                       | 否           | false      |

#### 输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 list 类型，存储文档的 ObjectID 信息；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：文档插入成功，message payload 如下：
```json
[
    "607e6f6f25e3aa9635c55ef2",
    "607e6f6f25e3aa9635c55ef3"
]
```

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330152935623](https://main.qcloudimg.com/raw/a4238c74c3ee23c6de9b6058b14dc1d0/mongo14.png)
 - item1：
   ![image-20210330153114736](https://main.qcloudimg.com/raw/1ee69cdd0a432743b5720d4e56b16f65/mongo15.png)
 - iterm2:
   ![image-20210330153206800](https://main.qcloudimg.com/raw/c5e6ae486b7840d2c589c77ccac87581/mongo16.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，Message error 保存报错信息。上例执行成功，返回 list：
   ![image-20210330153235144](https://main.qcloudimg.com/raw/71104358921271ec5eb005103cbe1cea/mongo17.png)
:::
::: 查询文档
#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 集合名称       | string   | 集合名称                                                     | 是           |            |
| 查询条件表达式 | string   | MongoDB 表达式格式，例如：{'field1': 'value1'}， {'field2': {'$gte': 1, '$lt': 10 }} | 是           |            |
| 排序字段       | string   | 排序字段                                                     | 否           |            |
| 降序显示文档   | bool     | 是否按排序字段降序显示文档                                   | 否           | false      |
| 每页文档数量   | int      | 查询返回的每页文档数量                                       | 否           |            |
| 最大文档数量   | int      | 查询返回的最大文档数量                                       | 否           |            |

#### 输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 list 类型，成员为 dict 类型，保存文档的信息，键为字段名称，值为字段值，"_id" 字段为文档的 ObjectID 信息；若没有满足条件的文档或执行失败后，则 payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：文档查询成功，message payload 如下：
```json
[
    {
        "_id": "607e63275e1e4e04f692d306",
        "name": "ccc",
        "score": 100
    },
    {
        "_id": "607e6f6f25e3aa9635c55ef2",
        "name": "aaa",
        "score": 10
    }
]
```

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330154248224](https://main.qcloudimg.com/raw/37e8e905f712af7e420d864143d4467a/mongo18.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，Message error 保存报错信息。上例执行成功，返回文档信息。
![image-20210330154931239](https://main.qcloudimg.com/raw/9c01aeffc1f2d667a9b311d47ec97134/mongo19.png)


:::
::: 获取满足指定条件的文档数
#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 集合名称       | string   | 集合名称                                                     | 是           |            |
| 查询条件表达式 | string   | MongoDB 表达式格式，例如：{'field1': 'value1'}， {'field2': {'$gte': 1, '$lt': 10 }} | 是           |            |

#### 输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示满足查询条件的文档数量；若没有满足条件的文档或执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330155136363](https://main.qcloudimg.com/raw/1419f0ce7d9af40e11e1f12092dbdae6/mongo20.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，Message error 保存报错信息。上例执行成功，返回文档数量。
   ![image-20210330155200782](https://main.qcloudimg.com/raw/135bd026f00080c4630f52cb8fda6c3e/mongo21.png)
:::
::: 更新文档
#### 参数配置

| 参数                                     | 数据类型 | 描述                                                         | 是否必填 | 默认值|
| ---------------------------------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 集合名称                                 | string   | 集合名称                                                     | 是           |            |
| 查询条件表达式                           | string   | MongoDB 表达式格式，例如：{'field1': 'value1'}， {'field2': {'$gte': 1, '$lt': 10 }} | 是           |            |
| 待更新内容                               | string   | 待更新文档信息，JSON 字符串格式                               | 是           |            |
| 只更新第一个满足条件的文档               | bool     | 是否只更新第一个满足条件的文档                               | 否           |            |
| 没有满足查询条件的文档时，创建一个新文档 | bool     | 没有满足查询条件的文档时，创建一个新文档                     | 否           |            |

#### 输出
操作执行成功后，输出结果会保存在Message消息体的payload；执行失败后，错误信息会保存在Message消息体的error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 dict 类型，包含以下字段：满足条件的文档数量 matchedCount、更新的文档数量 modifiedCount、新创建的文档数量 upsertedCount；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：操作执行成功，message payload 如下：
```json
{
    "matchedCount": 3,
    "modifiedCount": 3,
    "upsertedCount": 0
}
```

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
 ![image-20210330155649865](https://main.qcloudimg.com/raw/01251c182f2ae7ddd366ec586b3687e4/mongo22.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，Message error 保存报错信息。上例执行成功，返回文档更新信息。
   ![image-20210330155921560](https://main.qcloudimg.com/raw/13d4d91313bc1713b092c490de11bb5a/mongo23.png)
:::
::: 删除文档
#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 集合名称       | string   | 集合名称                                                     | 是           |            |
| 查询条件表达式 | int      | MongoDB 表达式格式，例如：{'field1': 'value1'}， {'field2': {'$gte': 1, '$lt': 10 }} | 是           |            |

#### 输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示已删除的文档数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330160121961](https://main.qcloudimg.com/raw/fce4bdc20f8b8d43bcc9ff9b36a5c0ca/mongo24.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，Message error 保存报错信息。上例执行成功，返回已删除的文档数量。
   ![image-20210330160154044](https://main.qcloudimg.com/raw/899b60d2147c815ad98a6420f618cd91/mongo25.png)

:::
</dx-tabs>

### 索引操作
<dx-tabs>
::: 创建单列索引
#### 参数配置

| 参数     | 数据类型 | 描述     | 是否必填 | 默认值 |
| -------- | -------- | -------- | ------------ | ---------- |
| 集合名称 | string   | 集合名称 | 是           |            |
| 字段名称 | string   | 字段名称 | 是           |            |

#### 输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为创建的索引名称；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330160335023](https://main.qcloudimg.com/raw/ad3b1d93cdb37ec5fb5a4ecc048c20ed/mongo26.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，Message error 保存报错信息。上例执行成功，索引名称：
   ![image-20210330160424013](https://main.qcloudimg.com/raw/28d48d5484f00f1a24bc8af778397062/mongo27.png)
:::
::: 查看索引
#### 参数配置

| 参数     | 数据类型 | 描述     | 是否必填 | 默认值 |
| -------- | -------- | -------- | ------------ | ---------- |
| 集合名称 | string   | 集合名称 | 是           |            |

#### 输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 list 类型，成员为 dict 类型，保存索引信息；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：操作执行成功，message payload 如下：
```json
[
    {
        "key": {
            "_id": 1
        },
        "name": "_id_",
        "v": 2
    },
    {
        "key": {
            "score": 1
        },
        "name": "score_1",
        "v": 2
    }
]
```

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210330160608850](https://main.qcloudimg.com/raw/647fc2ba20eea77cc6045689b0934bf3/mongo28.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，返回索引信息：
   ![image-20210330160628897](https://main.qcloudimg.com/raw/dfc73ac34707164decc1fccfacb4ef3e/mongo29.png)

:::
::: 删除索引
#### 参数配置

| 参数     | 数据类型 | 描述     | 是否必填 | 默认值|
| -------- | -------- | -------- | ------------ | ---------- |
| 集合名称 | string   | 集合名称 | 是           |            |
| 索引名称 | string   | 索引名称 | 是           |            |

#### 输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示索引删除成功；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 MongoDB 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
  ![image-20210330160754523](https://main.qcloudimg.com/raw/5df7377627ad8c6b45033ba4a25d6c7c/mongo30.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功：
   ![image-20210330160849211](https://main.qcloudimg.com/raw/ac3062229c8a1d6f577aa08f428d7029/mongo31.png)
:::
</dx-tabs>

