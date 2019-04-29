The counting of active users can be trigged by uploading the following logs:
### Page View Log
Each time a user browses the App pages, the terminal generates a log and sends it to the MTA server.
>**Note:**
> Before SDK2.3.0, it is necessary to set code for each page to report the page view log. As of SDK2.3.0, automatic reporting of log is supported by simply initializing the code once.

### Custom Event Log
When a user triggers an event that you are tracking, the terminal generates a log and sends it to the MTA server.

### Backend-Frontend Switch Log
When an App process switches from the backend to the frontend, the terminal reports a log to the MTA server (APIs of SDK 2.3.0 or later are needed).

### Program Error Log
Whenever a Crash or program error occurs with the App, the terminal reports a log to record this error.

### Account Reporting Log
If you have set reporting user accounts as the basis of statistics, a log is generated each time an account is reported.

### Network Speed Monitoring Log
When the App calls the API or domain name configured by developer for monitoring network speed, it generates a log.

### Session Log
Each time the App is used (it is launched or the process keeps running at backend for more than 30 seconds before switching to the frontend),the SDK reports a session log.
