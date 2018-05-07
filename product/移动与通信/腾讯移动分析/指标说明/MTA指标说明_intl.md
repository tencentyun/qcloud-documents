## Glossary ##
**1. User**

A user refers to a device that installs a specified App. The device ID is used as the user ID. For an iOS device, the device ID is its OpenUDID. For an Android, the device ID is its IMEI+MAC.

**2. Launch**

A launch is counted every time a user opens a visible page of an App.

If a user switches from the launched App to the backend and then back to the App within 30 seconds, no new launch is created. If the switchback action happens after 30 seconds, a new launch is created. The default value is 30 seconds. Users can define this value as needed.

**3. Channel**

A channel refers to a platform from which an App is downloaded and installed. If a user downloaded and installed an App from multiple channels, the user is counted in the number of users using the first channel.

The channel information can be acquired from the installation package. For more information, please see the development document.

**4. Version**

The App-defined version information includes version upgrades and usage of each version. If a user has upgraded an App to multiple versions, the user is counted in the number of users using the latest version. Therefore, filtering by version is not reliable, because the number of users using each version changes when new versions come out.

## Metric Description ##

| Metric Name | Description |
| :--------: | :------|
| New user<br> (Offline + Real-time) | A user who launches the App for the first time. Users who reinstall the App after uninstallation do not belong to new users. (Deduplication) <br><br> Offline calculation: Remove duplicate user IDs from all logs and compare the remaining user IDs with the historical record. The user IDs not listed in the record are counted as new users. Offline calculation is very accurate. <br><br> Real-time calculation: Due to large calculation pressure and costs, the SDK that marks new users and old users is used to calculate new users .Real-time calculation is not as accurate as offline calculation. |
| New account | An account under which the App is launched for the first time. If the App is launched by multiple devices under one account, it is considered that the App is launched under the account for one time. Developers need to manually configure and report the account data (after deduplication). |
| Active user <br>(Offline + Real-time) | Default: Active users are calculated based on visit duration by tracking logs of "Page Visit" and "Frontend and Backend Switch". New users and upgrading users are counted as active users by default. <br><br> To calculate active users of special Apps that often run at backend, such as security and music Apps, users can apply to the platform for tracking logs (such as page visit, frontend and backend switch, session log, error log, and custom event) according to their needs. |
| Active account | An account under which the App is launched. The account under which the App is launched for multiple times is counted as one active account. The account under which the App is launched by multiple devices is counted as one active account. Developers need to manually configure and report the account data (after deduplication). |
| Proportion of New Users | Number of new users/number of active users |
| Cumulative users | Number of users who launched the App up to now. A user who launched the App for multiple times is counted once. (Deduplication) <br><br> Cumulative users up to the current day = Historical cumulative users + New users on the current day |
| Weekly (Monthly) active rate | Weekly (Monthly) active users/Accumulative users |
| launch count <br>(Offline + Real-time) | Number of times the App is launched. <br><br> Remove duplicates in logs of "Page Visit" and "Frontend and Backend Switch" as well as duplicate session IDs in "Session" log. |
| Cumulative launch count | Number of times the App is launched up to now. |
| Duration of use | By default, it refers to the duration of use shown on the visible interface after the App is launched. |
| Page visit duration | The duration from the start of page visit to the end of page visit. Closing the App, switching to the backend, and interruption by phone call equal end of page visit. |
| Number of visits to a page| A page visit is calculated from the start to the end of the visit to a page. Closing the App, switching to the backend, and interruption by phone call equal end of page visit. |
| Number of visited pages | Number of pages that a user has visited. The page that has been visited for multiple times is counted once. (Deduplication) |
| Ranking by page visits | Sort all pages by the number of visits to them. |
| Ranking by page visit duration | Sort all pages by the total visit duration of each page. |
| Upgrading user | A user who upgraded the App to the specified version, which is determined by the version string. A user who downgraded the App from a version is counted as an upgrading user of that version. (Deduplication) |
| Bounce rate | Number of visits to a page after which users immediately close the App to the total number of visits to the page. If a visit is terminated due to any error, it will not be counted for the bounce rate. |
| Average duration of use | Duration of use/launch count |
| Average duration of use per user | Total duration of use/number of active users |
| Average launch count per user | Launch count/number of active users |
| Average page visit duration per user | Page visit duration/number of active users |
| Average page visits per user | Number of visits to the page/number of active users |
| Average page visit duration | Visit duration on a page/number of visits to the page |
| Average visit duration per page | Visit duration on all pages/number of visited pages |
| Average visit frequency per page | Number of visits to all pages/number of visited pages |
| Daily/Weekly/Monthly active user (DAU/WAU/MAU) | A user who launched the App and browsed pages on a device within the last 1/7/30 day(s). A user who launched the App for multiple times within the last 1/7/30 day(s) is counted as one active user. |
| DAU/WAU | DAU refers to the number of active users on the selected day. WAU refers to the number of active users within the past 7 days starting from the selected day (inclusive). <br> This ratio is used to measure the user loyalty to an App. Higher ratio means higher user loyalty. |
| DAU/MAU | DAU refers to the number of active users on the selected day. MAU refers to the number of active users within the past 30 days starting from the selected day (inclusive).<br> This ratio is used to measure the user loyalty to an App. Higher ratio means higher user loyalty. A DAU/MAU ratio of less than 20% means poor user loyalty. |
| Churned user | A user who was active in one observation period, but inactive in the next observation period. |
| Returning user | A user who was active in the first observation period, inactive in the second observation period, and became active in the third observation period. |
| AU within the past N days/weeks/months | A user (active) who has launched the App daily/weekly/monthly within the past N days/weeks/months starting from the specified day. |
| Loyal user | A user (active) who has launched the App weekly within the past 5 weeks starting from the specified day.
| N-day retained user| A new user who still uses the App after N days. The proportion of these N-day retained users in the total new users for the same period is N-day retention rate. |
| Triggering user | A user who triggered an event. (Deduplication) |
| Event count | Number of times the event was triggered by users |
| Event duration | The total length of time an event lasted (For example, if a user plays the song A for 10 minutes and pauses it for 15 minutes, the duration of the playback event is 10 minutes and that of pause event is 15 minutes) |
| Average duration of event | Event duration/event count |
| Average duration of event per user | Event duration/number of triggering users |
| Average events per launch | Event count/launch count |
| Average events per user | Event count/number of triggering users |
| User engagement | Number of triggering users/number of active users |
