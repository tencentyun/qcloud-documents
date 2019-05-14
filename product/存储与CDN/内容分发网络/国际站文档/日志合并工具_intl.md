## Instructions
This script is used to obtain the log data packet of a specified domain on the specified date (within 30 days).

[Download](https://mc.qcloudimg.com/static/archive/b958077bcfeb0a4a35995f4790a91f7c/GetDayLog.zip)


### Preparation Before Using
You need to install requests library to use the python script mentioned above. Use the following command:
```
pip install requests
```

##### Parameter Description

```
host: domain
-u SECRET_ID
-p SECRET_KEY
--day: date
--dstpath: download link of the log
```

+ You can acquire SecretId and SecretKey from [Cloud API Key](https://console.cloud.tencent.com/capi);
+ You can only download logs from within 30 days;
+ By default, the storage path for the log of specified date is the current path.


### Example

```
python GetDayLog.py www.test.com -u XXXXXXXXXXXXXXX -p XXXXXXXXXXXXXX --day 20161130 --dstpath /home/test/
```

When used, you will be able to see the desired log file in the specified directory. The file name will be:

```
20161130-www.test.com.gz
```


