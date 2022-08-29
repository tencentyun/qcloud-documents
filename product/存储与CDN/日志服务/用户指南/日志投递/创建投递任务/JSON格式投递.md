## 概述

您可以通过 [日志服务控制台](https://console.cloud.tencent.com/cls)，将数据按照 JSON 格式投递到对象存储（Cloud Object Storage，COS），下面将为您详细介绍如何创建 JSON 格式日志投递任务。

## 前提条件

1. 开通日志服务，创建日志集与日志主题，并成功采集到日志数据。
2. 开通腾讯云对象存储服务，并且在待投递日志主题的地域已创建存储桶，详细配置请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 确保当前操作账号拥有配置投递的权限，子账号/协作者投递权限问题请参见 [子账号配置投递](https://cloud.tencent.com/document/product/614/33098) 文档。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击**日志主题**。
3. 单击需要投递的日志主题ID/名称，进入日志主题管理页面。
4. 单击**投递至 COS** 页签，进入投递至 COS 配置页面，依次填写配置信息。  
![](https://qcloudimg.tencent-cloud.cn/raw/481df5d574e8e634a4e4db4b2f757e6d.png)
**配置项说明如下：**
<table>
   <tr>
      <th>配置项</th>
      <th>解释说明</th>
      <th>规则</th>
      <th>是否必填</th>
   </tr>
   <tr>
      <td nowrap="nowrap">投递任务名称</td>
      <td>配置投递任务的名称。</td>
      <td nowrap="nowrap">字母、数字、_和-</td>
      <td>必填</td>
   </tr>
   <tr>
      <td nowrap="nowrap">COS存储桶</td>
      <td>与当前日志主题同地域的存储桶作为投递目标存储桶。</td>
      <td>列表选择</td>
      <td>必填</td>
   </tr>
   <tr>
      <td>COS 路径</td>
      <td>COS 存储桶的路径。默认按照/年/月/日/小时/，例如/2022/7/31/14/这种格式在 COS上来存储投递的日志文件。这里支持 <a href="http://man7.org/linux/man-pages/man3/strptime.3.html"> strftime</a> 的语法 ，例如投递时间是 2022/7/31 14:00，/%Y/%m/%d/生成的路径是/2022/7/31/。/%Y%M%d/%H/生成的路径是/20220731/14/。</td>
      <td>非<code>/</code>开头</td>
      <td>可选</td>
   </tr>
   <tr>
      <td>文件命名</td>
	  <td>选项1：投递时间命名，推荐这个选项，例如202208251645_000_132612782.gz代表的是投递时间_日志主题分区_offset，Hive 也可以加载这种文件。</br>
选项2：随机数命名，旧版的命名方式，这种命名方式 Hive 不识别，因为 Hive 不识别_开头的文件，可以在 COS 路径配置项里面添加自定义前缀，例如/%Y%M%d/%H/Yourname。 </td>
      <td>/</td>
      <td>必填</td>
   </tr>
   <tr>
      <td>压缩格式</td>
			<td>为了帮助用户节约读流量费用，我们将日志文件压缩后再投递到 COS，支持 Snappy\lzop\gzip。</td>
      <td>gzip\snappy\lzop</td>
      <td>必填</td>
   </tr>
   <tr>
      <td nowrap="nowrap">投递文件大小</td>
      <td>需要投递的原始日志文件的大小，和投递间隔时间配合使用，哪个条件先触发，就按照哪个规则去压缩文件，然后投递到 COS。例如配置256M，15分钟，如果文件大小在5分钟就到了256MB，那么文件大小这个条件先触发投递任务。</td>
      <td nowrap="nowrap">5 - 256</br>单位：MB</td>
      <td>必填</td>
   </tr>
   <tr>
      <td nowrap="nowrap">投递间隔时间</td>
      <td>指定间隔多长时间，触发一次投递，和投递文件大小配合使用，哪个条件先触发，就按照哪个规则去压缩文件，然后投递到 COS。例如配置256MB，15分钟，如果文件大小在15分钟时仅为200MB，间隔时间这个条件先触发投递任务。</td>
      <td>300 - 900</br>单位：秒</td>
      <td>必填</td>
   </tr>
</table>
5. 单击**下一步**，进入高级配置，选择投递格式为 JSON，勾选您需要投递的字段即可，其中_CONTENT_是用户的日志数据，_SOURCE_、_FILENAME_、_HOSTNAME_、_TIMESTAMP_、_TAG_元信息均为 CLS 的元数据字段，请您根据实际情况勾选。
![](https://qcloudimg.tencent-cloud.cn/raw/155a6c79f9463837385e15cee8041d32.png)

