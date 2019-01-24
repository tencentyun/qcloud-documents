# 1. Basic LVB Billing
## 1.1 Traffic/Bandwidth Billing
LVB service can generate traffic or bandwidth costs.** Traffic and bandwidth are billed according to downlink data**, namely according to the traffic or bandwidth generated for watching LVB. Uplink push is not charged.
Traffic or bandwidth can be billed in package and postpaid modes, but you can select only one mode.

### 1.1.1 Prepaid Traffic Package

After applying for video service, enter "Tencent Cloud Console" -> "Live Video Broadcasting". When using the service for the first time, you can get a traffic package for free. The following list details prepaid and postpaid packages:

<table class="t">
<tbody><tr>
<th> Package List
</th><th> LVB Traffic (downlink)
</th><th> Price (USD)
</th></tr>
<tr>
<td style="text-align: center;"> 2.9 USD Package
</td><td style="text-align: center;"> 10 GB
</td><td style="text-align: center;"> 2.9
</td></tr>
<tr>
<td colspan="3" style="text-align: center;"> Note: New user can get a 2.9 USD package for free.
</td></tr>
<tr>
<td style="text-align: center;"> 7.5 USD Package
</td><td style="text-align: center;"> 50 GB
</td><td style="text-align: center;"> 7.5
</td></tr>
<tr>
<td style="text-align: center;"> 14.5 USD Package
</td><td style="text-align: center;"> 100 GB
</td><td style="text-align: center;"> 14.5
</td></tr>
<tr>
<td style="text-align: center;"> 72.0 USD Package
</td><td style="text-align: center;"> 500 GB
</td><td style="text-align: center;"> 72.0
</td></tr>
<tr>
<td style="text-align: center;"> 143.8 USD Package
</td><td style="text-align: center;"> 1 TB
</td><td style="text-align: center;"> 143.8
</td></tr>
<tr>
<td colspan="3" style="text-align: center;"> Note: Packages are valid for one year, and 0.17 USD/GB will be charged for the traffic beyond the package quota which can be offset if you renew the package during a calendar month.
</td></tr></tbody></table>

Notes:
1. Traffic purchased during a calendar month will be added to the remaining traffic. The calendar month begins at 00:00 of the first day of current month and ends at 24 :00 of the last day of current month.
For example, if you purchased 20 GB traffic on January 10th and 10 GB on January 31st, and you used 25 GB traffic in January, then the traffic would not exceed the package quota, with 5 GB remained. The package validity period would be prolonged for one year from January 31st. If you used 5 GB traffic beyond the package quota in January, and did not purchase more, then you would be charged for the exceeded traffic, and your traffic in February would not be impacted, namely, if you purchase 10 GB traffic on February 1st, you can use 10 GB traffic. The package validity period would be prolonged for one year from February 1st.
2. You can buy any LVB package at anytime.
3. These packages only contain traffic. Using more than 5 channels or value-added services can produce extra costs. For more information, please see **1.2 Channel Billing** and **2.  Value-Added LVB Service Billing* * in this document.


### 1.1.2 Postpaid LVB

In addition to the package mode, postpaid mode is also available for LVB, that is, you pay the bill for current month in next month. You can choose bandwidth or traffic postpaid mode, out of which only one is allowed. **Traffic and bandwidth are billed according to downlink data** (playback data).
**For consultation on or application for postpaid mode, contact Tencent commercial personnel. Tel: 4009-100-100**

**1. Bandwidth postpaid mode**
 1) Bandwidth price: 3.5 USD/Mbps/month (the default price). Bandwidth supports tiered prices. For more information, contact Tencent commercial personnel. Tel: 4009-100-100.
 2) Billing items: Peak bandwidth (the maximum bandwidth consumption) 
 3) Billing mode: Postpaid 
 4) Billing cycle: A calendar month 
 5) Measurement rules: The system takes 5 minutes as the time granularity, and collects overall bandwidth data of streaming media across network-wide nodes.
**2. Traffic postpaid mode**
 1) Traffic price: 0.17 USD/GB/month
 2) Billing items: traffic (overall traffic amount used in the current month) 
 3) Billing mode: Postpaid
 4) Billing cycle: A calendar month


**Examples of traffic/bandwidth consumption:**
1. Example of traffic consumption
Traffic consumption of an LVB channel=(LVB bitrate/8)*LVB duration (seconds)*number of viewers
For example, if the LVB bitrate is 500 Kbps, the LVB duration is 1 hour, and the number of viewers is 100, then the traffic consumption is about 22.5 GB.
It is calculated as follows: 500/8*3600*100 = 22500000 KB, 22500000 KB/1000/1000=22.5 GB
*The traffic billed is the sum of the traffic consumed in all LVB channels.*
2. Examples of bandwidth consumption
Bandwidth consumption of an LVB channel=LVB bitrate*number of viewers
For example, if the LVB bitrate is 500 Kbps, and the number of viewers is 100, then the traffic consumption is about 50 Mbps.
It is calculated as follows: 500*100 = 50000 Kbps, 50000/1000=50 Mbps
*The bandwidth billed is the sum of the bandwidth consumed in all concurrent LVB channels.*
**Note: This calculation example is only used to estimate bandwidth and traffic consumption, so you can choose a suitable billing mode. The actual bandwidth and traffic billed is subject to the bills.**


## 1.2 Channel Billing
Tencent Cloud LVB service provides each account with 5 free channels for debugging. If you need more channels for your product, the extra channel will be charged 9.2 USD/channel/month. The overall channels equal the maximum concurrent actual push channels in a month. For more information, contact QQ: 3358225043.

Notes:
1. Each 50 MB of concurrent bandwidth can deduct the cost of one channel. This takes effect only when the billing is based on bandwidth.
2. LVB code mode and channel mode are billed according to this standard. Under LVB code mode, a video ID indicates a channel. 
3. There are no restrictions on the number of channels.
For example, if the bandwidth billed is 100 MB, the maximum concurrent actual channels are 10, then the number of billed channels=10-5-(100/50)=3

# 2. Value-Added LVB Service Billing

Using value-added LVB services can produce related costs. Currently, the billed value-added LVB services include recording, screencap and porn detection.

## 2.1 Recording Costs
The price of recording in Tencent Cloud LVB service: 4.6 USD/channel/month. The overall channels equal the maximum concurrent recording channels in a month.
The recorded files are stored in the Tencent Cloud VOD system and can produce VOD and storage costs. It can also produce VOD traffic/bandwidth costs during video playback. For information on VOD billing, please see [Product Price](https://cloud.tencent.com/product/vod#price)

## 2.2 Screencap and Porn Detection Costs

1. Billing items: LVB screenshot and picture porn detection.
2. Price: 
  1) Screenshot price: 0.015 USD/1,000 screenshots. The first 999 are free of charge, and the extra quantity will be billed. The screenshots less than 1,000 will be counted as 1,000. For example, 3600 will be counted as 4000. 
  2) Picture porn detection: 0.20 USD/1,000 screenshots. The first 999 are free of charge, and the extra quantity will be billed. The screenshots less than 1,000 will be counted as 1,000. For example, 3600 will be counted as 4000. 
3. Notes
The screenshot feature only produces screenshot costs. However, to enable picture porn detection, you must enable screenshot so that two costs will be produced.

