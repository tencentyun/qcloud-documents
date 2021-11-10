## 简介
Table 组件是一个内置的表结构组件，提供基于 Table 的增删改查等操作，仅用于操作 RecordSet。  

## 配置

| 参数   | 数据类型 | 描述             | 是否必填 | 默认值 |
| :----- | :------- | :--------------- | :------- | ------ |
| 表名   | string   | 表名             | 是       |    -    |
| 列信息 | struct   | 表的列信息       | 是       |  -      |
| depend | struct   | 列之间的依赖关系 | 否       |   -     |

### 列信息
列信息支持 int、float、bool、string、decimal、data、time、datatime 八种类型，其中 string 类型需要配置长度信息，decimal 类型需要配置精度、小数位信息。
存在如下限制：
- 必须配置主键且只能配置一个。
- 索引只能配置一个。

**示例**
![image-filter-1](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/a9e4a145bdd7c0d301fcf09004e4e1fb.png)

### 外键
外键用于指定列与列之间的依赖信息，外健字段表示本 table 与表内字段的依赖关系，关联表表示与应用内其他 table 的字段存在依赖关系，关联表字段用于选取关联表中存在依赖关系的字段。
**示例**
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/4e7b8ff84d0fa7084593e4bfd1309841.png)

## 操作说明
Table 目前支持查询、插入、合并、删除、计算差值等操作。
<dx-tabs>
::: 查询
#### 参数配置

| 参数     | 数据类型 | 描述                    | **是否必填** | **默认值** |
| -------- | -------- | ----------------------- | ------------ | ---------- |
| 过滤条件 | list     | 查询过滤条件            | 是           |        -    |
| 输出字段 | list     | 选择要输出的字段        | 是           |      -      |
| 分区数   | int      | 分数数量                | 是           |      -      |
| 开启缓存 | bool     | 对输出 RecordSet 是否缓存 | 是           |     -       |

![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/560003461dca9005705c38ec76416a1b.png)

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
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/560003461dca9005705c38ec76416a1b.png)
3. 执行操作，输出结果如下：
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/287892d787c93fe939c3bbdabb243a43.png)
:::
::: 插入
#### 参数配置

| 参数       | 数据类型      | 描述                                                         | **是否必填** | **默认值** |
| ---------- | ------------- | ------------------------------------------------------------ | ------------ | ---------- |
| 忽略错误   | bool          | 忽略插入错误                                                 | 否           | true       |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload                 | 是           |   -         |
| 字段校准   | list          | 对输入数据集进行字段校准                                     | 否           |     -       |
| 字段映射   | enum          | 字段映射，数据表字段和 RecordSet 类型数据字段的映射，插入数据表字段的值为 RecordSet 类型数据字段的值 | 是           |         -   |

![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/d526c1928541ae32f4015d059a4a21de.png)

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
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/d526c1928541ae32f4015d059a4a21de.png)
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

![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/47548a63f235d0b25b3059c7a55935bf.png)

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
2. 配置过滤条件、字段映射等信息。
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/47548a63f235d0b25b3059c7a55935bf.png)
3. 执行操作，如果成功，则输出 payload 为上一个组件的 payload。
:::
::: 删除
#### 参数配置

| 参数       | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| ---------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |       -     |
| 字段校准   | list          | 对输入数据集进行字段校准                     | 否           |       -     |
| 过滤条件   | list          | 删除的过滤条件                               | 是           |       -     |

![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/1ced4d468aee7f7acaf79c29c5b2a397.png)

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
2. 配置字段映射等信息。
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/1ced4d468aee7f7acaf79c29c5b2a397.png)
3. 执行操作，如果成功，则输出 payload 为上一个组件的 payload。
:::
::: 计算差值
#### 参数配置

| 参数       | 数据类型      | 描述                                         | **是否必填** | **默认值** |
| ---------- | ------------- | -------------------------------------------- | ------------ | ---------- |
| 输入数据集 | RecordSet 类型 | 输入数据集，若未填写，默认为 message 的 payload | 是           |    -        |
| 字段校准   | list          | 对输入数据集进行字段校准                     | 否           |     -       |
| 输入模式   | enum          | 全量、增量                                    | 是           |     -       |
| 主键配置   | list          | 计算时主键的映射关系                         | 是           |      -      |
| 比对字段   | list          | 计算时需要根据主健是否相当                   | 是           |   -         |
| 开启缓存   | bool          | 对输出 RecordSet 是否缓存                      | 是           |  -          |

![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/514ca9087fd0651fb72cfa0beb9ee482.png)

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
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/514ca9087fd0651fb72cfa0beb9ee482.png)
3. 执行操作，输出如下：
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Table/4506e9bfda8b178748d5a2c9abcc5873.png)
:::
</dx-tabs>
