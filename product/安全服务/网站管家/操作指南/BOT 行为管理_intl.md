## Overview
Tencent Cloud WAF bot behavior management can identify and classify friendly and malicious bots. It also adopts targeted traffic management policies accordingly. For example, allowing traffic of search engine bots, while not responding to traffic of malicious product data crawling, or responding in a slower manner or adopting differentiated response policies. It can deal with the resource consumption, information leakage and invalid marketing caused by malicious bots, while maintaining the normal running of friendly bots (such as search engines and advertising programs).
## Configuration Case
1. Log in to [WAF Console](https://console.cloud.tencent.com/guanjia), click **Bot Behavior Management** -> **Bot Overview**, and select the domain from the drop-down box at the upper left corner of the page. This page shows the request statistics and the proportion diagram of bot types for the selected domain (take the test domain as an example, bot requests are indicated in red, while the total requests, sum of normal requests and bot requests, are indicated in green).
#### Notes:
 - Known bot type: Public bots such as search engines.
 - Unknown bot type: Undisclosed bots.
 - Custom bot type: Bots configured by users.

 ![1](https://main.qcloudimg.com/raw/80f75e08b94456a5b966d4b2e3e64cfa.png)
2. Click **Bot Settings**, and you can see two tabs: **Known Type Preset** and **Custom Policy**.
### Known Type Preset
Click **Known Type Preset**, and you can see bot type, number of bot types, action and operation (**Monitor** and **Block**).
#### Notes:
 - Monitor actions: Monitor but do not block normal requests to see if there are malicious bot behaviors.
 - Block actions: Block the detected malicious bot behaviors, and then a custom policy based on the result will be automatically generated in "Protection Settings" of the domain name.

 ![2](https://main.qcloudimg.com/raw/939a830742eff05b7562025742bce9ae.png)
### Custom Policy
Click **Custom Policy** -> **Add Policy**.
 ![3](https://main.qcloudimg.com/raw/0d579157a429b1ae1eea676866ed7db6.png)
Fill in the Policy Name and Policy Description, select a matching field (**Request path** is selected here), select **Include** for Logic Symbol, enter "/admin" as path content, select **Monitor** for Action, select **Enable** for Policy Switch, and click **OK** to add it.
>**Note:**
>Up to 10 conditions can be added to each custom policy. The relationship between the conditions is **and**, that is, the policy takes effect only when all conditions are satisfied.
 
 ![4](https://main.qcloudimg.com/raw/6d963c5f67cbaf521421482093f3a6d8.png)

#### Notes:  
 - Monitor actions: Monitor but do not block normal requests to see if there are malicious bot behaviors.
 - Block actions: Block the detected malicious bot behaviors, and then a custom policy based on the result will be automatically generated in **Protection Settings** of the domain name.
 - Allow actions: No monitoring or blocking.
For more information on configurations, please see [Custom Policy Configuration](#peizhi)

3. Click **Bot Details**, and you can see three tabs: **Unknown Type**, **Known Type**, and **Custom Type**. Here we take the **Unknown Type** as an example.
 ![5](https://main.qcloudimg.com/raw/755687bf21ccf4ff6d92e84a17c8dbfc.png)
To view details of a bot, click **View Details** of the data item:
 ![6](https://main.qcloudimg.com/raw/3c8c880b17fb94def64e4c2616ae6644.png)
#### Notes:
 - IP type: IDC stands for internet data center, and BS stands for base station.
 - Behavior information entropy: 0.5 is the reference value. The smaller the value, the more exceptional the behavior.
 - Monitor actions: Monitor but do not block normal requests to see if there are malicious BOT behaviors.
 - Block actions: Block the detected malicious bot behaviors, and then a custom policy based on the result will be automatically generated in **"Protection Settings"** of the domain name.
 >
 >The AI model of a bot learns data access modes, and generates models when the data reaches a certain amount.
 >The learning duration of the AI model depends on the website type and access traffic. Generally, the learning cycle is two weeks.


Attachment:
<span id="peizhi">
#### Custom Policy Configuration</span>

| Matching Field | Logic Symbol | Matching Content |
|---------|---------|---------|
| Whether referer exists | Yes or No | - |
| Request rate | Greater than | Count/min |
| Number of requests	 | Greater than | Count |
| referer content | Include | For example, no-referrer-when-downgrade |
| Whether UA exists | Yes or No | - |
| UA content | Include | For example, Mozilla |
| UA type | Belong to | Select as needed |
| Request parameter | Include | For example, 15 |
| Request path | Include | For example, /admin |
| IP range | Include | A single IP and IP range are supported. |

