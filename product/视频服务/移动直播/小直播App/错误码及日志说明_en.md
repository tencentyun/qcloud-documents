## How to check the logs of business servers
 You can focus your attention on the following two logs:
- Log of Nginx: In case of an error code returned by HTTP (such as 404, 500, etc.), please check Nginx's log at error level, which is located in subdirectory /logs under Nginx's installation directory. The reasons for the error are usually the configuration problems of Nginx, PHP or MySQL.
- Log in business server code: If a response is returned for the request, but the returnValue in the JSON of the response package is not 0, this means the request failed. In this case, check the file under the /log under the directory where the PHP code is located. If the log directory does not exist, create a log directory (For the old version of code, no directory is created by default) and then add read/write permissions (it is recommended to execute chmod 777 to enable all permissions)

## How to check the logs of mobile devices
The path to iOS mobile device's log: `Library/Caches/rtmpsdk_date.log`
The path to Android mobile device's log: sdcrad/`tencent/imsdklogs/com/tencent/qcloud/xiaozhibo/rtmpsdk_date.log `

## Description of Error Codes

| Error Code | Description |
|---------|---------|
| 1000 | The JSON format of the request package is valid, but invalid parameter is found (In most cases, the invalid parameter is the Action field). To fix the error, please see [Protocol Formats at Background](https://cloud.tencent.com/document/product/454/7895) |
| 2003| The database operation failed. Please verify whether the database table has been created correctly. You can create a database table by referring to the createdb.sh in PHP code. For more information on the error code, please check the log file mysql_errorxxx (xxx is the date of error) under the /log under the directory where PHP code is located |
| 4001| JSON of the request package is null or in an incorrect format. Please check the JSON format using any of the JSON format check tools available online. This error usually occurs when you initiate a request through curl or postman by generating the JSON format by yourself. If you initiate the request through Mini LVB, this error will not occur. Please pay attention to the difference |
| 4002| Some of the parameter values of the request package are invalid. To fix the error, please see [Protocol Formats at Background](https://cloud.tencent.com/document/product/454/7895) |
| 4003| The number of Cloud Image authentications has exceeds the daily limit (currently, a maximum of 100 users are allowed to use the feature each day) |
| 500 | This is an HTTP error code, which may be caused by the incorrect database configuration. Please check the log at error level under the /logs under Nginx's installation directory. This log also provides the information on other HTTP error codes |

For errors related to registration, login and messages, please see [Instant Messaging Error Codes](https://cloud.tencent.com/document/product/269/1671)
For error codes related to COS (for uploading images, covers), please see [COS Error Codes](https://cloud.tencent.com/document/product/436/6281)
 
     

