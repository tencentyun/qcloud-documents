### Configure application's user attributes
In **Application Manager** -> **Configuration Management** -> **Configure User Attributes**, configure your user attributes.
![](//mc.qcloudimg.com/static/img/f13b7cf19b89de685fef8e00daeb91e4/image.png)
### Reporting attributes on the code side

#### Reporting custom user attributes on Android:
```java
// Encapsulate MTA user attribute parameters in key-value format
JSONObject customProperty = new JSONObject();
customProperty.put("user attribute 1", "attribute value 1");
customProperty.put("user attribute 2", "attribute value 2");
// Call the API for reporting
// context: app context; customProperty: custom attribute value
StatService.reportCustomProperty(context, customProperty);
```
#### Reporting custom user attributes on iOS:
```
/**
User-defined attributes are supported

@param kvs: in key-value format, such as "user attribute 1", "attribute value 1"
*/
+ (void)setUserProperty:(NSDictionary *)kvs;
```




