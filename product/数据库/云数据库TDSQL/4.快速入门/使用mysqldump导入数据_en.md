mysqldump is easy to use but has long downtime, so it is suitable for small amount of data that allows relatively long downtime.

###  1. Use mysqldump to export the data from local database as data files.

> Notes: Do not perform data updates during export. It only exports data. Stored procedures, triggers, and functions are excluded.

```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName --skip-triggers > /tmp/dbName.sql

Parameter Description:

localIp: Server IP address of the local database
userName: Migration account of the local database
dbName: Name of the database to migrate
/tmp/dbName.sql: Name of the backup file
```

###  2. Use mysqldump to export stored procedures, triggers, and functions.

> Notes: If you do not use stored procedures, triggers, or functions in your database, skip this step. When exporting stored procedures, triggers, and functions, you need to remove the definer to be compatible with the Cloud Database.

```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/triggerProcedure.sql
Parameter Description:

localIp: Server IP address of the local database
userName: Migration account of the local database
dbName: Name of the database to migrate
/tmp/triggerProcedure.sql: Name of the backup file
```

### 3. Upload the data file and the stored procedure file to the CVM.
> Make sure the CVM and the CDB are well connected and the CVM has sufficient storage space.

###  4. Log in to the CVM to import the data files and stored procedure files into the target CVM.

> Make sure you have a database account with the appropriate permissions, or you may need to go to the Console to create an account

```
mysql -h xxx.xxx.xxx.xxx:xxxx -u userName -p dbName < /tmp/dbName.sql
mysql -h xxx.xxx.xxx.xxx:xxxx -u userName -p dbName < /tmp/triggerProcedure.sql
Parameter Description:

xxx.xxx.xxx.xxx:xxxx Instance connection address (here it refers to the private network address)
userName: Migration account of RDS database
dbName: Name of the database to import
/tmp/dbName.sql: Name of the data file to import
/tmp/triggerProcedure.sql: Name of the stored procedure file to import
```
