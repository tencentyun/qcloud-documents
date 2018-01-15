## Service Limits

1. You cannot change any data in mysql, information_schema, performance_schema, and sysdb

2. SQL statements cannot be used to set permission for accounts, which can only be done via Console.

The following 19 kinds of permissions are supported:
SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER,
CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW,
CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, SHOW DATABASES.

3. Super admin account is not supported.

4. It is recommended to use innoDB storage engines.
