## 简介

iPaaS Database 连接器可连接第三方关系型数据库系统并执行 SQL 操作。用户通过连接器配置来配置数据库的连接参数，配置成功后便可执行对应的数据库操作。

iPaaS Database 连接器目前支持的数据库有：MySQL、Oracle、PostgreSQL、Sql Server。

## 连接器配置

**Database 连接器配置参数**

| 参数       | 数据类型 | 描述                                                  | **是否必填** | **默认值** |
| ---------- | -------- | ----------------------------------------------------- | ------------ | ---------- |
| 数据库类型 | enum     | 数据库类型，支持 MySQL、Oracle、PostgreSQL、Sql Server | 是           |   -         |
| 地址       | string   | 数据库地址                                            | 是           |   -         |
| 端口号     | int      | 数据库端口号                                          | 是           |    -        |
| 用户名     | string   | 用于连接数据库的用户名                                | 是           |     -       |
| 密码       | string   | 用于连接数据库的用户密码                              | 是           |      -      |
| 超时时间   | int      | 数据库连接超时时间（单位秒），最长超时时间为30秒  | 否           | 5          |

**连接器配置界面**
![image-20210322164328964](https://main.qcloudimg.com/raw/98c6f0f4afc3899b27c176274daf0fb8/database1.png)

##  操作说明

Database 连接器目前支持查询、插入、更新、删除、存储过程（目前仅支持 Sql Server）操作。

### 查询操作
<dx-tabs>
::: SQL 模式
#### 参数配置

**查询逻辑配置**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 操作模式，支持简单模式-单表查询、简单模式-多表查询和 SQL 模式 | 是           | SQL 模式    |
| 查询语句 | string   | SQL 模式参数，SQL 语句，支持两种写法：<br>1. 原生 SQL。例如："select * from p where age=12" <br> 2. 嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入。例如："select * from p where age = :age"，在“输入参数”中，填入变量名 key 为"age"，value 值为"12"，此时待执行的查询语句为“select * from p where age=12” | 是           |   -         |
| 输入参数 | dict     | SQL 模式参数，输入参数列表，列表元素为字典，key 对应“查询语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |      -      |

![image-20210706145020450](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database37.png)

#####  输出
查询操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，键表示数据库字段名称，值表示数据库字段值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
    {
        "book_auth": "aaa",
        "book_id": 1,
        "book_name": "a",
        "book_price": "25.16"
    },
    {
        "book_auth": "bbb",
        "book_id": 2,
        "book_name": "b",
        "book_price": "15.26"
    }
 ]
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "Login error: mssql: Cannot open database \"test\" that was requested by the login. Using the user default database \"master\" instead."
}
```

#### 案例
1. 添加 Database 连接器组件，选择查询操作。
![image-20210322174020999](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database7.png)
2. 新建连接器配置，填写配置参数，单击**测试连接**，测试连接器配置是否正确。
![image-20210322174307139](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database9.png)
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“查询语句”为 `select * from books where book_price > :book_price`，输入参数中 key 为 book_price，value 为30，正确的查询结果如下：
![image-20210706145213416](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database38.png)
4. 查询结果：
 - 查询成功后，message payload 中包含了查询结果：
![image-20210420133927943](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database12.png)
 - 若查询过程中出现错误，message error 中会包含错误信息：
![image-20210322192839811](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database13.png)
:::
::: 简单模式-单表查询
#### 参数配置

**查询逻辑配置**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 操作模式，支持简单模式-单表查询、简单模式-多表查询和 SQL 模式 | 是           | SQL 模式    |
| 表选择   | enum     | 简单模式-单表查询参数，待查询的数据表                        | 是           |         -   |
| 字段选择 | list     | 简单模式-单表查询参数，查询的数据表字段                      | 是           |      -      |
| 过滤条件 | list     | 简单模式-单表查询参数，查询的过滤条件                        | 否           |      -      |

**输出配置**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 输出模式 | enum     | 查询所得数据的输出模式，支持普通模式和 RecordSet 模式          | 是           | 普通模式   |
| 是否缓存 | bool     | 输出模式为 RecordSet 模式时的参数，输出的 RecordSet 数据是否支持缓存 | 否           | false      |
| 分区数量 | int      | 输出模式为 RecordSet 模式时的参数，输出的 RecordSet 数据分区数设置，范围[1,10] | 是           | 1          |

#### 输出
查询操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，键表示数据库字段名称，值表示数据库字段值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择查询操作。
2. 新建连接器配置或选择已创建的连接器配置。
3. 配置中的“表选择”选择数据表“books”，“字段选择”填写“book_id”和“book_name”字段，输出模式选择“普通输出”，过滤条件中填写如下内容：
   ![image-20210706145432851](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database39.png)
4. 查询成功后，message payload 中包含了查询结果：
![image-20210624192504242](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database30.png)
:::
::: 简单模式-多表查询
#### 参数配置

**通用**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 操作模式，支持简单模式-单表查询、简单模式-多表查询和 SQL 模式 | 是           | SQL 模式    |

**查询逻辑配置**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 连接类型 | enum     | 简单模式-多表查询参数，支持 INNER JOIN、LEFT JOIN、RIGHT JOIN | 是           |        -    |
| 连接条件 | list     | 简单模式-多表查询参数，数据表间 join 查询的连接条件            | 是           |         -   |
| 过滤条件 | list     | 简单模式-单表查询参数，查询的过滤条件                        | 否           |     -       |
| 字段选择 | list     | 简单模式-多表查询参数，查询的数据表字段                      | 是           |    -        |

**输出配置**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 输出模式 | enum     | 查询所得数据的输出模式，支持普通模式和 RecordSet 模式          | 是           | 普通模式   |
| 是否缓存 | bool     | 输出模式为 RecordSet 模式时的参数，输出的 RecordSet 数据是否支持缓存 | 否           | false      |
| 分区数量 | int      | 输出模式为 RecordSet 模式时的参数，输出的 RecordSet 数据分区数设置，范围[1,10] | 是           | 1          |

#### 输出
查询操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，list 成员为 dict 类型，键表示数据库字段名称，值表示数据库字段值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |


#### 案例
1. 添加 Database 连接器组件，选择查询操作。
2. 新建连接器配置或选择已创建的连接器配置。
3. 在配置中填写如下配置：
   ![image-20210706155231095](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database48.png)
4. 查询成功后，message payload 中包含了查询结果：
![image-20210624192504242](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database32.png)
:::
::: Recordset 输出模式
#### 输出

查询操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 RecordSet 类型数据；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择查询操作。
2. 新建连接器配置或选择已创建的连接器配置。
3. 在配置中填写如下配置，输出模式选择“RecordSet 模式”：
   ![image-20210706155048420](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database47.png)
4. 查询成功后，message payload 中包含了查询结果，该查询结果为 RecordSet 类型：
![image-20210624194603160](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database34.png)
5. 可以通过“For Each”组件对 RecordSet 数据进行迭代：
![image-20210624194833360](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database35.png)
 - 迭代结果如下：
![image-20210624194921846](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database36.png)
:::
</dx-tabs>





### 插入操作
<dx-tabs>
::: SQL 模式
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句 | 是           | SQL 模式    |
| 插入语句 | string   | SQL 模式参数，SQL 语句，支持两种写法：<br>1. 原生 SQL <br> 2. 嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |        -    |
| 输入参数 | dict     | SQL 模式，输入参数列表，列表元素为字典，key 对应“插入语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |     -       |

![image-20210706154015476](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database40.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段，当为 MySQL 数据库时，会额外包含“lastId”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：MySQL 数据库的插入操作，执行成功后，message payload 值如下：
```json
{
    "lastId": 1,
    "rowsAffected": 1
}
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "Login error: mssql: Cannot open database \"test\" that was requested by the login. Using the user default database \"master\" instead."
}
```

#### 案例
1. 添加 Database 连接器组件，选择插入操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“插入语句”为 `insert into books (book_auth, book_name, book_price) values (:book_auth, :book_name, :book_price)`，输入参数使用 Dataway 格式编写：
```python
def dw_process(msg):
	return {
	'book_auth': 'test',
	'book_name': 'ipaas',
	'book_price': 100,
	}
