# Downloading Data Subscription SDK
[Click to Download][1]

## Logs Released by SDK
### Version 2.6.0
1. Multiple channels can be subscribed via a single SDK.
2. Subscription of "stop", "start" and other operations performed on Client is supported.
3. Serialization of DataMessage.Record is supported.
4. SDK performance is optimized and resource consumption is reduced.

### Version 2.5.0
1. Bugs occurred with small probability in high-concurrency scenarios are fixed.

2. Record of unique global auto-increment ID in transactions is supported.

### Version 2.4.0
1. The subscription logic is optimized by working with backend to accurately display SDK's current consumption time point.

2. The problem occurred while encoding a few special characters in the backend is fixed.

3. **A number of compatibility issues are fixed. We recommend that users who use older versions upgrade the software to this version ASAP.**

# Brief Description of Data Subscription SDK Sample Code
---
Subscription sample code using Tencent Cloud Binlog:
```
public class Main {
	
	public static void main(String[] args) throws Exception {
		//Create a context
		SubscribeContext context=new SubscribeContext();
		
		//User secretId, secretKey
		context.setSecretId("AKID-522dabaa14dceed746ba8ccfb58e9e6f");
		context.setSecretKey("AKEY-0ff4c4557c1183fc572baecfa505869d");

		//serviceIp and servicePort subscribed
		context.setServiceIp("10.108.112.24");
		context.setServicePort(50120);
			
		//Create a client
		SubscribeClient client=new DefaultSubscribeClient(context);
			//Create a subscription listener
			ClusterListener listener= new ClusterListener() {
			@Override
			public void notify(List<ClusterMessage> messages) throws Exception {
				//Consume subscribed data
				for(ClusterMessage m:messages){
					for(Record.Field f:m.getRecord().getFieldList()){
						if(f.getFieldname().equals("id")){
							System.out.println("seq:"+f.getValue());
						}
					}
					//Consumption acknowledgment
					m.ackAsConsumed();   
				}  
			}
			@Override
			public void onException(Exception e){
				System.out.println("listen exception"+e);
			}};
		//Add a listener
		client.addClusterListener(listener);
		//Configure subscription channel requested
		client.askForGUID("dts-channel-B2eG8xbLvi472wV3");
		//Launch the client
		client.start();
	}
}
```
The whole process is an intuitive, typical producer-consumer model, in which SDK, as a consumer, continually pulls subscribed Binlog data from a server, consumes data and acknowledges data consumption:
 1. First, configure parameters and create a consumer client `SubscribeClient`;
 2. Next, create a listener `ClusterListener` to consume received Binlog subscription data and return acknowledgment message after consumption;
 3. Finally, launch the client to start the process.
The listener `ClusterListener` allows users to handle data received according to their own demands and filter received Binlog data by type, for example, filtering out all `drop` statements.
 
 In the sample code, users must provide five parameters. Among them, `secretId` and `secretKey` are key values associated with users' Tencent Cloud accounts which can be viewed in "Tencent Cloud Console" -> "Cloud Products" -> "Cloud API Key" -> "API Key" and are used by SDK to authenticate user actions. The other three parameters including `serviceIp` `servicePort` and `channelId` are related to users' Binlog subscription, which will be displayed on the console after subscription contents are configured on the related pages of Tencent Cloud TencentDB for MySQL. For detailed operations, please see Console Operation Guide.
 
 Note: Since the data subscription SDK has been connected to CAM permission control, the root account has all the permissions by default and can directly access with the cloud API key of the root account. A sub-account has no permission by default and requires its root account to grant it access to the operation `name/dts:AuthenticateSubscribeSDK` or access to all DTS operations `QcloudDTSFullAccess`.

# SDK API Description
---
## SubscribeContext Class
---
### Class Description
This is mainly used to set user SDK configuration information, including security credential secretId, secretKey, and IP and port of subscription service.

### Construction Method
public SubscribeContext()

### Class Method

#### **Configure Security Credential secretId**
---
##### Function Prototype
public void setSecretId(String secretId)

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| secretId | String | Security credential secretId, which can be viewed in "Tencent Cloud Console" -> "Cloud Products" -> "Cloud API Key" -> "API Key" |

