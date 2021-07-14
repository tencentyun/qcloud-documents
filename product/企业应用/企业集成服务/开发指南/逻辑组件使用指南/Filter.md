## 简介
Filter 组件仅用于操作 [RecordSet]()。它可以对输入的 RecordSet（一种表单数据）进行过滤，并生成一个子集。  

## 操作配置

### 基本配置

| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值      |
| :--------- | :------- | :----------------------------------------------------------- | :------- | ----------- |
| 输入数据 | RecordSet      | Filter 组件的数据源                              | 否       | `msg.payload`           |

#### 配置界面
![image-filter-1](https://main.qcloudimg.com/raw/f7cefc66bed5a271da8f1e7815042be0/image-filter-1.png)

### 字段选择
用于指定新生成的 RecordSet 中要包含的字段。默认将数据源的字段进行罗列，用户只需要勾选希望输出的字段即可。用户也可以给输出的 RecordSet 注入一些额外的字段，字段的默认值将为空。
![image-filter-2](https://main.qcloudimg.com/raw/d3f2b7c481f2efb1bfedd5efaa56cfd6/image-filter-2.png)

### 过滤条件
用于配置字段需要满足的条件，支持图形化配置（默认）和表达式两种方式。  

#### 图形化配置（默认）
如果使用默认方式，用户可以给数据源中的字段配置1到多个原子过滤条件，原子过滤条件间默认是逻辑“与”的关系。  
- 每个原子过滤条件都由三部分组成：字段名、操作、目标值。  
 - 字段名：数据源中的字段名。
 - 操作：支持 `==,!=,>=,<=,>,<,StartWith,EndWith,Contain,In,NotIn,IsNull,IsNotNull`，详见下表。
<table>
<thead>
<tr>
<th>操作</th>
<th>说明</th>
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
![image-filter-3](https://main.qcloudimg.com/raw/ea031b6d889ca6da5875555e8e21d113/image-filter-3.png)
![image-filter-4](https://main.qcloudimg.com/raw/9a99e8fd95bf8135b2a66b5a5ba466cd/image-filter-4.png)
- 原子过滤条件间默认是逻辑“与”的关系。如果用户需要配置更复杂的逻辑，可以使用编排逻辑功能。  
 - 每个原子过滤条件有一个唯一的序号，用户在编排逻辑输入框内，用序号对原子过滤条件进行逻辑编排。
 - 支持逻辑与（And）、或（Or）、非（Not）的组合，且忽略大小写。
 - 用户也可以用括号来控制优先级。
![image-filter-5](https://main.qcloudimg.com/raw/601292f4ef7e953d420c343b2bce66dc/image-filter-5.png)
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

#### 表达式
如果使用表达式，则需要编辑一个返回 bool 类型的表达式。
![image-filter-6](https://main.qcloudimg.com/raw/8fe7776a0f2af0c4a9dad181afd5d468/image-filter-6.png)
表达式里面的内容示例：
![image-filter-7](https://main.qcloudimg.com/raw/a523215b6d5eaa218d974fdf49777546/image-filter-7.png)


## 案例
针对一个学生表按指定条件进行过滤，示例图如下。
![image-filter-8](https://main.qcloudimg.com/raw/60d30469ee96de1e6c4f8546383dae6a/image-filter-8.png)
1. 用 RecordSet Encoder 组件创建一个学生表，包含`name, age, address, socre, adult`字段，然后在 RecordSet Encoder 组件里添加 SetPayload 组件，用表达式给学生表添加一些数据。
![image-filter-9](https://main.qcloudimg.com/raw/8aaee48533e8e08584b9f90398f4eabf/image-filter-9.png)
![image-filter-10](https://main.qcloudimg.com/raw/56030c67630074aee8488fba756eae02/image-filter-10.png)
2. 用 Filter 组件进行过滤，生成一个新的学生表，仅包含`name, age, address`3个字段，然后配置5个原子过滤条件，最后对原子过滤条件进行逻辑编排`(1or2)and not3 and4 and5`，其中每个数字都代表对应序号的原子顾虑条件。
![image-filter-11](https://main.qcloudimg.com/raw/a17ff2eb98d6b970b883ff6d7239b8c1/image-filter-11.png)
3. 在调试模式下进行单元测试，并查看结果。输出的结果将只包含一个学生的数据：`["王五", 30, "湖南省长沙市"]`。
![image-filter-12](https://main.qcloudimg.com/raw/4c4f06a829c08b616159514dd975c2be/image-filter-12.png)
![image-filter-13](https://main.qcloudimg.com/raw/400b255d9dd60830aee48c4571ed31b8/image-filter-13.png)
![image-filter-14](https://main.qcloudimg.com/raw/e2774ac33ffb0adfa205e100e94ef33b/image-filter-14.png)

