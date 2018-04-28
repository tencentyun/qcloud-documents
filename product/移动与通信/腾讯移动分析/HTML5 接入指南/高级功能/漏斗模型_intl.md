### Description
If multiple processes are nested, user loss generated in each process is used to calculate the user conversion rate in each step.
### Application Scenarios
The next event can be performed only after the previous event has been performed. Calculate the proportion of users who enter into the next event after they have went through the previous one. For example: proceed through item **purchasing process** -> **event steps**, and then enter **item page** -> **purchase button** -> **purchased successfully**.

### Tips on Usage
1. Log in to [Mobile Tencent Analytics Console](http://mta.qq.com/mta/overview/ctr_all_app_new), select **HTML5 App** and click on your App. **Create Funnel Model** in [Funnel Model List](http://mta.qq.com/h5/visitor).
2. **Unfold and View** code, and then copy the code into the page.

### Notes
1. Funnel event has at least two steps.
2. Generated event ID cannot be changed during modification.
3. The event ID and event name under the same funnel must be unique.
4. The next event must be the next process of the previous event, and they must be correlative.
5. "mta js sdk" must be embedded in the page.
6. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and then update the new mta h5 and report js.

