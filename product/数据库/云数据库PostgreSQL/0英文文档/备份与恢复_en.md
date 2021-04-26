## 1. Download Backup Files
CDB for TDSQL provides full backup and incremental backup using three Hadoop distributed file systems deployed across data centers. The backup files are retained for 30 days by default. You can download backup files by going to "Instance Management" -> "Backup and Recovery", as shown below. You can select and download files based on backup times.
![](//mccdn.qcloud.com/img568a2e3f345ee.jpg)

## 2. Backup Settings
### 2.1. Backup period and rules
CDB for TDSQL allows you to set the backup storage period to adjust the backup space. The default storage period is 30 days, which is the maximum value. The minimum value is 1 day. You can also contact Tencent
service personnel for a longer backup period.
![](//mccdn.qcloud.com/img568a2ead5818f.png)

Default backup rules:
- Log files are backed up in real time with a delay of about 5 minutes. Depending on the log size, there is a delay from backup completion till the download is available on the page.
- Cold backup includes full backup + incremental backup, with full backup performed at least once a week and incremental backup at least once a day. The backup generation time is the time when the load is at the lowest level, which is automatically selected by the system.
- The relevant backup rules comply with the applicable regulations for backup of regulators such as Bank of China.

## 3. Data Recovery
Data recovery can be achieved through rollback. For more information, please see [CDB Rollback](http://cloud.tencent.com/doc/product/237/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%9B%9E%E6%A1%A3).