```
4. 插入结果：
 - 插入成功后，message payload 中包含了执行结果：
![image-20210323113311938](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database15.png)
 - 若插入过程中出现错误，message error 中会包含错误信息：
![image-20210323113745340](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database16.png)
:::
::: 简单模式
#### 参数配置

**通用**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句 | 是           | SQL 模式    |

**插入逻辑配置**

| 参数     | 数据类型 | 描述                                                 | **是否必填** | **默认值** |
| -------- | -------- | ---------------------------------------------------- | ------------ | ---------- |
| 表选择   | enum     | 简单模式参数，待操作的数据表                         | 是           |       -     |
| 字段配置 | list     | 简单模式参数，待插入的字段信息，包括字段名称和字段值 | 是           |    -        |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段，当为 MySQL 数据库时，会额外包含“lastId”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择插入操作。
2. 新建连接器配置或选择已创建的连接器配置。
3. 在配置中填写如下配置：
   ![image-20210706154130804](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database41.png)
4. 插入成功后，message payload 如下：
![image-20210624195845881](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database39.png)
:::
</dx-tabs>





### 更新操作
<dx-tabs>
::: SQL 模式
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句 | 是           | SQL 模式    |
| 更新语句 | string   | SQL 模式参数，SQL 语句，支持两种写法：<br>1. 原生 SQL  <br>2. 嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |       -     |
| 输入参数 | dict     | SQL 模式，输入参数列表，列表元素为字典，key 对应“更新语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |    -        |

![image-20210706154234388](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database42.png)

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error为dict类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
{
    "rowsAffected": 1
}
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "Login error: mssql: Cannot open database \"test\" that was requested by the login. Using the user default database \"master\" instead."
}
```

