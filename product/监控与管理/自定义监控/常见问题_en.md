## 1. There is no data when I check the monitoring object view in CCM.
If there is no data on a specific CCM object, please follow the steps below for troubleshooting:
- Check whether you have reported the data. If not, you can report the data by referring to the API [User Data Reporting](https://www.qcloud.com/doc/product/397/%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E4%B8%8A%E6%8A%A5).
- If so, please check whether the data is successfully reported.
- If there is no problem in the above steps, please submit a ticket.

## 2. How many types of alarm rules in CCM and how do they work?
CCM has 2 types of alarm rules: wildcard metric dimension alarm rule and object alarm rule.

| Type | Definition | Entry | Priority |
|---------|---------|---------|
| Wildcard metric alarm rule | The wildcard rule for all the objects under the statistical type of a specific metric | "CCM" -> "Monitor Configuration" -> "Alarm Management" | It has a lower priority than object alarm rule |
| Object alarm rule | The alarm rule for a specific object | "CCM" -> "Monitor Configuration" -> "Alarm Management" | It has a higher priority than wildcard metric alarm rule |

Example:
Metric to be reported: CPU utilization. Statistical type: max, and 5-minute period. Objects to be reported: 1.1.1.1 and 2.2.2.2.

Wildcard metric rule is set as follows: CPU utilization (Max, 5 min) > 80%; number of statistical periods for alarm: 2.
Object alarm rule is set as follows: Configure the rule to 1.1.1.1. CPU utilization (Max, 5 min) > 90%; number of statistical periods for alarm: 1.

- The object 1.1.1.1 has 2 alarm rules, and the object alarm rule is valid.
CPU utilization (Max, 5 min) > 90%; number of statistical periods for alarm: 1.
- The object 2.2.2.2 has an alarm rule, and the wildcard rule is valid.
CPU utilization (Max, 5 min) > 80%; number of statistical periods for alarm: 2.
