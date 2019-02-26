## Overview
A JSON log automatically extracts the key at the first layer as the field name, and the value at the first layer as the field value, to realize structured processing of the entire log. A complete log ends with a line break `\n`. For example, the original log data is:
```
{"action":"GET","time":"2017-12-10 08:00:00","status":"200","ip":"172.168.xxx.xxx"}
```

The log is structured by CLS into: `action:GET`, `time:2017-12-10 08:00:00`, `status:200` and `ip:172.168.xxx.xxx`.

## Collection Configuration
### 1. Log in to the console
Log in to the [CLS console](https://console.cloud.tencent.com/cls), and select **Logset** in the left navigation bar.

### 2. Enable LogListener
Click the logset for which the LogListener needs to be enabled for log collection, then click the log topic to be configured in **Log Topic**, and click **Edit** in the upper right corner of the **Collection Configuration** page to enter the edit mode. Enable **Collection Status** and **LogListener**.

### 3. Enter collection path
Enter the full path of a log to be collected in the "Collection Path" instead of a directory. The path should start with "/" and end with a character other than "/", for example `/data/log/cls.log`. File name supports regular expression, but not wildcard. **Note: Only log file name can use regular expression in the collection path.**

### 4. Associate server group
Select the target server group from the server group list, and associate it with the current log topic. Please note that the associated server group should be in the same region with the log topic. Learn about [how to create server groups>>](/document/product/614/17412)

### 5. Select JSON mode
Choose **JSON** from the **Key-value Extraction Mode** drop-down box.

### 6. Configure collection time
- Log time is measured in seconds.
- The time attribute of a log is defined in two ways: collection time and original timestamp.
- Collection time: The time attribute of a log is determined by the time when CLS collects the log.
- Original timestamp: The time attribute of a log is determined by the timestamp in the original log.

#### 6.1 Use the collection time as the time attribute of logs
Always enable **Collection Time**, as shown below:
![](https://main.qcloudimg.com/raw/d914adee3d01da92f0fa0aed6e6ca782.png)


#### 6.2 Use the original timestamp as the time attribute of logs
If you disable the collection time, you need to enter the time key of the original timestamp and the appropriate time parsing format. The conversion format supports all strftime functions.
![](https://main.qcloudimg.com/raw/9eaf345586b1970e919c846f5080705d.png)

Here are examples on how to enter **Time Format Parsing**:
Example 1: Original timestamp: `10/Dec/2017:08:00:00`, Parsing format: `%d/%b/%Y:%H:%M:%S`

Example 2: Original timestamp: `2017-12-10 08:00:00`, Parsing format: `%Y-%m-%d %H:%M:%S`

Example 3: Original timestamp: `12/10/2017, 08:00:00`, Parsing format: `%m/%d/%Y, %H:%M:%S`

> **Note:**
>
> Second can be used as the unit of log time. If the time is entered in a wrong format, the collection time is used as the log time.

### 7. Use filter
The filter is designed to add filtering rules based on your business needs to help you filter out valuable log data. For JSON logs, you can configure filtering rules based on the key-value pair parsed out. A filtering rule is a regular expression. The filtering rule you created is hit when a log matches the regular expression, only in this case the log can be collected.

For example, to collect log data with status = 400 or 500, configure status for the key, and (400|500) for the filtering rule.
![](https://main.qcloudimg.com/raw/eb6477dc340ab78986b74dfcdd7d9053.png)
