

## 简介

iPaaS Database 连接器可连接第三方关系型数据库系统并执行 SQL 操作。用户通过连接器配置来配置数据库的连接参数，配置成功后便可执行对应的数据库操作。

iPaaS Database 连接器目前支持的数据库有：MySQL、Oracle、PostgreSQL、Sql Server。

## 连接器配置

Database 连接器配置参数：

| 参数       | 数据类型 | 描述                                                  | **是否必填** | **默认值** |
| ---------- | -------- | ----------------------------------------------------- | ------------ | ---------- |
| 数据库类型 | enum     | 数据库类型，支持 MySQL、Oracle、PostgreSQL、Sql Server | 是           |            |
| 地址       | string   | 数据库地址                                            | 是           |            |
| 端口号     | int      | 数据库端口号                                          | 是           |            |
| 用户名     | string   | 用于连接数据库的用户名                                | 是           |            |
| 密码       | string   | 用于连接数据库的用户密码                              | 是           |            |
| 超时时间   | int      | 数据库连接超时时间（单位秒），最长超时时间为30秒  | 否           | 5          |

连接器配置界面如下：
![image-20210322164328964](https://main.qcloudimg.com/raw/98c6f0f4afc3899b27c176274daf0fb8/database1.png)

##  操作说明

Database 连接器目前支持查询、插入、更新、删除、存储过程（目前仅支持 Sql Server）操作。

<dx-tabs>
::: 查询操作
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 查询语句 | string   | SQL 语句，支持两种写法：<br><li>原生 SQL。例如："select * from p where age=12" <br><li>嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入。例如："select * from p where age = :age"， 在“输入参数”中，填入变量名key为"age"，value值为"12"，此时待执行的查询语句为“select * from p where age=12” | 是           |            |
| 输入参数 | dict     | 输入参数列表，列表元素为字典，key 对应“查询语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |            |

![image-20210322171606343](https://main.qcloudimg.com/raw/31bf5b5ae21aaf9a267d64ec451fdb2d/database2.png)

####  输出

查询操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

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
![image-20210322174020999](https://main.qcloudimg.com/raw/dedd178d8b4df665832d87897429ba6a/database7.png)
![image-20210322174047443](https://main.qcloudimg.com/raw/cd82cdd13a97f7c8f716f72d22d7a6bc/database8.png)
2. 新建连接器配置，填写配置参数，单击【测试连接】，测试连接器配置是否正确。
![image-20210322174307139](https://main.qcloudimg.com/raw/f420cf6b8d1fa8a342de570ace1107b6/database9.png)
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“查询语句”为 `select * from books where book_price > :book_price`，输入参数中 key 为 book_price，value 为30，正确的查询结果如下：
![image-20210322192557544](https://main.qcloudimg.com/raw/35ebbe479ca0c2fa8497df8cbdbc1882/database10.png)
 - 输入参数：
![image-20210322192627158](https://main.qcloudimg.com/raw/3155c2ff8992732871bbb7c7525907d1/database11.png)
 - 查询成功后，message payload 中包含查询结果：
![image-20210420133927943](https://main.qcloudimg.com/raw/c5692b1041aa1bf1438e365e997b085a/database12.png)
 - 若查询过程中出现错误，message error 中会包含错误信息：
![image-20210322192839811](https://main.qcloudimg.com/raw/a3bd53257d44fc38d27bbe30396d17d7/database13.png)
:::
:::插入操作
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 插入语句 | string   | SQL 语句，支持两种写法：<br><li>原生 SQL <br><li>嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |            |
| 输入参数 | dict     | 输入参数列表，列表元素为字典，key 对应“插入语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |            |

![image-20210322172218290](https://main.qcloudimg.com/raw/820018678917ea12f16d3d78001352d7/database3.png)

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

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
![image-20210322200119025](https://main.qcloudimg.com/raw/764e7a54c4c4164098ca326fdf98dd03/database14.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“插入语句”为`insert into books (book_auth, book_name, book_price) values (:book_auth, :book_name, :book_price)`，输入参数使用 Dataway 格式编写。
   ```python
   def dw_process(msg):
   	return {
   	'book_auth': 'test',
   	'book_name': 'ipaas',
   	'book_price': 100,
   	}
   ```
4. 插入成功后，message payload 中包含执行结果：
![image-20210323113311938](https://main.qcloudimg.com/raw/95f39bcfd62f2ff38566142f6b8d4974/database15.png)
 - 若插入过程中出现错误，message error 中会包含错误信息：
![image-20210323113745340](https://main.qcloudimg.com/raw/4aebc8d23b216c0fc5fb5e0f304c2b96/database16.png)

:::
::: 更新操作
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 更新语句 | string   | SQL 语句，支持两种写法：<br><li>原生 SQL <br><li>嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |            |
| 输入参数 | dict     | 输入参数列表，列表元素为字典，key 对应“更新语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |            |

![image-20210322172447485](https://main.qcloudimg.com/raw/8b1325dfa2eca66568df4d5a31df280d/database4.png)

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

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

1. 添加 Database 连接器组件，选择更新操作。
   ![image-20210323125132684](https://main.qcloudimg.com/raw/61cdaf1e3b0011545f477b95e3213860/database17.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“更新语句”为`update books set book_price = :book_price where book_name = :book_name`，输入参数如下：
   ```python
   def dw_process(msg):
   	return {
   	'book_price': 200,
   	'book_name': 'ipaas'
   	}
   ```
4. 更新成功后，message payload 中包含执行结果：
   ![image-20210323130616820](https://main.qcloudimg.com/raw/5ac3d9e66ad7f686ee08f8f82df35524/database18.png)
 - 若更新过程中出现错误，message error 中会包含错误信息：
   ![image-20210323130616820](https://main.qcloudimg.com/raw/90f76091a191b8081fb109df4058fada/database19.png)

:::
::: 删除操作
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| -------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 删除语句 | string   | SQL 语句，支持两种写法：<br><li>原生SQL<br><li>嵌入占位符的 SQL，使用参数化输入（冒号+参数），可防止 SQL 注入 | 是           |            |
| 输入参数 | dict     | 输入参数列表，列表元素为字典，key 对应“删除语句”中的参数化变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |            |

![image-20210322172616207](https://main.qcloudimg.com/raw/ba93bd39ed5e265102603eff90ee760a/database5.png)

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

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
   ![image-20210323142957123](https://main.qcloudimg.com/raw/ac7c291f583dcb6091bdf83d37c73494/database20.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入 SQL 语句及输入参数。例如：“删除语句”为`delete from books where book_name = :book_name`，输入参数如下：
   ```python
   def dw_process(msg):
   	return {
   	'book_name': 'ipaas'
   	}
   ```
 - 删除成功后，message payload 中包含执行结果：
![image-20210323143317272](https://main.qcloudimg.com/raw/69ba53c2ffdbdc946927af9daf73f3fb/database21.png)
 - 若执行过程中出现错误，message error 中会包含错误信息：
![image-20210323144550095](https://main.qcloudimg.com/raw/acc8d0750d0daf89a42aa986b9816b40/database22.png)
:::
::: 存储过程操作
#### 参数配置

| 参数             | 数据类型 | 描述                                                         | **是否必填** | **默认值** |
| ---------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 存储过程名称     | string   | 待调用存储过程的名称                                         |              |            |
| 存储过程输入参数 | string   | 待调用存储过程的输入参数，输入参数顺序必须和存储过程传入参数顺序一致，使用参数化（冒号+参数名）输入，参数间以英文逗号相隔 | 是           |            |
| 输入参数         | dict     | 输入参数列表，列表元素为字典，key 对应“存储过程输入参数”中的变量名，key 值需要与参数化变量名一致，value 为该变量的值 | 否           |            |
| 存储过程输出参数 | list     | 待调用存储过程的输出参数信息，输出参数顺序需要和存储过程的输出参数一致，列表添加时需要输入“字段名称”及“字段类型”信息；若使用表达式输入，列表元素字段名称命名为 'fieldName'，字段类型为 'fieldType' |              |            |

![image-20210322172755536](https://main.qcloudimg.com/raw/4059f3b4b9b339b370b69b0e274412c1/database24.png)

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

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
![image-20210323144706499](https://main.qcloudimg.com/raw/8b0dc537e9ff2ce516d5e232aa2a24c8/database23.png)
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入参数信息。例如：“存储过程”为 getBookId，输入参数 dataway 表达式如下：
   ```python
   def dw_process(msg):
   	return {
   	'name': 'aaa',
   	'price': 0,
   	}
   ```
   输出参数表达式如下：
   ```python
   def dw_process(msg):
   	return [
   	{'fieldName':'id', 'fieldType':'INT'}, 
   	{'fieldName':'book_name', 'fieldType':'VARCHAR'}
   	]
   ```
   界面如图：
   ![image-20210323145420670](https://main.qcloudimg.com/raw/ac839855a3c756a59cf0efa8d008934b/database6.png)
4. 执行成功后，message payload 中包含执行结果：
![image-20210323145529825](https://main.qcloudimg.com/raw/f89ec03710cc4ec3ac6fe9c86dea9562/database25.png)
 - 若执行过程中出现错误，message error 中会包含错误信息：
![image-20210323145701162](https://main.qcloudimg.com/raw/270403b4347dfa04398ef849d904d35a/database26.png)
 - 若查询过程中出现错误，message error 中会包含错误信息。


:::
</dx-tabs>

