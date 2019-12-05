TOP N 排名意为从研究对象中得到所需的N个数据，并从排序列表中选取最大或最小的 N 个数据。

## 1. 添加组件
从右侧组件窗格中，拖拽<img src="https://main.qcloudimg.com/raw/7535cbbb12ca85a0ad09515a0f70f6a1.png"  style="margin:0;">柱状图图表组件到编辑区。

## 2. 绑定数据
从左侧数据列表中，拖拽维度“产品名称”到图表组件 Y 轴，拖拽度量“销售额”到图表组件 X 轴，生成柱图。

![](https://main.qcloudimg.com/raw/a13df7d5b18b47acc9c0e343dc580a1d.png)
## 3. 设置高级排序
1. 在绑定区域，打开“产品名称”的操作菜单，选择【更多排序】>【高级排序】。

![](https://main.qcloudimg.com/raw/f00ef16592a66c03869d9670f74a5f04.png)

2. 在高级排序对话框中，选择【降序】，【聚合列】；选择列为“销售额”，聚合方式为“总和”，即系统将根据产品的总销售额来进行排名。

![](https://main.qcloudimg.com/raw/68e7d341a2ae81ae3e6039ca688c8a67.png)

3. 在 TOP N 区域，输入数字5，即排名后，系统只展现销售额最高的五种产品。单击【确定】，最终得到如下 TOP 5 图表。

![](https://main.qcloudimg.com/raw/473a6da8324c5effe51dd7b10b96918c.png)