#### 案例
1. 添加 Database 连接器组件，选择更新操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“更新语句”为 `update books set book_price = :book_price where book_name = :book_name`，输入参数如下：
```python
def dw_process(msg):
	return {
	'book_price': 200,
	'book_name': 'ipaas'
	}	 
```
4. 更新结果：
 - 更新成功后，message payload 中包含了执行结果：
 ![image-20210323130616820](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database18.png)
 - 若更新过程中出现错误，message error 中会包含错误信息：
 ![image-20210323130616820](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database19.png)
:::
::: 简单模式
#### 参数配置
**通用**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- | 
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句| 是           | SQL 模式    |

**更新逻辑配置**：

| 参数     | 数据类型 | 描述                                   | **是否必填** | **默认值** |
| -------- | -------- | -------------------------------------- | ------------ | ---------- |
| 表选择   | enum     | 简单模式参数，待操作的数据表           | 是           |    -        |
| 字段配置 | list     | 简单模式参数，待更新的字段名称和字段值 | 是           |     -       |
| 过滤条件 | list     | 简单模式参数，更新条件                 | 否           |   -         |

####  输出
操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择更新操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入如下配置：
   ![image-20210706154417793](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database43.png)
4. 更新成功后，message payload 中包含了执行结果：
   ![image-20210624200725113](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database42.png)
:::
</dx-tabs>





### 删除操作
<dx-tabs>
::: SQL 模式
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句| 是           | SQL 模式    |
| 删除语句 | string   | SQL 模式，SQL 语句，支持两种写法：<br>1. 原生 SQL<br>  2. 嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |  -          |
| 输入参数 | dict     | SQL 模式，输入参数列表，列表元素为字典，key 对应“删除语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |       -     |

