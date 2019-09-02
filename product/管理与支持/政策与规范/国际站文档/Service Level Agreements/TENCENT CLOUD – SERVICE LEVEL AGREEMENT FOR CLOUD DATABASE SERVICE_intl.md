## 1.	INTRODUCTION
This agreement forms part of, and is incorporated into, the Tencent Cloud Service Level Agreement between you and us, in relation to your use of Tencent Cloud.
## 2.	SERVICE LEVELS
### 2.1 Introduction

The following Service Levels apply to Tencent Cloud's Cloud Database service.

Service Credits are calculated in accordance with the Tencent Cloud Service Level Agreement. As set out in Sections 2.2 and 2.3 of that Agreement: 

 &emsp;(a)	All Service Levels will be calculated on a per-account, per-complete calendar month basis.

&emsp;(b) 	except for the Database Expansion Support Service Level, Service Credits are calculated as a percentage of the total Charges paid by Organisation to Tencent in respect of the Cloud Database service provided during the relevant calendar month in which the Service Level was calculated.      

###  2.2 Data Storage Persistence Service Level
<table style="width:700px">
<tbody>
<tr>
<th style="width: 200px;">Service Level</th>
<td style="width: 500px;">At least 99.9996% Persistence for Organisation’s data storage on Tencent Cloud.  </td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">
For the purposes of this Service Level, <b>"Persistence" </b>means a maximum of four storage volume will experience data loss each month if Organisation has requested 1,000,000 data storage instances during that complete calendar month.
</td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Service Credit</th>
<td style="text-align: center; width: 500px;">
<table>
<thead>
<tr>
<th style="text-align: center; width: 240px;">Persistence </th>
<th style="text-align: center; width: 240px;">Service Credit</th>
</tr>
</thead>
<tbody>
<tr>
<td>99.0% to < 99.9996%</td>
<td>10%</td>
</tr>
<tr>
<td>95.0% to < 99.0%</td>
<td>25%</td>
</tr>
<tr>
<td>< 95.0%</td>
<td>50%</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>


###  2.3	Service Availability Service Level
<table style="width:700px">
<tbody>
<tr>
<th style="text-align: center; width: 200px;">Service Level</th>
<td style="width: 500px;">At least 99.95% Service Availability for Cloud Databases.</td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">
For the purposes of this Service Level,<b> "Service Availability" </b>means the availability of one or more specific Cloud Databases (based on the total number of active instances running at that time) to the Organisation per-complete calendar month.</br></br>
A service failure that returns to normal within less than 5 minutes will not be counted as service unavailability. The service unavailable time is a period of time from when the service failure begins through to when the service returns to normal, including the maintenance time.
</br>
</td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Service Credit</th>
<td style="text-align: center; width: 500px;">
<table>
<thead>
<tr>
<th style="text-align: center; width: 240px;">Persistence </th>
<th style="text-align: center; width: 240px;">Service Credit</th>
</tr>
</thead>
<tbody>
<tr>
<td>99.0% to < 99.95%</td>
<td>10%</td>
</tr>
<tr>
<td>95.0% to < 99.0%</td>
<td>25%</td>
</tr>
<tr>
<td>< 95.0%</td>
<td>50%</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>


###  2.4	Database Expansion Support Service Level
<table style="width:700px">
<tbody>
<tr>
<th style="text-align: center; width: 200px;">Service Level</th>
<td style="width: 500px;">Completing all requests from Organisation for expanded resource in accordance with the Service Availability Request metric below.   </td>
</tr>
<tr>
<th style="width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">
<b>"Service Availability Request" </b> means where the actual resource is being expanded by:</br></br>

<ul>•	less than 10 Cloud Databases, the application process will be completed within one working hour from the time that the relevant request was submitted by the Organisation and registered in Tencent's system;</br></br>

•	between 10 to 30 Cloud Database, the application process will be completed within 24 working hours from the time that the relevant request was submitted by the Organisation and registered in Tencent's system; and</br></br>

•	more than 30 Cloud Databases, the timeframe for completing the application process will be subject to Tencent’s prior approval. Such expansion requests will not be used to calculate this Service Level, and no Service Credits apply to such expansion requests. </br>
</ul>

This Service Level only applies where: (a) the original capacity of the Cloud Database service is 50% or less of the expanded resource (following fulfilment of the relevant request); and (b) the maximum expanded resource capacity is 600GB. </br></br>

This Service Level only applies where the request for expansion will be manually performed.  </br></br>

In the above Service Levels, a "<b>working hour</b>" means a working hour between 9am to 6pm, Monday to Friday, China Standard Time (CST), excluding any national holidays in China. Any time outside such working hours will not be used to calculate this Service Level. </br></br>

</td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Service Credit</th>
<td style="width: 500px;">
The below Service Credit will be payable against the specific database resource being expanded, where all Tencent application expansion processes related to that action fail to complete (in accordance with the corresponding Service Level) in any complete calendar month.</br></br>
<table>
<tr>
<th style="width: 400px;">Service Credit</th>
</tr>
<tr>
<td>10% of the Charges payable (during the relevant calendar month in which the Service Level was calculated) for the specific database resource being expanded. </td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>


