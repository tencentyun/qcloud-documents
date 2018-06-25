### Feature Overview
For custom events, MTA platform provides basic statistical analysis service and data detail export service. Users can obtain detailed data, and conduct deeper analysis of data value based on their own business characteristics to promote business development. The platform provides two data export methods: online download and backend push.
### Online Download
For grouping parameter events, users can directly download the data details on the MTA page. But the download is not supported for other events.
**Note:** The grouping event only retains the details of the latest 1 million grouping parameter event. The specific page is shown as below. You can directly click to download the file.
![](//mc.qcloudimg.com/static/img/767d6144f0bd28375eb160d94143f614/image.png)
### Backend Push

For all events, user can select a specific event, and the platform pushes data details of the event to the user-configured server via FTP.
**Note:** Users need to configure server information, and ensure smooth linkage. The specific operations are as follows:

Step 1: Configure the server information. Specifically, configure the server information, and debug to check whether the linkage is connected with the platform server. When the user-configured server and the platform server are connected, the server status is [Connected].
![](//mc.qcloudimg.com/static/img/608ab4870713590d78a7dd4bf352ad46/image.png)
Step 2: Configure the event export switch. Specifically, for custom events, you can set the switch for backend push. The server pushes events with the push status of [On] to the specified server once per hour. You can view the push status on the **Backend Push Monitoring** page.
![](//mc.qcloudimg.com/static/img/716ba1e1543812874ed7cfcb9085d7b4/image.png)
### Data Format
For online download and backend push, details are exported in jason string, and the specific fields are as follows:

| Name | Description |
|---------|---------|
| ui | The user id. IMEI for Android, and IFA or openUDID for iOS |
| mc | The mac address of device |
| ts | The timestamp |
| idx | The event index |
| cui | Custom user id |
| av | App version |
| ch | The channel for App installation (promotion) |
| id | The ID (int) corresponding to ky |
| ei | Custom event id |
| du | The duration |
| kv | Key-Value parameter of custom event |


