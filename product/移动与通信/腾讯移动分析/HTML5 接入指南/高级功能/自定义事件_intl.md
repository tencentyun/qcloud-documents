### Description
Calculate the number of clicks of an event by adding H5 click reporting code in page element.
### Application Scenarios
1. Calculate the number of clicks of the specified button or link in the page.
2. Calculate the number of clicks of html tags that require click effect.

### Tips on Usage
1. Add event ID and event name in [Event List](http://mta.qq.com/mta/overview/ctr_all_app_new).
2. Embed the code onclick="MtaH5.clickStat ('Event ID')" in html tags that require click effect.

### Notes
1. Event name contains letters, numbers and underlines.
2. Event ID contains letters and numbers.
3. Event ID and event name must be unique.
4. "mta js sdk" must be embedded in the page.
5. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and then update the new mta h5 and report js.

