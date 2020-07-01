LogListener is a log collection Agent provided by Tencent Cloud's Cloud Log Service (CLS). It reports log data in real time according to the preset collection policy. This document introduces how the Agent works.

## Mechanism 
After being successfully deployed, the CLS LogListener monitors the associated log files in real time. It senses the changes (including those of the file content, and those of the file inode in Linux system) of the target log files mainly through Inotify, the notification mechanism for file system modifications. When LogListener senses a change of a log file, it collects and reports the new log, and records the current location. If the system restarts, it continues to collect the log from the recorded location.
![](https://main.qcloudimg.com/raw/6fbd9f15d394c044c54b434ad4c93ecb.png)

## Example
We use the following example to intuitively explain the collection policy of the CLS Agent:
```
    2018-01-01 10:00:01 echo log_1 >> cls.log
    2018-01-01 10:00:02 start LogListener
    2018-01-01 10:00:03 echo log_2 >> cls.log
    2018-01-01 10:00:04 echo log_3 >> cls.log
    2018-01-01 10:00:05 echo log_4 >> cls.log
    ......
```
In the above scenario, LogListener collects log_2, log_3, log_4... into CLS. That is, the Agent automatically monitors and reports all incremental logs after the time point when the process starts for the first time. Note: The Agent will monitor the inode of the file. When the log file cls.log is modified using vim, and because the vim mechanism will modify the inode, the log system will take the file as a completely new log file and will collect and report the contents of the entire file.
> **Notes:**
> - LogListener automatically starts after the server restarts.
> - After the LogListener process hangs up and restarts, it will continue to report the log starting from the recorded offset position.
> - A log file can only be reported to one log topic. If more than one log topic is associated with a log file, the configuration information will be overwritten. Actually, the log file is only uploaded to the last topic.
