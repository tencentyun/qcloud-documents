## 概述

您可以通过 [日志服务控制台](https://console.cloud.tencent.com/cls)，将数据按照 Parquet 格式投递到对象存储（Cloud Object Storage，COS），Parquet 文件可以被 Hive 加载，多用于大数据的计算分析，下面将为您详细介绍如何创建 Parquet 格式日志投递任务。

>! Parquet 文件大多用于大数据平台，由于 Parquet 本身有一定的压缩率，加上文件压缩格式（snappy/lzop/gzip），因此，投递文件大小要配置的大一些，建议不小于200MB（投递到 COS 大约在50M）。
>

## 前提条件

1. 开通日志服务，创建日志集与日志主题，并成功采集到日志数据。
2. 开通腾讯云对象存储服务，并且在待投递日志主题的地域已创建存储桶，详细配置请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 子账号/协作者需要主账号授权，授权步骤参考 [基于 CAM 管理权限](https://cloud.tencent.com/document/product/614/68373)，复制授权策略参考 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374#.E6.8A.95.E9.80.92-cos)。
4. 已授权给腾讯云 CLS 服务角色访问 COS 的权限。大部分用户通过控制台操作时，系统会引导用户完成授权；小部分用户跨过控制台，直接调用 API，这部分客户需要手动去授权，详情参考 [投递权限查看及配置](https://cloud.tencent.com/document/product/614/71623)。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击**日志主题**。
3. 单击需要投递的日志主题ID/名称，进入日志主题管理页面。
4. 单击**投递至 COS** 页签，进入投递至 COS 配置页面，依次填写配置信息。
<img src="https://qcloudimg.tencent-cloud.cn/raw/55dcde82e346e82790ddc71eea687328.png" style="width: 60%;" /></br>
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
      <td nowrap="nowrap">COS 存储桶</td>
      <td>与当前日志主题同地域的存储桶作为投递目标存储桶。</td>
      <td>列表选择</td>
      <td>必填</td>
   </tr>
   <tr>
      <td>COS 路径</td>
      <td>COS 存储桶的路径。默认按照/年/月/日/小时/如/2022/7/31/14/ 这种格式在COS上来存储投递的日志文件，这里支持 <a href="http://man7.org/linux/man-pages/man3/strptime.3.html"> strftime</a> 的语法 ，例如投递时间是2022/7/31 14:00，/%Y/%m/%d/生成的路径是/2022/7/31/。/%Y%M%d/%H/生成的路径是/20220731/14/。</td>
      <td>非<code>/</code>开头</td>
      <td>可选</td>
   </tr>
   <tr>
      <td>文件命名</td>
	  <td>选项1：投递时间命名，推荐这个选项，例如202208251645_000_132612782.gz代表的是投递时间_日志主题分区_offset，Hive 也可以加载这种文件。</br>选项2：随机数命名，旧版的命名方式，这种命名方式 Hive 不识别，因为 Hive 不识别_开头的文件，可以在 COS 路径配置项里面添加自定义前缀，例如/%Y%M%d/%H/Yourname。</td>
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
      <td>需要投递的原始日志文件的大小，和投递间隔时间配合使用,哪个条件先触发，就按照哪个规则去压缩文件，然后投递到 COS。例如配置256M，15分钟，如果文件大小在5分钟就到了256MB，那么文件大小这个条件先触发投递任务。</td>
      <td nowrap="nowrap">5 - 256，单位：MB</td>
      <td>必填</td>
   </tr>
   <tr>
      <td nowrap="nowrap">投递间隔时间</td>
      <td>指定间隔多长时间，触发一次投递，和投递文件大小配合使用,哪个条件先触发，就按照哪个规则去压缩文件，然后投递到 COS。例如配置256MB，15分钟，如果文件大小在15分钟时仅为200MB，间隔时间这个条件先触发投递任务。</td>
      <td>300 - 900，单位：s</td>
      <td>必填</td>
   </tr>
</table>
5. 单击**下一步**，进入高级配置，选择投递格式为 Parquet，如下图所示， `__SOURCE__` 、`__FILENAME__`、`__HOSTNAME__`是 CLS 的元数据字段，如果不需要，可以删除。配置项说明参考下表。
<img src="https://qcloudimg.tencent-cloud.cn/raw/04b931fa49f0a1d04f4f754d75e810fe.png" style="width: 60%;" /></br>
**配置项说明如下：**
<table>
   <tr>
      <th>配置项</th>
      <th>解释说明</th>
      <th>规则</th>
      <th>是否必填</th>
   </tr>
   <tr>
      <td nowrap="nowrap">键值名称（key）</td>
      <td>写入 Parquet 文件的键值（key）字段。系统会自动拉取日志中的键值供用户选择，如果后续用户在日志中又新增了其他字段，可以单击下方的添加按钮自行添加，但不能和已有的键值重名，字段名支持字母、数字、_和-。</td>
      <td nowrap="nowrap">列表选择</td>
      <td>必填</td>
   </tr>
   <tr>
      <td>数据类型</td>
      <td>该字段在 Parquet 文件中的数据类型，String、boolean、int32、int64、float、double。</td>
      <td>列表选择</td>
      <td>必填</td>
   </tr>
   <tr>
      <td>解析失败赋值</td>
      <td>数据类型解析（转换）失败时，可以自定义赋值，String类型的空就是空字符串"",NULL表示未知。布尔、整型、浮点型均可自定义赋值。</td>
      <td>列表选择</td>
      <td>必填</td>
   </tr>
   </table>


