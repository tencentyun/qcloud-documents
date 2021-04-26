## Restoring a Database Instance to a Specified Time

You can use the rollback tool at console to roll back a database or table on Tencent Cloud platform. Based on cold backup and Binlog, the tool can be used to roll back data in real time.

The CDB rollback tool can roll back the data to the specified time (accurate to the second) by rebuilding images and real-time logs in a temporary instance regularly, and ensure that all data have the same time slice. During the rollback, the access to the original database or table is not affected.

