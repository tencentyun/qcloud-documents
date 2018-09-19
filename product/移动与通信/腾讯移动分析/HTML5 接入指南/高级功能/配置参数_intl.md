### Description
Add multiple parameter configurations for the same event to achieve a more detailed tracking result. You can add multiple parameters under an event, and set multiple values under a parameter.
### Application Scenarios
Calculate the number of clicks of html tags that require click effect under different categories in different locations, and also calculate the total clicks.

### Tips on Usage
1. Add event ID and event name in [Event List](http://mta.qq.com/mta/overview/ctr_all_app_new).
2. Click **Parameter Configuration** to configure parameters.
3. Add parameter and parameter name.
4. Copy generated code.
5. "True" in the code is the default value of new parameter, and can be modified to other letters or numbers.
```
MtaH5.clickStat('test',{paramid:'true'})
```

### Notes
1. Parameter name contains letters and numbers.
2. Parameter ID contains letters and numbers.
3. Parameter ID and parameter name under the same event must be unique.
4. "mta js sdk" must be embedded in the page.
5. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and then update the new mta h5 and report js.

