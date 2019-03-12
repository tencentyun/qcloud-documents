## How to check the logs of business servers
 You can focus your attention on the following two logs:
- Log of Nginx: In case of an error code returned by HTTP (such as 404, 500, etc.), check Nginx's log at the error level, which is located in the subdirectory /logs under Nginx's installation directory. The reasons for the error are generally the configuration problems of Nginx, PHP or MySQL.
- Log in business server code: If a response is returned for the request, but the code in the JSON of the response package is not 200, this means the request failed. In this case, check the file in the /log under the directory where the PHP code is located. If the log directory does not exist, create a log directory and then add read/write permissions (it is recommended to execute chmod 777 to enable all permissions).

## How to check the logs of mobile devices
The path to iOS mobile device's log: `Document/Caches/rtmpsdk_date.log`
The path to Android mobile device's log: sdcrad/`tencent/imsdklogs/com/tencent/qcloud/xiaozhibo/rtmpsdk_date.log `

## Error Codes

| Error Code | Description |
|---------|---------|
| 498 | Verification failed |
| 500| The database operation failed. Verify whether the database table has been created correctly. For more information on the error code, please check the log file mysql_errorxxx (xxx is the date of error) in the /log under the directory where PHP code is located |
| 601 | Update failed |
| 602 | Invalid parameter |
| 610 | Incorrect format of user name |
| 611 | Incorrect format of password |
| 612 | User already exists |
| 621 | Wrong password |
| 620 | User does not exist |

For errors related to IM, please see [IM Error Codes](https://cloud.tencent.com/document/product/269/1671)
For error codes related to COS (for uploading images, covers), please see [COS Error Codes](https://cloud.tencent.com/document/product/436/6281)
