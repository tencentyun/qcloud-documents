### Feature Overview
After developers set the Key-Value on the Mobile Tencent Analytics website, the latest online parameter value can be dynamically obtained by calling API. The feature can be used in the following scenarios:
1. Content update, such as copywriting, price, welcome messages of App;
2. On-off control, such as Ad enabling and disabling;
3. Simple logic control, for example, changing the display of content when certain conditions are met;
4. Automatic update of Apps.

### Android Code Integration
**Update mechanism**

Online parameters configured by users at the frontend are not issued in real time. Instead, they are updated when SDK reports the session statistics logs. After parameters are configured for 10 minutes, you can exit the App to the backend for more than 30 seconds to trigger a timeout or terminate the App process and restart it, a session will be generated and parameters will be updated.

**Integration codes**

```
String StatConfig.getCustomProperty(String key, String defaultValue)
```
**Parameters**
key: the key configured by users at the frontend;
**Returned Value**
The value corresponding to key. If it does not exist, defaultValue is returned.

```
protected void someAction() { 
    // Get online parameter onlineKey
    String onlineValue = StatConfig.getCustomProperty("onlineKey", "off" );
    if(onlineValue.equalsIgnoreCase("on")){
        // do something
    }else{
        // do something else
    }
```
### iOS Code Integration
#### APIs

```
/**
 Get parameters configured on frontend console of MTA
 Before calling this function, you need to configure the parameters in **Custom Parameter** under **App Configuration Management** on frontend console of MTA for the configuration to take effect.
 It takes 3 to 5 minutes for the configuration to take effect after you configure them for the first time or change the parameter configuration.

 @param key Parameter key
 @param v Default value returned when no parameter is obtained
 @return Parameter value or default
 */
- (NSString *)getCustomProperty:(NSString *)key default:(NSString *)v;
```
#### Example

```
[[MTAConfig getInstance] getCustomProperty:@"parameter name" default:nil];
```
>**Note:**
>[Parameter name] must be the same as the one configured on the MTA console.
