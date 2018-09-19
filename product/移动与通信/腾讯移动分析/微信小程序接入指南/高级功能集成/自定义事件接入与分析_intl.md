### Description
Calculate the number of times the event is triggered by adding a custom event reporting code to the method.
### Procedure
1. Enable custom event tracking on the [Console](http://mta.qq.com/mta/overview/ctr_all_app_new), and obtain eventID.
2. Update App.onLaunch to report the initialization code, and insert eventID.
3. Configure custom events and parameters (if needed) in **Basic Analysis** -> **Custom Events** -> **Event List**, and custom event code is generated. Call mta.Event.stat(...) at the location where event occurs. For example:

```java
mta.Event.stat("ico_search", {"query":"Tesla"});//Track a search event here
```
 
"ico_search" is the event ID which is customized in the configuration management page.
"query" is the key of event parameter which is customized in the configuration management page.
"Tesla" is the value of event parameter which is input by the user in the business system.
### Notes
1. Event name contains letters, numbers and underlines.
2. Event ID contains letters and numbers.
3. Event ID and event name must be unique.
4. The mta Mini Program SDK must be embedded.
5. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and set the event ID according to **Instructions on SDK Configuration**.

