## 简介

跳过循环（Continue）组件类似于终止循环组件，搭配遍历和条件循环组件使用。跳过循环的作用是跳出当前循环，执行下一次循环。

## 操作指引

### 连接说明

无

### 参数配置

无

### 数据预览

无

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | <ul><li>在“遍历”组件中，“跳过循环”后，payload 的值为下一次遍历的数据。</li><li>在“条件循环”组件中，“跳过循环”后，payload 继承自“跳过循环”的上一个组件输出的 payload。</li></ul> |
| error       | 无                                                           |
| attribute   | <ul><li>在“遍历”组件中使用时，“跳过循环”后，attribute 继承自“遍历”的上一个组件输出的 attribute。</li><li>在“条件循环”组件中使用时，“跳过循环”后，attribute 继承自“条件循环”的上一个组件输出的 attribute。</li></ul> |
| variable    | <ul><li>在“遍历”中使用时，“跳过循环”后，variable 中的变量继承自“跳过循环”的上一个组件输出的 variable 变量。</li><li>在“条件循环”组件中使用时，variable 中的变量继承自“跳过循环”的上一个组件输出的 variable 变量。</li></ul> |

## 案例

在本案例中，我们使用 For Each 对列表中的奇数求和，遇到偶数，使用 Continue 跳出当次循环。
1. 添加 For Each 组件，填入要遍历的集合 [1,2,3,4,5]。
2. 添加 Choice 组件，在 When 节点中对数据进行筛选。
3. 在 When 节点中加入 Continue 节点。
![](https://qcloudimg.tencent-cloud.cn/raw/4d1e4ee5b19258efe978f4f271ef6780.png)
