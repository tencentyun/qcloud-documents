You can customize event analysis. You can track user behaviors such as number of clicks by configuring the event in the console and tracking it via codes at backend. For more information, please see [Help Documentation](https://cloud.tencent.com/document/product/549/13059
).
When an App is created, three events are registered by default. Upon integration of the SDK, the custom event feature is available after you add the sample event tracking code.

### API Content
```
void StatService.trackCustomKVEvent(Context ctx, String event_id, 
Properties properties)
```
### Parameters

| Parameter Name | Description |
|---|---|
| Ctx | device context of the page |
| event_id | Event ID |
| args | Event parameter |

### Codes

The following three events are preconfigured by MTA in the console. You can collect the desired data by adding an event tracking code to the specific position.
```
// The homepage entry event for counting the number of times that users enter the homepage
StatService.trackCustomKVEvent(this, "homepage", null);

// The user registration event for counting the number of times that users click the registration button
StatService.trackCustomKVEvent(this, "register", null); 

// The user login event for counting the number of times that users click the login button
StatService.trackCustomKVEvent(this, "login", null);

```

