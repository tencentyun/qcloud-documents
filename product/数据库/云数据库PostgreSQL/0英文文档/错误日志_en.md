## 1. Feature Description

Error logs refer to logs generated due to operations, SQL, and system running errors when the database is running, which are often used by developers to find out the business system or database causes of the problems.

Tencent CDB for TDSQL provides error log view feature in "Instance Management" -> "Performance Optimization", as shown below:

![](https://mc.qcloudimg.com/static/img/4b38c35fffd0eb69f52b30026077e871/pgsql-errorlog.png)


## 2. Default Setting of Error Log

Error log feature: Enabled by default

Logging level of error log: log_min_error_statement=ERROR.

Analyzed data output latency: 1 to 5 minutes.

Logging duration: 7 days (the maximum volume is the latest 10,000 records)




