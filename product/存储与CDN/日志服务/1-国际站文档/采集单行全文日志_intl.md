## Overview
A log in the mode of full text in a single line refers to a complete log in a single line. CLS uses the line break `\n` as the end mark of a log collected. To manage logs in a structured manner, each log has a default key `__CONTENT__`, but the log data itself is not structured, and the log field is not extracted. The time attribute of a log is determined by the collection time.

## Collection Configuration

### 1. Log in to the console
Log in to the [CLS console](https://console.cloud.tencent.com/cls), and select **Logset** in the left navigation bar.

### 2. Enable LogListener
Click the logset for which the LogListener needs to be enabled for log collection, then click the log topic to be configured in **Log Topic**, and click **Edit** in the upper right corner of the **Collection Configuration** page to enter the edit mode. Enable **Collection Status** and **LogListener**.

### 3. Enter collection path
Enter the full path of a log to be collected in the "Collection Path" instead of a directory. The path should start with "/" and end with a character other than "/", for example `/data/log/cls.log`. File name supports regular expression, but not wildcard. **Note: Only log file name can use regular expression in the collection path.**

### 4. Associate server group
Select the target server group from the server group list, and associate it with the current log topic. Please note that the associated server group should be in the same region with the log topic. Learn about [how to create server groups>>](/document/product/614/17412).

### 5. Select the mode of full text in a single line
Choose **Full text in a single line** from the **Key-value Extraction Mode** drop-down box.

### 6. Use filter
The filter is designed to add filtering rules based on your business needs to help you filter out valuable log data. In the mode of full text in a single line, a log is parsed into a key-value pair with the key of `__CONTENT__` by default, so the filtering rules in this mode can only be configured based on `__CONTENT__`. A filtering rule is a regular expression. The filtering rule you created is hit when a log matches the regular expression, only in this case the log can be collected.
