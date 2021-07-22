此表格重点介绍客户。

现在，您已经通过创建维度、度量和可视化获得了足够的经验，所以不再需要详细的步骤了。唯一的例外是在属性面板中进行更改时有所不同。如果您需要有关到目前为止学到了什么的提醒，可以参考前面的主题。

编辑时的 Customer Details 工作表
![](https://main.qcloudimg.com/raw/d712fd953a910e0657c90062a890d23a.png)
 
## 添加筛选器窗格
1.	添加筛选器窗格 Period。
2.	使用维度 Manager 添加新的筛选器窗格。

## 添加散点图
散点图使用 Customer 维度以及 Sales 和 Quantity 度量。您需要创建 Quantity 度量，然后将其另存为主条目。使用 Sales Qty 字段和 Sum 聚合函数。由于 Sales Qty 字段包含两个词，因此需要在表达式中使用方括号将其括起来：[Sales Qty]。表达式应当和以下相似：Sum ([Sales Qty])
在属性面板中的外观底部对 Y 轴和 X 轴使用范围设置，以排除这些轴的负值部分。
您可能已注意到有两个度量添加到了散点图中。散点图用于可视化两个或三个度量之间的关系。在此例中，所比较的度量是 Sales 和 Quantity。每一个气泡代表一个 Customer 维度值。应当将可视化命名为 Customer Sales and Quantity。

## 添加 Customer KPIs 表格
名为 Customer KPIs 的表格使用维度 Customer。

您可从属性面板中的数据向表格添加更多列：使用可用作主条目的度量 Sales、Quantity 和 Margin Percent。按照屏幕截图中的相同顺序进行添加。

对于最后两列，需要创建剩余度量：
- 对于 # of Invoices 度量，使用以下表达式：
```
Count (Distinct [Invoice Number])Copy
```
- 对于 Average Sales per Invoice 度量，使用以下表达式：
```
Sum(Sales)/Count(Distinct [Invoice Number])Copy
```

>?两个表达式中要使用限定符 Distinct。通过使用 Distinct，您可以确保只计算一次发票编号，即使它在数据源中出现多次也是如此。Distinct 会检索出唯一的编号。请注意，Distinct 在字段名称前必须跟一个空格。

### 调整数字格式
1.	在属性面板中，单击【数据】。
2.	单击【Sales】并将“数字格式”设置为货币。
3.	单击此度量以将其关闭。
4.	单击【Quantity】并将“数字格式”设置为数字 (1,000)。
5.	单击此度量以将其关闭。
6.	单击【Margin Percent】并将“数字格式”设置为数字 (12.3%)。
7.	单击此度量以将其关闭。
8.	单击【Average Sales per Invoice】并将“数字格式”设置为货币。
9.	单击此度量以将其关闭。

## 将 Customer KPIs 表格转换为透视表
将表格“客户 API”转换为透视表可让您包括更多维度或度量，并重新整理它们以便通过有用的方式更灵活地分析数据。

透视表将维度和度量显示为表格中的行和列。在透视表中，您可以同时通过多个度量并以多个维度分析数据。可以重新排列度量和维度以获取不同的数据视图。在行与列之间来回移动度量和维度的活动称为“透视”。

透视表的一个优势是互换性，即能够将行条目移动到列并将列条目移动到行。这种灵活性非常强大，可让您重新排列数据并获得同一数据集的多个不同视图。根据您要关注的内容，可以移动维度和度量以提取感兴趣的数据，并隐藏过于详细或与分析无关的数据。

转换后的表格 Customer Details
![](https://main.qcloudimg.com/raw/ed70555509a3d614d5afa68fd45aaea9.png)
 
### 转换表格
执行以下操作：
1.	在资源面板中，单击![](https://main.qcloudimg.com/raw/f9c80d7ad384d529ba9e9ecc6bd2b3cc.png)以打开图表。
2.	将透视表拖到 Customer KPIs 表格的中心，然后选择转换为：透视表。
3.	在右侧属性面板中的数据下，单击添加数据，然后单击行。
4.	在列表中，选择 Product Group。
5.	再次选择添加数据，并添加 Product Type 行。
6.	将标题客户 API 添加到可视化中。
7.	单击工具栏中的![](https://main.qcloudimg.com/raw/4f1f0adaae61c1548d3770b31b290be8.png)完成编辑。

现在，您可以按产品组和类型查看单个客户的销售额。通过单击客户、产品组或产品类型，或选择表格中的单个条目，您可以筛选在表格中查看的选择项。通过将产品组或产品类型移动到度量并进行筛选，您可以获得所显示数据的不同视图。
