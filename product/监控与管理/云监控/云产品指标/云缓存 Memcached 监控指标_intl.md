 Cloud Monitor of Tencent Cloud provides the following monitoring metrics for Cloud Cache Service Memcached instance:

| Metric | Description |
|--|--|
| Tablespace |The total space assigned to the current business |
| Used space |The space actually used by the current business |
| Number of records | Number of records and key-value pairs stored by the current business |
| GET counts| When the time granularity of query is five minutes, it indicates the number of read (GET) visits in the last five minutes. When the time granularity of query is one day, the value should be the peak of the day (counts per second) |
| SET counts| When the time granularity of query is five minutes, it indicates the number of write (SET) visits in the last five minutes. When the time granularity of query is one day, the value should be the peak of the day (counts per second) |
| DELETE counts	| When the time granularity of query is five minutes, it indicates the number of write (DELETE) visits in the last five minutes. When the time granularity of query is one day, the value should be the peak of the day (counts per second) |
| Total counts| When the time granularity of query is five minutes, it indicates the number of GET/SET/DELETE visits in the last five minutes. When the time granularity of query is one day, the value should be the peak of the day (counts per second) |
| Timeout counts| When the time granularity of query is five minutes, it indicates the number of GET/SET/DELETE timeout in the last five minutes. When the time granularity of query is one day, the value should be the peak of the day (counts per second) |

For more information about the monitoring metrics of Cloud Cache Service, please see [Read Monitoring Data API](https://cloud.tencent.com/doc/api/405/4667) in the Cloud Monitor API.

