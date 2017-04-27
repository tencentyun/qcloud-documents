# 数据订阅SDK下载
[点击下载][1]

# 数据订阅SDK示例代码简介
---
使用腾讯云Binlog订阅示例代码如下：
```
public class Main {
	
	public static void main(String[] args) throws Exception {
		//创建一个context
		SubscribeContext context=new SubscribeContext();
		
		//用户secretId、secretKey
		context.setSecretId("AKID-522dabaa14dceed746ba8ccfb58e9e6f");
		context.setSecretKey("AKEY-0ff4c4557c1183fc572baecfa505869d");

		//订阅的serviceIp和servicePort
		context.setServiceIp("10.108.112.24");
		context.setServicePort(50120);
			
		//创建客户端
		SubscribeClient client=new DefaultSubscribeClient(context);
			//创建订阅listener
			ClusterListener listener= new ClusterListener() {
			@Override
			public void notify(List<ClusterMessage> messages) throws Exception {
				//消费订阅到的数据
				for(ClusterMessage m:messages){
					for(Record.Field f:m.getRecord().getFieldList()){
						if(f.getFieldname().equals("id")){
							System.out.println("seq:"+f.getValue());
						}
					}
					//消费完之后，确认消费
					m.ackAsConsumed();   
				}  
			}
			@Override
			public void onException(Exception e){
				System.out.println("listen exception"+e);
			}};
		//添加监听者
		client.addClusterListener(listener);
		//设置请求的订阅通道
		client.askForGUID("dts-channel-B2eG8xbLvi472wV3");
		//启动客户端
		client.start();
	}
}
```
整个流程是个典型的生产者消费者模型，SDK作为消费者不断地从服务器拉取订阅的Binlog数据，消费数据，消费完确认消费完数据，比较直观：
 1. 首先配置参数，创建消费客户端`SubscribeClient`
 2. 然后创建一个监听器`ClusterListener`，消费收到的Binlog订阅数据，消费完之后返回确认消息
 3. 最后启动客户端，开始流程
在监听器`ClusterListener`中，可以根据用户自身的需求，对收到的数据进行操作，还可以对收到Binlog数据根据类型进行过滤，比如过滤掉所有`drop`语句等。
 
 注意到示例代码中，用户需要提供五个参数。其中，`secretId`和`secretKey`是跟用户腾讯云帐号关联的密钥值，可以在腾讯云管理中心-->云产品-->云API密钥-->API密钥中查看，SDK用这两个两个参数来对用户操作进行鉴权；另外三个参数`serviceIp` `servicePort` `channelId`都是与用户Binlog订阅相关的，在腾讯云CDB for MySQL相应页面配置好订阅内容后，会展示在控制台上，具体操作步骤请参考控制台操作指引。

# SDK API说明
---
## SubscribeContext类
---
### 类说明
主要用于设置用户SDK的配置信息，其中包括安全凭证secretId，secretKey，订阅服务的IP和端口。

### 构造方法
public SubscribeContext()

### 类方法

#### **设置安全凭证secretId**
---
##### 函数原型
public void setSecretId(String secretId)

##### 输入参数

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| secretId | String| 安全凭证secretId，可以在腾讯云管理中心-->云产品-->云API密钥-->API密钥中查看 |

##### 返回结果
无
##### 抛出异常
无

#### **设置安全凭证secretKey**
---
##### 函数原型
public void setSecretKey(String secretKey)

##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| secretKey| String| 安全凭证secretKey，可以在腾讯云管理中心-->云产品-->云API密钥-->API密钥中查看 |

##### 返回结果
无
##### 抛出异常
无

#### **设置订阅服务的IP地址**
---
##### 函数原型
public void setServiceIp(String serviceIp)

##### 输入参数

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| serviceIp| String| 订阅服务的IP地址，可以在控制台的订阅通道配置页面查看 |

##### 返回结果
无
##### 抛出异常
无

#### **设置订阅服务的端口**
---
##### 函数原型
public void setServicePort(String servicePort)

##### 输入参数

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| servicePort| String| 订阅服务的端口号，可以在控制台的订阅通道配置页面查看 |

##### 返回结果
无
##### 抛出异常
无



## SubscribeClient接口和DefaultSubscribeClient接口
---
`DefaultSubscribeClient`类实现了`SubscribeClient`接口
###类说明
用于构建订阅SDK的客户端程序，也就是Binlog消息的消费者。

`DefaultSubscribeClient`根据用户的需求提供了同步确认和异步确认的两种实现。在同步的情况下，在每次客户端消费完Binlog消息之后，同步地确认已经收到的消息，这样确保了确认完的消息服务器可以尽快收到，此种模式下SDK整体性能不如异步确认的方式；在异步的情况下，消费者程序异步确认消息，也就是拉取消息和确认消息异步执行，相互不影响，性能比同步确认好。用户可以根据需求选择不同的确认模式。

