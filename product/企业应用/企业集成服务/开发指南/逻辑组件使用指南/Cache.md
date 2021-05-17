

## 简介

Cache 组件用于缓存流运行中产生的中间数据，同一个应用中的不同流，可以共享 Cache 组件中缓存的数据。目前 Cache 组件只能缓存字符串类型数据，并对每个用户的使用空间进行限制，每个用户可存储的数据量最大为10MB，可存储的数据条数最大为1000条，单条数据大小不能超过100KB，数据的缓存时间最长为30天。存储数据量和数据条数，都支持动态配置，如果需要扩容，可联系管理员进行操作。

## 操作说明
<dx-tabs>
::: 存储
#### 参数配置

| 参数     | 数据类型 | 描述                                              | 是否必填 | 默认值 |
| :------- | :------- | :------------------------------------------------ | :------- | ------ |
| 键值     | String   | 数据的唯一标识，根据该参数查找数据。                | 是       | 无     |
| 数据     | String   | 待存储的数据。                                      | 是       | 无     |
| 存储时长 | int      | 数据过期时间，取值范围为1~2592000，不支持永久保存。 | 是       | 无     |

![image-20210325141434795](https://main.qcloudimg.com/raw/6566310ff4b897b0c4998abab39e7a3a/image-20210325141434795.png)

#### 输出
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当数据存储成功后，payload 中的值为“OK”；存储失败时，则值为“fail”。|
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 存储成功时，variable 中的信息与上个组件相同；存储失败时，variable 在上个组件的信息基础上增加变量“err”，“err”描述失败原因。 |

- **存储成功**
当存储成功时，payload 中的值为“OK”。
![image-20210324205926945](https://main.qcloudimg.com/raw/354e39e6a1ea097456ddbfc3375c4717/image-20210324205926945.png)
- **存储失败**
 - 当存储失败时，payload 中的值为“fail”。
![image-20210324210211926](https://main.qcloudimg.com/raw/c92777c6b24e0ac50da373a1bceb5917/image-20210324210211926.png)
 - 存储失败时，变量“err”中包含失败的原因。
![image-20210324210417203](https://main.qcloudimg.com/raw/712d80009b316d905f89e28224b5a54a/image-20210324210417203.png)

:::
::: 存储（仅在键不存在时，执行存储）
当选择该操作时，如果已经使用设置的键保存过数据，且该数据未过期，则会保存失败。
#### 参数配置

| 参数     | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| :------- | :------- | :----------------------------------------------------------- | :------- | ------ |
| 键值     |String   | 数据的唯一标识，根据该值索引数据，如果两个数据的键相同，则后执行的存储操作会覆盖之前的数据。 | 是       | 无     |
| 数据     | String   | 待存储的数据。                                                 | 是       | 无     |
| 存储时长 | int      | 数据过期时间，取值范围为1~2592000，不支持永久保存。            | 是       | 无     |

#### 配置界面
![image-20210325141508498](https://main.qcloudimg.com/raw/6881e4dd4b95ee850af6095d5a787675/image-20210325141508498.png)

#### 输出
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当数据存储成功后，payload 中的值为“OK”， 存储失败时，则值为“fail”。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 存储成功时，variable 中的信息与上个组件相同；存储失败时，variable 在上个组件的信息基础上增加了变量“err”，“err”描述失败原因。 |

- **存储成功**
当设置的键不存在时，payload 输出“OK”。
  ![image-20210324211422269](https://main.qcloudimg.com/raw/e985dfc68a50822d379acb26869f31ac/image-20210324211422269.png)
- **存储失败**
 - 当存储失败时，payload 中的值为“fail”。
  ![image-20210324211321183](https://main.qcloudimg.com/raw/6194c5dc410c9f7218531d53c6bae3b0/image-20210324211321183.png)
 - 存储失败时，变量“err”中可查看失败的原因。
![image-20210324211257584](https://main.qcloudimg.com/raw/ec69e5978638f3cb9ef013c22cef64b9/image-20210324211257584.png)

:::
:::  读取
#### 参数配置

| 参数 | 数据类型 | 描述                               | 是否必填 | 默认值 |
| :--- | :------- | :--------------------------------- | :------- | ------ |
| 键值 | String   | 数据的唯一标识，根据该参数查找数据。 | 是       | 无     |

#### 配置界面
![image-20210325141532915](https://main.qcloudimg.com/raw/b6a43a5070ca1b332a32ed78373ae30f/image-20210325141532915.png)

#### 输出
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 读取存在时，payload 保存待查找的数据；数据不存在时，payload 中为空字符串。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 读取成功时，variable 中的信息与上个组件相同；读取失败时，variable 在上个组件的信息基础上增加变量“err”，“err”描述失败原因。 |

- **数据存在**
当要查找的数据存在时，payload 中会保存待查找的数据，使用 msg.payload 即可读取该数据。
 ![image-20210324211911854](https://main.qcloudimg.com/raw/6f855e7ead68655ea507f8d5d2aef67f/image-20210324211911854.png)
- **数据不存在**
当要查找的数据不存在时，payload 中返回空字符串。
![image-20210324212103960](https://main.qcloudimg.com/raw/1f221bb1988289bcbc25c101d4736bed/image-20210324212103960.png)

:::
:::  删除
#### 参数配置

| 参数 | 数据类型 | 描述                               | 是否必填 | 默认值 |
| :--- | :------- | :--------------------------------- | :------- | ------ |
| 键值 | String   | 数据的唯一标识，删除该值标识的数据。 | 是       | 无     |

#### 配置界面
![image-20210325141559982](https://main.qcloudimg.com/raw/7cf2e76ed7f100b1239fadd673fca173/image-20210325141559982.png)

#### 输出
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当数据删除成功后，payload 中的值为“deleted”；当待删除的数据不存在时，payload 中的数据为“data not exist”。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 删除成功时，variable 中的信息与上个组件相同；删除失败时，variable 在上个组件的信息基础上增加变量“err”，“err”描述失败原因。 |

- **删除成功**
删除成功后，payload 中会返回“deleted”。
![image-20210324212344222](https://main.qcloudimg.com/raw/26b1bc78f703022b0b59960a55d933d0/image-20210324212344222.png)
- **删除失败**
当删除一个不存在的数据时，payload 中的值为“data not exist”。
 ![image-20210324212558660](https://main.qcloudimg.com/raw/a0e9627e8750204436a06bdd928783f1/image-20210324212558660.png)

:::
::: 检查是否存在
#### 参数配置

| 参数 | 数据类型 | 描述                               | 是否必填 | 默认值 |
| :--- | :------- | :--------------------------------- | :------- | ------ |
| 键值 | String   | 数据的唯一标识，查找该值对应的数据。 | 是       | 无     |

#### 配置界面
![image-20210325141628439](https://main.qcloudimg.com/raw/3540f4d00303466a9c7b31fde98a7384/image-20210325141628439.png)

#### 输出
**组件输出的 message 信息如下：**

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当数据存在时，payload 中的数据为整数1；当数据不存在时，payload 中的数据为整数0。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 执行成功时，variable 中的信息与上个组件相同；执行失败时，variable 在上个组件的信息基础上增加变量“err”，“err”描述失败原因。|

- **数据存在**
当要查找的数据存在时，payload 中的值为1。
![image-20210324212920915](https://main.qcloudimg.com/raw/83627f8f69af1db1032b10eddea52945/image-20210324212920915.png)
- **数据不存在**
当数据不存在时，payload 中的值为0。
 ![image-20210324212814560](https://main.qcloudimg.com/raw/e660ecb04f4f682f640dd1ae6862d82e/image-20210324212814560.png)

:::
</dx-tabs>



## 案例

### 存储数据
1. 添加 Cache 组件。
 ![image-20210330105137767](https://main.qcloudimg.com/raw/b2b533f5551f1a6c746221e882aa97fa/image-20210330105137767.png)
2. 选择“存储”。
![image-20210330110257487](https://main.qcloudimg.com/raw/818d33faf2c86038d617721906e8a905/image-20210330110257487.png)
3. 填入键值、数据、存储时长。
![image-20210330105432960](https://main.qcloudimg.com/raw/a651032d0bf98881eb366ef60631ea79/image-20210330105432960.png)

### 读取数据
1. 选择“读取”。
![image-20210330110039545](https://main.qcloudimg.com/raw/3b322ab45b70ff174c59c716b967863a/image-20210330110039545.png)
2. 填入键值即可读到数据，下一个节点可以使用 msg.payload 访问获取到的数据。
![image-20210330110113536](https://main.qcloudimg.com/raw/389153e09aec4d2ee36f108327956572/image-20210330110113536.png)
