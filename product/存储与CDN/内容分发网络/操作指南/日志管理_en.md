You can download the detailed log containing the information about users' access to a connected domain for analysis; CDN provides logs about domains on an hourly basis, and you can download CDN logs for the last 30 days.

## Log Download
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and select **Logs** page. You'll see the **Log Management** feature provided by CDN.
![](https://mc.qcloudimg.com/static/img/043e70b6829ce67d6af125b51736b249/1.png)
Select the domain for which you want to check logs and the date range, then click **Query** to get the log download link, and click the link to download:
![](https://mc.qcloudimg.com/static/img/9d9544788db54ab4c1fb920629be77ab/2.png)
If there was no request for the domain on that day, no log would be generated. In this case, "No Data" will appear.
**Note:**
+ CDN logs are provided on an hourly basis by default, with 24 log files generated each day;
+ CDN logs have a latency of about half an hour in terms of real-timeness and will not be updated after 2 hours.

## Log Field Description
The order and meaning of fields in the downloaded log are shown in the following table:

| Order | Log Content                |
| ----- | -------------------------- |
| 1     | Request time               |
| 2     | Client IP of access domain |
| 3     | Domain accessed            |
| 4     | Request path of file       |
| 5     | Bytes of current access    |
| 6     | Province                   |
| 7     | ISP                        |
| 8     | HTTP status code           |
| 9     | Referer info              |
| 10    | Response time (ms)         |
| 11    | User-Agent                 |
| 12    | range parameter            |
| 13    | HTTP Method                |
| 14    | HTTP protocol ID           |
| 15    | Cache HIT/MISS             |

### Region Code
1: North China; 2: Northwest China; 3: Northeast China; 4: East China; 5: Central China; 6: Southwest China; 7: South China; 8: Other Regions;
### Province Code
22: Beijing; 86: Inner Mongolia; 146: Shanxi; 1069: Hebei; 1177: Tianjin; 119: Ningxia; 152: Shaanxi; 1208: Gansu; 1467: Qinghai; 1468: Xinjiang; 145: Heilongjiang; 1445: Jilin; 1464: Liaoning; 2: Fujian; 120: Jiangsu; 121: Anhui; 122: Shandong; 1050: Shanghai; 1442: Zhejiang; 182: Henan; 1135: Hubei; 1465: Jiangxi; 1466: Hunan; 118: Guizhou; 153: Yunnan; 1051: Chongqing; 1068: Sichuan; 1155: Tibet; 4: Guangdong; 173: Guangxi; 1441: Hainan; 0: Other; 1: Hong Kong, Macao and Taiwan; 1: Overseas;
### ISP Mapping
2: China Telecom; 26: China Unicom; 38: CERNET; 43: Great Wall Broadband; 1046: China Mobile; 3947: China Tietong Telecom; -1: Overseas ISPs; 0: Other ISPs;

## Note

The bandwidth or traffic data recorded in logs is returned data packet at the application layer (HTTP protocol), and due to such mechanisms as TCP protocol packet loss, three-way handshake and re-transmission, is smaller than that counted through TCP layer.



## Overseas CDN Log Download

Overseas CDN is under beta test. If you have activated overseas CDN, you can download overseas CDN logs from log management page of overseas CDN console. Overseas CDN provides domain logs at an hourly basis with a latency of one to two days. You can download the CDN logs for the last 30 days. The fields in overseas CDN log are the same as the ones in domestic CDN log, except that Province field will be replaced by overseas region. The overseas region and ISP mappings are shown below.

### Overseas Region Code
73: India; 1195: Indonesia; 1176: Singapore; 57: Thailand; 144: Vietnam; 3701: Malaysia; 2588: Philippines; 2026: Taiwan; 1044: Japan; 3379: Korea; 1200: Hong Kong; 3839: Canada; 669: United States; -2: Other Overseas Regions; -3: Unknown;

### Overseas ISP Code
-1: Overseas ISP;
