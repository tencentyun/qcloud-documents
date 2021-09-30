

## 简介

Redis 是使用 ANSI C 编写的开源、支持网络、基于内存、分布式的 [键值对存储数据库](https://zh.wikipedia.org/wiki/键值-值数据库)。

iPaaS Redis 连接器可连接第三方 Redis 服务并执行操作。用户通过连接器配置来配置 Redis 的连接参数，配置成功后便可执行 Redis 操作。

## 连接器配置
### 连接方式
iPaaS Redis 连接器支持三种 Redis 服务的连接方式：
- Cluster 模式
- NonCluster 模式
- Sentinel 模式

### 配置参数

Redis 连接器配置参数如下：

| 参数          | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| Redis 连接模式 | enum     | Redis 连接模式，支持 Cluster 模式、NonCluster 模式、Sentinel 模式 | 是           |   -         |
| 集群地址      | string   | Cluster 模式参数，Redis 集群地址，格式为 host:port，以逗号相隔  | 是           |    -        |
| 地址          | string   | NonCluster 模式参数，Redis 服务地址                            | 是           |   -         |
| 端口号        | int      | NonCluster 模式参数，Redis 服务端口号                          | 是           |    -        |
| 哨兵地址集合  | string   | Sentinel 模式参数，哨兵地址集合，格式为 host:port，以逗号相隔  | 是           |     -       |
| 主节点名称    | string   | Sentinel 模式参数，哨兵集群主节点名称                         | 否           |    -        |
| 密码          | string   | 密码，用于验证 Redis 连接                                      | 否           |  -          |

### 配置界面
**Cluster 模式连接器配置界面：**
![image-20210323163220110](https://main.qcloudimg.com/raw/32af491fe5d2dda38059b7ca7b358288/redis1.png)
**NonCluster 模式连接器配置界面：**
![image-20210323163318486](https://main.qcloudimg.com/raw/200ac48bd76efc2df32dcfa5d077c4e1/redis2.png)
**Sentinel 模式连接器配置界面：**
![image-20210323163349353](https://main.qcloudimg.com/raw/25829301c493e8578a95a9a4c5b2cecc/redis3.png)

## 操作说明

Redis 连接器的操作分为键操作、字符串、列表、哈希、集合、有序集合等操作。
![image-20210323193916591](https://main.qcloudimg.com/raw/db995653eb92a799cedfadc1de483283/redis4.png)
### 键操作
<dx-tabs>
::: exists
#### 参数配置
| 参数 | 数据类型 | 描述 | 是否必填| 默认值|
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |     -       |

####  输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 int 类型，1表示键存在，0表示键不存在；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
![image-20210323194824490](https://main.qcloudimg.com/raw/46d6495d90c5e14f0545168a9ec6d482/redis5.png)
2. 新建连接器配置，填写配置参数，单击**测试连接**，测试连接器配置是否正确。
![image-20210323194919388](https://main.qcloudimg.com/raw/f3dd5819722c55e150379769136f3df8/redis6.png)
3. 在通用配置中，填入待查询的键。
 ![image-20210323195005501](https://main.qcloudimg.com/raw/205783ee7ffd20de8f7d802ac2956633/redis7.png)
4. 执行成功后，message payload 中包含查询结果。
 ![image-20210323195030290](https://main.qcloudimg.com/raw/6192b1b7969a759c717e278963fb9435/redis8.png)
:::
::: del
删除键。
#### 参数配置
| 参数 | 数据类型 | 描述 | 是否必填 | 默认值|
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |   -         |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 int 类型，1表示键删除成功，0表示删除的键不存在；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填入待删除的键。
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。
:::
::: expire/pexpire
设置键的过期时间。

#### 参数配置

| 参数     | 数据类型 | 描述                         | 是否必填 | 默认值 |
| -------- | -------- | ---------------------------- | ------------ | ---------- |
| 键       | string   | 键                           | 是           |    -        |
| 过期时间 | int      | 键的过期时间                 | 是           |      -      |
| 时间单位 | enum     | 过期时间的单位，支持秒、毫秒 | 是           | 秒         |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 bool 类型，true 表示键过期时间设置成功，false 表示键不存在或者不能为键设置过期时间；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
  ![image-20210324105808665](https://main.qcloudimg.com/raw/e61bacd79ac5d3ec1cf812c172cf3a0a/redis9.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。上例执行成功，返回 true：
![image-20210324105907041](https://main.qcloudimg.com/raw/805f955d49774c18fd05e354f076b1e6/redis10.png)
:::
::: expireat/pexpireat
设置键的过期时刻。

#### 参数配置

| 参数         | 数据类型 | 描述                               | 是否必填 | 默认值|
| ------------ | -------- | ---------------------------------- | ------------ | ---------- |
| 键           | string   | 键                                 | 是           |     -       |
| 键的过期时刻 | int      | 键的过期时刻，时间戳格式           | 是           |      -      |
| 时间戳单位   | enum     | 过期时刻的时间戳单位，支持秒、毫秒 | 是           | 秒         |

####  输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 bool 类型，true 表示键过期时刻设置成功，false 表示设置失败；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
  ![image-20210324110831804](https://main.qcloudimg.com/raw/e31e5edde5d42e1fc97408d14958bbc6/redis11.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。上例执行成功，返回 true：
![image-20210324110907585](https://main.qcloudimg.com/raw/2913a60031e28a9a2bc63a20bff42b60/redis12.png)

:::
::: ttl/pttl
获取键的剩余生存时间。

#### 参数配置

| 参数     | 数据类型 | 描述                                   | 是否必填 | 默认值 |
| -------- | -------- | -------------------------------------- | ------------ | ---------- |
| 键       | string   | 键                                     | 是           |   -         |
| 时间单位 | enum     | 键剩余生存时间的时间单位，支持秒、毫秒 | 是           | 秒         |

####  输出

操作执行成功后，输出结果会保存在 Message 消息体的 payload；执行失败后，错误信息会保存在 Message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 int 类型，-2表示键不存在，-1表示键存在但没有设置剩余生存时间，其他情况表示按时间单位返回的键剩余生存时间；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324111508036](https://main.qcloudimg.com/raw/637aeb2def76b5178714c4f4555c849f/redis13.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。上例执行成功，按秒为单位，返回键的剩余生存时间：
![image-20210324111612227](https://main.qcloudimg.com/raw/e136e31921c0467ba5bbc4e12adac4b1/redis14.png)

:::
::: persist
移除键的过期时间。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值|
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |  -          |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 bool 类型，true 表示键的过期时间移除成功，false 表示键不存在或键没有设置过期时间；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324112431289](https://main.qcloudimg.com/raw/fb9ae0d34399c4774dbd600134176a4f/redis15.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。上例执行成功，返回 true：
![image-20210324112522398](https://main.qcloudimg.com/raw/5f9bdb704bccbfc5db2b7e136c5aa17f/redis16.png)
:::
</dx-tabs>


### 字符串操作
<dx-tabs>
::: get
获取键的值。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 |默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |       -     |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为 string 类型，表示键对应的值；当键不存在或执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324113404289](https://main.qcloudimg.com/raw/8f467c8024ddc397b4328aa695a8f659/redis17.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。
 - 上例执行成功，返回键值：
   ![image-20210324113440406](https://main.qcloudimg.com/raw/0f134f9a51f1e930e4a66c0fac6e93d9/redis18.png)
 - 若键不是字符串类型，返回错误：
   ![image-20210324113539134](https://main.qcloudimg.com/raw/c005bb878f0d2313586c001de74b42d2/redis19.png)

:::
::: set/setnx
设置键的值。

#### 参数配置

| 参数               | 数据类型 | 描述                                            | 是否必填 | 默认值 |
| ------------------ | -------- | ----------------------------------------------- | ------------ | ---------- |
| 键                 | string   | 键                                              | 是           |   -         |
| 值                 | string   | 值                                              | 是           |   -         |
| 键的超时时间       | enum     | 键的超时时间，单位为秒，默认为0，不设置超时时间 | 否           | 0          |
| 键存在时使操作无效 | bool     | 开启对应 Redis SETNX 操作，关闭对应 Redis SET 操作  | 否           | false      |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，键设置成功后，payload 值为"OK"，设置失败后，payload 值为 false；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324114142900](https://main.qcloudimg.com/raw/845767bd3040954f592cc6289a325935/redis20.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。上例执行成功：
![image-20210324114222486](https://main.qcloudimg.com/raw/f47984aee7cf18e0091ebab7eb182fe0/redis21.png)

:::
::: incrby/incrbyfloat
将键存储的值加上增量值。

#### 参数配置

| 参数     | 数据类型  | 描述                               |是否必填 |默认值 |
| -------- | --------- | ---------------------------------- | ------------ | ---------- |
| 键       | string    | 键                                 | 是           |    -        |
| 增量值   | int/float | 增量值                             | 是           |    -        |
| 数值类型 | enum      | 增量值的数值类型，支持整型、浮点型 | 是           | 1          |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为执行命令后键对应的值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324145824849](https://main.qcloudimg.com/raw/516e9935b22a788ae075336919e38068/redis22.png)
4. 执行成功后，message payload 中保存执行结果；执行失败后，message error 保存报错信息。
 - 上例执行成功：
   ![image-20210324150156831](https://main.qcloudimg.com/raw/9be4148c4417f13264a573f08c639e2c/redis23.png)
 - 若键不是数值类型，报错：
   ![image-20210324150253309](https://main.qcloudimg.com/raw/e7b22002725e43e170a3bba7f37d4cda/redis24.png)
:::
::: decrby
将键存储的值减去减量值。

#### 参数配置

| 参数   | 数据类型 | 描述   | 是否必填 | 默认值 |
| ------ | -------- | ------ | ------------ | ---------- |
| 键     | string   | 键     | 是           | -           |
| 减量值 | int      | 减量值 | 是           | 1          |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为执行命令后键对应的值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。

:::
::: getrange
获取键的子字符串。

#### 参数配置

| 参数     | 数据类型 | 描述               | 是否必填 | 默认值 |
| -------- | -------- | ------------------ | ------------ | ---------- |
| 键       | string   | 键                 | 是           |    -        |
| 起始索引 | int      | 字符串的起始索引值 | 是           |   -         |
| 终止索引 | int      | 字符串的终止索引值 | 是           |   -         |

####  输出

操作执行成功时，输出结果会保存在 message 消息体的 payload；执行失败时，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为截取得到的子字符串；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
  ![image-20210324151337102](https://main.qcloudimg.com/raw/9f0adebcba1662db8418c0273aba7ee3/redis25.png)
>!test-key 对应的字符串为"ipaas"。
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，返回截取后的字符串：
   ![image-20210324151510819](https://main.qcloudimg.com/raw/7e820b7e00d7025eec5124ca87cd1422/redis26.png)
:::
::: strlen
获取键字符串的长度。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |   -         |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示键字符串的长度；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324151754607](https://main.qcloudimg.com/raw/2b9bc3d84df907035f99f3ba5a2cf2b0/redis27.png)
>!test-key 对应的字符串为"ipaas"。
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，返回截取后的字符串：
  ![image-20210324151827082](https://main.qcloudimg.com/raw/abb14108bd98e6af5d32a45e9d774cbb/redis28.png)
:::
</dx-tabs>

###  列表操作

<dx-tabs>
::: push-to-list
将元素插入列表。

#### 参数配置

| 参数                     | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| ------------------------ | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 键                       | string   | 键                                                           | 是           |     -       |
| 待插入值                 | string   | 待插入元素值                                                 | 是           |   -         |
| 列表左端插入             | bool     | 开启表示由列表左端插入，关闭表示由列表右端插入               | 否           | false      |
| 列表不存在时是否操作无效 | bool     | 开启表示当键不存在时操作无效，关闭表示当键不存在时创建新的列表 | 否           | false      |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示插入元素后列表的长度；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324152428774](https://main.qcloudimg.com/raw/c73a25e95acc00d54a6ccc782f974d3d/redis29.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。
:::
::: pop-from-list
移除列表元素。

#### 参数配置

| 参数             | 数据类型 | 描述                                               | 是否必填 | 默认值|
| ---------------- | -------- | -------------------------------------------------- | ------------ | ---------- |
| 键               | string   | 键                                                 | 是           |   -         |
| 移除列表左端元素 | bool     | 开启表示移除列表左端元素，关闭表示移除列表右端元素 | 否           | false      |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值表示列表移除的元素值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324153134366](https://main.qcloudimg.com/raw/37989ee0e93bf53110906c58a6e84a3d/redis31.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，返回移除的元素值：
   ![image-20210324153306205](https://main.qcloudimg.com/raw/b4516d240aaf96b48478b45ecb559130/redis32.png)
:::
::: llen
返回列表的长度。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |    -        |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示列表的长度；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。
4. 执行成功后，message payload 中保存查询结果；执行失败后，Message error 保存报错信息。
:::
:::  lindex
通过索引获取列表元素。

#### 参数配置

| 参数   | 数据类型 | 描述         | 是否必填| 默认值 |
| ------ | -------- | ------------ | ------------ | ---------- |
| 键     | string   | 键           | 是           |    -        |
| 索引值 | int      | 列表的索引值 | 是           |     -       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值表示列表中下标为指定索引值的元素；如果指定索引值不在列表的区间范围内或执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324153848083](https://main.qcloudimg.com/raw/5302f8819decbae2de1234f2319e1863/redis33.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
   ![image-20210324153937906](https://main.qcloudimg.com/raw/bbee5e9a3efcc77785294757cbb3d2f5/redis34.png)
:::
::: lset
通过索引设置元素的值。

#### 参数配置

| 参数   | 数据类型 | 描述         | 是否必填| 默认值 |
| ------ | -------- | ------------ | ------------ | ---------- |
| 键     | string   | 键           | 是           |     -       |
| 索引值 | int      | 列表的索引值 | 是           |     -       |
| 值     | string   | 待设置的值   | 是           |    -        |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为"OK"；执行失败后，payload 为空         |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
   ![image-20210324154406351](https://main.qcloudimg.com/raw/0c8d681ece38790fd7d5e7e24c9f0367/redis35.png)
4. 执行成功后，message payload中保存了查询结果；执行失败后，message error保存报错信息。上例执行成功，结果如下：
   ![image-20210324154514552](https://main.qcloudimg.com/raw/2ecab7cdcd4ce8ffdb49bd07f3545dee/redis36.png)
:::
</dx-tabs>



### 哈希操作
<dx-tabs>
::: hset
为哈希表字段赋值。
#### 参数配置

| 参数                           | 数据类型 | 描述                                             | 是否必填 | 默认值 |
| ------------------------------ | -------- | ------------------------------------------------ | ------------ | ---------- |
| 键                             | string   | 键                                               | 是           | -           |
| 字段名                         | string   | 哈希表的字段名                                   | 是           |   -         |
| 值                             | string   | 哈希表字段对应的值                               | 是           |   -         |
| 哈希字段名不存在时是否操作无效 | bool     | 开启对应 Redis HSETNX 操作，关闭对应 Redis HSET 操作 | 否           | false      |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示设置成功，false 表示哈希表中字段已经存在且旧值已被新值覆盖或给定字段已经存在且没有操作被执行；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324155200331](https://main.qcloudimg.com/raw/d93d3997ca020a6106bbd6bd324f30e4/redis37.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324155240503](https://main.qcloudimg.com/raw/05e7458e29a1beb4fbaedb4713f2d63f/redis38.png)
:::
::: hgetall
获取哈希表的所有字段和值。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |       -     |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 dict 类型，键为哈希表字段名，值为哈希表字段值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
    {
        "id": 1,
        "name": "a",
        "price": "25.16"
    },
    {
        "id": 2,
        "name": "b",
        "price": "15.26"
    }
 ]
```

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324155539484](https://main.qcloudimg.com/raw/42f4bb277faebbeecdd8466c622fa269/redis39.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324155623793](https://main.qcloudimg.com/raw/40630e45d61f1e9eaf2b1d5e4d49830e/redis40.png)

:::
::: hget
获取哈希表指定字段的值。

#### 参数配置

| 参数       | 数据类型 | 描述           | 是否必填 | 默认值 |
| ---------- | -------- | -------------- | ------------ | ---------- |
| 键         | string   | 键             | 是           |     -       |
| 哈希字段名 | string   | 哈希表字段名称 | 是           |    -        |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为哈希表字段对应的值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324160043698](https://main.qcloudimg.com/raw/d295fbe0d5aaf5b810800a4e64f90ffd/redis41.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324160151646](https://main.qcloudimg.com/raw/4609a50697bf90d6d1167c55f89b1f51/redis42.png)
:::
::: hincrby/hincrbyfloat
为哈希表字段值加上增量值。

#### 参数配置

| 参数       | 数据类型  | 描述                           | 是否必填 | 默认值 |
| ---------- | --------- | ------------------------------ | ------------ | ---------- |
| 键         | string    | 键                             | 是           |   -         |
| 哈希字段名 | string    | 哈希表字段名称                 | 是           |   -         |
| 增量值     | int/float | 增量值                         | 是           | 1          |
| 数值类型   | enum      | 增量值的类型，支持整型、浮点型 | 是           | 整型       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**
 
| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为操作执行后字段的值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324160632952](https://main.qcloudimg.com/raw/71321da9ebacb09dec36f2fc3ff653ac/redis43.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324160734502](https://main.qcloudimg.com/raw/f6dace4b10cd4979df09c0ba73250fe3/redis44.png)
:::
::: hlen
为哈希表字段值加上增量值。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |       -     |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 int 类型，表示哈希表字段的数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324160930993](https://main.qcloudimg.com/raw/1a08a1fec879e3c477cff0883aad6b8e/redis45.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324161002240](https://main.qcloudimg.com/raw/b5785a67de8468d81d1ff963398713cd/redis46.png)
:::
::: hdel
删除哈希表字段。

#### 参数配置

| 参数   | 数据类型 | 描述           | 是否必填 | 默认值 |
| ------ | -------- | -------------- | ------------ | ---------- |
| 键     | string   | 键             | 是           |   -         |
| 字段名 | string   | 哈希表字段名称 | 是           |     -       |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**
 
| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为哈希表成功删除字段的数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324161206710](https://main.qcloudimg.com/raw/b6d1612c8e42c3fc8b4320fa7588e10d/redis47.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324161236277](https://main.qcloudimg.com/raw/e624bba7b017cb34968642cc382933cd/redis48.png)
:::
</dx-tabs>


### 集合操作
<dx-tabs>
::: sadd
集合添加元素。

#### 参数配置

| 参数   | 数据类型 | 描述           | 是否必填 | 默认值 |
| ------ | -------- | -------------- | ------------ | ---------- |
| 键     | string   | 键             | 是           |   -         |
| 元素值 | string   | 待添加的元素值 | 是           |     -       |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为插入成功的元素数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324164751110](https://main.qcloudimg.com/raw/6c42db8d619d0edad3255b2880022213/redis49.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324164824384](https://main.qcloudimg.com/raw/cb35e920506dd7a8cb27ec572f463b41/redis50.png)

:::
:::  spop
移除集合元素。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |     -       |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为移除的元素值；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324165112686](https://main.qcloudimg.com/raw/25a50399239c0a09f8988d7e8b61fc63/redis51.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324165152625](https://main.qcloudimg.com/raw/d09b7a2497ce823f74df7cf0c590cdf1/redis52.png)

:::
::: srandmember
返回集合随机元素。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |     -       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为元素值；执行失败后，payload 为空       |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324165340677](https://main.qcloudimg.com/raw/7c7481d6bf4b8564664ea98b992253c0/redis53.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324165441560](https://main.qcloudimg.com/raw/f39f2086f7fd85dc085cb82529c39998/redis54.png)

:::
::: sismember
判断元素是否是集合元素。

#### 参数配置

| 参数   | 数据类型 | 描述   | 是否必填 | 默认值 |
| ------ | -------- | ------ | ------------ | ---------- |
| 键     | string   | 键     | 是           |   -         |
| 元素值 | string   | 元素值 | 是           |     -       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为 bool 类型，true 表示元素在集合存在，false 表示元素不存在；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324165646217](https://main.qcloudimg.com/raw/c321048ec09e16fd69d13d159eeed395/redis55.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324165704212](https://main.qcloudimg.com/raw/1e006e3280e6fe89bd547fd2abb25ccb/redis56.png)

:::
::: scard
返回集合元素数量。

#### 参数配置

| 参数 | 数据类型 | 描述 | 是否必填 | 默认值 |
| ---- | -------- | ---- | ------------ | ---------- |
| 键   | string   | 键   | 是           |    -        |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为集合元素数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324165920992](https://main.qcloudimg.com/raw/dcbdfc93dae0cb023ff025a3fbc6e9f3/redis57.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324170000280](https://main.qcloudimg.com/raw/f1ef054b47dc1a69d01360fc1aa7b232/redis58.png)
:::
::: srem
移除集合指定元素。

#### 参数配置

| 参数   | 数据类型 | 描述           | 是否必填 | 默认值 |
| ------ | -------- | -------------- | ------------ | ---------- |
| 键     | string   | 键             | 是           |-            |
| 元素值 | string   | 待移除的元素值 | 是           |   -         |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为成功删除的元素数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324170212753](https://main.qcloudimg.com/raw/11b9a24805b23cd8e54c430397cbdc63/redis59.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324170247457](https://main.qcloudimg.com/raw/ab98463fd71354377fee07c3558d3fe7/redis60.png)
:::
</dx-tabs>




### 有序集合操作

<dx-tabs>
::: zadd
有序集合添加元素。

#### 参数配置

| 参数     | 数据类型 | 描述             | 是否必填 | 默认值 |
| -------- | -------- | ---------------- | ------------ | ---------- |
| 键       | string   | 键               | 是           |   -         |
| 元素值   | string   | 待添加的元素值   | 是           |    -        |
| 元素分数 | float    | 元素值对应的分数 | 是           |   -         |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为成功添加的新成员的数量，不包括被更新的、已经存在的成员；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324170539246](https://main.qcloudimg.com/raw/9163ee2f23dcda637e0e6363f5af1651/redis61.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324170801708](https://main.qcloudimg.com/raw/7f3a72f9736d51d5e2dba3b1e21666ea/redis62.png)

:::
::: zrange/zrevrange
返回有序集合指定区间的元素。

#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 键             | string   | 键                                                           | 是           |      -      |
| 起始索引       | int      | 有序集合的起始索引                                           | 是           |     -       |
| 终止索引       | int      | 有序集合的终止索引                                           | 是           |      -      |
| 升序显示元素值 | bool     | 开启表示按元素分数值递增（从小到大）显示，关闭表示按元素分数值递减显示 | 是           | true       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值 list 类型，表示有序集合的成员列表；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
	"test1",
  "test2",
  "test3".
]
```

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324171603567](https://main.qcloudimg.com/raw/a5128bdd721c25fbb749c65d5cb13148/redis63.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，Message error 保存报错信息。上例执行成功，结果如下：
![image-20210324171736311](https://main.qcloudimg.com/raw/ba1bbcd24e29cd99e406d823d9155228/redis64.png)

:::
::: zrangebyscore/zrevrangebyscore
返回有序集合中指定分数区间的成员列表。

#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 键             | string   | 键                                                           | 是           |       -     |
| 最小分数值     | int      | 元素的最小分数值                                             | 是           |      -      |
| 最大分数值     | int      | 元素的最大分数值                                             | 是           |      -      |
| 升序显示元素值 | bool     | 开启表示按元素分数值递增（从小到大）显示，关闭表示按元素分数值递减显示 | 是           | true       |

####  输出

操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值 list 类型，表示有序集合的成员列表；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

例如：执行成功后，message payload 值如下：
```json
[
	"test1",
  "test2",
  "test3".
]
```

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324172022065](https://main.qcloudimg.com/raw/35cd667553d1bdd8fc878524dbeef424/redis65.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324172052533](https://main.qcloudimg.com/raw/d8b03042b8c1bb41a3479f3ac6f020de/redis66.png)

:::
::: zcard
返回有序集合元素数量。

#### 参数配置

| 参数           | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| -------------- | -------- | ------------------------------------------------------------ | ------------ | ---------- |
| 键             | string   | 键                                                           | 是           |  -          |
| 最小分数值     | int      | 元素的最小分数值                                             | 是           |    -        |
| 最大分数值     | int      | 元素的最大分数值                                             | 是           |     -       |
| 升序显示元素值 | bool     | 开启表示按元素分数值递增（从小到大）显示，关闭表示按元素分数值递减显示 | 是           | true       |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为有序集合成员的数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324172218465](https://main.qcloudimg.com/raw/b1349989703b340b84eca61d4cd69564/redis67.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324172303955](https://main.qcloudimg.com/raw/32a9d8910fdd0f0916969ef171c4c1d5/redis68.png)
:::
::: zrem
移除有序集合指定元素。

#### 参数配置

| 参数   | 数据类型 | 描述   | 是否必填 | 默认值 |
| ------ | -------- | ------ | ------------ | ---------- |
| 键     | string   | 键     | 是           |  -          |
| 元素值 | int      | 元素值 | 是           |   -         |

####  输出
操作执行成功后，输出结果会保存在 message 消息体的 payload；执行失败后，错误信息会保存在 message 消息体的 error。

**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 值为有序集合成功移除的成员数量；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 添加 Redis 连接器组件。
2. 新建连接器或选择已创建的连接器。
3. 在通用配置中，填写相关参数。例如：
![image-20210324172436009](https://main.qcloudimg.com/raw/1e431bafb61be2eee8e9591d6ff2f48a/redis69.png)
4. 执行成功后，message payload 中保存查询结果；执行失败后，message error 保存报错信息。上例执行成功，结果如下：
![image-20210324172559789](https://main.qcloudimg.com/raw/c9357879e91b1c87c976668e63164a85/redis70.png)
:::
</dx-tabs>