![image-20210706154506714](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database44.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
{
    "rowsAffected": 1
}
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "Login error: mssql: Cannot open database \"test\" that was requested by the login. Using the user default database \"master\" instead."
}
```

#### 案例
1. 添加 Database 连接器组件，选择删除操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“删除语句”为 `delete from books where book_name = :book_name`，输入参数如下：
```python
def dw_process(msg):
	return {
	'book_name': 'ipaas'
	} 
```
4. 删除结果：
 - 删除成功后，message payload 中包含了执行结果：
![image-20210323143317272](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database21.png)
 - 若执行过程中出现错误，message error 中会包含错误信息：
![image-20210323144550095](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database22.png)

:::
::: 简单模式
#### 参数配置

**通用**

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 操作模式 | enum     | 支持简单模式和 SQL 模式；简单模式可辅助编写操作语句，SQL 模式下可编写结构化 SQL 语句 | 是           | SQL 模式    |

**删除逻辑配置**

| 参数     | 数据类型 | 描述                         | **是否必填** | **默认值** |
| -------- | -------- | ---------------------------- | ------------ | ---------- |
| 表选择   | enum     | 简单模式参数，待操作的数据表 | 是           |        -    |
| 过滤条件 | list     | 简单模式参数，删除条件       | 否           |        -    |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 list 类型，包含“rowsAffected”字段；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择删除操作。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入如下配置：
   ![image-20210706154559845](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database45.png)
4. 删除成功后，message payload 中包含了执行结果：
	![image-20210323143317272](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database21.png)
:::
</dx-tabs>




### 批量插入操作
#### 参数配置
**输入配置**

| 参数                 | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| -------------------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集           | Recordset 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           | -           |
| 输入数据集 Schema 校准 | list          | 对输入数据集进行字段校准                     | 否           |   -         |

**插入逻辑配置**

| 参数     | 数据类型 | 描述               | **是否必填** | **默认值** |
| -------- | -------- | ------------------ | ------------ | ---------- |
| 表选择   | enum     | 待操作的数据表     | 否           |         -   |
| 过滤条件 | list     | 批量更新的过滤条件 | 是           |    -        |

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为前一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Database 连接器组件，选择批量插入操作。
2. 新建连接器或选择已创建的连接器。
3. 通过“RecordSet Encoder”生成 RecordSet 类型的数据，在“Encoder”组件中设置如下 Schema：
   ![image-20210624201918451](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database45.png)
4. 在“Encoder”组件选择“Set Payload”组件，按如下配置设置：
```python
def dw_process(msg):
    return [['xiaomi',66.66,'e'], ['xiaoming',66.66,'f'], ['xiaohua',66.66,'g']]
```
 - 测试组件如下：
![image-20210624203014745](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database47.png)
5. 构造好 RecordSet 数据后，输入数据集如下：
```python
def dw_process(msg):
    return msg.payload	 
