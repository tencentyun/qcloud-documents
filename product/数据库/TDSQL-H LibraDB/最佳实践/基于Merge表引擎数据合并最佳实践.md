当需要将已有OLTP数据库实例中的多个表进行读合并时，可基于Merge表引擎合并，将多个表数据实时汇聚到一个LibraSQL分析引擎进行分析。

## 场景概述

<table class="table-striped">
 <thead><tr><th width=20%>场景</th><th width=80%>说明</th></tr></thead>
 <tbody>
 <tr>
 <td>场景一</td>
 <td>将多个源OLTP实例多个表数据，实时汇集到一个 LibraSQL 分析引擎进行分析。</td>
 <tr>
 <td>场景二</td>
 <td>将同一个源OLTP实例多个数据库中的多个表数据，实时汇集到一个 LibraSQL 分析引擎进行分析。</td>
 </tbody></table>

## 使用限制

请参见基于Merge表引擎数据合并中的使用限制。

## 注意事项

添加CDC任务通用注意事项请参见[添加CDC](https://cloud.tencent.com/document/product/1488/63678)。

## 场景一

#### 场景示例

<table class="table-striped">
 <thead><tr><th width=25%>多表归并CDC任务</th><th width=40%>源端OLTP库表名</th><th width=35%>合并至目标端库表名</th></tr></thead>
 <tbody>
 <tr>
 <td>任务一</td>
 <td>源端OLTP 1<br />database1：tableA和tableB</td>
 <td>databaseA：tableA_log和tableB_log</td></tr>
 <tr>
 <td>任务二</td>
 <td>源端OLTP 2<br />database2：tableC和tableD</td>
 <td>databaseA：tableC_log和tableD_log</td></tr>
 </tbody></table>

任务一和任务二均启动后，源端OLTP 1和源端OLTP 2中指定的多个库表将会实时同步至目标端指定的库表，再通过Merge表引擎，实现数据读取时合并。

#### 操作步骤

以下步骤仅以场景示例为例，其他场景案例请参考该操作步骤执行。

1. 创建CDC任务一。

   1. 参考[添加CDC任务](https://cloud.tencent.com/document/product/1488/63678)并已进入设置指定对象步骤。

      **示例：**源端为：OLTP 1对象选择**指定对象**。

   2. **多表归并**开关默认关闭。

   3. 在**源库对象**中选择库表。

      **示例：**database1：tableA和tableB

   4. 单击![](https://qcloudimg.tencent-cloud.cn/raw/a5a9e29bbdc569bfe45a64837fe87aba.png)，**已选对象**中将展示已选择的库表。

   5. 将鼠标悬停至目标库，单击![](https://qcloudimg.tencent-cloud.cn/raw/bdc8b09d2728c26f767e32cd29c891a3.png)修改库名称。

      **示例：**databaseA

   6. 在**已选对象**右侧单击**批量改名**，在弹出的**批量添加已选对象表名后缀**对话框中输入后缀，单击**确定**。

      **示例：**_log

      已选对象中将显示修改后的库表名称。

      **示例：**databaseA：tableA_log和tableB_log

   7. 单击**下一步**，进入[添加CDC任务](https://cloud.tencent.com/document/product/1488/63678)的高级设置步骤，继续执行其他步骤，启动CDC任务后，该配置生效。

      **任务启动后，源端已指定的表会同步并至目标端的指定库表中。**

      **示例：**database1：tableA和tableB数据会分别同步至databaseA：tableA_log和tableB_log中。

2. 创建CDC任务二。

   参考创建CDC任务一的步骤。

   **示例：**源端为OLTP 2，在**源库对象**中选择库表database2：tableC和tableD，合并到目标端的指定库表命名为databaseA：tableC_log和tableD_log。

   **任务启动后，源端已指定的表会同步并至目标端的指定库表中。**

   **示例：**database2：tableC和tableD数据会分别同步至databaseA：tableC_log和tableD_log中。

3. 利用 Merge 表能力，匹配具有相同命名模式和表结构的数据表，构造虚拟表，完成表数据查询合并。

   ```sql
   CREATE TABLE ... Engine=Merge(currentDatabase(), tables_regexp)
   ```
   
   其中，tables_regexp是一个正则表达式，用于匹配指定数据库中的表名。
   
   **示例：**
   
      ```sql
   -- 在当前数据库下，按照普通表tableA_log的表结构建立Merge表table_all,其中table_all是虚拟表， .*_log匹配当前数据库中表名的正则表达式
   CREATE TABLE table_all on cluster default_cluster as databaseA.tableA_log  Engine=Merge(currentDatabase(), '.*_log') ;
           
   -- 当查询Merge表时，LibraSQL分析引擎会自动查询所有带后缀_log的表(即tableA_log、tableB_log、tableC_log、tableD_log)，将结果汇聚返回
   select * from table_all;
      ```


#### 操作结果

**源OLTP 1与源OLTP 2实现多源合一：在目标端使用Merge表引擎查询任务一和任务二中数据时，多个表数据合并返回。**

**示例：**当查询Merge表时，LibraSQL分析引擎会自动查询所有 *_log（即tableA_log、tableB_log、tableC_log、tableD_log）表，将结果汇聚返回。



## 场景二

#### 场景示例

<table class="table-striped">
 <thead><tr><th width=25%>多表归并CDC任务</th><th width=40%>源端OLTP库表名</th><th width=35%>合并至目标端库表名</th></tr></thead>
 <tbody>
 <tr>
 <td>任务一</td>
 <td>源端OLTP 3<br /><ul><li>A_1：d_1和d_2<li>A_2：c_1和c_2</td>
 <td><ul><li>A_1：d_1_log和d_1_log<li>A_2：c_1_log和c_2_log</td></tr>
 </tbody></table>

任务一启动后，源端OLTP 3中指定的库表会分别实时同步至目标端指定的库表，再通过Merge表引擎，实现数据读取时合并。

#### 操作步骤

以下步骤仅以场景示例为例，其他场景案例请参考该操作步骤执行。

1. 创建CDC任务一。

   1. 参考[添加CDC任务](https://cloud.tencent.com/document/product/1488/63678)并已进入设置指定对象步骤。

      **示例：**源端为：OLTP 3

   2. 在**设置对象**页面，同步对象选择**指定对象**。

   3. **多表归并**开关默认关闭。

   4. 在**源库对象**中选择库表。

      **示例：**A_1：d_1和d_2，A_2：c_1和c_2

   5. 单击![](https://qcloudimg.tencent-cloud.cn/raw/a5a9e29bbdc569bfe45a64837fe87aba.png)，**已选对象**中将展示已选择的库表。

   6. 在**已选对象**右侧单击**批量改名**，在弹出的**批量添加已选对象表名后缀**对话框中输入后缀，单击**确定**。

      **示例：**_log

      已选对象中将显示修改后的库表名称。

      **示例：**A_1：d_1_log和d_1_log，A_2：c_1_log和c_2_log

   7. 单击**下一步**，进入[添加CDC任务](https://cloud.tencent.com/document/product/1488/63678)的高级设置步骤，继续执行其他步骤，启动CDC任务后，该配置生效。

      **任务启动后，源端已指定的表会同步并至目标端的指定库表中。**
      
      **示例：**A_1：d_1和d_2、A_2：c_1和c_2数据会分别同步至A_1：d_1_log和d_1_log、A_2：c_1_log和c_2_log中。

2. 使用 Merge 表引擎，匹配具有相同命名模式的库，且库中有相同命名模式和表结构的数据表，构造虚拟表，完成表数据查询合并。

   ```sql
   CREATE TABLE ... Engine=Merge(REGEXP(expression), tables_regexp)
   ```
   
   其中，expression是用于匹配数据库名称的正则表达式。tables_regexp是一个正则表达式，用于匹配指定数据库中的表名。
   
   **示例：**
   
      ```sql
   -- 按照普通表 d_1_log的表结构建立Merge表table_all,其中table_all是虚拟表,A_*匹配数据库名称的正则表达式，.*_log匹配数据库中表名的正则表达式
   CREATE TABLE table_all on cluster default_cluster as A_1.d_1_log ENGINE=Merge(REGEXP('A_*'), '.*_log');
           
   -- 当查询 Merge 表时，LibraSQL分析引擎会自动查询所有A_*数据库(即A_1、A_2)中的带后缀_log的表(即d_1_log、d_2_log、c_1_log、c_2_log)，将结果汇聚返回
   select * from table_all;
      ```

#### 操作结果

**源OLTP 3实现同源多表合一：在目标端使用Merge表引擎查询任务一中数据时，跨库多个表数据合并返回。**

**示例：**当查询Merge表时，LibraSQL分析引擎会自动查询A_1、A_2中的带后缀_log 的表（即d_1_log、d_2_log、c_1_log、c_2_log），将结果汇聚返回。