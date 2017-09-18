## Performance Monitoring
Cloud Database for MySQL provides various performance monitoring items to make it easy for users to view and obtain the operation information of instances. You can log in to [Tencent Cloud Console][1], click "Relational Database" in the navigation bar to enter [Cloud Database Console][2], and click "Management"-"Instance Monitoring" to view the items.

## Instance Types That Can Be Monitored

Tencent Cloud's CDB for MySQL can monitor master instances and read-only instances, and provides an independent monitoring view for each instance for query.

## Monitoring Metrics

### 1. Connection Monitoring

- Queries per second (QPS)
- Maximum number of connections (max\_connections)

### 2. Access Monitoring

- Number of slow queries (slow\_queries, in counts per second (cps))
- Number of full table scans (select\_scan, in cps)
- Number of queries (com\_select, in cps) _ - Number of updates (com\_update, in cps) _ - Number of deletions (com\_delete, in cps) _ - Number of insertions (com\_insert, in cps) _ - Number of overwrites (com\_replace, in cps) _ - Number of queries (queries, in cps)
- Current number of connections (threads\_connected) _ - Query rate (query rate, in percentage)

### 3. Load Monitoring

- Real disk capacity (in MB), data space used by a database
- Total disk capacity (in MB), the sum of data space and binlog space used by a database
- Volume rate (in percentage)
- Outbound traffic of private network (bytes\_sent, in MB/s)
- Inbound traffic of private network (bytes\_received, in MB/s)

### 4. Query Cache Monitoring

- Cache hit rate (qcache\_hit\_rate, in percentage)
- Cache usage (qcache\_use\_rate, in percentage)

### 5. Table Monitoring

- Number of temporary tables (created\_tmp\_tables, in cps)
- Number of table lock waits (table\_locks\_waited, in cps)

### 6. InnoDB Engine Monitoring

Cache hit rate (innodb cache hit rate, in percentage)
Cache usage (innodb cache use rate, in percentage)
- Number of disk reads (innodb os file reads, in cps)
- Number of disk writes (innodb os file writes, in cps)
- Number of fsyncs (innodb os fsyncs, in cps)

### 7. MyISAM Engine Monitoring

Cache hit rate (innodb cache hit rate, in percentage)
Cache usage (innodb cache use rate, in percentage)

> More monitoring metrics will be available in the future.

[1]:	https://console.qcloud.com/
[2]:	https://console.qcloud.com/cdb/ "Cloud Database Console"

