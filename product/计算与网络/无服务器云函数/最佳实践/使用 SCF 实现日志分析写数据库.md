## 操作场景
在本文档示例中，我们用到了云函数（SCF），对象存储（COS），云数据库 MySQL。其中，COS 用来存储需要分析的日志文件，SCF 实现从 COS 下载日志文件并进行统计分析，把分析的结果写入到 MySQL 数据库中。

## 操作步骤
<span id="step01"></span>
### 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos)，选择左侧导航栏中的【存储桶列表】。
2. 参考 [创建存储桶](https://cloud.tencent.com/document/product/436/38484#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6) 创建一个存储桶，主要参数信息设置如下：
 - **名称**：命名为 loganalysis。
 - **所属地域**：选择北京地域。
 - **访问权限**：选择“私有读写”。

<span id="step02"></span>
### 创建 MySQL 云数据库
1. 参考 [购买方式](https://cloud.tencent.com/document/product/236/5160) 创建一个 MySQL 云数据库。由于数据库需要付费购买，您可以选择在北京地域购买 [云数据库 MySQL 入门机型](https://cloud.tencent.com/act/event/cdbbasic.html)。
2. 购买完成后，给数据库添加可访问的用户名和密码，并创建新库 `mason_demo`。

<span id="step03"></span>
### 创建云函数 SCF
1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面。
设置以下参数信息，并单击【下一步】。如下图所示：
 - **函数名称**：命名为 “LogAnalysis”。
 - **运行环境**：选择 “Python 2.7”。
 - **创建方式**：选择【模板函数】。
 - **模糊搜索**：输入“日志分析写数据库”，并进行搜索。
单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/e42d9b4102f3e13ebf1722de5875d1ac.png)
4. 保持默认配置，单击【完成】，完成函数的创建。
5. 在使用本模板函数时，您需要按照提示在函数配置中，添加环境变量。
 进入已创建的云函数“函数配置”页面，单击右上角【编辑】，新增环境变量参考表格进行填写。如下图所示：
![](https://main.qcloudimg.com/raw/3112dba5a8cac82c295c17a593ed222e.png)
<table>
  <tbody><tr>
          <th>key</th>
          <th>value</th>
      </tr>
      <tr>
          <td>dbhost</td>
          <td rowspan="2">请参考 <a href="https://cloud.tencent.com/document/product/236/3130" target="_blank">访问 MySQL 数据库</a> 获取。</td>
      </tr>
      <tr>
          <td>dbport</td>
      </tr>
      <tr>
          <td>dbuser</td>
          <td>已创建的 MySQL 数据库的用户名。</td>
      </tr>
			<tr>
          <td>dbpwd</td>
          <td>已设置的 MySQL 帐号密码。</td>
      </tr>
      <tr>
          <td>dbname</td>
          <td>需备份的数据库名称，本文以 <code>mason_demo</code> 为例。</td>
      </tr>
       <tr>
      <td>cosregion</td>
      <td> Bucket 所在地域。</td>
      </tr>
  </tbody></table>
	
>! 
>- 如果数据库使用的是内网地址，则函数也需要在【函数配置】页面中，选择和数据库相同的 VPC 和子网。如下图所示：
![](https://main.qcloudimg.com/raw/a329381190dcf6ad0883f5f8a51a9567.png)
>- 您需要给函数配置运行角色，来给函数授予访问账户中的对象存储（COS）数据的权限，详情请参见 [创建函数运行角色](https://cloud.tencent.com/document/product/583/41755)。您也可以直接在函数代码中替换为账户实际使用的 SecretId 及 SecretKey，可前往 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取。



<span id="step04"></span>
#### 配置 COS 触发器
在函数详情页面，选择左侧【触发管理】并单击【创建触发器】。在弹出的“创建触发器”窗口中为云函数添加 COS 触发器。如下图所示：
![](https://main.qcloudimg.com/raw/2f2cb84e50b4ec09078ea675a3bdd3c2.png)
主要参数信息如下，其余配置项请保持默认：
 - **触发方式**：选择 “COS触发”。
 - **COS Bucket**：选择 [创建 COS Bucket](#step01) 步骤中已创建的存储桶 loganalysis。
 - **事件类型**：选择“全部创建。”

<span id="step05"></span>
### 测试函数功能
1. 下载 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip) 中的日志文件，并解压出 demo-scf1.txt。
2. 切换至 [对象存储控制台](https://console.cloud.tencent.com/cos/bucket)，选择创建好的存储桶 loganalysis，单击【上传文件】。
3. 在弹出的“上传文件”窗口中，选择下载好的 demo-scf1.txt，单击【确定上传】。
4. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。
在函数详情页面中选择【日志查询】页签，可以看到打印出的日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
5. 切换至 MySQL 管理界面，查看数据库中的分析结果。
>?您可以根据自身的日志格式编写具体的处理方法，数据库的写方法也可以修改为增量写。
