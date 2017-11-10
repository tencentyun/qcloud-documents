## Fee Types of ILVB
1. Basic Network Fee
•	Payment period:
(1) Charge on a monthly basis. In the settlement between the 1st and 5th day of every month, the fee for the service actually used in last month is deducted from Tencent Cloud account, and an amount equivalent to 120% of the fee for the last month is frozen in the balance;
(2) Upon the settlement in next month, the frozen amount is unfrozen first, and the fee for current month is deducted from the unfrozen amount.
2. Fee for Additional Capabilities (optional)
• Non-interactive broadcasting uses LVB capabilities. Its fee is calculated based on the monthly OC peak bandwidth consumed by it. The price of OC peak bandwidth is described below.

## Basic Network Fee
### Calculation formula
 ![](//mccdn.qcloud.com/static/img/e045f054cc19ceb13344f2c8c0b7fc03/image.jpg)
 
Note: If you have a large business volume or need to access service separately, please contact Tencent Cloud customer manager to negotiate and customize the price.

### Pricing
<div class="mod-price">
    
    <div class="tab-content-detail column-4">
       
        </div>
        <div class="slide-text"></div>
        <div class="text-content">
        </div>
        <div class="slide-text"> </div>
        <div class="price-content">
            <table>
                <colgroup>
                    <col class="col1">
                    <col class="col2">
                    <col class="col3">
                    <col class="col4">
                    <col class="col5">
                </colgroup>
                <thead>
                    <tr>
                        <th colspan="2">DC Bandwidth</th>
                        <th colspan="2">OC Bandwidth</th>
                        <th rowspan="2">Fee (CNY)</th>
                    </tr>
                    <tr>
                        <th>Monthly Peak Bandwidth:</th>
                        <th>Unit Price (CNY/Mbps/month)</th>
                        <th>Monthly Peak Bandwidth:</th>
                        <th>Unit Price (CNY/Mbps/month)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan="6">
                            <span>X</span>
                        </td>
                        <td rowspan="6">
                            <span>120</span>
                        </td>
                        <td>
                            <span>Y<5 Gbps</span>
                        </td>
                        <td>
                            <span>23</span>
                        </td>
                        <td>
                            <span>X*120+Y*23</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>5≤Y<50 Gbps</span>
                        </td>
                        <td>
                            <span>21.5</span>
                        </td>
                        <td>
                            <span>X*120+Y*21.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>50≤Y<100 Gbps</span>
                        </td>
                        <td>
                            <span>20.5</span>
                        </td>
                        <td>
                            <span>X*120+Y*20.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>100≤Y<300 Gbps</span>
                        </td>
                        <td>
                            <span>19.5</span>
                        </td>
                        <td>
                            <span>X*120+Y*19.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>300≤Y<500 Gbps</span>
                        </td>
                        <td>
                            <span>18.5</span>
                        </td>
                        <td>
                            <span>X*120+Y*18.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>500 Gbps≤Y</span>
                        </td>
                        <td>
                            <span>17.5</span>
                        </td>
                        <td>
                            <span>X*120+Y*17.5</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

### Calculation formula of monthly basic network fee 

<iframe src="https://avc.qcloud.com/calculator/index.html" width=400px height=400px border=0 style=border:none></iframe>

## Note:
### Monthly peak bandwidth:
•	At DC and OC, peak bandwidth value (in Mbps) is collected every 5 minutes. The highest value of the month is used as the monthly peak bandwidth of DC for billing;
### Data Center (DC)
•	It can send upstream/downstream audio and video data, being suitable for multi-person audio/video interaction.
#### Scenarios where DC is largely used:
(1) When viewers have permission to send upstream audio/video ([Note] Whether viewers join the broadcasting is set and switched by developer. A wrong setting may cause large traffic to flow through DC. Be sure to carefully read the setting method: [Click here to view](https://cloud.tencent.com/doc/product/268/3227))
(2) If no upstream audio/video traffic is generated, when the number of room members is small (for example, not more than 5), the traffic flows following a path of VJ -> DC -> OC -> viewer, but the use of OC can cause a waste of traffic from DC to OC. Therefore, in this case, DC is directly used to send downstream traffic.

### Outer Center (OC)
•	It can only send downstream audio/video data, being suitable for scenarios where viewers only watch the video.
(As shown in the figure, if no viewer sends upstream video data, and the number of online members in the room is more than five, most of traffic is generated from OC. But a certain proportion of bandwidth comes from DC-->OC, which accounts for almost 10%)

### Traffic Flow Diagram
#### A room with more than 5 people where joint broadcasting is not implemented
![](//mccdn.qcloud.com/static/img/1cb95629a1101c5381ce64194b478fbd/image.png)

####  A room with not more than five people where joint broadcasting is not implemented
In case of a small number of room members, use of OC may cause a waste of the traffic from DC-->OC. In this case, DC is directly used to send downstream traffic.
 ![](//mccdn.qcloud.com/static/img/3dd9c91f847457a5d456256d895f56d4/image.jpg)
 
#### A room where joint broadcasting is implemented
 ![](//mccdn.qcloud.com/static/img/1e463c571da0514f6c01e3aa3b6f9bf5/image.jpg)
