SCF provides a quota limit for each user account.


## Quota Limits

Quota limits based on user accounts are as follows:

| Item | Default Quota Limit |
| --- | --- |
| Maximum number of SCFs per region | 20 |
| Maximum number of concurrently executed instances per SCF | 20 |
| Maximum number of triggers configured for an SCF | 4, including a maximum of 2 COS triggers, a maximum of 2 CMQ triggers, or a maximum of 2 CKafka triggers |

Quota limits based on operating environments are as follows:

| Item | Quota Limit |
| --- | --- |
| Memory | 128-1536 MB. The increment is 128 MB. |
| Temporary cache (Directory /tmp) | 512 MB |
| SCF running duration | 1-300 seconds |
| Number of file descriptors | 1024 |
| Number of processes and threads | 1024 |
| Size of a synchronous request event | 6 MB |
| Size of a synchronous request response | 6 MB |
| Size of an asynchronous request event | 128 KB |

## Quota Increase

The following quotas can be increased:

* Maximum number of SCFs per region
* Maximum number of concurrent runs per SCF
* Maximum number of triggers configured for an SCF

To increase quota limits, [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&step=1) that describes the quotas of items you want to increase to.

