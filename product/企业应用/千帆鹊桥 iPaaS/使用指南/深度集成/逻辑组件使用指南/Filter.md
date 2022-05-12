## 简介
RecordSet Filter 组件用于操作 RecordSet，可以对输入的 RecordSet 进行过滤，并生成一个新的 RecordSet。  

## 操作配置
### 参数配置

#### 配置数据源

| 参数       | 数据类型  | 描述                         | 是否必填 | 默认值        |
| :--------- | :-------- | :--------------------------- | :------- | ------------- |
| 输入数据集 | RecordSet | RecordSet Filter 组件的数据源 | 否       | `msg.payload` |

![image-filter-1](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-1.png)

#### 配置输出字段
用于指定新生成的 RecordSet 中要包含的字段。默认将数据源的字段罗列出来，用户只需要勾选希望输出的字段即可。用户也可以给输出的 RecordSet 注入额外的字段，且字段的默认值将为空。
![image-filter-2](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-2.png)

#### 配置过滤条件
用于配置字段需要满足的条件，支持图形化配置（默认）和表达式两种方式。  
<dx-tabs>
::: 图形化配置（默认）
如果使用图形化配置（默认）方式，用户可以给数据源中的字段配置1到多个原子过滤条件，原子过滤条件间默认是逻辑“与”的关系。  
- 每个原子过滤条件都由三部分组成：字段名、操作、目标值。  
 - 字段名：数据源中的字段名。
 - 操作：支持`==,!=,>=,<=,>,<,StartWith,EndWith,Contain,In,NotIn,IsNull,IsNotNull`，详见下表。
<table>
<thead>
<tr>
<th><strong>操作</th>
<th><strong>说明</th>
</tr>
</thead>
<tbody><tr>
<td>==</td>
<td>判断相等</td>
</tr>
<tr>
<td>!=</td>
<td>判断不相等</td>
</tr>
<tr>
<td>&gt;=</td>
<td>比较大小</td>
</tr>
<tr>
<td>&lt;=</td>
<td>比较大小空</td>
</tr>
<tr>
<td>&gt;</td>
<td>比较大小空</td>
</tr>
<tr>
<td>&lt;</td>
<td>比较大小空</td>
</tr>
<tr>
<td>StartWith</td>
<td>判断字符串是否以另一个字符串开头</td>
</tr>
<tr>
<td>EndWith</td>
<td>判断字符串是否以另一个字符串结尾</td>
</tr>
<tr>
<td>Contain</td>
<td>判断字符串包含</td>
</tr>
<tr>
<td>In</td>
<td>判断是否在列表中</td>
</tr>
<tr>
<td>NotIn</td>
<td>判断是否不在列表中</td>
</tr>
<tr>
<td>IsNull</td>
<td>判断是否为空</td>
</tr>
<tr>
<td>IsNotNull</td>
<td>判断是否非空</td>
</tr>
</tbody></table>
 - 目标值：支持手动填写和列表选择两种方式。手动填写时，可以将目标值设置常量或输入表达式；列表选择时可以将目标值设置为数据源中其他字段。
![image-filter-3](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-3.png)
![image-filter-4](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-4.png)

- 原子过滤条件间默认是逻辑“与”的关系。如果用户需要配置更复杂的逻辑，可以使用编排逻辑功能。  
 - 每个原子过滤条件有一个唯一的序号，用户在编排逻辑输入框内，用序号对原子过滤条件进行逻辑编排。
 - 支持逻辑与（And）、或（Or）、非（Not）的组合，且忽略大小写。
 - 用户也可以用括号来控制优先级。
![image-filter-5](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-5.png)
 - 示例
```txt
(1 OR 2) AND NOT 3
(1 Or 2) AnD nOT 3
(1  AND 2) AND NOT 3
1 or 2 and (not 3)
not 1 or 2 or 3
not(1 or 2 or 3)
(not 1 or 2) and 3
1 and not( 2 or 3)
1or2and3or4
```
::: 
::: 表达式
当图像化配置过滤条件无法满足业务需求时，可以使用表达式输入进行补充。用户需要勾选表达式，并编辑一个返回 bool 类型的 Dataway 表达式。  
![image-filter-6](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-6.png)
表达式里面的内容示例如下：
![image-filter-7](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-7.png)

:::
</dx-tabs>


### 输入 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 默认是 payload，如果用户有配置，则采用用户配置的值            |
| error       | 空                                                           |
| attribute   | 空                                                           |
| variable    | 继承上一个组件输出 message 中的 variable 数据，在 RecordSet Filter 组件中可以操作 Variables，且不会影响输出 message 中的数据 |


### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 输出的 RecordSet，其包含的字段为用户配置的输出字段            |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 类型为 dict，继承上一个组件的 attribute                        |
| variable    | 继承上一个组件的 variable                                     |


## 案例
针对一个学生表按指定条件进行过滤，示例图如下。
![image-filter-8](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-8.png)
1. 用 RecordSet Encoder 组件创建一个学生表，包含 `name, age, address, socre, adult` 字段，并在 RecordSet Encoder 组件里面添加 SetPayload 组件，在学生表中使用表达式添加数据。
   ![image-filter-9](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-9.png)
   ![image-filter-10](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-10.png)
2. 用 Filter 组件进行过滤，生成一个新的学生表，仅包含 `name, age, address` 3个字段，并配置5个原子过滤条件，最后对原子过滤条件进行逻辑编排 `(1or2)and not3 and4 and5`，其中每个数字都代表对应序号的原子过滤条件。
   ![image-filter-11](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-11.png)
3. 在调试模式下进行单元测试，并查看结果。输出的结果将只包含一个学生的数据：`["王五", 30, "湖南省长沙市"]`
   ![image-filter-12](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-12.png)
   ![image-filter-13](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-13.png)
   ![image-filter-14](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/img/Filter/image-filter-14.png)