### 构造方法
#### **构造DefaultSubscribeClient**
---
##### 函数原型
public DefaultSubscribeClient(SubscribeContext context, boolean isSync) throws Exception
##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| context| SubscribeContext| 用户SDK的配置信息 |
| isSynce | boolean | 表示SDK是否使用同步消费模式 |

##### 返回结果
`DefaultSubscribeClient`实例

##### 抛出异常

 - 	IllegalArgumentException：如果用户提交的参数context，有参数不合理将抛此异常。不合理包括：没有安全凭证或者格式出错，没有服务的IP和端口，或者格式出错。
 - Excetion：如果SDK内部初始化出错，将抛Exception异常。
 
#### **构造DefaultSubscribeClient**
---
##### 函数原型
public DefaultSubscribeClient(SubscribeContext context) throws Exception

##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| context| SubscribeContext| 用户SDK的配置信息 |

##### 返回结果
`DefaultSubscribeClient`实例，默认为异步确认消息

##### 抛出异常

 - 	IllegalArgumentException：如果用户提交的参数context，有参数不合理将抛此异常。不合理包括：没有安全凭证或者格式出错，没有服务的IP和端口，或者格式出错。
 - Excetion：如果SDK内部初始化出错，将抛Exception异常。
 
### 类方法
#### **添加SDK消费客户端的监听者**
---
##### 函数说明
将监听者`ClusterListener`加入到一个`SubscribeClient`中，才可以订阅通道中的增量数据
##### 函数原型
public void addClusterListener(ClusterListener listener) throws Exception

##### 输入参数

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| listener| ClusterListener| 消费客户端需要使用的监听者，消费Binlog消息的主流程应该实现在`ClusterListener`这里面 |

##### 返回结果
无
##### 抛出异常

 - IllegalArgumentException：如果用户提交的参数listener为空，将抛IllegalArgumentException异常。
 - Exception：当前SDK暂时仅支持一个Listener，如果加入多个监听者，将抛Exception异常。
 
#### **请求某个订阅通道的增量数据**
---
##### 函数原型
public void askForGUID(String channelId)

##### 输入参数

| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| channelId| String| 订阅通道的ID，可以在控制台的订阅通道配置页面查看 |

##### 返回结果
无

##### 抛出异常
无

#### **启动SDK客户端**
---
##### 函数原型
public void start() throws Exception

##### 输入参数

无

##### 返回结果
无

##### 抛出异常

 - Exception：如果SDK内部启动出错，将抛Exception异常

#### **停止SDK客户端**
---
##### 函数原型
public void stop() throws Exception

##### 输入参数

无

##### 返回结果
无

##### 抛出异常

 - Exception：如果SDK内部关闭出错，将抛Exception异常

## ClusterListener接口
---
### 接口说明
这是一个回调接口，SDK用户需要实现这个接口的notify函数消费订阅数据，另外通过实现onException函数来处理消费过程中可能出现的异常。
### 接口函数
#### **通知SDK消费客户端订阅消息**
---
##### 函数说明
主要用来实现对增量数据的消费，但SDK接收到数据时，会通过notify通知ClusterListener消费数据
##### 函数原型
public abstract void notify(List<ClusterMessage> messages) throws Exception

##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| messages| List<ClusterMessage>| 订阅数据数组，ClusterMessage具体实现详见其定义 |

##### 返回结果
无

##### 抛出异常

消费订阅数据时，如果有异常会抛到用户实现的onException函数中，用户可以根据需求自行处理。

#### **消费订阅数据时的异常处理**
---
##### 函数说明
主要用来实现对消费订阅数据时的异常处理，用户在onException可以自己实现自己的安全退出策略。

##### 函数原型
public abstract void onException(Exception exception)

##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| exception| Exception| Java标准库中的Exception类 |

##### 返回结果
无

##### 抛出异常
无

## ClusterMessage类
---
### 类说明
类ClusterMessage将通过notify函数传递消费的订阅数据。每个ClusterMessage保存CDB for MySQL中的一个**事务**的数据记录，事务中的每条记录通过Record保存。

### 类方法
#### **从ClusterMessage中获取记录**
---
##### 函数原型
public Record getRecord()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
| Record | 变更记录，对应某个事务中某条具体的记录，比如begin，commit，update，insert等|

##### 抛出异常
无


#### **确认消费完的数据**
---
##### 函数说明
用于向订阅服务器确认已消费完的数据，根据在SubscribeClient中设置的值，此函数执行同步或者异步的消息确认。用户消费完之后一定要调用这个数据，否则可能影响正常的逻辑，SDK会收到重复的数据。

##### 函数原型
public void ackAsConsumed() throws Exception

##### 输入参数
无

##### 返回结果
无

##### 抛出异常

 - Exception：如果确认过程出现内部错误，将抛出异常。

## Record类
---
### 类说明
表示订阅的Binlog数据中的某一条记录，通常是某个事务`ClusterMessage`的成员，记录可能是begin，commit，update语句等。

### 类方法
#### **获取Record的属性值**
----
##### 函数原型
public String getAttribute(String key)

