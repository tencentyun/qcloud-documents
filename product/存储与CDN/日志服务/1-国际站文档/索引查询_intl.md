CLS provides diversified search features, supports real-time log query, and returns results in a second to help you quickly locate business problems.

## Starting Search

Log search is a very important capability provided by CLS. You can define the query conditions to query hundreds of millions of log data in a second. Specific steps are as follows:

1. Log in to [CLS Console](https://console.cloud.tencent.com/cls).
2. Select **Log Search** on the left of the console.
3. Select the time range, logset, and log topic.
4. Enter keywords, and click **Search** to get results.

## Search Rules
The time range, logset, and log topic are all required to perform log search. The default time range is the current day. You can select the logset and log topic as needed. The search box can be left empty, which means no filter conditions, and all valid log data will be returned.

### Full-text search
Each piece of log data in the log topic with full-text index enabled is split into multiple phrases by delimiters, so that you can search for the log by specific keywords.

For example, to search for log data containing the keyword "error", enter `error` in the search box and search for it.

### Key-value search
Log data of the log topic with key-value index enabled is managed based on the specified key-value pairs. You can search for the log by specifying a key field.

For example, to search for log data with "error" as the "status", enter `status:error` in the search box and search for it.

### Fuzzy keyword search
CLS provides fuzzy query that allows you to search logs by special fuzzy keywords. Details are described below:

| Metacharacter | Description |
|-----|:-----|
| * | A keyword for fuzzy query, which can refer to zero, one, or multiple characters. For example, entering `abc*` will return all the logs starting with `abc`. |
| ? | A keyword for fuzzy query, indicating that only one character can be placed at a specific location. For example, entering `ab?c` will return all the logs that start with `ab` and end with `c`, with only one character in between. |


### Multiple-keyword search
When you search for logs using multiple keywords (separated with commas, semicolons, or spaces), the log data meeting the **"AND"** logic is returned. That is, the returned logs contain all the keywords. Multi-keyword search is available in both full-text index and key-value index.

For example, to search for log data containing "error" and "400", enter `error 400` in the search box and search for it.

### Cross-topic search
Log search allows you to select only one logset but multiple log topics under the logset, which means that you can search for log data across multiple log topics under one logset at the same time, making it easier for troubleshooting.

## Notes
1. Before performing log search, make sure the index is enabled for relevant log topics. Otherwise, no valid logs will be found.
2. Before performing key-value search, make sure the index field to query is successfully configured in the index configuration of log topic.
3. Results are displayed in reverse order by default.

