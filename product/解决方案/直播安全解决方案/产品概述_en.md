## Solution Overview

Tencent Cloud LVB security solution is designed to deal with four issues in LVB industry - porny live broadcasting, porn redirection, sexuality detection and malicious text detection. The solution is even available for the users whose video streams are not hosted in Tencent Cloud. You can customize your own security solutions based on current needs, or use the multi-channel LVB monitoring system provided by Tencent Cloud to quickly build your own manual audit system.

## Solution Principle

Tencent Cloud LVB security solution can detect LVB flow with porny information, then feedback the result to developers and demonstrate it on the porn detection management platform. The principle is that Tencent Cloud takes screenshots of video streams from live rooms at specified time interval (a custom value, such as 10 seconds), rates the porny level of such screenshots using Cloud Image's porny image recognition technology, and then sends the callback of suspicious images with a score (set by users) of more than 80 and relevant room information to the developer, who, based on the returned results, preferably sends the suspicious images to the auditor for auditing and then takes further actions such as banning the images.

## Advantages

<style>
table th:first-of-type {
    width: 200px;
}
</style>

| Advantage | Description |
|---------|---------|
| Labor saved | Let's take the platform with 10 thousand daily active LVB rooms as an example, 3 auditors in the shift working mode can complete the porny LVB detection. |
| More timely detection | The majority of reviewers in LVB industry deal with not only the porny LVB content but also customer complaints. The LVB reviews always delay due to insufficient manpower. Let's take a LVB platform with 1,500 daily active rooms and 50 customer service staff as an example, it takes 10 minutes to detect porny LVB in it. </br>In BSP, the time taken to detect porny LVB is based on the screenshot capturing time set by developers. The minimum time can be set to be 1 second. |
| Decreased rate of omissions in manual review | Omissions occur in manual LVB review inevitably. While BSP can maximize the detection of porny content and inform the reviewers using Cloud image's image detection technology, thus decreasing the rate of omissions in manual review. |
| Mornitor the efficiency of reviewers | Supervisor of review can use the porn detection result notification message of BSP to evaluate the efficiency of ordinary reviewers. |

