本文为您详细介绍在 CODING 中的 Backlog 与迭代规划功能。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击【立即使用】进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 单击菜单栏中的【项目协同】>【待规划】，进入未规划页面。

## 功能介绍

在 CODING 项目协同的待规划页面您可以：
- 维护**未完成并且未规划进迭代**的事项，即维护 Backlog 。
- 管理**未完成**的迭代

![](https://main.qcloudimg.com/raw/5e2dad75ce73f78169c567125bfdcc1e.png)

在未规划页面我们推荐的最佳使用流程如下：

- 产品负责人在 Backlog 中录入和调整需求顺序。
- 迭代开始前团队评估 Backlog 中排序靠前的需求。
- 创建迭代，将需求纳入到迭代中。
- 开始迭代。
- 迭代完成后，该迭代将不会显示在未规划页。

## 维护 Backlog

Backlog 页面展示未完成并且未规划到迭代中的事项，可通过拖拽事项上下排序，并且支持创建事项。

### 查看 Backlog 列表

选择【项目协同】>【待规划】，进入未规划页面。
![](https://main.qcloudimg.com/raw/c1a0bbc455bc8f95c6a28f41d695ff90.png)
Backlog 列表展示属性如下：
![](https://main.qcloudimg.com/raw/c1527f97144a01c0bc7a4dcc1d43cf2a.jpg)

- 事项类型，包含需求、任务和缺陷
- 事项引用 ID
- 优先级
- 处理人
- 子任务数（若有）
- 所属史诗（若有）
- 故事点（若有）

在事项列表中单击任意事项，可在右侧查看到指定事项的详情页：
![](https://main.qcloudimg.com/raw/e4d97e29d8f6c483fa65156c716b2403.png)

### Backlog 列表排序

事项列表支持拖拽排序，新创建的事项默认排在列表最后。单击事项行，就可以对该行进行拖拽。
![](https://main.qcloudimg.com/raw/b75279080cfb12a148198958c50a163b.jpg)

>! 在旧项目中首次使用 Backlog ，会按照创建时间逆序初始化顺序。

### 创建事项

在 Backlog 下方可创建需求、任务和缺陷。
![](https://main.qcloudimg.com/raw/2cf2f9a141b2627dc8abf58bf2d07d2f.jpg)
可使用标题快捷创建事项，也可选择【完整创建】形式弹窗创建事项。
![](https://main.qcloudimg.com/raw/ac369005ad484b3eb7c68029dc7b2c92.jpg)

## 管理未完成迭代

未完成迭代区域展示当前项目下所有未完成的迭代，包含未开始和进行中的迭代。可在当前区域直接创建新迭代。

### 查看未完成迭代列表
选择【项目协同】>【待规划】，进入未规划页面。
![](https://main.qcloudimg.com/raw/bf116ac7efa6007c526f23441d902504.png)
迭代列表中，每个迭代可展开和收缩事项列表。默认情况下当前页面只展示第一个迭代，其他迭代收缩起来。每个迭代展示的基本信息如下：

- 迭代名称
- 迭代事项数量
- 迭代状态
- 开始时间
- 结束时间
- 总故事点数（若有）

每个迭代内包含的事项列表属性与 Backlog 中一致，可通过拖拽形式调整迭代内事项的顺序。

### 迭代操作

您可对每个迭代进行的操作包括：
- 收缩、展开迭代下事项列表。
![](https://main.qcloudimg.com/raw/b18484ea77894fb716509f006942309c.jpg)
- 单击迭代后的编辑按钮，选择【在新标签页打开】，即可在新页面打开迭代。
![](https://main.qcloudimg.com/raw/30897826bc4b8999693063a698a4a11f.png)
- 开始迭代或完成迭代。
- 编辑迭代。
- 删除迭代。
![](https://main.qcloudimg.com/raw/13557e1cd721ce20f62ed54f79f1004a.jpg)
- 创建事项。
![](https://main.qcloudimg.com/raw/d6f9dd4401b0dd8d3335c148f641ba86.jpg)

### 规划迭代

在未规划页可进行迭代规划。 通过将 Backlog 中的事项拖进未完成迭代中或将迭代内的事项拖动到另一个迭代内来进行规划。
![](https://main.qcloudimg.com/raw/3658f78fea21150dc12368f82a16342b.jpg)
**您还可以批量拖动事项进行迭代规划**，根据右上角 TIPS 提示（不同操作系统提示不同）单击事项可选中多条，选中后的事项呈蓝色高亮，此时拖拽高亮的事项可同时将它们加入到指定迭代。
![](https://main.qcloudimg.com/raw/198d1a979f39439a8580f5fb8cd9e989.png)
