This section provides an example about how to use the SQL Server API "View Backup List".

## 1. View Backup List
To use API [View Backup List](/doc/api/449/6422), you need to input instance ID and start/end time. In case of a large number of backups, the results need to be displayed in pages.

By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://sqlserver.api.qcloud.com/v2/index.php?Action=ListBackup
&SecretId=AKID6SYaSQcgHd5xxxxxxxlAWpGkaDa55q8
&Nonce=39586
&Timestamp=1470125343
&Region=gz
&Signature=DL6pfNGL1ZC5zM6ceOTVsF7qEKs%3D
&resourceId=mssql-q6g71pcf
&startTime=2016-09-27 00:00:00
&endTime=2016-09-28 00:00:00
&pageSize=10
&pageNo=0
```

The returned results of the above request are as follows:

```
{
    "code":"0",
    "message":"",
    "data":{
        "backupList":[
            {
                "fileName":"backup_540316.tar",
                "size":"1440",
                "startTime":"2016-09-27 02:03:15",
                "endTime":"2016-09-27 02:21:45",
                "internalAddr":"http://10.66.185.141:58366/download/backup_540316.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzPsYYttIeozrDQeh2yfY/Dq/8OltqtK/+Bg3+plnNy5TzRhaYuCh+DpYehlAXVPBHPARU+zHUfxGkimTw+RxB5BBmgF/TTvwQXHfyjCr2DnQ==",
                "externalAddr":"http://119.29.47.51:9097/download/backup_540316.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzPsYYttIeozrDQeh2yfY/Dq/8OltqtK/+Bg3+plnNy5TzRhaYuCh+DpYehlAXVPBHPARU+zHUfxGkimTw+RxB5BBmgF/TTvwQXHfyjCr2DnQ=="
            }
        ],
        "totalCount":"1"
    }
}
```
