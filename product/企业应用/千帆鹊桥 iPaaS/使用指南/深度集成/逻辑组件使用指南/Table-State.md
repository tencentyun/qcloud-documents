## 简介
Table 组件是由 iPaaS 提供存储的内置表结构组件，提供基于 Table 的增删改查等操作，仅用于操作 RecordSet。  


一般情况前一个节点为 RecordSet Encoder，将数据封装成 RecordSet，通过 Table 组件实现数据的查询、插入、合并、删除、比对等。使用 Table 组件时选择合适的操作 > 配置连接 > 配置操作。

## 连接配置
选择通用存储中创建的表名，此表为操作的目标表。

| 参数   | 数据类型 | 描述             | 是否必填 | 默认值 |
| :----- | :------- | :--------------- | :------- | ------ |
| 表名   | string   | 表名             | 是       |    -    |

## 操作说明
Table 组件包含插入、查询、合并、删除、比对操作。
<dx-tabs>
::: 查询
#### 参数配置

| 参数     | 数据类型 | 描述                    | **是否必填** | **默认值** |
| -------- | -------- | ----------------------- | ------------ | ---------- |
| 过滤条件 | list     | 查询过滤条件            | 是           |        -    |
| 输出字段 | list     | 选择要输出的字段        | 是           |      -      |
| 分区数   | int      | 分数数量                | 是           |      -      |
| 开启缓存 | bool     | 对输出 RecordSet 是否缓存 | 是           |     -       |

查询界面如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/29a1f0ac902ba3240d697ce0c974c8ff.png" width="560px">


####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为查询到的数据集构成的 RecordSet；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 配置过滤条件、输出字段等信息。
<img src="https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/560003461dca9005705c38ec76416a1b.png" width="560px">
3. 执行操作，输出结果如下：
<img src="https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/287892d787c93fe939c3bbdabb243a43.png" width="560px">

:::
::: 插入
#### 参数配置

| 参数       | 数据类型      | 描述                                                         | **是否必填** | **默认值** |
| ---------- | ------------- | ------------------------------------------------------------ | ------------ | ---------- |
| 忽略错误   | bool          | 忽略插入错误                                                 | 否           | true       |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload                 | 是           |   -         |
| 字段校准   | list          | 对输入数据集进行字段校准                                     | 否           |     -       |
| 字段映射   | enum          | 字段映射，数据表字段和 RecordSet 类型数据字段的映射，插入数据表字段的值为 RecordSet 类型数据字段的值 | 是           |         -   |

默认插入界面如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b41835519946c3ac1debd43db2c826a4.png" width="560px">

>?
>- 如果前一个节点输出 RecordSet，Table 将自动感知数据结构，并将来源字段与目标表字段根据同名映射自动进行映射。
>- 在字段映射后方有 schema 维护按钮，可点击查看、管理输入的 schema 在 schema 维护面板中可进行手工维护 schema 的字段信息，当前一节点输出的 schema 发生了调整，可在 schema 手工刷新与前一节点输出的 schema 保持一致，同时将根据同步映射原则进行重新映射（将覆盖上次的映射）。
><img src="https://qcloudimg.tencent-cloud.cn/raw/5883606eea0257c6158ebdeba1df4fe6.png" width="560px">
![]()


####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为上一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 配置字段映射等信息。
<img src="https://qcloudimg.tencent-cloud.cn/raw/04d779ca0c74beda6031a3e82929f86f.png" width="560px">
3. 执行操作，如果成功，则输出 payload 为上一个组件的 payload。

:::
::: 合并
#### 参数配置

| 参数       | 数据类型      | 描述                                                         | **是否必填** | **默认值** |
| ---------- | ------------- | ------------------------------------------------------------ | ------------ | ---------- |
| 只执行插入 | bool          | 数据不存在时执行插入操作                                     | 是           | false      |
| 只执行更新 | bool          | 数据存在时执行更新操作                                       | 是           | false      |
| 忽略错误   | bool          | 忽略插入错误                                                 | 否           | true       |
| 输入数据集 | RecordSet类型 | 输入数据集，若未填写，默认为 message 的 payload                 | 是           | -           |
| 字段校准   | list          | 对输入数据集进行字段校准                                     | 否           |     -       |
| 过滤条件   | list          | 合并的过滤条件                                               | 是           |    -        |
| 字段映射   | enum          | 字段映射，数据表字段和 RecordSet 类型数据字段的映射，插入数据表字段的值为 RecordSet 类型数据字段的值 | 是           |   -         |

![](https://qcloudimg.tencent-cloud.cn/raw/fc924f87080e6c37d45c94d9c493508e.png)

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为上一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 设置输入数据集，默认为return msg.payload。
3. 配置过滤条件，字段映射等信息。
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/47548a63f235d0b25b3059c7a55935bf.png)

![](https://qcloudimg.tencent-cloud.cn/raw/21971263dc557853e51d3c28097ae87f.png)
3. 执行操作，如果成功，则输出 payload 为上一个组件的 payload。
:::
::: 删除
#### 参数配置

| 参数       | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| ---------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |       -     |
| 字段校准   | list          | 对输入数据集进行字段校准                     | 否           |       -     |
| 过滤条件   | list          | 删除的过滤条件                               | 是           |       -     |

![](https://qcloudimg.tencent-cloud.cn/raw/a81c393ebb12ca8f31d153e2edb1904b.png)

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为上一个组件的 payload；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为dict类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 配置删除逻辑等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/af3d80c20199e9f21956812c3d9cf478.png)
3. 执行操作，如果成功，则输出 payload 为上一个组件的payload。
:::
::: 比对
#### 参数配置

| 参数       | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| ---------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |    -        |
| 字段校准   | list          | 对输入数据集进行字段校准                     | 否           |     -       |
| 输入模式   | enum          | 全量、增量                                    | 是           |     -       |
| 主键配置   | list          | 计算时主键的映射关系                         | 是           |      -      |
| 比对字段   | list          | 计算时需要根据主健是否相当                   | 是           |   -         |
| 开启缓存   | bool          | 对输出 RecordSet 是否缓存                      | 是           |  -          |

![](https://qcloudimg.tencent-cloud.cn/raw/8f2fef2dea9b9324ef87d07e1095eabd.png)

####  输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 执行成功后，payload 为计算差值后生成的 RecordSet；执行失败后，payload 为空 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”元素：“Code”表示错误类型，“Description”表示错误具体信息 |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

输出 RecordSet 中 op_type 字段取值为 Add、Modify、Deleted，分别表示新增、修改、删除。

#### 案例
1. 新建连接器或选择已创建的连接器。
2. 配置输入模式、主键配置、比对字段等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/4ce73c521209cb22260ffddd8130a66a.png)
3. 执行操作，输出如下：
<img src="https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/4506e9bfda8b178748d5a2c9abcc5873.png" width="560px">
:::
</dx-tabs>
