To provide secure and consistent instance services, Tencent Cloud imposes the following service limits for CDB for PostgreSQL.

| Operation | Permission Description |
|---------|---------|---------|
| Root permission of database | Super user permission is unavailable | 
| Restart instance | Currently unavailable | 
| Modify configuration of database parameters | Currently unavailable | 
| Database backup | Only support using pg_dump to create dump data | 
| Data recovery | Only support using psql to recover dump data created by pg_dump | 
| Build database replication model | HA model is automatically built based on PostgreSQL stream replication, eliminating the need to build it manually. <br>PostgreSQL Standby nodes are invisible to users and thus cannot be directly accessed | 




