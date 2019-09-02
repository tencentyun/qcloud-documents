## Overview
A separator-based log refers to a log structured using the specified separator. A complete log ends with a line break `\n`. You need to define a unique key for each separate field for CLS to process separator-based logs.
For example, the original log data is:
```
10002345987;write;error;topic does not exist
```

If the separator for log parsing is specified as a semicolon (;), the log is split into four fields, each with a unique key: eventid, action, status and msg. CLS will then structure the log into four key-value pairs: `Eventid:10002345987`, `action:write`, `status:error` and `msg:topic does not exist`.


## Collection Configuration
### 1. Log in to the console
Log in to the [CLS console](https://console.cloud.tencent.com/cls), and select **Logset** in the left navigation bar.

### 2. Enable LogListener
Click the logset for which the LogListener needs to be enabled for log collection, then click the log topic to be configured in **Log Topic**, and click **Edit** in the upper right corner of the **Collection Configuration** page to enter the edit mode. Enable **Collection Status** and **LogListener**.

### 3. Enter collection path
Enter the full path of a log to be collected in the "Collection Path" instead of a directory. The path should start with "/" and end with a character other than "/", for example `/data/log/cls.log`. File name supports regular expression, but not wildcard. **Note: Only log file name can use regular expression in the collection path.**

### 4. Associate server group
Select the target server group from the server group list, and associate it with the current log topic. Please note that the associated server group should be in the same region with the log topic. Learn about [how to create server groups>>](/document/product/614/17412).

### 5. Select separator mode
Choose **Separator** from the **Key-value Extraction Mode** drop-down box.

### 6. Select a separator
First, you need to select a unique separator. The system splits the log sample using the selected separator and displays it in the parsing result. You need to define a unique key for each field. Log collection supports a variety of separators. Common separators include space, tab, comma, semicolon and vertical bar. If you use another symbol as the separator of log data, such as double vertical bar `||`, you can also parse the log using a custom separator.
![](https://main.qcloudimg.com/raw/ed19bf882878819d5dd59857a95e284e.png)

### 7. Configure collection time
- Log time is measured in seconds.
- The time attribute of a log is defined in two ways: collection time and original timestamp.
- Collection time: The time attribute of a log is determined by the time when CLS collects the log.
- Original timestamp: The time attribute of a log is determined by the timestamp in the original log.


#### 7.1 Use the collection time as the time attribute of logs
Always enable **Collection Time**, as shown below:
![](https://main.qcloudimg.com/raw/d914adee3d01da92f0fa0aed6e6ca782.png)

#### 7.2 Use the original timestamp as the time attribute of logs
If you disable the collection time, enter the time key of the original timestamp and the appropriate time parsing format. The conversion format supports all strftime functions.
![](https://main.qcloudimg.com/raw/9eaf345586b1970e919c846f5080705d.png)

Here are examples on how to enter **Time Format Parsing**:
Example 1: Original timestamp: `10/Dec/2017:08:00:00`, Parsing format: `%d/%b/%Y:%H:%M:%S`  

Example 2: Original timestamp: `2017-12-10 08:00:00`, Parsing format: `%Y-%m-%d %H:%M:%S`  

Example 3: Original timestamp: `12/10/2017, 08:00:00`, Parsing format: `%m/%d/%Y, %H:%M:%S`  

> **Note:**
> Second can be used as the unit of log time. If the time is entered in a wrong format, the collection time is used as the log time.


### 8. Use filter
The filter is designed to add filtering rules based on your business needs to help you filter out valuable log data. For separator-based logs, you can configure filtering rules based on the key-value pair parsed out. A filtering rule is a regular expression. The filtering rule you created is hit when a log matches the regular expression, only in this case the log can be collected.

For example, to collect log data with errorcode = 400 or 500, configure errorcode for the key, and (400|500) for the filtering rule.

