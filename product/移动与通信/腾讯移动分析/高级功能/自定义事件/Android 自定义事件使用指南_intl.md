### Registering Custom Events
The registration (configuration) of a custom event includes the registration of event ID and the registration of parameter information under the event ID.
1. Log in to the [MTA frontend](http://mta.qq.com/) and select **Application Analysis** -> **Event Analysis** -> **Custom Event**. 
2. Select **New Event**, and fill in the event ID, key, value and other information as required.
3. You can view the details of all parameters reported under the event ID in **Parameters** under **View Details**.

### [Statistics on Clicks] Events with Key-Value Parameter

```java
void StatService.trackCustomKVEvent(Context ctx, String event_id, 
Properties properties)
```

1. Parameter
Ctx: Context of the device on the page
event_id: Event ID
properties Key-Value: Parameter pair. The type of both key and value is String.
2. Calling location: Anywhere in the code
```java
public void onOKBtnClick(View v) {
// Calculate the number of clicks on a button. Object: OK button
Properties prop = new Properties();
    prop.setProperty("name", " OK ");
    StatService.trackCustomKVEvent(this, " button_click", prop);
}
public void onBackBtnClick(View v) {
// Calculate the number of clicks on a button. Object: back button
Properties prop = new Properties();
    prop.setProperty("name", " back ");
    StatService.trackCustomKVEvent(this, " button_click", prop);
}
```

### [Statistics on Clicks] Events with Arbitrary Parameter
1. Parameter: 
Ctx: Device context of the page
event_id: Event ID
args: Event parameter
2. Calling location: Anywhere in the code
```java
public void onClick(View v) {
// Calculate the number of clicks on a button. Object: OK button
    StatService.trackCustomEvent(this, "button_click", "OK ");
}
```

### [Statistics on Duration] Events with Key-Value Parameter

You can specify the start and end time of an event to report an event with a statistical duration.
```java
void StatService.trackCustomBeginKVEvent(
Context ctx, String event_id, Properties properties)
void StatService.trackCustomEndKVEvent(
Context ctx, String event_id, Properties properties)
```
1. Parameter
Ctx: Device context of the page
event_id: Event ID
properties Key-Value: Parameter pair. The type of both key and value is String.
2. Calling location: Anywhere in the code
```java
public void onClick(View v) {
Properties prop = new Properties();
    prop.setProperty("level", "5");
// Calculate the time that the user has spent to pass a level. Level: 5
// Before the user passes the level
StatService.trackCustomBeginKVEvent(this, " playTime", prop);
    // The user is playing the game...
    // .......
    // When the user has passed the level
StatService.trackCustomEndKVEvent(this, " playTime", prop);
}
```

### [Statistics on Duration] Custom Events with Statistical Duration

You can specify the start and end time of an event to report an event with a statistical duration.

```java
void StatService.trackCustomBeginEvent(
Context ctx, String event_id, String... args)
void StatService.trackCustomEndEvent(
Context ctx, String event_id, String... args)
```
1. Parameter
Ctx: Context of the device on the page
event_id: Event ID
args: Event parameter
2. Calling location: Anywhere in the code
```java
public void onClick(View v) {
    // Calculate the time that the user has spent to pass a level
// Before the user passes the level
StatService.trackCustomBeginEvent(this, " playTime", "level5");
    // The user is playing the game...
    // .......
    // When the user has passed the level
StatService.trackCustomEndEvent(this, " playTime", " level5");
```
>**Note:**
>Events can be reported properly only when trackCustomBeginEvent and trackCustomEndKvent come in pairs with the same parameter list.
