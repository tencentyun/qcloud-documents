
本文为您介绍通过控制台使用逻辑编辑器的案例。

## 操作步骤
1. 登录 [腾讯云图控制台](https://console.cloud.tencent.com/tcv)，选择对应大屏，向画布中添加 Tab 列表和基础柱状图。
![](https://main.qcloudimg.com/raw/5e99ef5490cd2a798274adf30c09dec8.gif)
2. 修改 Tab 列表，使得列表项变为**显示**、**隐藏**，并设置为默认**显示**。
![](https://main.qcloudimg.com/raw/cc09b64a58ec213b41e73b0336b5e6ea.gif)
3. 分别右键单击 Tab 列表和通用标题组件，单击**导出到逻辑编辑器**。
<img src="https://main.qcloudimg.com/raw/2756b35355feb17b9c9f41719dcfe2cf.png"  style="zoom:55%;"><br>
也可以使用快捷方式导出到逻辑编辑器。
<img src="https://main.qcloudimg.com/raw/29e85721694da72a35fe45387cc8e31e.png"  style="zoom:45%;">
4. 单击左上角的**逻辑编辑器**。
<img src="https://main.qcloudimg.com/raw/7c681543989b5c48ba1a61594ad0cbfb.png"  style="zoom:45%;"><br>
5. 在逻辑编辑器中将已导入组件拖动至画布。
![](https://main.qcloudimg.com/raw/cec8d9122b0231ef6fee19744cccfb43.gif)
6. 将分支判断节点拖动到画布中，并创建连线。
![](https://main.qcloudimg.com/raw/e9f320c122d7b2bcbdce28d26f4a1788.gif)
7. 实现分支判断的逻辑，先查看 Tab 列表 当 Tab 选中变更时 事件传递的数据。这里查看后可以看到该事件传递的数据是选中的数据项，这里我们根据之前第2步设置的变量，将判断函数做修改，当 `data.value === 'show'` 成立时，分支判断的满足事件将被调用。
8. 最后预览查看逻辑编辑器的运行效果。
![](https://main.qcloudimg.com/raw/67b857b4137b0a1de0654d9d38d571ee.gif)