##### Returned Result
None
##### Thrown Exception
None

#### **Configure Security Credential secretKey**
---
##### Function Prototype
public void setSecretKey(String secretKey)

##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| secretKey | String | Security credential secretKey, which can be viewed in "Tencent Cloud Console" -> "Cloud Products" -> "Cloud API Key" -> "API Key" |

##### Returned Result
None
##### Thrown Exception
None

#### **Configure Subscription Service IP Address**
---
##### Function Prototype
public void setServiceIp(String serviceIp)

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| serviceIp | String | IP address of subscription service, which can be viewed on the Subscription Channel Configuration page of the console |

##### Returned Result
None
##### Thrown Exception
None

#### **Configure Subscription Service Port**
---
##### Function Prototype
public void setServicePort(String servicePort)

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| servicePort | String | Port number of subscription service, which can be viewed on the Subscription Channel Configuration page of the console |

##### Returned Result
None
##### Thrown Exception
None



## SubscribeClient API and DefaultSubscribeClient API
---
The `DefaultSubscribeClient` class implements `SubscribeClient` API.
### Class Description
This is used to build the client program for subscribing SDK, i.e. consumer for Binlog messages.

Based on user requirements, `DefaultSubscribeClient` provides two implementation methods, synchronous acknowledgment and asynchronous acknowledgment. In synchronous mode, acknowledgment message is synchronously received each time the client consumes Binlog message, to ensure that message consumption acknowledgment can be received by the server as soon as possible. In this mode, the overall performance of SDK is lower compared to asynchronous mode. In asynchronous mode, the consumer program acknowledges message consumption asynchronously, that is, message pulling and acknowledgment are processed asynchronously and independently, in which case performance is higher than that in synchronous acknowledgment mode. Users may select acknowledgment mode as desired.

### Construction Method
#### **Construct DefaultSubscribeClient**
---
##### Function Prototype
public DefaultSubscribeClient(SubscribeContext context, boolean isSync) throws Exception
##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| context | SubscribeContext | Configuration information of user SDK |
| isSynce | boolean | Indicate whether synchronous consumption mode is used for SDK |

##### Returned Result
`DefaultSubscribeClient` instance

##### Thrown Exception

 - 	IllegalArgumentException: This exception is thrown when any parameter is invalid in the parameter context submitted by a user. Invalid situations: no security credential or incorrect format; no service IP/port or incorrect format.
 - Exception: This exception is thrown when an error occurs during the SDK internal initialization process.
 
#### **Construct DefaultSubscribeClient**
---
##### Function Prototype
public DefaultSubscribeClient(SubscribeContext context) throws Exception

##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| context | SubscribeContext | Configuration information of user SDK |

##### Returned Result
`DefaultSubscribeClient` instance. Asynchronous acknowledgment by default.

##### Thrown Exception

 - 	IllegalArgumentException: This exception is thrown when any parameter is invalid in the parameter context submitted by a user. Invalid situations: no security credential or incorrect format; no service IP/port or incorrect format.
 - Exception: This exception is thrown when an error occurs during the SDK internal initialization process.
 
### Class Method
#### **Adding a Listener for SDK Consumer Client**
---
##### Function Description
To subscribe for incremental data in the channel, add listener `ClusterListener` into a `SubscribeClient`.
##### Function Prototype
public void addClusterListener(ClusterListener listener) throws Exception

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| listener | ClusterListener | Listener to be used by a consumer client. The main process to consume Binlog messages should be implemented in `ClusterListener` |

##### Returned Result
None
##### Thrown Exception

 - IllegalArgumentException: This exception is thrown if the listener parameter submitted by user is empty.
 - Exception: The current SDK only supports one listener. This exception is thrown when several listeners are added.
 
#### **Request Incremental Data in a Certain Subscription Channel**
---
##### Function Prototype
public void askForGUID(String channelId)

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| channelId | String | Subscription channel ID, which can be viewed on the Subscription Channel Configuration page of the console |

##### Returned Result
None

##### Thrown Exception
None

#### **Launch SDK Client**
---
##### Function Prototype
public void start() throws Exception

##### Input Parameters

None

##### Returned Result
None

