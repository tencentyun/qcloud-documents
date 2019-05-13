Initialization (batch initialization) is required for the purchased Cloud Database (TDSQL) instances before you can use them, as shown below:
![](//mccdn.qcloud.com/static/img/7d6e94d91a4c132d70462029f1397ced/image.png)
The following parameters need to be initialized:
- 	Supported character set: character_set_server
- 	Table name case sensitivity: lower_case_table_names
- 	Size of INNODB engine data page: innodb_page_size
