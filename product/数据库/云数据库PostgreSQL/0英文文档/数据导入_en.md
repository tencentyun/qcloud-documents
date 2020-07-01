You can restore data backup files into the target CDB for PostgreSQL by using PostgreSQL logical backup.


## 1. Prepare PostgreSQL Instance

Purchase PostgreSQL instance, initialize instance and acquire connection address.
> Make sure the initialization character set is consistent with that of the original instance.

## 2. Logical Back-up Original Instance Data

Connect to the local (source) PostgreSQL database using PostgreSQL client.

Execute the following command to back up data.
```
pg_dump -U username -h hostname -p port databasename -f filename
```

Parameter description:

- username: user name of local database.
- hostname: host name of local database. You can use "localhost" if you're logging in from local database host.
- port: port number of local database.
- databasename: Name of local database to be backed up.
- filename: Name of the generated backup file.

For example, the database user "pgtest" wants to back up local PostgreSQL database. The user should use the following command to back up data after logging in to PostgreSQL host.

```
pg_dump -U pgtest -h localhost -p 4321= pg001 -f pg001.sql
```

## 3. Migrate Data Through CVM

It is suggested that you upload data to CVM in a secure way (such as encrypted compression) and restore data to target PostgreSQL via private network.

Log in to CVM.

In the PostgreSQL client, execute the following command to import data to target PostgreSQL.
```
psql -U username -h hostname -d desintationdb -p port -f dumpfilename.sql
```
Parameter description:

- username: user name of the PostgreSQL database on RDS.
- hostname: PostgreSQL database address on RDS.
- port: port number of the PostgreSQL database on RDS.
- databasename: PostgreSQL database name on RDS.
- filename: File name of the local backup data.
For example:

psql -U pgtest -h 10.xxx.xxx.xxx -d pg001 -p 4321 -f pg001.sql
Certain permission-related WARNING or ERROR may occur during the data import process, due to possible permission configuration differences between source and target database. These can be ignored.

## 4. Migrate Data Through Internet
You can also import data directly through the Internet by using tools such as pgAdmim, if the data volume is low (e.g. no more than 10 GB). For example:
![](https://mc.qcloudimg.com/static/img/a4d8bd006f5f5d976dab220589753f44/image.png)
