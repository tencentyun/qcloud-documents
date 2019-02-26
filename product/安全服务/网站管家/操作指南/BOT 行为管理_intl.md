## Overview
Tencent Cloud WAF BOT behavior management can identify and classify friendly and malicious bots. It also adopts targeted traffic management policies accordingly. For example, allowing traffic of search engine bots, while not responding to traffic of malicious product data crawling, or responding in a slower manner or adopting differentiated response policies. It can cope with issues such as resource consumption, information leakage and invalid marketing caused by malicious bots, while maintaining the normal running of friendly bots (such as search engines and advertising programs).
## Configuration Case
1. Log in to [WAF Console](https://console.cloud.tencent.com/guanjia), click **BOT Management** -> **BOT Overview**, and select the domain name from the drop-down box at the upper left corner of the page. This page shows the statistics of requests and the proportion chart of BOT types for the selected domain name (take the test domain as an example, BOT requests are indicated in red, while the total requests, sum of normal requests and BOT requests, are indicated in green).
#### Notes:
 - Known BOT type: Public BOTs such as search engines.
 - Unknown BOT type: Undisclosed BOTs.
 - Custom BOT type: BOTs configured by users.

![1](https://main.qcloudimg.com/raw/e327bd2bf7209098b3322ace0c7c14ed.png)
2. Click **BOT Policy Settings**, and you can see two tabs: **Default Known Type** and **Custom Rule**.
### Default known type
Click the **Default Known Type** tab, and you can see BOT types, number of BOT classes, action and operation (**Monitor** and **Block**).
#### Notes:
 - "Monitor" action: Monitor but do not block malicious BOT behaviors in normal requests.
 - "Block" action: Block the detected malicious BOT behaviors, and then a custom rule based on the result will be automatically generated in "Defense Settings" of the domain name.

![2](https://main.qcloudimg.com/raw/fe1ee09255054a08f2a570f7dabf328b.png)
### Custom Rule
Click the **Custom Rule** tab, and click **Add a Rule**.
![3](https://main.qcloudimg.com/raw/17dc3d47dbbed814f3ac217e9e411bc5.png)
Enter the rule name and description, select a field (ie, Request Path), select "includes" in Condition, enter "/admin" in Content, select "Monitor" in Action, select "Enable" in Rule Switch, and click **Confirm**.
>**Note:**
>A maximum of 10 conditions can be added to each custom rule. The relationship between the conditions is "and", that is, the rule takes effect only when all conditions are satisfied.
 
 ![4](https://main.qcloudimg.com/raw/0175d3116c4955497fda71e18b4538ae.png)
 #### Notes:  
 - "Monitor" action: Monitor but do not block malicious BOT behaviors in normal requests.
 - "Block" action: Block the detected malicious BOT behaviors, and then a custom rule based on the result will be automatically generated in **Defense Settings** of the domain name.
 - "Allow" action: No monitoring or blocking.
For more information on configurations, please see [Custom Rule Configuration](#peizhi)

3. Click **BOT Action Details**, and you can see three tabs: **Unknown Type**, **Known Type** and **Custom Type**. Here we take the **Unknown Type** as an example.
![5](https://main.qcloudimg.com/raw/a413918152f4fee0eea68a60c18325c6.png)
To view details of a BOT, click **View details** of the specific data item:
![6](https://main.qcloudimg.com/raw/9205e227c124e5d2889fe7987d21c260.png)
#### Notes:
 - IP type: IDC stands for Internet data center, and BS stands for base station.
 - Behavior information entropy: 0.5 is the reference value. The smaller the value, the more exceptional the behavior.
 - "Monitor" action: Monitor but do not block malicious BOT behaviors in normal requests.
 - "Block" action: Block the detected malicious BOT behavior, and then a custom rule based on the result will be automatically generated in **Defense Settings** of the domain name.
 >**Notes:**
 >The AI model of BOT learns data access modes, and generates models when the data reaches a certain amount.
 >The learning duration of the AI model depends on the website type and access traffic. Generally, the learning cycle is two weeks.


Attachment:
<span id="peizhi">
#### Custom Rule configuration</span>

| Matching Field | Condition | Matching Content |
|---------|---------|---------|
| referer exists | Yes or No | - |
| Request rate | Greater than | Count/min |
| Request count	 | Greater than | Count |
| referer content | Includes | For example, no-referrer-when-downgrade |
| UA exists | Yes or No | - |
| UA content | Includes | For example, Mozilla |
| UA type | Belong to | Select as needed |
| Request parameter | Includes | For example, 15 |
| Request path | Includes | For example, /admin |
| IP range | Includes | A single IP and IP range are supported. |

