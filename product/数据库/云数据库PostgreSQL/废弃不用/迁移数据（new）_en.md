If your data already reside in PostgreSQL, you can easily migrate the data to CDB for PostgreSQL by executing psql command.
Data migration is divided into two parts:
> (1) Perform logical backup and create dump data by executing pg_dump command.
> (2) Recover the backup data in the previous step to CDB for PostgreSQL.
Preparation: You should have completed the preparation of PostgreSQL instance. If not, please see documentations on how to apply for an instance and how to connect to an instance.

## Step 1
Connect to the local database using PostgreSQL, and back up data by executing the following command.

```
pg_dump -U username -h hostname -p port -d databasename -f filename
```

Parameter description


| Parameter | Description | 
|---------|---------|---------|
| username | User name of local database |
| hostname | Host name of local database. You can use "localhost" if you're logging in from local database host | 
| port | Port number of local database | 
| databasename | Name of local database to be backed up | 
| filename | Name of the generated backup file, e.g. mydump.sql | 


## Step 2
Preparation: Upload the backup data to the CVM in the same private network, and restore the data through the private network, to ensure network stability and data security.
After logging in to CVM, you can restore the data by executing the following command in PostgreSQL client.

```
psql -U username -h hostname -d desintationdb -p port -f dumpfilename
```
Parameter description


| Parameter | Description | 
|---------|---------|---------|
| username | User name of CDB for PostgreSQL database |
| hostname | IP of CDB for PostgreSQL database | 
| desintationdb | Name of CDB for PostgreSQL database | 
| port | Port number of CDB for PostgreSQL database | 
|dumpfilename | Name of the backup file, e.g. mydump.sql | 



