
## SubscribeContext 类

### 类说明
主要用于设置用户 SDK 的配置信息，其中包括安全凭证 secretId、secretKey、订阅服务的 IP 和端口。

### 构造方法
public SubscribeContext()

### 类方法
#### 设置安全凭证 secretId
**函数原型**
public void setSecretId(String secretId)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------| 
| secretId | String| 安全凭证secretId，可以在控制台的【访问管理】>【访问密钥】>【API密钥管理】查看 |

**返回结果**
无

**抛出异常**
无

#### 设置安全凭证 secretKey

**函数原型**
public void setSecretKey(String secretKey)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| secretKey| String| 安全凭证 secretKey，可以在控制台的【访问管理】>【访问密钥】>【API密钥管理】查看 |

**返回结果**
无

**抛出异常**
无


#### 设置订阅服务的 IP 地址

**函数原型**
public void setServiceIp(String serviceIp)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| serviceIp| String| 订阅服务的 IP 地址，可以在控制台的订阅通道配置页面查看 |

**返回结果**
无

**抛出异常**
无


#### 设置订阅服务的端口

**函数原型**
public void setServicePort(String servicePort)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| servicePort| String| 订阅服务的端口号，可以在控制台的订阅通道配置页面查看 |

**返回结果**
无

**抛出异常**
无


## SubscribeClient 接口和 DefaultSubscribeClient 接口
### 类说明
DefaultSubscribeClient 类实现了 SubscribeClient 接口。
用于构建订阅 SDK 的客户端程序，也就是 Binlog 消息的消费者。

DefaultSubscribeClient 根据用户的需求提供了同步确认和异步确认的两种实现。在同步的情况下，在每次客户端消费完 Binlog 消息之后，同步地确认已经收到的消息，这样确保了确认完的消息服务器可以尽快收到，此种模式下 SDK 整体性能不如异步确认的方式；在异步的情况下，消费者程序异步确认消息，也就是拉取消息和确认消息异步执行，相互不影响，性能比同步确认好。用户可以根据需求选择不同的确认模式。

### 构造方法
#### 构造 DefaultSubscribeClient

**函数原型**
public DefaultSubscribeClient(SubscribeContext context, boolean isSync) throws Exception

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| context| SubscribeContext| 用户 SDK 的配置信息 |
| isSynce | boolean | 表示 SDK 是否使用同步消费模式 |

**返回结果**
 DefaultSubscribeClient 实例
 
**抛出异常**
 - 	IllegalArgumentException：如果用户提交的参数 context，有参数不合理将抛此异常。不合理包括：没有安全凭证或者格式出错，没有服务的 IP 和端口，或者格式出错。
 - Excetion：如果 SDK 内部初始化出错，将抛 Exception 异常。
  
	
#### 构造 DefaultSubscribeClient

**函数原型**
public DefaultSubscribeClient(SubscribeContext context) throws Exception

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| context| SubscribeContext| 用户 SDK 的配置信息 |

**返回结果**
DefaultSubscribeClient 实例，默认为异步确认消息

**抛出异常**
 - 	IllegalArgumentException：如果用户提交的参数 context，有参数不合理将抛此异常。不合理包括：没有安全凭证或者格式出错，没有服务的 IP 和端口，或者格式出错。
 - Excetion：如果 SDK 内部初始化出错，将抛 Exception 异常。
 
### 类方法
#### 添加 SDK 消费客户端的监听者

**函数说明**
将监听者 ClusterListener 加入到一个 SubscribeClient 中，才可以订阅通道中的增量数据。

**函数原型**
public void addClusterListener(ClusterListener listener) throws Exception

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| listener| ClusterListener| 消费客户端需要使用的监听者，消费 Binlog 消息的主流程应该实现在`ClusterListener`这里面 |

**返回结果**
无

**抛出异常**
 - IllegalArgumentException：如果用户提交的参数 listener 为空，将抛 IllegalArgumentException 异常。
 - Exception：当前 SDK 暂时仅支持一个 Listener，如果加入多个监听者，将抛 Exception 异常。

 
#### 请求某个订阅通道的增量数据

**函数原型**
public void askForGUID(String channelId)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| channelId| String| 订阅通道的 ID，可以在控制台的订阅通道配置页面查看 |

**返回结果**
无

**抛出异常**
无


#### 启动 SDK 客户端

**函数原型**
public void start() throws Exception

**输入参数**
无

**返回结果**
无

