## Overview

When using LogListener to collect separator-based logs, \n is used as the terminator of a log. Logs are structured based on the separator configured for logs and the key field of each column you configured. For example, if the raw data of a log is `10002345987;write;error;topic does not exist`, then you can specify separator as the mode for parsing logs. In this case, the separator is semicolon, and keys are eventid, action, status and msg. So, the log is structured into four key-value pairs, i.e. `eventid:10002345987 action:write status:error msg:topic does not exist`.

## Configuration Steps

1. Go to the log topic for which separator-based parsing needs to be configured. On the configuration page, edit the collection configuration and configure the collection path and server groups.

2. Configure the key value extraction mode: Select **Separator** as the key value extraction method, and specify the separator. You can choose a common separator, such as space, tab, semicolon and vertical bar, or customize a separator. Custom separators support multiple characters, in which case the exact match rule applies during parsing of logs. For example, if && is set as a separator, abc&dce is not separated.

3. Configure time: The collection time is used as the log data time by default. You can also specify a key as the log data time (**in sec**), and configure the time conversion format (which **supports all strftime functions**, such as %Y-%m-%d %H-%M:%S).

4. Configure filter (optional): If you need to filter log data before collection, you can configure the filter. The filter allows you to specify a specific key and configure filtering rules to filter logs. For example, you can specify that log data with errorcode=200 are not collected. A maximum of five filtering rules can be configured and regular expressions are supported.

   ![](https://mc.qcloudimg.com/static/img/e8f12b5d261f5c5ba59a4370dcd44b49/image.png )

