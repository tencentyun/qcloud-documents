CLS provides real-time log query capability to help you quickly locate business problems. Before performing log search, you need to configure and enable the index.

## Enabling Index

Index is an optional feature for log topics. You need to select the log topic to query, and then enable its index feature. Specific steps are as follows:

1. Log in to [CLS Console](https://console.cloud.tencent.com/cls).
2. Select **Logset** on the left bar, and then enter the target logset and log topic.
3. In the Log Topic tab, select **Index Configuration**.
4. Enable **Full-text Index** or **Key-value Index** as needed, and select **Case-sensitive** (not selected by default).
5. Click **Save** to complete the index configuration.

> **Note:**
> After a log topic is created, its index is disabled by default. You need to manually enable it.

## Index Type
### Full-text Index

CLS takes a complete single log as text for query. After full-text index is enabled, you can search the log by keywords.
![Full-text Index](https://main.qcloudimg.com/raw/7347d861b8143c0ce7da5041488c3569.png)

### Key-value Index

CLS can configure key-value index according to the key set in the collection configuration. In the key-value index configuration, enter the appropriate key according to the index requirements, and specify its data type (text, long, or double).
![Key-value Index](https://main.qcloudimg.com/raw/d65bc5a6b68316eb5316019f5f41de07.png)

### Case Sensitivity

Case sensitivity refers to the distinction between uppercase and lowercase letters in a string. If you need to distinguish between uppercase and lowercase letters during search, select **Case-sensitive** next to the index switch.

## Data Type
CLS supports the following three types of fields:

| Name | Description |
|-----|:-----|
| text | Text|
| long | Integer |
| double | Floating-point number |

## Notes
1. Log data collected during the period when the index is disabled cannot be searched for.
2. When the index is enabled, logs can be searched for immediately after they are collected.
3. The data storage time is the same as that in the logset.
4. If a log topic is enabled and disabled for multiple times, the log data during the enabling period can be searched for.

