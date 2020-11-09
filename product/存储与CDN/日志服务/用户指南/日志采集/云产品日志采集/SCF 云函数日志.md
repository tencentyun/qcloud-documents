## 简介

在使用云函数 SCF 进行函数计算时，会产生大量的函数运行日志，云函数 SCF 运行日志已经和腾讯云的日志服务 CLS 平台打通，实时采集函数运行日志至日志服务平台。在日志服务平台您可以进行检索、投递和消费等更多操作。
![](https://main.qcloudimg.com/raw/ceb1528c2150af09913cac3c0a77f420.png)

## 接入步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，创建日志集以及日志主题（日志集地域请选择函数服务所在地域，暂不支持跨地域日志推送），详情请参见  [创建日志集和日志主题](https://cloud.tencent.com/document/product/614/34340)。
2. 如需进行日志检索，需要手动开启索引，如已开启，可跳过2 - 5步骤。
   请您登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，单击【日志集管理】，并进入目标日志集详情，在目标日志主题的右侧单击【管理】，进入到日志主题详情页。
	 ![](https://main.qcloudimg.com/raw/2a893c050df77744420146457fc73376.jpg)
3. 单击【索引配置】页签，进入索引配置页面。
4. 单击右上角的【编辑】，打开索引状态，开启全文索引，开启键值索引，填入键值索引信息。
	 ![](https://main.qcloudimg.com/raw/6b5ba57bbe763e3438940d93a03a569e.jpg)
5. 配置完后，单击【保存】即可。	 
   > ?如需进行更多操作如日志实时检索，日志投递消费等，请登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。更多功能请参见 [日志服务](https://cloud.tencent.com/document/product/614) 文档。
  #### SCF 日志字段说明
<table>
<thead>
<tr>
<th>字段</th>
<th>含义</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>SCF_RequestId</td>
<td>请求 ID</td>
<td>text</td>
</tr>
<tr>
<td>SCF_Namespace</td>
<td>命名空间</td>
<td>text</td>
</tr>
<tr>
<td>SCF_FunctionName</td>
<td>函数名</td>
<td>text</td>
</tr>
<tr>
<td>SCF_Qualifier</td>
<td>版本</td>
<td>text</td>
</tr>
<tr>
<td>SCF_StartTime</td>
<td>起始时间</td>
<td>long</td>
</tr>
<tr>
<td>SCF_Message</td>
<td>日志内容</td>
<td>text</td>
</tr>
<tr>
<td>SCF_Level</td>
<td>日志级别</td>
<td>text</td>
</tr>
<tr>
<td>SCF_Index</td>
<td>日志行号</td>
<td>long</td>
</tr>
<tr>
<td>SCF_Alias</td>
<td>函数别名</td>
<td>text</td>
</tr>
</tbody></table>
6. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，在左侧导航栏中，单击【函数服务】，进入函数服务列表页。
7. 单击需要实时采集日志的函数名称，进入**函数配置**页面，单击右上角的【编辑】，编辑函数信息。
8. 在**函数配置**中，为该函数服务配置步骤1创建好的日志集和日志主题，并单击【保存】。
![](https://main.qcloudimg.com/raw/3b3038810f5743fec2cfa6f1845cb4ca.jpg)

## 日志检索示例

使用实时检索功能之前，请确保您的函数服务日志已接入日志服务平台，并且需检索的日志主题已开启索引功能。若未开启索引，可参见文档 [开启索引](https://cloud.tencent.com/document/product/614/16981)。

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏单击【日志检索】，进入到日志检索页。
2. 选择检索的时间范围和日志主题，在输入框填写检索语法（语法支持关键词检索、模糊检索、范围检索等方式，详情请参见 [语法规则](https://cloud.tencent.com/document/product/614/16982)）。
3. 单击【搜索】，即可检索日志。
   示例1： `SCF_StartTime:1583233118007`查询时间等于1583233118007的日志
   ![](https://main.qcloudimg.com/raw/f687223e9a19f89c2de1878ebb009ce9.png)
   示例2: `SCF_Index:2` 查询 Index 等于2的日志
   ![](https://main.qcloudimg.com/raw/2243f7f8e3844ce638bbec7e71d72b59.png)


