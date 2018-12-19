## Cloud Log Service (CLS)

Cloud Log Service (CLS) provides a one-stop log data solution that allows you to easily access the system within 5 seconds to enjoy a complete range of reliable log services from log collection, storage, search, and to statistical analysis, without the need to consider resource problems such as scaling-up and scaling-down. The service can help you locate business issues with ease and deal with metric monitoring, security audit and other concerns about logs, greatly lowering the barrier to the log OPS.

Currently CLS is under internal trial. You can [click here](https://intl.cloud.tencent.com/apply/p/3w4g8jzhke5 ) to apply for a free trial. Your application for trying the service will be reviewed within 7 work days.

## Overview

CLS provides the following features:

- Log Collection: Collect logs to CLS from different log sources by using LogListener and API/SDK.


- Log Storage: Store log data using CLS.


- Log Index: Enable Log Index for log query, allowing users to pinpoint log problems quickly.


- Log Shipper: You can ship the specified logs to other cloud products to meet storage or other computing needs, for example, ship a log to a specified COS bucket to manage its lifecycle and meet the need for log audit.


### Log Collection

CLS supports collecting logs by using an agent and API/SDK, enabling you to easily collect log data from different regions, channels, platforms and data sources in real time and collect logs from various Tencent Cloud products.

- Real-time collection via Agent: Collect logs using LogListener. This method is featured by an easy installation as well as reliable and secure service, and supports most of mainstream Linux operating systems, delivering a high performance while taking up a small amount of resources.
- Collection via API/SDK (coming soon): Upload logs by calling API, without the need to install the agent. Multiple languages are supported.

### Log Index and Query

- Real-time index: Index collected log data in real time, allowing you to search data within 2 seconds.
- Excellent query performance: Query results are returned within seconds. Support searching TB-level log data and locating data quickly.
- Flexible query: Support full-text search, multi-keyword search, cross-topic query and other features.

### Log Shipper

This feature is used to ship logs to other Tencent Cloud products such as COS and TDF (coming soon) to meet the needs for log data storage and analysis.

- Ship to COS: Ship log data to the COS bucket under your account to store and manage the log data.
- Ship to CAS (coming soon): Ship log data to the CAS under your account to back up and store the log data for log audit.
- Ship to TDF (coming soon): Ship log data to TDF to allow customized data analysis.
