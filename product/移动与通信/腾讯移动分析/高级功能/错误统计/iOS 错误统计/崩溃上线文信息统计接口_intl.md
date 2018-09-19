When crash occurs, MTA automatically captures the crash stack and basic context information, and reports it at the next startup. In addition, developers can also call specific APIs to store additional context information that will be reported along with the crash report when crash occurs for debugging purpose.

```obj-c
/**
Set a custom tag
When crash occurs, the tag you set is reported to locate the problem

@param tagKey The Key of tag. If key is set, the new value will overwrite the old one.
@param tagValue The value of tag
*/
+ (void)setCustomTag:(NSString *)tagKey value:(NSString *)tagValue;


/**
Output diagnostic messages
When crash occurs, the last 50 output diagnostic messages are reported to locate the problem

@param log Diagnostic message
*/
+ (void)traceLog:(NSString *)log;
```
