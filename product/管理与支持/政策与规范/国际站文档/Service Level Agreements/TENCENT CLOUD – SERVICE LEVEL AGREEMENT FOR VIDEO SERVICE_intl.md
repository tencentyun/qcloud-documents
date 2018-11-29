## 1.	INTRODUCTION
This agreement forms part of, and is incorporated into, the Tencent Cloud Service Level Agreement between you and us, in relation to your use of Tencent Cloud.
## 2.	SERVICE LEVELS
Separate Service Levels apply to the Global Video Service and the Mainland China Video Service. 

A "**Video Service Level**" is either the Global Video Service Level or the Mainland China Video Service Level (as applicable). 

###  2.1 Global Video Service Level
The following is the "**Global Video Service Level**" for the Tencent Cloud Global Video Platform service (“**Global Video Service**”).

<table style="width:700px">
<tbody>
<tr>
<th style="width: 300px;">Global Video Service Level</th>
<td style="width: 400px;">At least 99.9996% Persistence for Organisation’s data storage on Tencent Cloud.  </td>
</tr>
<tr>
<th style="width: 300px;">Requirements/conditions for this Service Level</th>
<td style="width: 400px;">
"<b>Availability </b>" is calculated as the average result from five Tencent nominated major worldwide metropolitan backbone agents, geographically distributed across all active delivery regions (excluding Mainland China). </br></br>
See Section 3 below for detailed conditions.
</td>
</tr>
<tr>
<th style="width: 300px;">Service Credit</th>
<td style="center; width: 400px;">
See Section 4 below.  
</td>
</tr>
</tbody>
</table>

### 2.2	Mainland China Video Service Level
The following is the "**Mainland China Video Service Level**" for the Tencent Cloud Mainland China Video Platform service (“**Mainland China Video Service**”).

<table style="width:700px">
<tbody>
<tr>
<th style="width: 300px;">Mainland China Video Service Level</th>
<td style="width: 400px;">Mainland China Video Service Availability is at least 99.90%.  </td>
</tr>
<tr>
<th style="width: 300px;">Requirements/conditions for this Service Level</th>
<td style="width: 400px;">
"<b>Availability </b>" is calculated as the average result from five Tencent nominated major metropolitan backbone agents, geographically distributed across all active delivery regions within Mainland China. </br></br>
See Section 3 below for detailed conditions.

</td>
</tr>
<tr>
<th style="width: 300px;">Service Credit</th>
<td style="center; width: 400px;">
See Section 4 below.  
</td>
</tr>
</tbody>
</table>

## 3.	REQUIREMENTS & CONDITIONS FOR VIDEO SERVICE LEVEL
### 3.1	Calculation of Availability
For the purposes of each Video Service Level, "**Availability**" means the amount of time (in a complete calendar month) that the Video Service was available to Organisation.  

Calculation of each Video  Service Level refers only to the content delivery itself, and excludes the Cloud Console, Application User Interfaces (or APIs), and other related services. 

In calculating Availability: 

 (a) Unit time = 5 minute intervals. A service failure that returns to normal within less than 5 minutes will not be counted as service unavailability. Two or more continuous intervals (10 minutes or greater) of service unavailability shall be considered a failure.  Any period of service unavailability that is less than 10 minutes is not considered a failure. 

 (b) 	"**Unavailable**" means that the relevant Video Service is not available to be used by the end user in accordance with the relevant Specifications, only where such unavailability is caused by Tencent Cloud not operating in accordance with the relevant Specifications. The period of time where the service is unavailable is calculated from when the service failure begins through to when the service returns to normal, and excludes any unavailability caused by or in relation to any Exclusions. 

 (c) A service failure that returns to normal within less than 5 minutes will not be counted as service unavailability. The service unavailable time is a period of time from when the service failure begins through to when the service returns to normal, including the maintenance time.

For the purposes of calculating Availability for each of the Video Service Levels:

(d) Tencent's tests for calculating Availability will meet all of the following criteria:

&emsp;(i)	run equally from each agent, one or more times per hour

&emsp;(ii)	use an MP4 HTTP test object (500KB-5MB)

&emsp;(iii)	have "cache-control: public" (1 day) as the only test object TTL

&emsp;(iv)	utilize high availability Video Service accessible origin storage 

 (e)	All backbone “agent availability” problem samples will be trimmed from the pre-calculation final data.

 (f) Organisation may also provide additional data from any third party, independent from Organisation and commercially operated monitoring services meeting these same criteria, for Tencent's consideration.


### 3.2	Video Service Level-specific Exclusions
In addition to the Exclusions set out in Section 4 of the Tencent Cloud Service Levels Agreement, any non-Availability of any Video Service caused by any of the following Exclusions will not be calculated for the purposes of calculating any Video Service Level:

 (a) inaccessibility of Organisation’s site source server(s) due to modification of source station equipment or acceleration of domain name(s) DNS configuration, without prior express agreement with Tencent; and

 (b) where Tencent has provided additional capacity for Organisation’s relevant Video due to a sudden increase in end user traffic to Organisation’s site, without prior notice of such sudden increase from Organisation to Tencent. 

## 4.	SERVICE CREDITS
### 4.1	Introduction

Service Credits are calculated in accordance with the Tencent Cloud Service Level Agreement. As set out in Sections 2.2 and 2.3 of that Agreement: 

 (a) All Service Levels will be calculated on a per-account, per-complete calendar month basis.

 (b) Service Credits are calculated as a percentage of the total Charges paid by Organisation to Tencent in respect of the relevant Video Service provided during the relevant calendar month in which the Service Level was calculated.    

### 4.2	Global Video Service Level – Service Credit
<table>
<thead>
<tr>
<th style="text-align: center; width: 240px;">Persistence </th>
<th style="text-align: center; width: 240px;">Service Credit</th>
</tr>
</thead>
<tbody>
<tr>
<td>99.0% to < 99.90%</td>
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

### 4.3	Mainland China Video Service Level – Service Credit
<table>
<thead>
<tr>
<th style="text-align: center; width: 240px;">Persistence </th>
<th style="text-align: center; width: 240px;">Service Credit</th>
</tr>
</thead>
<tbody>
<tr>
<td>99.0% to < 99.90%</td>
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

### 4.4	Example of how Service Credit for a Video Service Level is calculated
 (a) Fault Time = (incident resolution time) minus (failure starting time).   

 (b) Fault time is calculated per minute. Faults under 1 minute will be rounded up and deemed as one minute. 
