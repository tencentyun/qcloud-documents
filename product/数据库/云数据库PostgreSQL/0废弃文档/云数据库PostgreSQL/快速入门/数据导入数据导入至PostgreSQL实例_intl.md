You can restore data backup files into the target TencentDB for PostgreSQL by using PostgreSQL logical backup.


## 1. Prepare a PostgreSQL Instance

Purchase a PostgreSQL instance, initialize the instance and obtain its connection address.
> Make sure the initialization character set is consistent with that of the original instance.

## 2. Logical Back-up Original Instance Data

Connect to the local (source) PostgreSQL database using PostgreSQL client.

Execute the following command to back up data.
```
pg_dump -U username -h hostname -p port databasename -f filename
```

Parameter description:

- username: The username of your local database.
- hostname: The name of your local database server. You can use "localhost" if you're logging in from your local database server.
- port: The port number of your local database.
- databasename: The name of your local database to be backed up.
- filename: The name of the generated backup file.

For example, the database user "pgtest" wants to back up its local PostgreSQL database. The user should use the following command to back up data after logging in to the PostgreSQL server.

```
pg_dump -U pgtest -h localhost -p 4321= pg001 -f pg001.sql
```

## 3. Migrate Data Through CVM

It is suggested that you upload data to a CVM in a secure way (such as encrypted compression) and restore data to the target PostgreSQL via a private network.

Log in to the CVM.

In the PostgreSQL client, execute the following command to import data to the target PostgreSQL.
```
psql -U username -h hostname -d desintationdb -p port -f dumpfilename.sql
```
Parameter description:

- username: The user name of the PostgreSQL database on RDS.
- hostname: The address of the PostgreSQL database on RDS.
- port: The port number of the PostgreSQL database on RDS.
- databasename: The name of the PostgreSQL database on RDS.
- filename: The file name of the local backup data.
For example:

psql -U pgtest -h 10.xxx.xxx.xxx -d pg001 -p 4321 -f pg001.sql
Because the permission configuration of the source may be different from that of the target database, certain permission-related WARNINGS or ERRORS may appear during the data import process, which can be ignored.

## 4. Migrate Data Through Internet
You can also import data directly through the Internet by using tools such as pgAdmim, if the data volume is not more than 10 GB. For example:
![](https://mc.qcloudimg.com/static/img/a4d8bd006f5f5d976dab220589753f44/image.png)

