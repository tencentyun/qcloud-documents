## Scenario Description
It is recommended to use AS (Auto Scaling) for common Web service server to get free access to convenient management and robust business.

For e-commerce websites, video websites and online education applications, client requests are sent to application server through cloud load balancer. In case of rapid changes in visits, AS service can flexibly scale up and down the number of application servers based on the number of requests.

![Alt text](https://mc.qcloudimg.com/static/img/ba977d67b59a73d6a137323b61d17ec4/01+%282%29.png)

## How to Use
Add the following clusters to a scaling group to provide further protection for the cluster:

- Frontend server cluster (access layer)

- Application server cluster (logic layer)

- Cache server cluster (data layer)

You can also set up timed scaling policies for expected business peaks (such as online promotions).

> **TIPS:** Move the CVMs in the cluster into the scaling group, and set the "scale-down exemption" for certain CVMs to ensure normal use of the cluster. At the same time, set the alarm scaling policy to cater with burst traffic or CC attacks.

## Benefits of AS
1. AS can provide further protection for your business by dealing with unexpected request traffic and avoiding SPOF;

2. By only estimating resident resources, instead of estimating resources based on the peak value, AS can dynamically adjust the elastic resources to save IT cost;

3. Rapid scale-up can be enabled in case of CC attacks to avoid request packet loss.



## Applicability

This solution is applicable to all websites, especially to those with large load fluctuation:

- E-commerce website

- Online education website

- Video website

- LVB website


## FAQ
> Is this solution applicable to common web services, such as internal systems or websites with steady traffic?

Common websites will also encounter unexpected situations, such as CC attacks, or piled visits due to unexpected incidents.

The solution will not cause any additional cost. By simply setting "scale-down exemption" for the planned CVM, the design and operation of websites will not be affected. When any accidents occur, AS can bring huge benefits, avoiding service suspension.

Therefore, we highly recommend this solution for you.

