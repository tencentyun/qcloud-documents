# Charges of ILVB
## Part 1: [Required] Basic Network Fee
Fee for the bandwidth consumed by basic audio/video business implemented through ILVB (excluding the consumptions of non-interactive broadcasting, recording and other additional features)

Monthly fee for the bandwidth that is actually used (Z)=Monthly peak bandwidth of data center (DC) (X) x Unit price+Monthly peak bandwidth of outer center (OC) (Y) x Tiered unit price

The unit price of DC bandwidth is 120 CNY/Mbps/month. The unit price of OC changes in tiers according to corresponding monthly peak bandwidth:

 <table>
        <tr>
            <th>Monthly peak bandwidth of DC</th>
			<th>Unit price of DC bandwidth</th>
            <th>Unit price of OC bandwidth</th>
            <th>Monthly fee for the bandwidth that is actually used (Z)</th>
            
        </tr>
        <tr>
            <th>Y≤5 Gbps</th>
            <th>120/Mbps/month</th>
            <th>23/Mbps/month</th>
            <th>120 X+23 Y</th>
        </tr>
<tr>
            <th>5 Gbps<Y≤50 Gbps </th>
            <th>120/Mbps/month</th>
            <th>21.5/Mbps/month</th>
            <th>120 X+21.5 Y</th>
        </tr>
<tr>
            <th>50 Gbps<Y≤ 100 Gbps</th>
            <th>120/Mbps/month</th>
            <th>20.5/Mbps/month</th>
            <th>120 X+20.5 Y</th>
        </tr>
<tr>
            <th>100 Gbps<Y≤300 Gbps</th>
            <th>120/Mbps/month</th>
            <th>19.5/Mbps/month</th>
            <th>120 X+19.5 Y</th>
        </tr>
<tr>
            <th>300 Gbps<Y≤500 Gbps</th>
            <th>120/Mbps/month</th>
            <th>18.5/Mbps/month</th>
            <th>120 X+18.5 Y</th>
        </tr>
<tr>
            <th>500 Gbps<Y</th>
            <th>120/Mbps/month</th>
            <th>17.5/Mbps/month</th>
            <th>120 X+17.5 Y</th>
        </tr>

      
    </table>

 
 Example of estimation of bandwidth consumption:<br />
If the playback bitrate of customer's ILVB business at viewer end is set to 1 MB, when 100 viewers watch video at a certain time at the same time, the bandwidth consumed at this point of time is 1*100=100 MB, and so on. The bandwidth usage is collected every five minutes, and the peak bandwidth of the month can be used to calculate the monthly fee.<br />

Note: If you have a high volume of business, contact your Tencent Cloud key client manager to negotiate for a lower price.<br />
Note:<br />
a. Monthly peak bandwidth:<br />
• DC and OC collect a peak bandwidth every five minutes (in Mbps). The highest value of the month is used as the monthly peak bandwidth of DC for billing.<br />
b. DC<br />
•	It can send upstream/downstream audio and video data, being suitable for multi-person audio/video interaction.<br />
Scenarios where DC is largely used:<br />
(1) When viewers have upstream audio and video permission<br />
**Note**: Whether viewer joins the broadcasting is configured and switched by developer. Wrong configuration may cause large-scale burst of traffic to flow through DC.<br />
(2) If no upstream audio/video traffic is generated, when the number of room members is small (for example, not more than five), the traffic flows following a path of VJ -> DC -> OC -> viewer, but the use of OC can cause a waste of traffic from DC to OC. Therefore, in this case, DC is directly used to send downstream traffic.<br />
c. OC<br />
•	It can only send downstream audio/video data, being suitable for scenarios where viewers only watch the video.<br />
(As shown in the figure, if no viewer sends upstream video data, and the number of online members in the room is more than five, most of traffic is generated from OC. But a certain proportion of bandwidth comes from DC-->OC, which accounts for almost 10%)<br />

# Part 2: [Optional] Additional Capacity Fee
Charges may be incurred only when additional capacity is activated and put into use, such as recording, non-interactive broadcasting, etc.<br />
Currently, additional capacities of ILVB include non-interactive broadcasting, recording and smart porn detection. A certain fee is charged if these capacities are used in customer's product. Each capacity has independent billing rules:<br />
## Billing of Non-interactive Broadcasting
With cloud LVB capacity, non-interactive broadcasting is used to implement audio/video playback outside the ILVB room. So non-interactive broadcasting is charged according to the billing standard of cloud LVB. For more information, please see pricing rules of cloud LVB.<br />
## Billing of Recording
The charges of recording feature are divided into two parts:<br />
(1) Recording channel occupation fee<br />
The charge is billed based on the maximum concurrent channels for the recording month, with a price of 30 CNY/channel/month.<br />
(2) Storage fee<br />
With cloud VOD capacity, storage feature is used to implement features such as storage, transcoding, re-play of recorded ILVB videos. You need to activate VOD service.<br />
So the storage fee is charged according to the billing standard of cloud VOD. For more information, please see pricing rules of cloud VOD.<br />

## Billing of Screenshot and Porn Detection Feature
1. Billing items: Screenshot, porn detection.<br />
2. Quote<br />
(1) Screenshot: 0.1 CNY/1,000 pieces (No fee is charged if the number of screenshots is less than 1,000. A fee will be charged if the number of screenshot is more than 1,000 (1,000 included). The minimum pricing unit is based on 1,000 screenshots, so less than 1,000 shall be counted as 1,000. For example, 3,600 is counted as 4,000)<br />
(2) Porn detection (confirmed): 1.3 CNY/1,000 images (Manual audit is not required. Algorithm is used)<br />
(2) Porn detection (unconfirmed): 0.4 CNY/1,000 images (Manual audit is required)<br />

# Part 3: [Optional] Technical Support Fee

Fees charged for the professional technical service, special resource support, etc. These services need to be activated through negotiation.<br />

Technical support service is a manual service provided by Tencent Cloud video team, covering access technology consultation, activation of special resources, etc. Specific service mode is determined through negotiation between customer and Tencent Cloud operation department<br />

The technical support service is applicable for the following customers:<br />

1. Lack of experienced resources for research and development of video Apps<br />

2. Make product available quickly in a short time frame<br />

3. Need for special feature which is expected to be used frequently once launched<br />

The activation, service mode, billing method of technical support service are confirmed through offline negotiation and signing contract<br />

If you are interested, please add QQ: 3358225043<br />

Please indicate your company name and connected service (ILVB/cloud LVB) when adding QQ number<br />
