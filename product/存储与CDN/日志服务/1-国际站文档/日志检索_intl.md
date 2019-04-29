CLS provides real-time log query to help you quickly pinpoint business problems. You can select multiple log topics in the same logset to perform cross-topic query.

## Procedure

### Enable Index

Select the log topic to be queried, and enable the index. Log topics whose indexes are not enabled will not be searched. The storage time of the index data needs to be consistent with that of the logset you set. If the index of a log topic is enabled and disabled for multiple times, the log data during the index enabling period can be retrieved.

> **Note:** After a logset is created, its index is not enabled by default. You need to manually enable it.

![](https://mc.qcloudimg.com/static/img/a2919cbb8a1dc385b587af60c81c44c7/image.png)

### Enter Keywords

Enter the **Log Search** page, and select the time for the log data to be queried. Select a logset and multiple log topics under the logset, and enter keywords to query.

CLS provides a full-text search capability, and supports multiple-keyword and cross-topic search. When you use multiple-keyword search, separate keywords by commas, semicolons, and spaces, and the result with "and" is returned. That is, the returned log data contains all the keywords.![](https://mc.qcloudimg.com/static/img/435ab38a97b7ea08bfd478d38129c788/image.png)

