## Overview
A log in the mode of full text in multi lines refers to a complete log that occupies multiple lines (such as a Java program log). In this mode, the line break `\n` cannot be used as the end mark of a log. To help CLS system distinguish among the logs, "First Line Regular Expression" is used for match. When a log in a line matches the preset regular expression, it is considered as the beginning of a log, and the next matching line will be the end mark of the log.  

In the mode of full text in multi lines, a default key `__CONTENT__` is also set, but the log data itself is not structured, and the log field is not extracted. The time attribute of a log is determined by the collection time.

## Collection Configuration

### 1. Log in to the console
Log in to the [CLS console](https://console.cloud.tencent.com/cls), and select **Logset** in the left navigation bar.

### 2. Enable LogListener
Click the logset for which the LogListener needs to be enabled for log collection, then click the log topic to be configured in **Log Topic**, and click **Edit** in the upper right corner of the **Collection Configuration** page to enter the edit mode. Enable **Collection Status** and **LogListener**.

> **Note:**
> LogListener should be updated to 2.1.4 or above for log collection.

### 3. Enter collection path
Enter the full path of a log to be collected in the "Collection Path" instead of a directory. The path should start with "/" and end with a character other than "/", for example `/data/log/cls.log`. File name supports regular expression, but not wildcard. **Note: Only log file name can use regular expression in the collection path.**

### 4. Associate server group
Select the target server group from the server group list, and associate it with the current log topic. Please note that the associated server group should be in the same region with the log topic. Learn about [how to create server groups>>](/document/product/614/17412).

### 5. Select the mode of full text in multi lines
Choose **Full text in multi lines** from the **Key-value Extraction Mode** drop-down box.

### 6. First line regular expression
Enter the first line regular expression according to the format of the first line in the mode of full text in multi lines.

### 7. Use filter
The filter is designed to add filtering rules based on your business needs to help you filter out valuable log data. In the mode of full text in multi lines, a log is parsed into a full string with the key of `__CONTENT__` by default. When using the filter, you can only enter the filtering rule for the entire full text log. A filtering rule is a regular expression. The filtering rule you created is hit when a log matches the regular expression, only in this case the log can be collected.

