## Overview
CLS supports shipping logs to Cloud Object Storage (COS), allowing persistent storage of log data. You just need to make configurations on the console, so that the logs can be shipped to COS based on the shipping interval, file size, shipping path and filtering rules. 

## How to Use
### Prerequisites

1. Activate the CLS, create a logset and a log topic, and the log data can be successfully collected.
2. Activate Tencent Cloud COS, and create a bucket in the region of the logset to which shipping tasks belong.
3. The current account has the **permission to write to** the specified bucket. If you configure log shipping as a collaborator, make sure that you have granted CLS the **permission to write to** the bucket under your primary account. Otherwise, shipping will fail. 

### Procedure
1. Log in to the [CLS console](https://console.cloud.tencent.com/cls), and click **Logset** in the left navigation bar. Select the logset to which a shipping task needs to be added, click the **Logset ID/Name** to go to the its details page.
![](https://main.qcloudimg.com/raw/b4560b57c179e20441fa56bd65803971.png)
2. Locate the log topic to be shipped, click **Configure** -> **Shipping to COS Configuration** to go to the **Shipping Configuration** page.
![](https://main.qcloudimg.com/raw/df645d270b696a380253435e079a8949.png)
3. Click **Add Shipping Task** to go to the **Ship to COS** page to complete the configuration information, and then click **OK**. For more information, please see [Configuration Items](#config).
![](https://main.qcloudimg.com/raw/b6a605b37631fbde4953c142c4f4c306.png)
4. Check whether the shipping status is enabled.
![](https://main.qcloudimg.com/raw/bf469f1b5cafb4c2445ff00a9b2da2ed.png)

<a id="config"></a>
### Configuration items
#### (Optional) Directory prefix
CLS allows you to define a directory prefix. Log files are shipped to the directory of the COS bucket. Log files are stored under the bucket by default with the path `{COS bucket}{directory prefix}{partition format}_{random}_{index}.{type}`, where `{random}_{index}` is a random number.

#### (Required) Partition format
A directory is generated automatically for the creation times of shipping tasks based on strftime syntax. "/" represents the first level of COS directory. The following is an example where directory prefix is `bucket_test/` and shipping time is 2018/7/31 17:14.

| Bucket Name | Directory Prefix | Partition Format | COS File Path |
| ----------- | -------- | ----------- | ------------------------------------------------- |
| bucket_test | logset/ | %Y/%m/%d    | bucket\_test:logset/2018/7/31\_{random}\_{index}    |
| bucket_test | logset/ | %Y%m%d/%H  | bucket\_test:logset/20180731/14\_{random}\_{index} |
| bucket_test | logset/ | %Y%m%d/log | bucket\_test:logset/20180731/log\_{random}\_{index} |

#### (Optional) Compress logs for shipping
You can compress log files before shipping. The size of an uncompressed file to be shipped is limited to 10 GB. Supported compress methods are gzip and lzop.

#### (Required) File size
It specifies the maximum size of **an uncompressed file to be shipped** within the shipping interval, which refers to the maximum size of the log file that can be shipped at the interval. A file greater than this size will be split into multiple log files. The maximum supported size is **from 100 MB to 10 GB**. 

#### (Required) Shipping interval
The shipping interval shall be **limited to 1 minute to 1 hour**. If you set it to 5 minutes, a log file is generated from your log data every 5 minutes, and multiple log files will be shipped together to your bucket at a regular interval (within half an hour). 


#### (Optional) Advanced options
Log shipping also allows you to filter logs based on log content before shipping, which is an advanced configuration. You can specify a key, perform regular extraction of the key value, and set a value to match with the extracted value. A log can be shipped only when the log data matches your configuration. Unmatched logs are not shipped. As shown in the figure below, if the "action" field is set to "write", the log is shipped. You can set a maximum of 5 shipping filters. 
![](https://main.qcloudimg.com/raw/fa774d5a865c2129f707465c55e416c7.png)

> **Note:**
For the log search in the mode of full text in a single line or full text in multi lines, default key is **CONTENT**.