##### 输入参数
| 参数名 | 类型 | 参数含义 |
|:-------------:|:-------------|:-------------|
| key| String| 属性值的名称 |

可能的属性键值为：
| 属性键值Key | 说明 |
|:-------------|:-------------|
|record_id |	Record的ID，这个ID在订阅过程中不保证递增|
|source_type |	Record对应数据库实例的引擎类型，目前取值为：mysql|
|source_category |	Record的类型，目前取值为：full_recorded|
|timestamp |	Record落binlog的时间，这个时间同时也是这条SQL在RDS中执行的时间|
|checkpoint | Record对应的binlog文件的位点，格式为:file_offset@file_name，filen_name为binlog文件的数字后缀|
|record_type | Record对应的操作类型，主要取值包括：insert/update/delete/replace/ddl/begin/commit/heartbeat |
|db 	|Record更新表，对应的数据库名|
|table_name |	Record更新表的表名|
|record_encoding|	Record对应的编码|
|primary |	 Record更新表的主键列名|
|fields_enc |	Record每个字段值的编码，各个字段之间用逗号隔开，如果非字符类型那么取值为空|


##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
| String| 属性值 |

##### 抛出异常
无


#### **获取记录的变更类型**
---
##### 函数原型
public DataMessage.Record.Type getOpt()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
| DataMessage.Record.Type| 记录类型 |

DataMessage.Record.Type可能的取值包括：insert、delete、update、replace、ddl、begin、commit、heartbeat。其中heartbeat为数据传输内部定义的心跳表，主要用于检查订阅通道是否健康，理论上每秒都会产生一条 heartbeat。

##### 抛出异常
无


#### **获取记录的在Binlog中的Checkpoint**
---
##### 函数原型
public String getCheckpoint()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
| String| 记录在Binlog中的Checkpoint，格式为:binlog_offset@binlog_fid。其中binlog_offset为变更记录在binlog文件中的偏移量，binlog_fid为binlog文件名。|

##### 抛出异常
无

#### **获取记录的在Binlog中的时间戳**
---
##### 函数原型
public String getTimestamp()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|时间戳字符串|

##### 抛出异常
无


#### **获取记录的对应的数据库名称**
---
##### 函数原型
public String getDbname()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|数据库名称字符串|

##### 抛出异常
无

#### **获取记录的对应的数据表名称**
---
##### 函数原型
public String getTableName()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|数据表名称字符串|

##### 抛出异常
无


#### **获取记录的对应的主键列名**
---
##### 函数原型
public String getPrimaryKeys()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|主键列名，如果是联合主键，这些列名之间用逗号分隔|

##### 抛出异常
无

#### **获取订阅实例的数据库类型**
---
##### 函数原型
public DBType getDbType()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|DBType|目前数据传输仅支持CDB for MySQL，为DBType.MYSQL|

##### 抛出异常
无

#### **获取Record的字段个数**
---
##### 函数原型
public int getFieldCount()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|int|Record字段的个数|

##### 抛出异常
无

#### **判断Record是否是事务中的第一条记录**
---
##### 函数原型
public Boolean isFirstInLogevent()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|Boolean|如果是事务中的第一条日志，返回True，否则返回False|

##### 抛出异常
无

#### **获取记录对应表的字段定义列表**
---
##### 函数原型
public List<Field> getFieldList()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|List<Field>|Field数组，具体见Field类定义|

##### 抛出异常
无

## Field类
---
### 类说明
Field类定义了每个字段的编码、类型、字段名、字段值以及是否为主键等属性。

### 类方法
#### **获取字段的编码格式**
----
##### 函数原型
public String getFieldEnc()

##### 输入参数
无
##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|String类型的字段编码|

##### 抛出异常
无

#### **获取字段名称**
----
##### 函数原型
public String getFieldname()

##### 输入参数
无
##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|String|String类型的字段名称|

##### 抛出异常
无


#### **获取字段的数据类型**
----
##### 函数原型
public Field.Type getType()

##### 输入参数
无

##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|Field.Type|Field.Type是一个枚举类型，对应MySQL支持的数据类型，包括：INT8,INT16,INT24,INT32,INT64,DECIMAL,FLOAT,DOUBLE,NULL,TIMESTAMP, DATE,TIME,DATETIME,YEAR,BIT,ENUM,SET,BLOB,GEOMETRY,STRING,UNKOWN;|

##### 抛出异常
无


#### **获取字段的值**
----
##### 函数原型
public ByteString getFieldname()

##### 输入参数
无
##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|ByteString|字段的值，当值为空时，值为NULL|

##### 抛出异常
无



#### **判断字段是否为主键**
----
##### 函数原型
public Boolean isPrimary()

##### 输入参数
无
##### 返回结果
| 类型 | 参数含义 |
|:-------------|:-------------|
|Boolean|如果字段为主键，返回True，否则返回False|

##### 抛出异常
无

[1]:	//mc.qcloudimg.com/static/archive/376dde7c54ff6cf025465008ea08e47f/binlogsdk-2.1.0.jar.zip