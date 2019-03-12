Logs can be collected via client or API/SDK. The logs collected to the CLS platform are structured according to a certain rule.

## Collection Methods

### Collect logs via API/SDK

You can upload structured logs to CLS by calling the [CLS API](https://cloud.tencent.com/document/product/614/12445). For more information, please see the [API for uploading logs](https://cloud.tencent.com/document/product/614/12406).

### Collect logs via LogListener client in real time

LogListener is the log collection Agent provided by Tencent Cloud CLS. By installing LogListener on the server, you can collect logs on the specified path in real time, and perform structured processing on the raw data of your logs. You can use LogListener to collect logs by following the steps below:

Step 1: Install Loglistener on the server.

Step 2: Create a server group on the Tencent Cloud CLS console.

Step 3: Associate the server group in the log topic, and complete the related configuration.

For more information, please see [how to collect logs using LogListener](https://cloud.tencent.com/document/product/614/14541).
> **Note:**
Quickly check whether LogListener collects logs successfully:
1. You need to enable index feature. For more information, please see [Enable Index](https://cloud.tencent.com/document/product/614/16981).
2. View logs in **Log Search** on the CLS console (there is a short delay in log search).

## Log Structuring

The structuring of logs is to store your log data on the CLS platform in key-value format. After logs are structured, you can download the structured logs, specify keys for search, or ship logs in a structured manner.

- Collection API allows you to upload structured log data directly.
- LogListener, the collection agent, allows you to specify a method for structuring log data, and perform structured parsing on the raw data of your unstructured logs. For example, if the raw data of a log is `10002345987;write;error;topic does not exist`, you can specify a separator when parsing logs. In this case, the separator is semicolon, and keys are eventid, action, status and msg. So, the log is structured into four key-value pairs: `eventid:10002345987 action:write status error msg:topic does not exist`.

