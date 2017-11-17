## Cloud Log Service (CLS)

Cloud Log Service (CLS) provides a one-stop log data solution that allows you to easily access the system within 5 seconds to enjoy a complete range of reliable log services from log collection, storage, search, and to statistical analysis, without the need to consider resource problems such as scaling-up and scaling-down. The service can help you identify business issues with ease and deal with metric monitoring, security audit and other concerns about logs, greatly lowering the barrier to the log OPS.

Currently CLS is under internal trial. You can [click here](https://cloud.tencent.com/act/apply/cloudlog) to apply for a free trial. Your application for trying the service will be reviewed within 7 working days.

## Overview

CLS provides the following features:

- Log collection: Collect logs to CLS from different log sources by using LogListener and API/SDK.


- Log storage: Store log data using CLS.


- Log indexing: Enable log indexing for log query, allowing users to pinpoint log problems quickly.


- Log delivery: You can deliver the specified logs to other cloud products to meet storage or other computing needs, for example, deliver a log to specified COS bucket to manage its lifecycle and meet the need for log audit.

![](https://mc.qcloudimg.com/static/img/a51bd8e655a9d8e17b93300b68170f9f/image.png)

### Log Collection

CLS supports collecting logs by using Agent and API/SDK, enabling you to easily collect log data from different regions, channels, platforms and data sources in real time and collect logs from various Tencent Cloud products.

- Real-time collection via Agent: Collect logs using LogListener. This method is featured by an easy installation as well as reliable and secure service, and supports most of mainstream Linux operating systems, delivering a high performance while taking up a small amount of resources.
- Collection via API/SDK (coming soon): Upload logs by calling API, without the need to install Agent. Multiple languages are supported.

### Log Indexing and Query

- Real-time indexing: Index collected log data in real time to enable data retrieval within 2 seconds.
- Excellent query performance: Query results are returned within seconds. Support retrieval of TB-level log data and quick data locating.
- Flexible query: Support full-text retrieval, multi-keyword search, cross-topic query and other features.

### Log Delivery

This feature is used to deliver logs to other Tencent Cloud products such as COS and TDF (coming soon) to meet the needs for log data storage and analysis.

- Delivery to COS: Deliver log data to the COS bucket under your account to store and manage the log data.
- Delivery to CAS (coming soon): Deliver log data to the CAS to back up and store the log data for log audit.
- Delivery to TDF (coming soon): Deliver log data to TDF to allow the customized data analysis.
