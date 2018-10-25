### Description
If multiple processes are nested, user loss generated in each process is used to calculate the user conversion rate in each step.
### Application Scenarios
The next event can be performed only after the previous event has been performed. Calculate the proportion of users who enter into the next event after they have went through the previous one. For example: proceed through item **purchasing process** -> **event steps**, and then enter **item page** -> **purchase button** -> **purchased successfully**.
### Tips on Usage
1. Enable custom event tracking on the [Console](http://mta.qq.com/mta/overview/ctr_all_app_new), and obtain eventID.
2. Update App.onLaunch to report the initialization code, and insert eventID.
3. **Create Funnel Model** in the funnel model list.
4. **Unfold and View** code, and then copy the code into the method.

### Notes
1. Funnel event has at least two steps.
2. Generated event ID cannot be changed during modification.
3. The event ID and event name under the same funnel must be unique.
4. The next event must be the next process of the previous event, and they must be correlative.
5. The mta WeChat Mini Program SDK must be embedded.
6. If the custom event tracking is not enabled when adding code, you need to enable it on the console, and set the event ID according to **Instructions on SDK Configuration**.

