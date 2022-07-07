
## 简介

遍历（For Each）是循环控制组件，类似于编程语言中的 for/foreach，在遍历组件中可以配置子流，对指定的数据集中每个元素执行子流处理逻辑。

## 操作说明

### 参数配置

| 参数  | 数据类型                 | 描述                                                                                                                                                                                | 是否必填 | 默认值         |
|:----|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----|-------------|
| 数据集 | string、list、dict、int | 待遍历的数据集。<ul><li>当类型为 string 时，遍历字符串的每个字符；</li><li>当类型为 list 时，遍历 list 的每个元素；</li><li>当类型为 dict 时，遍历 dict 中的 value；</li><li>当数据集类型为 int 时，例如3；实际遍历的数据集为[0,1,2]。</li> </ul>                                              | 是    | 无           |
| 计数器 | string               | 计数器是一个变量，该变量存储了当前的迭代次数，从0开始。<br/>这里填入变量名称，msg.vars.get('#计数器变量#')即可使用；<br/>例如：当计数器变量使用默认值 counter时<br/>第1次循环，msg.vars.get('counter')值为0。<br/>第2次循环，msg.vars.get('counter')值为1。        | 是    | counter     |
| 根信息 | string               | 根信息同样是一个变量，这里填入变量名称，根信息中保存了主流的 message 信息。<br/>msg.vars.get('#根信息名称#').payload 即可访问主流的payload数据。<br/>当使用默认值 rootMessage 时，使用 msg.vars.get('rootMessage').payload 即可在遍历的子流中访问主流的 payload 数据。 | 是    | rootMessage |

>?通常情况下，配置数据集即可。

### 配置界面

![img.png](https://qcloudimg.tencent-cloud.cn/raw/187d482281e50c13a36a4e6649768024.png)

### 数据预览

| 预览字段    | 数据类型 | 描述                               |
|:--------|:-----|:---------------------------------|
| payload | any  | 每次遍历的输入值，属于数据集的其中一个元素            |
| index   | int  | 每次遍历的位置，代表当前输入值在数据集中的下标位置，从0开始计数 |

![img_1.png](https://qcloudimg.tencent-cloud.cn/raw/2e2ae435ff91a34d41077714a372cad4.png)

数据预览的内容仅为子流可见，子流中的组件可以直接使用遍历组件的 Payload 和 index，如图所示：
![img_2.png](https://qcloudimg.tencent-cloud.cn/raw/0dbd10e4c31c27308ea64e86660a9a34.png)

### 输入到子流中的message

| message属性 | 值                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| payload   | 数据集中的元素，例如待迭代的数据集为[1,2,3]<br/>第一次循环，子流中payload的数据为1<br/>第二次循环为2<br/>当迭代的数据集为dict类型{"key":"key1", "value":"value1"}<br/>第一次循环，子流中的payload为value1<br/>第二次为value2            |
| error     | 空                                                                                                                                                                         |
| attribute | 空                                                                                                                                                                         |
| variable  | 继承主流中的variable数据，同时新增两个变量，一个是计数器，一个是根信息，若用户使用默认值，可使用表达式msg.vars.get('counter')和msg.vars.get('rootMessage')访问。<br/>若For Each中使用了Set Variable，则在子流执行过程中，新增的变量也会添加到varaible中 |

### 输出

遍历组件不会改变 Message 内容，后续节点只能感知到变量的变化。

## 案例

使用 For Each 组件遍历列表，为列表中的元素添加序号及前缀。

1. 初始化变量 listResult。
![img_4.png](https://qcloudimg.tencent-cloud.cn/raw/5f11f33f27d86776cfbe5924fcb2b5f6.png)
2. 添加遍历并配置组件。
![img_5.png](https://qcloudimg.tencent-cloud.cn/raw/ebeb4cbd6a8946beb07715598233c6d6.png)
3. 遍历的子流中设置变量, 给每个遍历的元素值添加前缀（元素的下标位置），并添加到 listResult 变量。
![img_6.png](https://qcloudimg.tencent-cloud.cn/raw/aea938a5c6ffcb16d90d72b8084cd318.png)
4. 单元测试输出效果。
![img_7.png](https://qcloudimg.tencent-cloud.cn/raw/8ad401315162662ed6368dd5d9e5eb10.png)