**抛出异常**
Exception：如果 SDK 内部启动出错，将抛 Exception 异常。


#### 停止 SDK 客户端

**函数原型**
public void stop(int waitSeconds) throws Exception
public void stop() throws Exception

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| waitSeconds | int| 等待时间，单位为秒，表示等待多久开始强制停止 SDK 的运行 |

其中，不带参数的 stop 函数会耐心等待线程停止，可能等待的时间较长，具体时间由系统的调度决定；建议对重启时间有要求的场景，始终使用带超时时间的 stop 函数。

**返回结果**
无

**抛出异常**
Exception：如果 SDK 内部关闭出错，将抛 Exception 异常。

## ClusterListener 接口

### 接口说明
这是一个回调接口，SDK 用户需要实现这个接口的 notify 函数消费订阅数据，另外通过实现 onException 函数来处理消费过程中可能出现的异常。

### 接口函数
### 通知 SDK 消费客户端订阅消息

**函数说明**
主要用来实现对增量数据的消费，但 SDK 接收到数据时，会通过 notify 通知 ClusterListener 消费数据。
**函数原型**
public abstract void notify(List&lt;ClusterMessage&gt; messages) throws Exception

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| messages| List&lt;ClusterMessage&gt;| 订阅数据数组，ClusterMessage 具体实现详见其定义 |

**返回结果**
无

**抛出异常**
消费订阅数据时，如果有异常会抛到用户实现的 onException 函数中，用户可以根据需求自行处理。

### 消费订阅数据时的异常处理

**函数说明**
主要用来实现对消费订阅数据时的异常处理，用户在 onException 可以自己实现自己的安全退出策略。

**函数原型**
public abstract void onException(Exception exception)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| exception| Exception| Java标准库中的 Exception 类 |

**返回结果**
无

**抛出异常**
无

## ClusterMessage 类
### 类说明
类 ClusterMessage 将通过 notify 函数传递消费的订阅数据。每个 ClusterMessage 保存 TencentDB for MySQL 中的一个**事务**的数据记录，事务中的每条记录通过 Record 保存。

### 类方法

#### 从 ClusterMessage 中获取记录

**函数原型**
public Record getRecord()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
| Record | 变更记录，对应某个事务中某条具体的记录，比如 begin，commit，update，insert 等|

**抛出异常**
无


#### 确认消费完的数据

**函数说明**

用于向订阅服务器确认已消费完的数据，根据在 SubscribeClient 中设置的值，此函数执行同步或者异步的消息确认。用户消费完之后一定要调用这个数据，否则可能影响正常的逻辑，SDK 会收到重复的数据。

>!这里 SDK 收到的所有消息都必须调用 ackAsConsumed，包括业务逻辑可能不关心的数据，否则 SDK 在获取一定的数据之后不会再拉取新的数据。

**函数原型**
public void ackAsConsumed() throws Exception

**输入参数**
无

**返回结果**
无

**抛出异常**
Exception：如果确认过程出现内部错误，将抛出异常。

## Record 类

### 类说明
表示订阅的 Binlog 数据中的某一条记录，通常是某个事务 ClusterMessage 的成员，记录可能是 begin，commit，update 语句等。

### 类方法
#### 获取 Record 的属性值

**函数原型**
public String getAttribute(String key)

**输入参数**

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| key| String| 属性值的名称 |
可能的属性键值为：

| 属性键值 Key | 说明 |
|:-------------|:-------------|
|record_id |	Record 的 ID，这个 ID 在通道内按字符串比较自增有序，不保证连续 |
|source_type |	Record 对应数据库实例的引擎类型，目前取值为：mysql|
|source_category |	Record 的类型，目前取值为：full_recorded|
|timestamp |	Record 落 binlog 的时间，这个时间同时也是这条 SQL 在 TencentDB 中执行的时间|
|sdkInfo | Record 对应的 binlog 文件的位点，格式为：file_offset@file_name，filen_name为binlog文件的数字后缀|
|record_type | Record 对应的操作类型，主要取值包括：insert/update/delete/replace/ddl/begin/commit/heartbeat |
|db 	|Record 更新表，对应的数据库名；DDL 类型的记录，此字段为空|
|table_name |	Record 更新表的表名；DDL 类型的记录，此字段为空|
|record_encoding|	Record 对应的编码|
|primary |	 Record 更新表的主键列名|
|fields_enc |	Record 每个字段值的编码，各个字段之间用逗号隔开，如果非字符类型那么取值为空|
|gtid |	Record 所在事务的 GTID 值 |


