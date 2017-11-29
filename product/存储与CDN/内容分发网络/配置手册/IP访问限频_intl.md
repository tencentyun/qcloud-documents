## Overview
CDN provides IP access frequency limit configuration which restricts how many times an IP is allowed to access a node within one second to prevent CC attacks.

## Configuration Instructions
Log in to [CDN Console](https://console.cloud.tencent.com/cdn) and go to "Domain Management" page. Then click **Manage** button to the right of the domain name to enter the management page:

![](https://mc.qcloudimg.com/static/img/f92d2ef7e4be2b69185ab43228f025ef/1.png)

You can see **IP Access Frequency Limit** in "Access Control":
![](https://mc.qcloudimg.com/static/img/0784483e76f03a7332d5fff0213351c5/2.png)

### Default Configuration
By default, IP Access Frequency Limit configuration is disabled.

### Custom Configuration
Click "On" button to enable IP Access Frequency Limit configuration. The system will suggest a threshold according to the average daily accesses of a single IP in the recent 30 days. You can see the given default threshold in the **Current IP access limit** field:

![](https://mc.qcloudimg.com/static/img/31400eda65e436b031c64835e377587a/3.png)

**Note**:

+ Default threshold is calculated as follows: Count the average access frequency of an IP at each of the 288 statical points for each day (one point per 5 minutes) and take the largest value among the values for all the statical points for each day. Then get the default threshold by dividing the sum of largest value for each day by 30 (the recent 30 days);
+ Minimum default threshold is 10QPS (for reference only). It is recommended to configure the threshold based on your business changes.

Click **Edit** button to customize the threshold:

![](https://mc.qcloudimg.com/static/img/8409ed363c89690665681d7f63a3693e/4.png)

**Note**:

+ IP access frequency limit is designed to restrict how many times an IP is allowed to access a node within one second. If the limit is exceeded, a 514 error will be returned;
+ Setting a reasonable threshold is recommended since a low frequency limit may affect the use by users who have a high access frequency.
