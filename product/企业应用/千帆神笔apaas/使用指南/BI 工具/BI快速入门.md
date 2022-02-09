---
sidebar_position: 0
---

神笔应用连接器 BI 定位于自助大数据分析工具，能够帮助企业的业务人员和数据分析师，开展以问题导向的探索式分析。本文将使用案例方式讲解如何使用神笔应用连接器 BI 工具，整体流程如下图所示： ![img](https://main.qcloudimg.com/raw/a99a53792d0254c6188e8330ccd8553d.png)

## 通过应用数据进行 BI 仪表板制作

### 路径

登录 [神笔应用连接器 设计态首页](https://apaas.cloud.tencent.com/)，单击【BI 工具(Beta)】>【仪表板】。

### 案例介绍

某公司是批发贸易公司，现需要对各省份的订单金额及商品品类维度等进行统计。

**准备工作**：某公司在神笔应用连接器 搭建对应的订单管理应用，订单管理应用已经发布上线并产生对应的业务数据。基于订单管理应用中的订单数据、商品数据进行统计分析。

**操作步骤**

1. 进入“BI 工具(Beta)”页签。

- 当应用未发布过时，进入“BI 工具(Beta)”页会出现如下提示，需要先发布应用才可使用 BI 工具功能。
  ![img](https://main.qcloudimg.com/raw/4213cea2f813ba6bc7a5fd543c02423a.png)
- 当应用发布过时，进入“BI 工具(Beta)”页会出现如下提示。BI 工具使用的是运行态的数据，若对象中有增删字段，则需要发布应用后才可使用最新的数据结构。勾选【不再提示】后，则后续进入仪表板列表时不会再弹出此提示。
  ![img](https://main.qcloudimg.com/raw/561b94c02bab719f40de1ad00148e502.png)

2. 在“BI 工具(Beta)”页，单击【新建仪表板】，输入仪表板名称“各省份销售金额统计”后新建仪表板，新建仪表板后将自动打开新标签页，进入仪表板编辑页面。
   ![img](https://main.qcloudimg.com/raw/5057c6c3e61c7d06b67c99cfe7e97fdd.gif)
3. 单击【添加组件】，选择订单管理应用中订单数据表{（数据表命名规则为对象名\_应用命名（租户 ID）}，进入组件配置页面。
   ![img](https://main.qcloudimg.com/raw/dc950143c494825053f8d3009c50246c.gif)
4. 选择分区柱形图，将“订单金额”指标拖入纵轴，“省份”维度拖入横轴，并将组件命名为“各省份销售金额统计”。
   ![img](https://main.qcloudimg.com/raw/4a3c7b7633b3de9d8490b58f2e74ffff.gif)  
   ![img](https://main.qcloudimg.com/raw/a698544e149121e8999e3535df10cf2e.png)
5. 单击组件配置页右上角【进入仪表板】，可调整该组件在仪表板中的位置及大小，也可以左侧组件按钮新增其他组件。配置好仪表板后，数据将自动保存，可直接关闭此页签。
   ![img](https://main.qcloudimg.com/raw/95137b27eecbceacf418ff144b3d7c26.gif)
6. 进入导航设置页签，添加菜单，页面类型选择“BI 页面”，下拉选到需要配置的 BI 仪表板。 ![img](https://main.qcloudimg.com/raw/40eec84e314e17f6c16ea5be31c303ce.gif)
7. 发布应用，即可在“订单管理”应用运行态的中查看已配置的仪表板。
   ![img](https://main.qcloudimg.com/raw/82225a71a8ea53f427338d71cbbd1582.png)

## 通过上传 Excel 文件进行 BI 仪表板制作

### 路径

登录 [神笔应用连接器 设计态首页](https://apaas.cloud.tencent.com/)，单击【应用设计】>【BI 工具(Beta)】>【数据加工】。

### 案例介绍

部分数据来源于其他系统导出或者手工记录的 Excel，可将 Excel 或 csv 格式文件按规范格式导入到 BI 工具中进行数据加工及可视化呈现。

**准备工作**：线下整理好待分析的 Excel 数据文件。上传前需要确认，添加的 Excel 首行不能有合并单元格，否则会上传失败。

**操作步骤**

1. 进入“BI 工具(Beta)”页签，单击【数据加工】，进入自助数据集，单击【添加表】，添加 Excel 文件，选择“示例数据” Excel 上传。
   ![img](https://main.qcloudimg.com/raw/363dc49b6b1778a0867ac121c809b86a.gif)
2. 选择示例数据集中的多个 sheet 页进行上传，单击【确定】，则会生成对应 sheet 页对应的数据表。
   ![img](https://main.qcloudimg.com/raw/bd545534f4dafd94161c787f5ec91036.png)  
    ![img](https://main.qcloudimg.com/raw/df08758b45d1653df539044fb3093f70.png)
3. 由于商品销售明细表中只有门店编码与商品编码，则可以在销售明细表中添加表关联，分别将商品信息、门店信息分别与销售明细表关联起来。
   > 一个商品会被销售多次，则关联关系选择为 N:1，通过门店编码关联起来。
   > ![img](https://main.qcloudimg.com/raw/b910f1d080cf5d8afe251a126bbc6f90.gif)  
   > ![img](https://main.qcloudimg.com/raw/5117b2ba2d69ecc86b44d0276e479827.png)
4. 添加自助数据集，命名为“销售明细总表”，选择三张表的字段合并到销售明细总表中。（添加表间关联后，才可将不同表的数据合并至一张自助数据集中。）
   ![img](https://main.qcloudimg.com/raw/29219d11251a0d249fded0925b738b1b.png)  
    ![img](https://main.qcloudimg.com/raw/0f4a5c973aad07dfc56f16528cbdb74b.gif)
5. 进入仪表板列表，单击【新建仪表板】，命名为“销售情况分析”，添加组件，并将“销售明细总表”作为组件数据源。
   ![img](https://main.qcloudimg.com/raw/ca2a865a8e421e2e56bd4c9bf5040039.png)
6. 进入组件配置页，选择自定义图表，将销售额、成本额拖入横轴，省份拖入纵轴，图形属性选择“线”型，则可以绘制“各省份销售额/成本对比图”。
   ![img](https://main.qcloudimg.com/raw/e70322016fd606351c0ed859449065ab.png)

- 选择饼图，按下图配置，可绘制“各商品销售情况统计表”。
  ![img](https://main.qcloudimg.com/raw/ef5d6a819a93740feb09b1e9f09b7132.png)

7. 进入仪表板中，拖放两个组件大小与位置。
   ![img](https://main.qcloudimg.com/raw/8ce273e5723c376f7cf5f1cb15cab332.png)
8. 进入“导航设置”页签，添加菜单，页面类型选择“BI 页面”，下拉选到需要配置的 BI 仪表板。
9. 发布应用，则在“订单管理”应用运行态的中可查看已配置的仪表板。
   ![img](https://main.qcloudimg.com/raw/6716dfa23ba02105faaa59509529e95f.png)