**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
| String| 属性值 |

**抛出异常**
无

#### **获取记录的变更类型**

**函数原型**
public DataMessage.Record.Type getOpt()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
| DataMessage.Record.Type| 记录类型 DataMessage.Record.Type 可能的取值包括：insert、delete、update、replace、ddl、begin、commit、heartbeat。其中 heartbeat 为数据传输内部定义的心跳表，主要用于检查订阅通道是否健康，理论上每秒都会产生一条 heartbeat。

**抛出异常**
无


#### 获取记录的在 Binlog 中的 Checkpoint

**函数原型**
public String getCheckpoint()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
| String| 记录在 Binlog 中的 Checkpoint，格式为：binlog_offset@binlog_fid。其中 binlog_offset 为变更记录在 binlog 文件中的偏移量，binlog_fid 为 binlog 文件名。|

**抛出异常**
无


#### 获取记录的在 Binlog 中的时间戳

** 函数原型**
public String getTimestamp()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|时间戳字符串|

**抛出异常**
无


#### 获取记录的对应的数据库名称

**函数原型**
public String getDbname()

**输入参数**
无

** 返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|数据库名称字符串|

**抛出异常**
无


#### 获取记录的对应的数据表名称

**函数原型**
public String getTableName()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|数据表名称字符串|

**抛出异常**
无


#### 获取记录的对应的主键列名

**函数原型**
public String getPrimaryKeys()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|主键列名，如果是联合主键，这些列名之间用逗号分隔|

**抛出异常**
无

#### 获取订阅实例的数据库类型

**函数原型**
public DBType getDbType()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|DBType|目前数据传输仅支持 TencentDB for MySQL，为 DBType.MYSQL|

**抛出异常**
无


#### 获取 Record 的字段个数

**函数原型**
public int getFieldCount()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|int|Record字段的个数，与该字段对应的表的列数相等，或者是列数的两倍（对于更新操作的 Record） |

**抛出异常**
无

#### 判断 Record 是否是事务中的第一条记录

**函数原型**
public Boolean isFirstInLogevent()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|Boolean|如果是事务中的第一条日志，返回 True，否则返回 False|

**抛出异常**
无


#### 获取记录对应表的字段定义列表

**函数原型**
public List&lt;Field&gt; getFieldList()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|List&lt;Field&gt;|Field 数组，具体见 Field 类定义|

>!
- 对于 INSERT 类型的记录，List 中 Field 是按订阅表的定义顺序按序对应，Field 中记录的值是插入的值，也即是后镜像。
- 对于 DELETE 类型的记录，List 中 Field 是按订阅表的定义顺序按序对应，Field 中记录的值是删除前的值，也即是前镜像。
- 对于 UPDATE 类型的记录，List 中包含修改前后的值，也即是同时包含前镜像、后镜像；其中前镜像（ 修改前的值 ）在list的偶数位，后镜像在list的奇数位；前镜像、后镜像的列表也与订阅表的定义顺序按序对应，因而此时 List 中 Field 的数量是对应订阅表列数的两倍。

**抛出异常**
无

## Field 类

### 类说明
Field 类定义了每个字段的编码、类型、字段名、字段值以及是否为主键等属性。

### 类方法
#### 获取字段的编码格式

**函数原型**
public String getFieldEnc()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|String 类型的字段编码|

**抛出异常**
无


#### 获取字段名称

**函数原型**
public String getFieldname()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|String|String 类型的字段名称|

**抛出异常**
无


#### 获取字段的数据类型

**函数原型**
public Field.Type getType()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|Field.Type|Field.Type 是一个枚举类型，对应 MySQL 支持的数据类型，包括： INT8, INT16, INT24, INT32, INT64, DECIMAL, FLOAT, DOUBLE, NULL, TIMESTAMP,  DATE, TIME, DATETIME, YEAR, BIT, ENUM, SET, BLOB, GEOMETRY, STRING, UNKOWN|

**抛出异常**
无


#### 获取字段的值

**函数原型**
public ByteString getFieldname()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|ByteString|字段的值，当值为空时，值为NULL|

**抛出异常**
无


#### 判断字段是否为主键

**函数原型**
public Boolean isPrimary()

**输入参数**
无

**返回结果**

| 类型 | 参数含义 |
|:-------------|:-------------|
|Boolean|如果字段为主键，返回 True，否则返回 False|

**抛出异常**
无

