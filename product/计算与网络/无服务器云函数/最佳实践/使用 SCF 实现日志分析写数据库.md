## 操作场景
在本文档示例中，我们用到了云函数（SCF），对象存储（COS），云数据库 MySQL。其中，COS 用来存储需要分析的日志文件，SCF 实现从 COS 下载日志文件并进行统计分析，把分析的结果写入到 MySQL 数据库中。

## 操作步骤
<span id="step01"></span>
### 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos)。
2. 创建一个 Bucket，命名为 loganalysis，并选择**北京**地域，权限选择 “私有读写”。

<span id="step02"></span>
### 创建 MySQL 云数据库
1. 创建一个 MySQL 云数据库。由于数据库需要付费购买，您可以选择在北京地域购买 [云数据库 MySQL 入门机型](https://cloud.tencent.com/act/event/cdbbasic.html)。
2. 购买完成后，给数据库添加可访问的用户名和密码，并创建新库。

<span id="step03"></span>
### 创建云函数 SCF
1. 登录[【云函数控制台】](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，进入【函数服务】页面。
2. 选择**北京**地域，单击【新建】，进入新建函数页面。
3. 填写以下参数信息，单击【下一步】。如下图所示：
 - 创建方式：选择 “模板函数”。
 - 函数名称：命名为 “LogAnalysis”。
 - 模板搜索：选择 “语言” 为 “Python 2.7” 的 “日志分析写数据库” 模板。
 - 鼠标移至模板函数上，可查看模板函数详情，支持下载操作。
 ![](https://main.qcloudimg.com/raw/88e11b73bdd2bfb1c30997dea17e9c8c.jpg) 
4. 保持默认配置，单击【完成】，完成函数的创建。
5. 在使用本模板函数时，您需要按照提示在函数配置中，添加环境变量。切换到【函数配置】页面，单击【编辑】，新增环境变量： dbhost、dbport、dbuser、dbpwd、dbname 和 cosregion。
>? 如果数据库使用的是内网地址，则函数也需要在【函数配置】页面中，选择和数据库相同的 VPC 和子网。如下图所示：
![](https://main.qcloudimg.com/raw/7fbca3ed985c75064e55d4faaced2669.jpg) 

<span id="step04"></span>
#### 配置 COS 触发器
>! “触发方式” 选择 “COS 触发”，COS Bucket 选择“loganalysis” ，事件类型选择“全部创建”，其它保持默认参数。
>
选择【触发方式】页面，单击【添加触发方式】，为云函数添加 COS 触发器。如下图所示：
![](https://main.qcloudimg.com/raw/6177f12247b6a4d1b98e3eac0e7cdb51.png) 

<span id="step05"></span>
### 测试函数功能
1. 下载 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip) 中的日志文件，并解压出 demo-scf1.txt。
2. 切换至 [对象存储控制台](https://console.cloud.tencent.com/cos/bucket)，选择创建好的 Bucket：loganalysis，单击【上传文件】。
3. 在弹出的 “上传文件” 窗口中，选择下载好的 demo-scf1.txt，单击【确定上传】。
4. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。在**运行日志**中可以看到打印出来的日志信息，如下图所示：
![](https://main.qcloudimg.com/raw/72f4b02e3fcc76653d495e1d3c6c2272.jpg)
5. 切换至 MySQL 管理界面，查看数据库中的分析结果。

用户可以根据您自身的日志格式编写具体的处理方法，数据库的写方法也可以改成增量写。
