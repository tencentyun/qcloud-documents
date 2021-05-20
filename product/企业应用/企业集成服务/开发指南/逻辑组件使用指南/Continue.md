

## 简介
 
Continue 组件类似于 Break 组件，搭配 For Each 和 While 组件使用。Continue 的作用是跳出当前循环，执行下一次循环。


## 操作配置

### 参数配置
无

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 在 For Each 组件中，Continue 跳出当前循环后，payload 的值为下一次循环遍历的数据。在 Whlie 组件中，Continue 跳出循环后，payload 继承自 Continue 的上一个组件输出的 payload。 |
| error       | 无。                                                           |
| attribute   | 在 For Each 组件中使用时，Continue 跳出循环后，attribute 继承自 For Each 的上一个组件输出的 attribute；在 While 组件中使用时，Continue 跳出循环后，attribute 继承自 While 的上一个组件输出的 attribute。 |
| variable    | 在 For Each 中使用时，Continue 跳出循环后，variable 中的变量继承自 Continue 的上一个组件输出的 variable 变量；在 While 组件中使用时，variable 中的变量继承自 Continue 的上一个组件输出的 variable 变量。 |

## 案例
在本案例中，我们使用 For Each 对列表中的奇数求和，遇到偶数，则使用 Continue 跳出当次循环。
1. 添加 For Each 组件，填入要遍历的集合[1,2,3,4,5]。
   ![image-20210330141940166](https://main.qcloudimg.com/raw/cfccb38bce1966da46ea62e40d6beb8f/image-20210330141940166.png)
   ![image-20210330142019571](https://main.qcloudimg.com/raw/6adafadd748011a95d0fdaca4be55add/image-20210330142019571.png)
2. 添加 Choice 组件，在 When 节点中对数据进行筛选。
![image-20210330143531318](https://main.qcloudimg.com/raw/4ed5854bb649b2acb46e49a01fa60a1e/image-20210330143531318.png)
![image-20210330143502312](https://main.qcloudimg.com/raw/3e34ed6088566f617abfe118f539a9aa/image-20210330143502312.png)
3. 在 When 节点中加入 Continue 节点。
![image-20210330143642462](https://main.qcloudimg.com/raw/e6511691d3ee441e4c04ba60df9a8052/image-20210330143642462.png)
