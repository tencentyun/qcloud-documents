
## 1. Overview of Service

Tencent Cloud Content Delivery Network Service (hereafter referred to as "CDN Service") is used to accelerate the delivery of such content as static web pages, dynamic content, file downloads and streaming media. The service supports billing methods on a basis of traffic or peak bandwidth. For more information, please visit Tencent Cloud official website.


## 2. Service Availability

> The service availability is not less than 99.9%.
>
> Availability = uptime of service within the service period for domain name/total service time within the service period for domain name

Notes:

+ A natural month is counted as a service period. A duration less than a month will not be counted as a service period. In this case, service availability will not be calculated.
+ Unavailability duration: If CDN Service has an error rate greater than 0.05% (exclusive) within a unit time period (5 minutes is taken as a statistical granularity), the service is considered unavailable within the unit time period; if this persists for 10 minutes or more, the duration will be counted in unavailability duration; if this persists for less than 10 minutes, the duration will not be counted in unavailability duration.
+ Error rate=(number of 5xx errors within unit time period+number of failed requests caused by unavailable node within unit time period)/total number of requests from the domain name within unit time period:
  + 5xx: HTTP status code, which indicates a server error.
  + Number of 5xx errors within unit time period: The number of 5xx errors returned by the domain name within unit time period due to CDN system's problem.
  + Number of failed requests caused by unavailable node within unit time period: In the event of an unavailable node, the number of failed requests caused by unavailable node within unit time period is calculated by multiplying the average number of requests from the customer domain name at this node within unit time period for the first 7 days by the unavailability duration of the node within unit time period. 
+ Any unavailability of service caused by one of the following reasons is not counted in the unavailability duration:
  + Failure of customer's origin server; 
  + Error caused by a banned domain name due to violation of laws or regulations by customer's content or other reasons;
  + Tencent Cloud node server cannot access customer's origin server normally because customer has made modifications to origin server configuration or the DNS configuration of acceleration domain name without notifying Tencent Cloud in advance;
  + Loss or leakage of data, password or other information caused by customer's improper maintenance or negligence in confidentiality;
  + Upgrade of operating system by customer without the notification to Tencent Cloud; 
  + Hacker attacks on customer's website;
  + Lower availability caused by customer's large-scale burst of traffic without the prior written notification to Tencent Cloud; 
  + System maintenance performed by Tencent Cloud, including cutover, repair, upgrade and simulated failure drill, by giving a prior notification to customer;
  + Any failure or configuration adjustment of network or device other than Tencent Cloud's devices;
  + Force majeure and accidents;
  + Other reasons that are not on account of Tencent Cloud.

**Example:**

>  (1) If the domain name is abc.com, the total number of requests within 5 minutes is 1,000,000, and 1000 5xx errors are returned, the error rate=(1000 + 0)/1000000 = 0.1%. Since 0.1% is greater than 0.05%, the service is considered unavailable within the 5 minutes.

> (2). The total duration of service for the domain name for current month (service period) is 30 (days) x 24 (hours) x 60 (minutes) = 43,200 minutes. Calculated according to an availability of 99.9%, the monthly unavailability duration is 43.2 minutes; if the unavailability duration calculated as shown in the example (1) exceeds 43.2 minutes, the service for current month will be deemed to not conform to SLA.

## 3. Network Access Capability

CDN service does not impose any limit on the bandwidth of public network ingress. With hundreds of cache nodes distributed across the country, it can ensure the customer's network access quality.


## 4. Failure Recovery Capability

By providing at least dual network redundancy and device redundancy, Tencent Cloud can offer fault-tolerant service for emergent network line failure to ensure the continuity of service. In addition, with a professional team that provides 7x24 maintenance service and technical support by means of tickets, telephone or other channels, Tencent Cloud boasts a series of excellent emergency response mechanisms covering efficient failure monitoring, automatic alarm, fast positioning and rapid recovery.


## 5. Resource Allocation Capability

+ CDN service does not set any limit on bandwidth and storage, so that customers can dynamically expand resources according to actual business needs. But for a large-scale traffic surge (business growth is equal to or greater than 30% of last month's billing bandwidth or total bandwidth increases by 50Gbps or more), customer needs to give a notice to Tencent Cloud at least 3 working days in advance, otherwise the service availability will be affected.
+ In case of no advance notice, CDN Service can provide an additional 30% or less (inclusive) of last month's billing bandwidth to meet the urgent need of customer, to ensure that the availability of connected domain name will not be significantly reduced. However, Tencent Cloud disclaims the obligation to ensure the service availability in case of customer's large-scale traffic surge without prior notice to Tencent Cloud and should not assume any responsibility for affected service availability caused by such traffic surge.

## 6. Destroyable Service and Data

During the use of CDN service, customer can access and download files at any time, and clear the cached file according to actual business needs. After being cleared, the file cannot be restored. The customer needs to go back to origin server to access the file again.

## 7. Service Privacy

Customer can configure access authentication policies according to actual needs to control and isolate external access to protect the privacy of data.

## 8. The Right to Know the Service Status

+ At present, the data cached by Tencent Cloud CDN service is distributed across the nation-wide nodes, and the node resources are allocated based on the domain name access. Customer can query the distribution of nodes for his or her domain name by submitting tickets to get a picture about the distribution of cached data.
+ Tencent Cloud Data Center will comply with applicable local laws and regulations. Customer has the right to know what is going on at all times and can make queries by submitting tickets.
+ Without the written content of customer, all customer data will not be provided to any third party, except as permitted by laws and regulations or required by regulatory authorities.
+ Customer's behavior log will not present any personal information of customer to others, unless such behavior log is used for the statistical analysis of the running status of Tencent Cloud CDN Service.



## 9. Audit of Service

In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may disclose information on the service used by customer, including operation log of key components, operation records of operation & maintenance personnel and operation records of customer, if required by the regulatory authorities or it is necessary to do so for other reasons such as collection of evidences during investigation into safety accidents.

## 10. Service Billing Accuracy

The prices of Tencent Cloud CDN Service are provided in customer's purchase page and order page. The charges for service are calculated according to the actual consumption of customer. For detailed billing standards, please refer to the billing models and prices released on Tencent Cloud official website.

## 11. Service Compensation

Service Compensation refers to the compensation offered by Tencent Cloud to customer in the event that the CDN service purchased by customer fails to conform to the requirement for service availability stated in the SLA as a result of failure or design defect of Tencent Cloud's devices or any improper operation performed by Tencent Cloud. The rules of compensation are as follows:

+ For each of customer's domain names for which Tencent Cloud fails to meet the requirement for service availability, the compensation amount is ten times that of the charge for the faulty domain name for the unavailability duration.
+ Compensation amount = average charge for the faulty domain name per minute within the last 24 hours before failure (if it is less than 24 hours, the charge is calculated based on the average value for the actual usage duration) x failure duration x 10.

**Description:**

>  Failure duration = the time when the failure is resolved - the start time of failure. The failure duration is calculated in minutes, and the duration less than 1 minute will be counted as 1 minute. For example, if the failure duration is 1 minute plus 1 second, it will be counted as 2 minutes.

> The compensation applies only to the customer who has used the CDN service and incurred a charge from the usage. The compensation will be paid in the form of vouchers, instead of cash. The compensation amount should not exceed the total amount the customer has paid for the faulty domain name.

## 12. Miscellaneous

The service terms under this agreement may be subject to the changes made by Tencent Cloud as necessary. Any changes involving the usage of service by customer will be pushed to customer via e-mail.
