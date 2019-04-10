本章节将为您介绍如何使用Sparkling笔记簿功能实现简单的SQL数据查询及数据可视化分析。更多数据开发细节可查看操作指南—[数据开发](https://cloud.tencent.com/document/product/1002/30555)章节。

## 前提条件
在进行数据分析之前，请确保您已根据快速入门第一、二章节内容建立Sparkling集群并已将数据导入集群中。
## 操作步骤
进入 [集群管理](https://sparkling.cloud.tencent.com) 页面，在左侧导航单击【工作区】进入数据开发页面。

##### 1. 新建笔记簿
点击工作区左上角“+”按钮，选择“新建笔记簿”，建立新笔记簿。
![](https://main.qcloudimg.com/raw/488a8fcb1ec3f7be04d97aba6bf8ad37.png)
##### 2. 查找数据库及数据表
在命令行输入以下命令后使用快捷键 Shift+Enter 或点击右上角运行按钮运行该命令行，查找当前集群下包含的数据库名。
![](https://main.qcloudimg.com/raw/f9462809f8c722ac8087f2b978f0ab23.png)
输入以下命令进入default数据库。
![](https://main.qcloudimg.com/raw/3fa7a16a31a74cab4bd174182a6edd42.png)
输入以下命令查找default数据库中包含的数据表名，可以看到之前导入的数据表new_table已经存在于Sparkling集群中。
![](https://main.qcloudimg.com/raw/e3ee9c1c2d8cab750b92d821fd7bbaa1.png)
##### 3. 执行简单的sql语句
执行以下命令查看new_table中的数据信息，其中pt列是Sparkling集群导入时增加的一列时间戳，默认定义为数据导入日期的前一天00：00
![](https://main.qcloudimg.com/raw/80ff8ed287fc30028d24d0f557f16f7f.png)
##### 4. 数据可视化分析
执行以下命令获取以enabled分组的检索行数，将结果绘制饼图如下：
![](https://main.qcloudimg.com/raw/2799eac2a99b772c1c09b771b98c9b0c.png)
执行以下命令获取以type分组的检索行数，绘制柱状图如下，其中点击Settings可以设置keys、groups、values值：
![](https://main.qcloudimg.com/raw/8e088464e329c30f7a6b9426885a454f.png)