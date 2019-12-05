CLS provides real-time log query capability to help you quickly locate business problems. Before performing log search, you need to configure and enable the index.

## How Does It Work

Log search is performed based on the key words of a log which are matched with the information you entered. You can flexibly adjust the key words by customizing a word separator or specifying whether to enable case sensitivity depending on your business needs. The following example uses a log to explain the word separator and case sensitivity.

```
10002345987;write;ERROR;code=400;topic does not exist;
```

### Word separator

The text of the original log can be split into several key words by use of a word separator to facilitate your search. For example:

- If the word separator is set to ";=", the log is split into 6 words: "10002345987", "write", "error", "code", "400", and "topic does not exist;". In exact search, you can find the log by typing any of the above words.
- If the word separator is set to null, the entire log is regarded as a word. In exact search, you have to type the entire word to search for the log.

### Case sensitivity

Case sensitivity refers to the precise distinction between uppercase and lowercase letters in a string. For example, when the word separator is ";=":

- If case sensitivity is enabled, the log cannot be found by typing "error". This is because "error" and "ERROR" are regarded as two different words.

- If case sensitivity is disabled, the log can be found by typing "error", "Error" or "ERROR".



## Enabling Index

Index is an optional feature for log topics. You need to select the log topic to query, and then enable its index feature. Specific steps are as follows:

1. Log in to the [CLS console](https://console.cloud.tencent.com/cls).
2. Select **Logset** on the left, and then enter the target logset and log topic.
3. In the Log Topic tab, select **Index Configuration**.
4. Enable Full-text Index or Key-value Index as needed, select Case-sensitive (not selected by default) and enter a word separator (default word separator: ```, "';=()[]{}?@&<>/:\n\t\r```).
5. Click **Save** to complete the index configuration.

> **Note:**
> After a log topic is created, its index is not enabled by default. You need to manually enable it.

## Index Type

### Full-text index

CLS uses a complete log as the text for search. When the full-text index is enabled, you can use key words to search for the log. You can also set a custom full-text word separator. The text of the original log is split into several key words by use of a word separator to facilitate your search.
![Full-text Index](http://chuantu.biz/t6/352/1533216745x-1404792742.png)

To illustrate the feature of full-text word separator, here are some examples for partial search.

| Full-text Word Separator | Exact Search | Fuzzy Search |
| ---------- | ------------------------------------------------------------ | ------------------------- |
| Set to null | Enter "10002345987;write;error;code=400;topic does not exist;" | Enter "10002345987*" |
| ;          | Enter "code=400" or "topic does not exist" | Enter "code=40?" or "code*" |
| ;=         | Enter "code", "400" or "code=400" | Enter "topic*" or "40?" |
| ;  =       | Enter "topic", "does", "not" or "exist" | Enter "do*" |

### Key value index

CLS can configure key value index according to the key in the collection configuration. In the key value index configuration, enter the appropriate key according to the index requirements, and specify its data type (text, long, or double). Custom word separators are supported by data in "text" type. Different word separators can be set for different keys.

![Key Value Index](http://chuantu.biz/t6/352/1533216775x-1404792742.png)



## Data Type

CLS supports the following three field types:

| Name | Type Description |
| ------ | :----------------------- |
| text   | Text |
| long   | Integer (Int 64) |
| double | Floating-point number (64 bit) |

## Notes

1. Log data collected during the period when the index is disabled cannot be found.
2. After the index is enabled, logs can be found immediately after they are collected.
3. The data storage time is the same as that in the logset.
4. If a log topic is enabled and disabled for multiple times, the log data during the enabling period can be found.

