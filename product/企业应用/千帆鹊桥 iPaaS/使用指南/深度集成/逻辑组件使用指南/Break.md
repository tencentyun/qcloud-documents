

## 简介
Break 组件需要和 For Each 或者 While 组件搭配使用，用来中断循环，即使循环条件没有 False 或者序列还未递归完成，也会停止执行循环语句。当存在嵌套循环时，Break 将跳出所在层的循环，并开始执行下一行代码。

## 操作说明
### 参数配置
无
### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 当在 For Each 组件中使用时，Break 跳出循环后，payload 中的数据继承自 For Each 的上一个组件的 payload；当在 While 组件中使用时，跳出循环后，payload 的数据继承自 Break 的上一个组件输出的 payload。 |
| error       | 空。                                                           |
| attribute   | 在 For Each 组件中使用时，Break 跳出循环后，attribute 继承自 For Each 的上一个组件输出的 attribute；在 While 组件中使用时，Break 跳出循环后，attribute 继承自 While 的上一个组件输出的 attribute。 |
| variable    | 在 For Each 中使用时，Break 跳出循环后，variable 中的变量是 For Each 的上一个组件输出的 variable 变量加上 For Each 子流中声明的 variable 变量；在 While 组件中使用时，variable 中的变量是 While 的上一个组件输出的 variable 变量加上 For Each 子流中声明的 variable 变量。 |

## 案例
1. 添加 For Each 组件，设置要遍历的列表。
![image-20210330103356127](https://main.qcloudimg.com/raw/090db72a82539e7608d139ee464e98b8/image-20210330103356127.png)
![image-20210330103843687](https://main.qcloudimg.com/raw/e70a1f4c9a0dcc1b95edfcdd13d7344f/image-20210330103843687.png)
2. 使用 Choice 组件，并在 When 节点中添加判断条件。
![image-20210330104239081](https://main.qcloudimg.com/raw/7f5dad53bd569f7fa4d6db49f5c3ba6f/image-20210330104239081.png)
![image-20210330104158775](https://main.qcloudimg.com/raw/c6aa28ff2419c479764e0c20c15e1f36/image-20210330104158775.png)
3. 在 When 节点中添加 Break 组件，当遍历到 BMW 时，跳出 For Each 循环。
![image-20210330104546573](https://main.qcloudimg.com/raw/2de10ea66e8af9d00a12a38c3bf0aa53/image-20210330104546573.png)
