Cloud Log Service (CLS) provides real-time log query capability to help you quickly locate business problems. Before performing log search, you need to configure and enable the index.

## Enabling Index

Index is an optional feature for log topics. You need to select a log topic to query, and then enable its index feature. Specific steps are as follows:

1. Log in to [CLS Console](https://console.cloud.tencent.com/cls).
2. Select **Logset** on the left, and then enter the target logset and log topic.
3. Select **Index Configuration**.
4. Enable **Full-text Index** or **Key-value Index** as needed, and select **Case-sensitive** (not selected by default).
5. Click **Save** to complete the index configuration.

> **Note:**
> After a log topic is created, its index feature is disabled by default. You need to manually enable it.

## Index Type
### Full-text index

CLS takes a complete single log as text for query. After full-text index is enabled, you can search the log by keywords.
![Full-text Index](
https://main.qcloudimg.com/raw/63bce8a39d0033ffd43f5a7644727dca.png)

### Key-value index

CLS supports key-value index configuration based on the key you set in the **Collection Configuration** tab. In the key-value index configuration, enter the appropriate key according to the index requirements, and specify its data type (text, long, or double).
![Key-value Index](
https://main.qcloudimg.com/raw/fe96d64574fd85c8f1c76ef4f3cdd79c.png)

### Case sensitivity

Case sensitivity refers to the accurate recognition of uppercase and lowercase letters in a string. If you need to recognize uppercase and lowercase letters during search, select **Case-sensitive** next to the index switch.

## Data Type
CLS supports the following three field types:

| Name | Description |
|-----|:-----|
| text | Text|
| long | Integer |
| double | Floating-point number |

## Notes
1. Log data collected during the period when the index is disabled cannot be searched for.
2. After the index is enabled, logs can be searched for immediately after they are collected.
3. The data storage time is the same as that set in the logset.
4. If a log topic is enabled and disabled for multiple times, the log data collected during the period when the topic is enabled can be searched for.

