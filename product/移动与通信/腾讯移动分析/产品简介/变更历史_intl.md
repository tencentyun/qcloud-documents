### MTA 1.6.3 Released on November 16, 2017

1. Added audience targeting in advertising. With one-click extraction of core users, advertisements can be rapidly delivered to the targeted potential users, thus improving advertising RO. For more information, please see [detailed descriptions
](https://cloud.tencent.com/document/product/549/13088).
2. Optimized the prompt for exporting the details of segmentation parameter events, and made it clear that logs within the last 30 days can be saved.
3. Fixed the problem of inconsistency between the used log quota as prompted and the number of saved logs in the segmentation parameter event to avoid misunderstanding.
4. Fixed the problem that the history trend data does not update promptly with the channel after switchover in data overview for Android.
5. Fixed the problem that user segments can be saved even if events are not defined in user segmentation.

### MTA 1.6.2 Released on November 9, 2017

1. Added the prompt of **Loading** while PV and UV metrics of HTML5 App and WeChat mini programs are loading asynchronously in the App list in the console, avoiding no data to display and improving user experience.
2. Optimized the prompt under the page path feature.
3. Fixed the problem that Chinese characters cannot be entered while a user is modifying an event ID after executing **New Custom Event**.

### MTA 1.6.1 Released on November 2, 2017

1. Added the prompt of **Report IDFA to view precise profile** in the user profile feature for iOS when data error is greater than 5%, helping users to report IDFA quickly to minimize data error.
2. Added analysis of installation sources and channels, through which you can count and analyze the number of clicks and activations, and compare advertising effects of different channels, so as to configure channels rationally.
3. Optimized the interaction style of data boards, improving user experience.
4. Fixed the problem that you are redirected to wrong pages when you click some data boards.
5. Fixed the problem that the data board cannot be loaded when it is redirected to another page and then redirected back to the original data board.
6. Fixed the problem that "---" is displayed when user segmentation size is 0.

### MTA 1.6.0 Released on October 26, 2017

1. Supported H5 data statistics in Hybird App. You can add H5 custom events and analyze H5 page and App as needed.
2. Added the feature of exporting the configured customer segments to Tencent Social Ads to achieve targeted advertising in the marketing system. This feature is under trial. Contact customer service if you want to try out it.
3. Added custom data board, which allows you to integrate different data reports to a board for quick view and share it to colleague.
4. Added generating user segments with one-click beside metrics to help you segment customers rapidly and view their data.
5. Optimized the description of average duration in the event parameter.
6. Fixed the problem that the displayed number of events is incorrect when you edit the existing user segments.
7. Fixed the problem that the version distribution report cannot be queried due to large data volume.

### MTA 1.5.9 Released on October 19, 2017

1. Added the feature of exporting event details. You can export events that contain event parameter logs locally by one click.
2. Fixed the problem that not all models are displayed when segmenting users by iOS models.
3. Fixed the problem that user segmentation does not work after it is enabled.
4. Fixed the problem that the file name cannot be read after the segmented user data is downloaded into a file.
5. Removed update reminder from the login board.

### MTA 1.5.8 Released on October 12, 2017 

1. Added user segmentation by number of events, helping developers to extract highly-valued and highly-active TAs.
2. Added user segmentation by active users, inactive users, and new users, helping developers to extract new, lost, and returning TAs.
3. Added statistics of installation source and channels for Beta version. If you want to try out, contact customer service.
4. Optimized the display of UI and the prompt that a repaired Crash may occur again.
5. Optimized the prompt of unavailable time selector for user profile.
6. Fixed the problem that the TA profile can be seen even when the TA size is smaller than 100.

### MTA 1.5.7 Released on September 28, 2017 

1. Optimized the **New User Group** button, making it clearer. 
2. Optimized the display of security verification for e-mail addresses of new users.
3. Optimized data update of channels and the version filter. The reported codes are updated in the filter in real-time, quickening the verification of these codes.
4. Fixed the problem of failure to display the **Configuration Management**module in Demo App.
5. Fixed the problem of abnormal display of page path UI.
6. Fixed lack of a reminder icon when metrics fluctuate.
7. Removed user feedback for Android. This feature is no longer supported by Android.

### MTA 1.5.5 Released on September 21, 2017

1. Allowed developers to **define user attributes depending on business** and report at the terminal, and view the activeness, key behaviors and funnel of TAs of different attributes in the console.
2. Added user segmentation by user devices' CPU, number of cores, and memory, helping developers to achieve compatibility on different devices.
3. Added a metric fluctuation reminder to make it easy for users to monitor business metrics.
4. Fixed the problem of failure to display the target e-mail address when you create a reminder for completion of exporting user segmentation details.
5. Fixed the unavailability of the edition and deletion buttons in the group management of channels.
6. Fixed the unavailability of the email button in data subscription.

### MTA 1.5.4 Released on September 11, 2017

1. Allowed **the funnel model to set steps by custom event parameters**, significantly expanding the application scope of this model.
2. Allowed **exporting and downloading user mobile number package by user segments**. You can import the mobile number package to your business database, and then push messages and ads.
3. Added de-duplicated metric reports regarding new users in **Historical Trend**, **Channel Distribution**, **Channel Effect**, and **Version Distribution**.
4. Optimized the event list filter and allowed visualized event tracking for filtering, so that you can quickly find events added by visualized event tracking when there is a large amount of event lists.
5. Removed the **New Value** button from the custom event parameter page to avoid the misunderstanding that custom event values should be declared in the console.
6. Removed the display of the error message of **No Data in the App** from the user center.
7. Fixed several problems in the data subscription page.
8. Fixed the problem of failure to find the appropriate permission when you define user groups by channel permissions in the permission system.