```
6. Database 组件通过数据表字段和 RecordSet 数据字段的映射关系来构造插入的数据信息，配置如下：
![image-20210701152327985](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database34.png)
7. 批量插入成功后，message 的 error 信息为空。

### 批量合并操作

#### 参数配置
**输入配置**

| 参数                 | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| -------------------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集           | Recordset 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |    -        |
| 输入数据集 Schema 校准 | list          | 对输入数据集进行字段校准                     | 否           |        -    |

**合并逻辑配置**

| 参数       | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ---------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 表选择     | enum     | 待操作的数据表                                               | 否           |   -         |
| 过滤条件   | list     | 批量更新的过滤条件                                           | 是           |      -      |
| 字段映射   | enum     | 字段映射，数据表字段和 Recordset 类型数据字段的映射，插入数据表字段的值为 Recordset 类型数据字段的值 | 是           |       -     |
| 只执行插入 | bool     | 数据不存在时执行插入操作                                     | 是           | false      |
| 只执行更新 | bool     | 数据存在时执行更新操作                                       | 是           | false      |

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为前一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 通过“RecordSet Encoder”组件生成 RecordSet 类型的数据。
3. 构造好 RecordSet 数据后，添加 Database 组件的“批量合并”操作，数据表字段和 RecordSet 数据字段的关系构成了合并的过滤条件，数据表字段和 RecordSet 数据字段的映射构成了合并的字段映射；Database 组件配置如下：
   ![image-20210701152525761](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database35.png)
4. 批量插入成功后，message 的 error 信息为空。

### 批量删除操作
#### 参数配置

**输入配置**

| 参数                 | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| -------------------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集           | Recordset 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |  -          |
| 输入数据集 Schema 校准 | list          | 对输入数据集进行字段校准                     | 否           |    -        |

**删除逻辑配置**

| 参数     | 数据类型 | 描述               | **是否必填** | **默认值** |
| -------- | -------- | ------------------ | ------------ | ---------- |
| 表选择   | enum     | 待执行操作的数据表 | 否           |    -        |
| 过滤条件 | list     | 批量删除的条件     | 是           |     -       |

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为前一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 通过“RecordSet Encoder”组件生成 RecordSet 类型的数据。
3. 构造好 RecordSet 数据后，添加 Database 组件的“批量删除”操作，数据表字段和 RecordSet 数据字段的关系构成了合并的过滤条件，Database 组件配置如下：
   ![image-20210706154654745](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database46.png)
 - 组件如下：
![image-20210624204634109](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database50.png)
4. 批量插入成功后，message 的 error 信息为空。

### 存储过程操作
#### 参数配置

| 参数             | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ---------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 存储过程名称     | string   | 待调用存储过程的名称                                         |       -       |     -       |
| 存储过程输入参数 | string   | 待调用存储过程的输入参数，输入参数顺序必须和存储过程传入参数顺序一致，使用参数化（冒号+参数名）输入，参数间以英文逗号相隔 | 是           |   -         |
| 输入参数         | dict     | 输入参数列表，列表元素为字典，key 对应“存储过程输入参数”中的变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |      -      |
| 存储过程输出参数 | list     | 待调用存储过程的输出参数信息，输出参数顺序需要和存储过程的输出参数一致，列表添加时需要输入“字段名称”及“字段类型”信息；若使用表达式输入，列表元素字段名称命名为'fieldName'，字段类型为'fieldType' |         -     |    -        |

![image-20210322172755536](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database24.png)

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，存储过程输出的 payload 取决于输出参数，payload 为 list 类型，list 成员为 dict 类型，键表示输出参数字段名称，值表示输出参数字段值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下，其中“id”和“book_name”为指定的输出参数字段：
```json
[
    {
        "id": 1,
        "book_name": "a",
    },
    {
        "id": 2,
        "book_name": "b",
    }
 ]
```
执行失败后，message error 值如下：
```json
{
    "Code": "CORE:RUNTIME",
    "Description": "Login error: mssql: Cannot open database \"test\" that was requested by the login. Using the user default database \"master\" instead."
}
```



#### 案例
1. 添加 Database 连接器组件，选择存储过程操作。
![image-20210323144706499](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database23.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入参数信息。例如：“存储过程”为 getBookId，输入参数 dataway 表达式如下：
```python
def dw_process(msg):
	return {
	'name': 'aaa',
	'price': 0,
	}
```
 - 输出参数表达式如下：
```python
def dw_process(msg):
	return [
	{'fieldName':'id', 'fieldType':'INT'}, 
	{'fieldName':'book_name', 'fieldType':'VARCHAR'}
	]
```
 - 界面如图：
  ![image-20210323145420670](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database6.png)
4. 执行结果：
 - 执行成功后，message payload 中包含了执行结果：
![image-20210323145529825](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database25.png)
 - 若执行过程中出现错误，message error 中会包含错误信息：
![image-20210323145701162](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Database/database26.png)
 - 若查询过程中出现错误，message error 中会包含错误信息。

