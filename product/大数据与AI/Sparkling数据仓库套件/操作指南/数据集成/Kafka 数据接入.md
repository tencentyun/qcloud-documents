本节将介绍 CKafka 数据接入方法。更多关于 CKafka 的信息请参见 [CKafka 产品介绍](https://cloud.tencent.com/document/product/597)。

## 操作步骤
登录 [Sparkling 控制台](https://sparkling.cloud.tencent.com)，在左侧导航单击【数据】进入数据接入页面，按以下操作步骤完成 Kafka 数据接入：
![](https://main.qcloudimg.com/raw/479a826c040c8251d96e52c7fad326c0.png)

### 1. 数据源配置
选择【Kafka】数据类型，支持【新建数据源】和【接入已有数据源】两种数据源接入方式。

- **新建数据源方式**
   a. 接入方式选择【新建数据源】。
	 b. 数据源部署方式选择腾讯云 CKafka。
	 c. 填写腾讯云 CKafka 实例 ID（可在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 获取）及  CKafka 创建者 UIN（实例创建者在 [账号信息](https://console.cloud.tencent.com/developer) 中的账号 ID）。
	 d. 单击【角色服务授权】，授权 Sparkling 服务访问其他相应服务。
	 ![](https://main.qcloudimg.com/raw/87ec4e2aeddf3ec47597a9dabb006039.png)
   e. 填写要接入的 Topic 。
   f. 选择【连通测试】>【测试连通性】确认是否可以连接到要接入的 Topic 所在的 CKafka。
   g. 待显示【数据连通正常】后，可以选择【保存数据源】选项将该数据源保存为已有数据源，待下次接入该数据源时可采用【接入已有数据源】方式。
	 ![](https://main.qcloudimg.com/raw/411c8491b23786dafcf50c20bfcb41b8.png)
   h. 单击高级配置开关按钮可以配置读取开始 OFFset，可以根据需求选择数据订阅是否忽略历史消息。
	 ![](https://main.qcloudimg.com/raw/a962c4bdf687ba5cc8582ee048054845.png)
   i. 填写 Schema 名称及添加字段。CKafka 数据需要用户指定数据 Schema 格式，您可以采用 Web 标注向导或上传 Schema 脚本方式指定，两种方式可以相互切换。
	 j. 填写完毕后单击【预览】可以查看数据预览，预览无误后单击【下一步】完成数据源配置操作。

- **接入已有数据源方式**
   a. 接入方式选择【接入已有数据源】。
	 b. 选择历史保存的已有数据源。
	 c. 输入 Topic 后的操作同 “新建数据源方式” 的步骤 h - j。
![](https://main.qcloudimg.com/raw/ef8584cefadfc4ba562a68ceb1c25232.png)
 
### 2. 目标配置
支持【新建表】方式目标配置。

a. 选择【新建表】并填写【标题】和【描述】。
b. 字段定义及分区部分可以设置字段名、描述及字段顺序，支持字段裁剪（可通过删除字段实现仅导入部分字段功能）。其中第一列“pt”列为默认分区字段，不支持删除操作，默认以该时间戳作为分区值。
c. 选择格式类型，支持【ORCFILE】和【PARQUET】两种格式。
d. 确认无误后，单击【下一步】完成新建表方式目标配置操作。
![](https://main.qcloudimg.com/raw/a0e2c96234a9266b88c33fd5ca0ec5be.png)

### 3. 订阅任务配置
a. 填写抽取条件。参考 SQL 语法填写 WHERE 后的过滤语句，不包括 “WHERE” 字段，如图所示筛选 name 为123的数据。
b. 设置起始时刻。将从该时刻开始进行数据导入任务调度。
c. 设置执行时长。设置该任务持续时间。
d. 设置单次数据条目。设置任务单次导入的数据条目，选择不限制表示单次导入当前阶段的所有最新数据。
![](https://main.qcloudimg.com/raw/9d30754a9c9eb82c858dd5ac578d5e3a.png)

### 4. 预览
在【预览】页可以查看当前设置的数据源配置、目标表配置、抽取规则、订阅任务配置等信息。确认无误后单击【完成】即可完成 Kafka 数据接入任务设置。
<img src="https://main.qcloudimg.com/raw/a974f8b545cc2130af91b53b13e33f71.png" style="zoom:70%">

