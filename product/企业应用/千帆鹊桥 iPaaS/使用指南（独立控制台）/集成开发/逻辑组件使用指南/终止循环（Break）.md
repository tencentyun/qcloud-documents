## 简介

终止循环（Break）组件需要和遍历（For Each）或者条件循环（While）组件搭配使用，用来中断循环，即使序列还未递归完成或者循环条件没有 False，也会停止执行循环语句。当存在嵌套循环时，终止循环组件将跳出自己所在层的循环，并开始执行下一个组件。

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
| payload     | <ul><li>当在“遍历”组件中使用时，终止循环后，payload 中的数据继承自“遍历”的上一个组件的 payload。</li><li>当在“条件循环”组件中使用时，终止循环后，payload 的数据继承自终止循环的上一个组件输出的 payload。</li></ul> |
| error       | 空                                                           |
| attribute   | <ul><li>在“遍历”组件中使用时，终止循环后，attribute 继承自“遍历”的上一个组件输出的 attribute。</li><li>在“条件循环”组件中使用时，终止循环后，attribute继承自“条件循环”的上一个组件输出的 attribute。</li></ul> |
| variable    | <ul><li>在“遍历”中使用时，终止循环后，variable 中的变量是“遍历”的上一个组件输出的 variable 变量加上“遍历”子流中声明的 variable 变量。</li><li>在“条件循环”组件中使用时，variable 中的变量是“条件循环”的上一个组件输出的 variable 变量加上“条件循环”子流中声明的 variable 变量。</li></ul> |

## 案例

1. 添加“遍历”组件，设置要遍历的列表。
2. 使用“条件判断”组件，并在“条件分支”中添加判断条件。
3. 在“条件分支”子节点中添加“终止循环”组件，当遍历到“BMW”时，跳出遍历流程。
![终止循环示例](https://qcloudimg.tencent-cloud.cn/raw/bfcfcce5eebdad85b4bd7ac3ed9afb85.jpg)