##### Thrown Exception

 - Exception: This exception is thrown if an internal error occurs when the SDK client is being launched.

#### **Stop SDK Client**
---
##### Function Prototype
public void stop(int waitSeconds) throws Exception

public void stop() throws Exception

##### Input Parameters

| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| waitSeconds | int | Waiting time in seconds, which indicates to forcedly stop SDK operation after waiting for a certain time |

"stop" function with no parameters will wait for the thread to stop, which may last for a long time. The specific time is determined by the system scheduling. It is recommended to use the stop function with timeout for scenarios where specific restart time is required.

##### Returned Result
None

##### Thrown Exception

 - Exception: This exception is thrown if an internal error occurs when the SDK client is being stopped.


## ClusterListener API
---
### API Description
This is a callback API. An SDK user should implement the notify function of this API to consume subscribed data, and handle exceptions that may occur during consumption process by implementing the onException function.
### API Function
#### **Notify SDK Consumer Client of Subscription Messages**
---
##### Function Description
This is mainly used to implement incremental data consumption. The SDK, however, will notify ClusterListener of subscription data via the notify function when it receives data.
##### Function Prototype
public abstract void notify(List<ClusterMessage> messages) throws Exception

##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| messages| List<ClusterMessage> | Subscription data array. For more information on implementation of ClusterMessage, please see its definition |

##### Returned Result
None

##### Thrown Exception

Any exception during subscription data consumption will be thrown to the onException function implemented by user, who can then handle them as needed.

#### **Handle Exceptions Occurred During Subscription Data Consumption**
---
##### Function Description
This is mainly used to handle exceptions occurred when consuming subscription data. Users can implement their own secure exit policy in onException.

##### Function Prototype
public abstract void onException(Exception exception)

##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| exception| Exception | Exception class in Java standard library |

##### Returned Result
None

##### Thrown Exception
None

## ClusterMessage Class
---
### Class Description
The ClusterMessage class delivers consumed subscription data through the notify function. Each ClusterMessage saves data records of one **transaction** in TencentDB for MySQL, and each record in the transaction is saved via Record.

### Class Method
#### **Acquire Record From ClusterMessage**
---
##### Function Prototype
public Record getRecord()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| Record | Change record corresponding to a specific record in a transaction, such as begin, commit, update, insert, etc. |

##### Thrown Exception
None


#### **Acknowledge Consumed Data**
---
##### Function Description
This is used to send acknowledgment to the subscription server about consumed data. This function executes synchronous or asynchronous acknowledgment according to the value configured in SubscribeClient. Users should always call this data after consumption process, otherwise normal logic may be affected in which case the SDK may receive duplicate data.

##### Function Prototype
public void ackAsConsumed() throws Exception

##### Input Parameters
None

##### Returned Result
None

##### Thrown Exception

 - Exception: This exception is thrown if an internal error occurs during the acknowledgment process.

## Record Class
---
### Class Description
This indicates a certain record in subscribed Binlog data, generally, a member of a certain transaction `ClusterMessage`. The record may be a begin, commit or update statement.

### Class Method
#### **Acquire Attribute Value of Record**
----
##### Function Prototype
public String getAttribute(String key)

##### Input Parameters
| Parameter Name | Type | Description |
|:-------------:|:-------------|:-------------|
| key | String | Name of attribute value |

Possible attribute key values are:

| Attribute Key Value | Description |
|:-------------|:-------------|
| record_id |	Record ID, which will be automatically added in order by string in the channel, but cannot be ensured to be added continuously |
| source_type | Database instance engine type of corresponding Record. Current available value: mysql |
| source_category | Record type. Current available value: full_recorded |
| timestamp | The time when the Record is stored into binlog. This is also the time when the SQL statement is executed in TencentDB |
| checkpoint | File check point of corresponding Record, in the format of file_offset@file_name, where filen_name is the number suffix of the binlog file |
| record_type | Operation type of Record. Main available values include insert/update/delete/replace/ddl/begin/commit/heartbeat |
| db | Database name of the Record update table |
| table_name | Name of Record update table |
| record_encoding | Encoding of Record |
| primary | Name of the primary key column of Record update table |
| fields_enc | Encoding of each field value of Record. Fields are separated using commas, and empty value is used for non-character type |


