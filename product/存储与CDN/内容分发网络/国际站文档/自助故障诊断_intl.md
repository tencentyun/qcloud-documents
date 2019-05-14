## Overview
CDN provides a self-diagnose tool that helps you perform self-inspection when you find that there is a problem while accessing a resource URL. The process of self-diagnose includes a series of inspection items such as checking the DNS resolution of connected domain, connection quality, the availability of sites and the consistency of data access, to help you locate the problem and provide solutions.

**Note: The resource URL to be diagnosed must be an "Activated" domain under your account. The bandwidth generated during the diagnosis process will be calculated as billing bandwidth. It is suggested that the target resources to be diagnosed do not exceed 200MBytes.**


## Instructions
### Current Device Access Diagnosis
You can initiate diagnosis through "Current device access diagnosis" when you find that there is a problem while accessing a resource. The procedure for current device access diagnosis is as follows:

1. From the console, go to Inspect Tool >> Self-diagnose page and select "Current device access diagnosis" tab;
2. Enter the resource URL to be diagnosed. Currently only URLs with the prefix "http://" are supported. Cannot diagnose URLs which start with "https" at this moment. Once the correct URL is entered, click "Get test URL", and a test address will be generated in the page;
3. Click the test address generated in step 2 to open the diagnosis page and start collecting diagnosis information. Please do not close the diagnosis page during the process, the page will close on its own when the process is completed;
4. After the diagnosis, you can go to "Diagnosis report" tab to review the results.

![self](https://mc.qcloudimg.com/static/img/30d52a0a7b01e4b9f802177ceda62bb0/1.png)


### User Access Diagnosis 
When a user reports that there is a problem while accessing resource, you can locate the problem using "User access diagnosis", and solve the problem through actions suggested by Tencent Cloud. The procedure for user access diagnosis is as follows:

1. From the console, go to Inspect Tool >> Self-diagnose page and select "User access diagnosis" tab;

2. Enter the resource URL to be diagnosed. Currently only URLs with the prefix "http://" are supported. Cannot diagnose URLs which start with "https" at this moment. Once the correct URL is entered, click "Get test URL", and a test address will be generated in the page;
3. Send this test address to your user. Diagnosis information will be collected when your user opens the test URL. Please do not close the page during the process.
4. After the diagnosis, you can go to "Diagnosis report" tab to review the results that have been collected from the user.

![users](https://mc.qcloudimg.com/static/img/215ff9302a2e2f5026140d6dff9ac794/2.png)


### Reviewing the Diagnosis Report
From the console, go to Inspect Tool >> Self-diagnose page and select "Diagnosis report" tab to see a list of diagnosis reports. Diagnosis reports that have been generated will be presented in the page, sorted by time of creation.
![list](https://mc.qcloudimg.com/static/img/fd6eeaf8759acbe844d90bef5da29003/3.png)
You can click "Check" to view the details of the report. 
![detail](https://mc.qcloudimg.com/static/img/ad105416d8677a8d37faa252bef7489d/4.png)

The Report Details page is divided into two sections, "Diagnosis object" and "Diagnosis report":

**Diagnosis object**: Contains Diagnosis ID, abnormal URL, abnormal domain name, origin type information.
**Diagnosis report:** Contains diagnosis results about CNAME, DNS resolution, site availability, link quality, and data access consistency.


**Item 1: CNAME**
1. Normal: If the CNAME that is actually resolved from the diagnosis domain is consistent with the CNAME that should be deployed and resolved, the result will be "normal".
2. Abnormal CNAME Configuration: If the CNAME that is actually resolved from the diagnosis domain is not consistent with the CNAME that should be deployed and resolved, the result will be "abnormal". You can click "Check details" to review the CNAME that is actually resolved and the one that should be deployed and resolved as well as its CDN provider. Only one CNAME is presented in the details if multiple CNAMEs are actually resolved from the diagnosis domain. In this case, it is suggested that you change the CNAME configuration at the DNS service provider. If the CNAME configuration is abnormal, other diagnosis items will not be commenced.

**Item 2: DNS Resolution**
1. Normal: If the actual node accessed by the diagnosis domain is consistent with the optimal node, the result will be "normal". You can click "Check details" to review Client IP, Local DNS, IPs of the actual node and the optimal node, regions and ISP information
2. Non-optimal path: If the actual node accessed by the diagnosis domain is different from the optimal node, the result will be "non-optimal path". It is suggested that you contact Tencent Cloud technicians.
3. Failed to obtain node IP: Under circumstances such as when the IP of the diagnosis domain is hijacked, or the connection to the node failed, the diagnosis result will be "failed to obtain node IP". It is suggested that you contact Tencent Cloud technicians.

**Item 3: Site availability**
1. Normal: If the connections to the node and the origin server are normal, the diagnosis result will be "normal connections to node and origin server"
2. Abnormal: If the connections to the node or the origin server are abnormal, the diagnosis result will be "abnormal connection to node" or "abnormal connection to origin server" or "abnormal connection to both node and origin server". It is suggested that you contact Tencent Cloud technicians.

**Item 4: Link quality**
1. Normal: If the access to the diagnosis domain is normal, the diagnosis result will be "normal", and the total resource access latency will be presented. You can also click "Check details" to review details about the time spent within every part of the link.
2. Abormal: If the access to the diagnosis domain failed, the diagnosis result will be "abnormal". It is suggested that you contact Tencent Cloud technicians. If link quality is diagnosed as abnormal, data access consistency diagnosis will not be commenced.

**Item 5: Data Access Consistency**
1. Normal: If diagnosed resources can be normally accessed at the origin and the node plus they have the same MD5, the diagnosis result will be "normal". You can click "Check details" to review the information about the resources at origin server and node.
2. Abnormal origin server resource: If a status code such as 4XX, 5XX occurred when accessing resources at the origin server, or the MD5 values of resources on different origin servers are inconsistent, the diagnosis result will be "abnormal origin server resource". It is suggested to check the resources at the origin server. You can also click "Check details" to review more details about the resources at origin server and node.
3. Abnormal CDN resource: If resources at origin server are normal, but a status code of 4XX or 5XX was returned when accessing resources at the node, or the MD5 values of resources at origin and node are inconsistent, the diagnosis result will be "abnormal CDN resource". It is suggested that you contact Tencent Cloud technicians. You can also click "Check details" to review more details about the resources at origin server and node.

If you're not able to solve the problem using the diagnosis report, we suggest that you submit a ticket, or contact Tencent Cloud technicians for troubleshooting.
