云数据仓库套件 Sparkling 提供数据开发 IDE 供用户对数据进行 ETL 、清洗加工和计算等操作，同时支持任务定时调度功能。笔记簿（Notebook）是数据开发 IDE 的核心功能组件，通过使用笔记簿可以方便用户进行任务管理。

## 操作步骤
1. 进入 [集群管理](https://sparkling.cloud.tencent.com) 页面，在左侧导航单击【工作区】进入数据开发页面。
2. 管理笔记簿。
在左侧栏可以执行笔记簿的新建、刷新、重命名、删除操作。![](https://main.qcloudimg.com/raw/3f6e09745ad24a128fe61e8eba57bcab.png)
3. 编辑执行命令。
![](https://main.qcloudimg.com/raw/c7bd2dd56fb8870a95ef532731c88b44.png)
   a. 运行并查看执行结果。
   在命令栏中输入 SQL 语句后在右上角运行或使用快捷键 Shift+Enter 即可查看当前语句执行结果。
   b. 可视化查询结果。
   通过以下按键对查询结果进行可视化操作，如绘制柱状图、饼图等。
	 ![](https://main.qcloudimg.com/raw/beccda50a4d06e69c0dc450ef9b2515e.png)
   c.	下载查询结果
   可以对查询结果进行下载，支持 CSV 和 TSV 两种格式的数据。
   d.	添加代码段。
   在下方单击【添加代码段】，添加新的命令栏。
   e.	运行所有命令。
   在左上角单击【运行所有】，可以依次执行当前笔记簿下所有命令栏内语句。
	 f. 定时调度。
   在左上角单击【定时调度】，弹出定时调度设置框，可选择间隔周期并定义调度时间，例如天：00时00分，即每日0点0分自动开始执行任务。选择例行时长及前序并发设置项后单击【确定】，即可完成定时调度设置。可在页面左侧【任务】栏查看该 notebook 任务具体细节。
> ?此处调度周期设置完成后，任务第一次执行是开始时间+一个调度周期。
>
![](https://main.qcloudimg.com/raw/b289c3592e130c58fd6a2d76730a9929.png)

4. 使用 SQL IDE。
通过进入 SQL IDE 可以查看数据表信息，完成数据的管理、查询、下载等操作。
a.	进入 SQL IDE 界面。
在右上角单击<img src="https://main.qcloudimg.com/raw/712bdbcd5c1001d683646a11b0c9557d.png"  style="margin:0;">进入 SQL IDE 界面。
b.	查看数据目录。
在 SQL IDE 界面左侧导航栏可以查看当前集群下所有创建和授权的数据。
![](https://main.qcloudimg.com/raw/88b61430f99dcc8023325b82f6819470.png)
c.	编辑 SQL 代码。
在右侧 SQL 编辑器可以执行代码的编辑。目前 SQL 支持 DDL 和 DML 语法规范，并完全兼容 ANSI SQL 2003。编辑完成后单击下方【执行】可查看耗时、更新时间及运行结果，完成数据可视化及下载等操作。
![](https://main.qcloudimg.com/raw/77cc986281b6720e2c69bfcca6098bb7.png)
 




 





