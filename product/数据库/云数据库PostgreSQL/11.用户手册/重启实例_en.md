Restart is indispensable to the maintenance of CDB. Restarting PostgreSQL instance is equivalent to restarting database (service and process) on a local server.

## Use Console to Restart Instances

1) Log in to [CDB for PostgreSQL Console](https://console.cloud.tencent.com/pgsql).

2) Click "Restart" in the operation column on the instance list to restart a single running PostgreSQL instance.

## Notes About Database Restart

1) Please exercise great caution when restarting a database, which plays a vital role in the business. Before the restart, it is recommended to disconnect the database from server and **stop writing** data.

Generally, it takes a dozen seconds to a few minutes to wait until the restart is completed. The instance cannot provide any service during the process.

3) **There is a possibility of failure of database restart, which is normal. In case of a failure of restart, you can (manually) click "Restart" to try again. 

4) Staring an instance does not change any of its physical attributes, so the public IP, private IP, and any data stored on the instance will remain unchanged.

5) After the restart, reconnection to the database is needed. Please make sure your business has a reconnection mechanism.


