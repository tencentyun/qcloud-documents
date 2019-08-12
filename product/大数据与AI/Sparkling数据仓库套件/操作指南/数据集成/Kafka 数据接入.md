## 操作场景

云数据仓库套件 Sparkling 支持多样化的数据接入方式和数据源管理。数据接入方式包括：

- 关系型数据库（RDBMS）接入：可以通过 RDBMS 数据接入方式将云数据库 MySQL 、分布式数据库 TDSQL 中的数据接入到 Sparkling 中。
- 腾讯云对象存储（COS）数据接入：可以通过生成账户密钥，建立存储桶（bucket）的方式进行 COS 数据接入。
- 腾讯云消息队列（CKafka）数据接入：可以通过 Kafka 数据接入方式将腾讯云 CKafka 中的数据接入 Sparkling 中。

本节将介绍 CKafka 数据接入方法。更多关于 CKafka 的信息请参见 [CKafka 产品介绍](https://cloud.tencent.com/document/product/597/10066)。

## 操作步骤

登录 [Sparkling 控制台](https://sparkling.cloud.tencent.com)，在左侧导航单击【数据】进入数据接入页面，按以下操作步骤完成 Kafka 数据接入：
![](https://main.qcloudimg.com/raw/009acb9b28f03361d74cf10417a16d3d.png)

### 1. 数据源配置

选择【Kafka】数据类型，支持【新建数据源】和【接入已有数据源】两种数据源接入方式。

- **新建数据源方式**
  a. 接入方式选择【新建数据源】。
   b. 数据源部署方式选择腾讯云 CKafka。
   c. 填写腾讯云 CKafka 实例 ID（可在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 获取）及  CKafka 创建者 UIN（实例创建者在 [账号信息](https://console.cloud.tencent.com/developer) 中的账号 ID）。
   d. 单击角色服务授权，授权 Sparkling 服务访问其他相应服务。
   ![](https://main.qcloudimg.com/raw/87ec4e2aeddf3ec47597a9dabb006039.png)
  e. 填写要接入的 Topic 。
  f. 单击【测试连通性】确认是否可以连接到要接入的 Topic 所在的 CKafka。
  g. 待显示【数据连通正常】后，可以选择【保存数据源】选项将该数据源保存为已有数据源，待下次接入该数据源时可采用【接入已有数据源】方式。
   ![](https://main.qcloudimg.com/raw/411c8491b23786dafcf50c20bfcb41b8.png)
  h. 数据源高级配置。
  - 选择当前数据编码格式：目前 Sparkling 支持 AVRO、JSON、CSV 三种编码格式。CSV 编码格式下可以设置字段分隔符：目前可以使用“,”、“\t”、空格、“|”、“;”等），不支持“\n”、“\*”等分隔符。
  - 配置读取开始 OFFset，可以根据需求选择数据订阅是否忽略历史消息或从最开始订阅数据。如果数据量比较大，从最开始订阅数据时会耗用比较长时间。
  - 选择 Rcord Key：目前 Sparkling 只采用用户自定义 Schema 解析 Value 部分。
    ![](https://main.qcloudimg.com/raw/ba355a6ab9d79136b45b4fe4fa78ec91.png)

 i. 指定数据 Schema 格式。 
	 - AVRO 格式目前支持 Web 标注向导或上传 Schema 脚本方式指定，两种方式可以相互切换。
		 - 标注向导
		 用户需要输入Schema 名称及添加字段。完成添加字段后会自动生成 Schema 脚本，单击【Schema 脚本】即可查看。
		 ![](https://main.qcloudimg.com/raw/e3f0aabe692bb3a1902ccf994f272d11.png)
		 - Schema 脚本
		 用户可手动输入Schema 脚本。手动完成输入之后，会自动在【标注向导】生成对应字段。
		![](https://main.qcloudimg.com/raw/2434402d48a4e3ec79ebec0be20157a0.png)
		
		>?JSON 和 CSV 格式目前只支持用户手动添加字段。CSV 格式下可以在第四列输入该字段所处序列（排序默认从0开始）。

 j. 填写完毕后单击【预览】可以查看数据预览，预览无误后单击【下一步】完成数据源配置操作。
![](https://main.qcloudimg.com/raw/a74bb43f0bdb8f8e94b087ef3e5ebbbd.png)

- **接入已有数据源方式**
  a. 接入方式选择【接入已有数据源】。
   b. 选择历史保存的已有数据源。
   c. 输入 Topic 后的操作同“新建数据源方式”的步骤 h - j。
  ![](https://main.qcloudimg.com/raw/c1a1293eebce3752c7e50893d88acdb5.png)

### 2. 目标配置

目前支持【新建表】方式目标配置。

a. 选择【新建表】并填写【标题】和【描述】。
b. 字段定义及分区部分可以设置字段名、描述及字段顺序，支持字段裁剪（可通过删除字段实现仅导入部分字段功能）。其中第一列“pt”列为默认分区字段，不支持删除操作，默认以该时间戳作为分区值。
c. 选择格式类型，支持【ORCFILE】和【PARQUET】两种格式。
d. 确认无误后，单击【下一步】完成新建表方式目标配置操作。
![](https://main.qcloudimg.com/raw/a0e2c96234a9266b88c33fd5ca0ec5be.png)

### 3. 订阅任务配置

a. 填写抽取条件。参考 SQL 语法填写 WHERE 后的过滤语句，不包括“WHERE”字段，如图所示筛选 name 为123的数据。
b. 设置起始时刻。将从该时刻开始进行数据导入任务调度。
c. 设置执行时长。设置该任务持续时间。
d. 设置单次数据条目。设置任务单次导入的数据条目，选择不限制表示单次导入当前阶段的所有最新数据。
![](https://main.qcloudimg.com/raw/9d30754a9c9eb82c858dd5ac578d5e3a.png)

### 4. 预览

在【预览】页可以查看当前设置的数据源配置、目标表配置、抽取规则、订阅任务配置等信息。
![](https://main.qcloudimg.com/raw/de92830243973747b9c2bc101abf238b.png)
确认无误后单击【完成】即可完成 Kafka 数据接入任务设置。
