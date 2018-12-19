### Why cannot I view the data?
Timestamp: Check whether the time of the test device is set to the current time.
### How are your users (and other metrics) defined? What features do I have to set myself, and what features are available after accessing?
For more information, please see [Glossary](https://cloud.tencent.com/document/product/549/13114) and quick start, which provide notes for the places to be filled out.
### Why real-time data cannot be viewed until the next day?
Do not set the channel or version to 0 or leave it empty.

### Why is the data different from my own statistics?
In view of network and experience, some report policies are set. Not all data will be reported immediately, because a 7-day regression model is added at the backend and data are divided into different levels, and data of high level are preferred to be reported. Please pay attention to the data level and report policy, and check the features enabled by the accessed MTA. The real-time data are the successfully reported data, but not the final data.

### A new channel has been released today. Why doesn't it appear in the channel report?
The channel is not shown in real time, so the channel released today will not be seen until tomorrow.

### When can I see the correct data after I have configured the calculation event?
What we now see in real time is the result based on common event calculation. The result obtained based on the calculation event configuration rule can be seen the next day. The calculation event needs to be configured both in the frontend report of MTA and in the codes.

### Why does the statistics of the funnel model only count the number of users but not the number of events?
The number of users at a certain step in the funnel model refers to the number of users who have completed this step and the previous steps. The association between events is based on "users who meet the two conditions". That is why there is only the number of users, but not the number of events. The reference of the number of events in this definition is not very significant.

### Why does it prompt that parameters are missing and the call failed?
Check whether any permission setting is missing based on demo.

### Why are lots of errors like this shown in error management after we change the version to 2.0?
![](//mc.qcloudimg.com/static/img/04d1ec11a9acf14070b0e4f8c1e46977/image.jpg)
![](//mc.qcloudimg.com/static/img/2717779cb72046bb757fc88e5062b876/image.jpg)
Crash is reported by many users with incompatible models, and the backend is full of this type of error.
![](//mc.qcloudimg.com/static/img/48a168fa224c57880dd4c5dc303e6cb3/image.png)
This is a problem in previous SDKs. The actual crash is caused by the App. Ignore the two lines of stacks if they appear.

