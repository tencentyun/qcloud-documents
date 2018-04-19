Custom events can be used to provide statistics on the number of occurrences, duration, and trend of certain user-defined event-tracking points, such as clicks on ads, number of messages, etc. Generally, event_id represents the statistics of a certain behavior or feature (for example, counting the number of times the **Click** button was triggered), and parameter is used to identify the objects for which statistics is needed (for example, the button named **OK**). An event is uniquely identified by the combination of "event_id" and "parameter".

**Custom events are used in two scenarios:**
1. Statistics on number of occurrences: Count the number of times the specified behavior was triggered;
2. Statistics on duration: Count the time consumed by the specified behavior in seconds. It only takes effects when the APIs begin and end are used together.

Both Key-Value and variable-length string parameters are available for each event type. It is recommended to use the APIs using Key-Value parameters because they can express more content. If both of the parameter types are used in the code, it is recommended to use different event_ids.

>**Note:**
>event_id needs to be configured on Tencent's MTA website before it can be used in statistics. It cannot contain spaces or escape characters.

**Add events as shown in the figure below:**
![](//mc.qcloudimg.com/static/img/6c4dc4f4aa204f78127284a9b7af95ca/image.jpg)
**Add event parameters as shown in the figure below:**
![](//mc.qcloudimg.com/static/img/63fe65b08b8243445f7ff26c5b167645/image.jpg)
