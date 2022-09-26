## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至 COS 以便于对数据进行分析与下载等操作。

## 前提条件

- 该功能目前依赖对象存储（COS）产品，使用时需开通相关产品功能。
- 已创建好数据流出的目标存储桶。

## 操作步骤

### 创建任务

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **对象存储（COS）**，单击**下一步**。
4. 配置数据源信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f8b47026ccb8b0982605b59d7b926f5b.png)
   - 源 Topic 类型：选择数据源 Topic
     - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
     - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，一条数据流出任务最多支持选择 5 个源 Topic，选中的 Topic 内的数据格式需要保持一致方可转储成功。详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
   - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
   >? 目前解析消息需要满足以下条件：
   >
   >- 消息为 JSON 字符串结构。
   >- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。 
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f7e7312ad85b3342c57d8b587ac90241.png)
   - 目标存储桶：选择数据投递的目标存储桶。
   - 目录前缀：支持自定义目录前缀，日志文件会投递至对象存储 Bucket 的该目录下。
   - 分区格式：将投递任务创建时间按照 strftime 的语法自动生成目录 ，其中斜线`/`表示一级 COS 目录。
     分区格式请按照 [strftime 格式](http://man7.org/linux/man-pages/man3/strptime.3.html) 要求填写，不同的分区格式会影响投递到对象存储的文件路径。 以下举例说明分区格式的用法，例如投递至 bucket_test 存储桶，目录前缀为`logset/`，投递时间 2018/7/31 17:14，则对应的投递文件路径如下：
<table>
<thead>
<tr>
<th align="left">存储桶名称</th>
<th align="left">目录前缀</th>
<th align="left">分区格式</th>
<th align="left">COS 文件路径</th>
</tr>
</thead>
<tbody><tr>
<td align="left">bucket_test</td>
<td align="left">logset/</td>
<td align="left">%Y/%m/%d</td>
<td align="left">bucket_test:logset/2018/7/31_{random}_{index}</td>
</tr>
<tr>
<td align="left">bucket_test</td>
<td align="left">logset/</td>
<td align="left">%Y%m%d/%H</td>
<td align="left">bucket_test:logset/20180731/14_{random}_{index}</td>
</tr>
<tr>
<td align="left">bucket_test</td>
<td align="left">logset/</td>
<td align="left">%Y%m%d/log</td>
<td align="left">bucket_test:logset/20180731/log_{random}_{index}</td>
</tr>
</tbody></table>
   - 单文件大小：指定在该投递时间间隔中未压缩的投递文件上限，意味着在该时间间隔中，日志文件最大将为您设置的值，超过该上限，将被分成多个日志文件。
   - 存储格式：支持 CSV 和 JSON 格式。
   - 角色授权：使用对象存储（COS）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。
   ![](https://qcloudimg.tencent-cloud.cn/raw/2fadc80777e4f3b674e810a9252865c9.png)



