### Description
Add multiple parameter configurations for the same event to achieve a more detailed tracking result. You can add multiple parameters under an event, and set multiple values under a parameter.
### Application Scenarios
For the same event, drill down to obtain values of different parameters, and calculate the number of occurrences and the number of people covered.
### Tips on Usage
1. Add event ID and event name in the event list on the [Console](http://mta.qq.com/mta/overview/ctr_all_app_new).
2. Click **Parameter Configuration** to configure parameters.
3. Add parameter and parameter name.
4. Copy generated code.
5. Configure parameter to generate parameter ID: paramid. The default value of the parameter is **true** and can be modified to any other character.
**Code example:**
```java
mta.Event.stat ('event_id',{paramid:'true'}).
```

### Notes
1. Parameter name contains letters and numbers.
2. Parameter ID contains letters and numbers.
3. Parameter ID and parameter name under the same event must be unique.
4. The mta Mini Program SDK must be embedded in the page.
5. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and set the event ID according to **Instructions on SDK Configuration**.

