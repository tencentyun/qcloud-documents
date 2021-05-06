

## 简介
Break 组件需要和 For Each 或者 While 组件搭配使用，用来中断循环，即使循环条件没有 False 或者序列还未递归完成，也会停止执行循环语句。当存在嵌套循环时，Break 将跳出所在层的循环，并开始执行下一行代码。

## 操作说明
### 参数配置
无
### 输出
组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                        |
| error       |  执行成功后，error 为空；<br>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 继承上个组件的 variable 信息。                                   |


## 案例
1. 添加 For Each 组件，设置要遍历的列表。
![image-20210330103356127](https://main.qcloudimg.com/raw/090db72a82539e7608d139ee464e98b8/image-20210330103356127.png)
![image-20210330103843687](https://main.qcloudimg.com/raw/e70a1f4c9a0dcc1b95edfcdd13d7344f/image-20210330103843687.png)
2. 使用 Choice 组件，并在 When 节点中添加判断条件。
![image-20210330104239081](https://main.qcloudimg.com/raw/7f5dad53bd569f7fa4d6db49f5c3ba6f/image-20210330104239081.png)
![image-20210330104158775](https://main.qcloudimg.com/raw/c6aa28ff2419c479764e0c20c15e1f36/image-20210330104158775.png)
3. 在 When 节点中添加 Break 组件，当遍历到 BMW 时，跳出 For Each 循环。
![image-20210330104546573](https://main.qcloudimg.com/raw/2de10ea66e8af9d00a12a38c3bf0aa53/image-20210330104546573.png)
