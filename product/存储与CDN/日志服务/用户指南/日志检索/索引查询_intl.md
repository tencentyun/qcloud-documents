CLS provides comprehensive search features, supports real-time log query, and returns results in a second to help you quickly locate business problems.

## Starting Search

Log search is a very important capability provided by CLS. You can define the query conditions to query hundreds of millions of logs within a second. Specific steps are as follows:

1. Log in to [CLS Console](https://console.cloud.tencent.com/cls).
2. Select **Log Search** in the left of the console to enter the search page.
3. Select the time range, logset, and log topic.
4. Enter keywords, and click Search to get results.

## Search Rules
The time range, logset, and log topic are required for log search. The default time range is the current day. You can select the logset and log topic as needed. The search box can be left empty, which means no filter conditions, and all valid log data will be returned.

### Full-text Search
Log data of the log topic for which full-text index is enabled is split into multiple phrases with word separators, so that you can search the log by specific keywords.

For example, to search for log data containing the keyword "error", enter `error` in the search box and search for it.

### Key-value Search
Log data of the log topic for which key-value index is enabled is managed based on the specified key-value pairs. You can search the log by specifying a key field.

For example, to search for log data with "error" as the status, enter `status:error` in the search box and search for it.

### Fuzzy Keyword Search
CLS provides fuzzy query that allows you to search logs by special fuzzy keywords. Details are described below:

| Metacharacter | Description |
|-----|:-----|
| * | A keyword for fuzzy query, which can contain zero, one, or multiple characters. For example, entering `abc*` will return all the logs starting with `abc`. |
| ? | A keyword for fuzzy query, indicating that only one character can be placed at the specific location. For example, entering `ab? C` will return all the logs that start with `ab` and end with `c`, with only one character in between. |


### Multiple-keyword Search
When you search logs using multiple keywords (separated by commas, semicolons, or spaces), the log data meeting the "AND" logic is returned. That is, the returned log data contains all the keywords. Multi-keyword search is available in both full-text index and key-value index.

For example, to search for log data containing "error" and "400", enter `error 400` in the search box and search for it.

### Cross-topic Search
Log search allows you to select only one logset but multiple log topics under the logset, which means that you can search for logs across multiple log topics under one logset at the same time, making it easier for troubleshooting.

## Notes
1. Before performing log search, make sure the index feature is enabled for relevant log topics. Otherwise, no valid logs will be searched for.
2. Before performing key-value search, make sure the index field to query is successfully configured in the index configuration of log topic.
3. The search results are displayed in descending order by default.