##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Attribute value |

##### Thrown Exception
None


#### **Acquire Change Type of a Record**
---
##### Function Prototype
public DataMessage.Record.Type getOpt()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| DataMessage.Record.Type | Record type |

Possible values for DataMessage.Record.Type include: insert, delete, update, replace, ddl, begin, commit and heartbeat. "heartbeat" is a heartbeat table internally defined for data transfer and mainly used to check health status of a subscription channel. Theoretically, one heartbeat is generated each second.

##### Thrown Exception
None


#### **Acquire Checkpoint of a Record in Binlog**
---
##### Function Prototype
public String getCheckpoint()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Checkpoint of a record in Binlog, in the format of binlog_offset@binlog_fid. binlog_offset is the offset of the change record in binlog file, and binlog_fid is the name of binlog file. |

##### Thrown Exception
None

#### **Acquire the Timestamp of a Record in Binlog**
---
##### Function Prototype
public String getTimestamp()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Timestamp string |

##### Thrown Exception
None


#### **Acquire Database Name of Corresponding Record**
---
##### Function Prototype
public String getDbname()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Database name string |

##### Thrown Exception
None

#### **Acquire Data Table Name of Corresponding Record**
---
##### Function Prototype
public String getTableName()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Data table name string |

##### Thrown Exception
None


#### **Acquire Primary Key Column Name of Corresponding Record**
---
##### Function Prototype
public String getPrimaryKeys()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Primary key column name. For composite primary keys, the column names are separated by commas |

##### Thrown Exception
None

#### **Acquire Database Type of Subscription Instance**
---
##### Function Prototype
public DBType getDbType()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| DBType | Currently, only TencentDB for MySQL is supported for data transfer, that is, DBType.MYSQL |

##### Thrown Exception
None

#### **Acquire Number of Fields in Record**
---
##### Function Prototype
public int getFieldCount()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| int | Number of fields in Record |

##### Thrown Exception
None

#### **Check if Record is the First One in Transaction**
---
##### Function Prototype
public Boolean isFirstInLogevent()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| Boolean | True: it is the first log in the transaction. False: it is not the first log |

##### Thrown Exception
None

#### **Acquire the Field Definition List of a Record Table**
---
##### Function Prototype
public List<Field> getFieldList()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| List<Field> | Field array. For more information, please see the definition of Field class |

##### Thrown Exception
None

## Field Class
---
### Class Description
The Field class defines attributes of a field such as its encoding, type, name, value, and whether it is a primary key.

### Class Method
#### **Acquire the Encoding Format of a Field**
----
##### Function Prototype
public String getFieldEnc()

##### Input Parameters
None
##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Field encoding of String type |

##### Thrown Exception
None

#### **Acquire Field Name**
----
##### Function Prototype
public String getFieldname()

##### Input Parameters
None
##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| String | Field name of String type |

##### Thrown Exception
None


#### **Acquire Data Type of a Field**
----
##### Function Prototype
public Field.Type getType()

##### Input Parameters
None

##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| Field.Type | Field.Type is an enumeration type which corresponds to data types supported by MySQL, including INT8, INT16, INT24, INT32, INT64, DECIMAL, FLOAT, DOUBLE, NULL, TIMESTAMP, DATE, TIME, DATETIME, YEAR, BIT, ENUM, SET, BLOB, GEOMETRY, STRING, UNKOWN; |

##### Thrown Exception
None


#### **Acquire Field Value**
----
##### Function Prototype
public ByteString getFieldname()

##### Input Parameters
None
##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| ByteString | Field value. NULL if the value is empty |

##### Thrown Exception
None



#### **Check if the Field is a Primary Key**
----
##### Function Prototype
public Boolean isPrimary()

##### Input Parameters
None
##### Returned Result
| Type | Parameter Description |
|:-------------|:-------------|
| Boolean | True: the field is a primary key. False: it is not a primary key |

##### Thrown Exception
None

[1]:	//mc.qcloudimg.com/static/archive/2a5032c6100b9cb3316f978bb32519e5/binlogsdk-2.6.0-release.jar.zip
