
### Does the data subscription allow multiple SDKs to be connected to and consume one channel at a time?

No. A channel can only be connected with and consumed by one SDK. If you have multiple downstream SDKs to subscribe to the same database table, you can build multiple channels.

### Does the data subscription support connecting one SDK to multiple channels?

Yes. An SDK can consume multiple channels at a time.

### An error occurred while starting SDK: already has sdk on this channel.
A channel can only be connected with and consumed by one SDK. If you add a new connection, this error will be reported. In this case, confirm whether the program completely exits. If the error occurs again during reconnection after confirmation, the interval between restarts may be slightly longer, such as 20 seconds.

### When the data subscription subscribes to the real-time incremental data, is the new data only the added data or does it include modified data?
Data subscription can subscribe to the following incremental data: all additions, deletions and modifications (DML), and structure changes (DDL).

### A TencentDB instance and a local database have the same table structure, but different indexes. Does the data subscription support real time synchronization?
Yes. If the data subscription only subscribes to data changes, consumption will not be affected by different indexes. If it subscribes to structure changes, and indexes will change on the TencentDB instance, the structure changes may fail to be consumed locally due to different indexes.

### Why can't I modify the consumption time point of a data subscription channel?
When an error occurred while modifying a consumption time point, a prompt will appear on the interface. It is generally because the subscription channel is consumed by a downstream SDK. You can check the consumption source IP on the DTS console to see if there is a downstream SDK consuming data. If yes, stop the consumption and then modify the consumption time point.

### How can I determine whether the data is consumed normally?
When data is written into a channel (or some data is not consumed), if the data is consumed normally, the consumption time point on the console will be migrated normally.

### If a record at the consumer end is not acknowledged by the data subscription, why SDK receives duplicate data after restart?
When SDK has messages that have not been acknowledged, the SDK will continue pulling messages until its cache is full, and no new message will be received. At this point, the consumption time point saved on the server is that of the message not acknowledged.
When SDK is restarted, the server will push data again from the consumption time point of the message not acknowledged to avoid message loss. Therefore, the SDK will receive some repeated messages.

### When SDK quits and restarts after a few days, why does it fail to subscribe to data? Error: Maybe checkpint is too old?
The time range for data retention in a data subscription channel is 1 day, i.e. from [the current time - the current time of the next day]. The subscription channel will delete expired data. Therefore, if the data corresponding to the time point of the last consumption data when SDK quits is not within the valid data range of the current subscription channel, the data corresponding to this consumption time point cannot be subscribed to. To fix this problem, modify the consumption time point before starting SDK, to ensure it is within the valid data range.

### When SDK pulls data, it suddenly stops and cannot subscribe to any data. But after restarting, it consumes some data before stopping again.
In this case, it is more likely that the API ackAsConsumed is not called in the SDK code to report the consumption time point. Because the SDK has a limited cache space, if ackAsConsumed is not called to report the consumption time point, the data in the cache space will not be deleted. When the cache is full, new data cannot be pulled, and the SDK will stop and fail to subscribe to any data. Note: All messages here, including BEGIN and COMMIT messages, must be acknowledged for consumption. Messages unrelated to business logic are also included.

### How to ensure that the data subscribed to by SDK is a complete transaction, and will the record in the middle of the transaction be pulled based on the provided consumption time point?
No. Based on the user-specified consumption time point or the time point of the last acknowledged consumption, the server will search for the start point of the complete transaction corresponding to this consumption time point. Data is sent to the downstream SDK from the beginning of the entire transaction. So the full transaction content can be received.

### Is there any problem with the data subscription during the TencentDB master/slave switch or when the master database is restarted? Will the data be lost?
No. When a switching between master and slave occurs or when TencentDB instance is restarted, the data subscription will automatically perform switching. This process is transparent to the SDK.

### An error occurred while starting SDK: Do DTS authentication fail, caused by: get channel info from msg failed.
Confirm whether the input parameters are matched, including ip, port, secretId, secretKey, and channelId.

### When SDK is started, why does the system report that secretId has no permission?
Sub-account has no permission by default. It must be given the access to the operation "name/dts:AuthenticateSubscribeSDK", or the access to all DTS operations "QcloudDTSFullAccess" by the root account.

### Will the data subscription receive duplicate data?
No if data is consumed normally. If SDK quits abnormally, the information of the last acknowledgement time point is not reported timely, and duplicate data may be received when the SDK is started next time. But the probability is very low.
If a complete transaction is not acknowledged, the data is pulled again from the beginning of the transaction when the SDK is started next time. In this case, the data cannot be regarded as duplicate data. The core logic of the SDK guarantees the integrity of the transaction. 

### Can a data subscription instance subscribe to multiple TencentDB instances?
No. A data subscription channel can subscribe to only one TencentDB instance.

### What if OOM occurs while SDK is running?
Choose a host with better configurations. When a single SDK runs smoothly at high speed, it consumes less than 1-core CPU and less than 1.5 GB of memory.

