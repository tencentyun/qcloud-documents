## Overview

When you use LogListener to collect JSON logs, \n is used as the terminator of a log. The platform parses the first layer of JSON as a key-value pair.

## Configuration Steps

1. Go to the log topic for which JSON-based parsing needs to be configured. On the configuration page, edit the collection configuration and configure the collection path and server groups.

2. Configure the key value extraction mode: JSON.

3. Configure time: The collection time is used as the log data time by default. You can also specify a key as the log data time (**in sec**), and configure the time conversion format (which **supports all strftime functions**, such as %Y-%m-%d %H-%M:%S).

4. Configure filter (optional): If you need to filter log data before collection, you can configure the filter. The filter allows you to specify a specific key and configure filtering rules to filter logs. For example, you can specify that log data with errorcode=200 are not collected. A maximum of five filtering rules can be configured and regular expressions are supported.

   ![](https://mc.qcloudimg.com/static/img/0af46f5e283f0652ef4cb440c1c27aa4/image.png )

