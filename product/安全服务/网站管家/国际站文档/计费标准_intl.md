## Web Application Firewall (WAF) - Billing Documentation



### Billing method

Postpaid on a daily basis

### Billing formula

Daily billing = Daily peak QPS x QPS billing factor

### Tiered pricing

Notes:

(1) Daily peak QPS

It is calculated based on the data collected between 00:00:00 and 23:59:59 in a day. QPS of the website is subject to the total requests per second received on the WAF for accessing the domain name you configured. Once the domain name is configured, counting begins.

(2) QPS billing factor

Price is calculated based on tiered peak QPS factors.

```
If the peak QPS is between 5-50 (any number less than 5 is counted as 5), the billing factor per QPS is 0.2 USD/day.
If the peak QPS is between 50-200, the billing factor per QPS is 0.18 USD/day.
If the peak QPS is between 200-1,000, the billing factor per QPS is 0.15 USD/day.
If the peak QPS is greater than 1,000, the billing factor per QPS is 0.12 USD/day.
```

List of tiered prices:

| Peak QPS | QPS Billing Factor |
| -----------: | ----------: |
|      < 5 QPS | 0.2 USD/day |
|     5-50 QPS | 0.2 USD/day |
|   50-200 QPS | 0.18 USD/day |
| 200-1000 QPS | 0.15 USD/day |
|   > 1000 QPS | 0.12 USD/day |

Billing example: Suppose that today's peak QPS of the website is 15, the billing amount of today is 15 x 0.2=3 USD.

Note:
In the case of insufficient account balance, the WAF service will be suspended one day after the account is in arrears, and the WAF resources will be released in 7 days. You can pay off the arrears before the release of resources to resume defense service.

