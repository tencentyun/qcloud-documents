### Why are real-time data and offline data not matched?

Because pressure and cost of real-time calculation are too heavy, and the methods of real-time and off-line calculation are different, the data results of the two calculation methods are slightly deviated. The data of offline calculation is more accurate.

### Why is the number of new users greater than that of active users?

New user statistics takes all logs while active user statistics takes logs on **Page Access** and **Frontend and Backend Switch**. In extreme cases, for example, crash when an App is opened for the first time after download and installation, if MTA SDK has been loaded, an error log will be reported, but there will not be logs of page access and frontend and backend switch. And the user is counted as a new user instead of an active user.

### Why does the data change in a few days?

In case of network exceptions, SDK will report the previously unreported data together when the network is connected again. The backend adopts the policy of "7-day regression calculation", the data in the latest 7 days will be calculated again to ensure the authenticity and accuracy of the data. Therefore, there may be changes in the data within 7 days.
