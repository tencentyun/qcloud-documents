Logs can be collected via client or API/SDK. The logs collected to the CLS platform are structured according to a certain rule.

## Collection Methods

### Collecting logs via API/SDK

You can upload structured logs to CLS by calling [CLS API](https://cloud.tencent.com/document/product/614/12445). For more information, please see [API for Uploading Logs](https://cloud.tencent.com/document/product/614/12406).

### Collecting logs via LogListener in real time

LogListener is the agent provided by Tencent Cloud CLS for collecting logs. You can install it on your server to collect logs in the specified path in real time, and process the raw data of your logs in a structured way. You can use LogListener to collect logs by following the three steps below:

Step 1: Install Loglistener on the server.

Step 2: Create a server group on the Tencent Cloud CLS console.

Step 3: Associate the server group with the log topic, and complete the related configuration.

For more information, please see [Using LogListener for Logs Collection](https://cloud.tencent.com/document/product/614/14541).

## Log Structuring

The structuring of logs is to store your log data on the CLS platform in key-value format. After logs are structured, you can download the structured logs, specify key-values for retrieval, or perform structured shipping of logs.

- Collection API allows you to upload structured log data directly.
- LogListener, the collection agent, allows you to specify a method for structuring log data, and perform structured parsing on the raw data of your unstructured logs. For example, if the raw data of a log is `10002345987;write;error;topic does not exist`, then you can specify separator as the mode for parsing logs. In this case, the separator is semicolon, and keys are eventid, action, status and msg. So, the log is structured into four key-value pairs, i.e. `eventid:10002345987 action:write status:error msg:topic does not exist`.

