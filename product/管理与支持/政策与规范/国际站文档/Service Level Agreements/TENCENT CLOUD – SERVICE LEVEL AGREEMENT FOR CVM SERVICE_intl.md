## 1.	INTRODUCTION
This agreement forms part of, and is incorporated into, the Tencent Cloud Service Level Agreement between you and us, in relation to your use of Tencent Cloud.
## 2.	SERVICE LEVELS
###   2.1 Introduction       
  
  The following are the Service Levels for Tencent Cloud’s Cloud Virtual Machine service ("**CVM**").
 
 Service Credits are calculated in accordance with the Tencent Cloud Service Level Agreement. As set out in Sections 2.2 and 2.3 of that Agreement: 
 
&emsp;(a) All Service Levels will be calculated on a per-account, per-complete calendar month basis.

&emsp;(b) Except for the CVM Expansion Support Service Level, Service Credits are calculated as a percentage of the total Charges paid by Organisation to Tencent in respect of the CVM service provided during the relevant calendar month in which the Service Level was calculated.
 
###  2.2 Data Storage Persistence Service Level

<table style="width:700px">
<tbody>
<tr>
<th style="width: 200px;">Service Level</th>
<td style="width: 500px;">At least 99.999% Persistence for all CVM block storage instances requested by Organisation. </td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">For the purposes of this Service Level, <b>"Persistence"</b> means a maximum of one storage volume will experience data loss each calendar month if Organisation has requested 100,000 CVM block storage instances in that same month. </td>
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
<td>99.0% to < 99.999%</td>
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

###  2.3 Service Availability Service Level

<table style="width:700px">
<tbody>
<tr>
<th style="width: 200px;">Service Level</th>
<td style="width: 500px;">At least 99.95% Service Availability for all CVMs. </td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">
For the purposes of this Service Level,<b> “Service Availability"</b> means the average availability of all CVMs to Organisation, within the same region per-complete calendar month.</br></br>

Any service failure that returns to normal within less than 5 minutes will not be counted as service unavailability. The service unavailable time is a period of time from when the service failure begins through to when the service returns to normal, including the maintenance time.</br>

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

### 2.4  CVM Expansion Support Service Level

<table style="width:700px">
<tbody>
<tr>
<th style="text-align: center; width: 200px;">Service Level</th>
<td style="width: 500px;">Completing all requests from Organisation for expanded resource in accordance with the Service Availability Request metric below.  </td>
</tr>
<tr>
<th style="width: 200px;">Requirements/conditions for this Service Level</th>
<td style="width: 500px;">
<b>"Service Availability Request" </b>means where the actual resource is being expanded by:</br></br>

<ul>•	less than 50 CVM instances will be completed within 10 minutes (of a working hour) from the time that the relevant request was submitted by the Organisation and registered in Tencent's system </br></br>

•	less than 200 CVM instances will be completed within 1 working hour from the time that the relevant request was submitted by the Organisation and registered in Tencent's system</br></ul>

This Service Level only applies where the original capacity of the CVM service is 50% or less of the expanded resource (following fulfilment of the relevant request). </br></br>

This Service Level only applies where the Organisation has requested for the expansion to be manually performed. </br></br>

Scale-out schedule for requests for scaling out computing for more than 200 CVM instances or no less than 50% from the current capacity will be coordinated by a dedicated account manager.  Such expansion requests will not be used to calculate this Service Level, and no Service Credits apply to such expansion requests. </br></br>

This policy applies to the following CVM resources: CPUs, memory, disks, and bandwidth. Scale-out can support a maximum of 48 CPU cores, 368GB of memory, 7,200GB of local disk, 4TB of single cloud disk, bandwidth up to 200Mbps. The granularity of the allocation may vary based on each resource type. Please refer to the Specifications for further details.</br></br>

In the above Service Levels, a <b>"working hour"</b> means a working hour (or minutes) between 9am to 6pm, Monday to Friday, Hong Kong time, excluding any public holidays in Hong Kong. Any time outside such working hours will not be used to calculate this Service Level. </br></br>

 </td>
</tr>
<tr>
<th style="text-align: center; width: 200px;">Service Credit</th>
<td style="width: 500px;">
The below Service Credit will be payable against the specific CVM resources being expanded, where all Tencent application expansion processes related to that action fail to complete (in accordance with the corresponding Service Level) in any complete calendar month.</br></br>
<table>
<tr>
<th style="width: 400px;">Service Credit</th>
</tr>
<tr>
<td>10% of the Charges (during the relevant calendar month in which the Service Level was calculated) payable for the specific CVM resource being expanded.</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>


