## Concept

COS provides users with several storage levels, including Standard Storage, Low-frequency Storage and Nearline Storage. Users may choose their storage level according to their business scenarios, they can also adjust storage level either automatically or manually when using COS, to fit their current business scenario. Refer to [Billing Item Overview](/document/product/436/6239) for detailed prices

## Standard Storage

High-frequency Storage provides users with Cloud Object Storage with high reliability, high availability and high performance. High-frequency Storage has low access latency and high throughput, which means it is suitable for business scenarios with large amount of hot files and data that is accessed frequently.

Suitable scenarios: Hot videos, social images, mobile applications, game programs, dynamic websites

## Low-frequency Storage

Low-frequency Storage provides users with Cloud Object Storage with high reliability, relatively low storage cost and access latency. Low-frequency Storage is suitable for business scenarios with low access frequency. Low-frequency Storage has lower storage cost, while maintaining a Time to First Byte within milliseconds. Users can read data with fast speed when retrieving data, without the need to wait. But this method comes with a minimum storage time requirement. Retrieving or deleting data early will incur a certain cost.

Suitable scenarios: Online disk, big data analysis, government-enterprise business data, low-frequency files, monitoring data

## Nearline Storage

Nearline Storage provides users with online storage with high reliability and low cost. Nearline Storage is positioned between online storage and offline storage. Nearline Storage is suitable for business scenarios where the data is not accessed frequently, but is still required to be read online when necessary. The most obvious feature of Nearline Storage is that its price is similar with that of offline storage, while Nearline Storage is still able to respond within seconds.

Suitable scenarios: Medical archives, business logs, contract/legal archives, media data archives, disaster recovery backup

## Performance Comparison

| Product Comparison   | Standard Storage          | Low-frequency Storage          | Nearline Storage          |
| ------ | ------------- | ------------- | ------------- |
| Persistency    | 99.999999999% | 99.999999999% | 99.999999999% |
| Availability    | 99.95%        | 99.9%         | 99%           |
| Minimum storage time | None             | 30 days           | 90 days           |
| Retrieval fee   | None             | Charge by usage (GB)      | Charge by usage (GB)      |
| Time to first byte  | Millisecond            | Millisecond            | Second             |


