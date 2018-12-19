Initialization is required for the purchased Cloud Database MariaDB (TDSQL) before you can use the instances, as shown below:
![](//mccdn.qcloud.com/static/img/7d6e94d91a4c132d70462029f1397ced/image.png)

The following parameters need to be initialized:

- 	Supported character set: character_set_server
- 	Table name case sensitivity: lower_case_table_names
- 	Length of INNODB engine data page: innodb_page_size (Default value for MySQL is 16K. Modification of this value will affect the length of Innodb index data page and the creation of the index. Smaller value means better performance.)
- 	Strongsync configuration: The Strongsync feature is enabled when you launch the instance.
