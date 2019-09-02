
With the cloud monitoring capabilities of Tencent Cloud, you can retrieve statistical data by a set of ordered time series data (called "Metrics"). You can use these metrics to verify whether your system is running as expected, and if the threshold is exceeded, scaling will be involved.

## AS Monitoring Metrics
AS supports the following metrics:

- CPU utilization
- Memory utilization
- Private network inbound bandwidth
- Public network inbound bandwidth
- Private network outbound bandwidth
- Public network outbound bandwidth

Each metric supports the following dimensions:

- Maximum value
- Minimum value
- Average value


## Metric Aggregation Method

Tencent Cloud AS currently only provides the statistics of the "Maximum" value of the monitoring items.

The basic rule for the maximum statistics is to take a value per minute (one value per minute) with each passing period the monitoring items set for each CVM. If the values for multiple consecutive multiple periods (the number of periods can be customized) meet the set rules, the alarm scaling activity will be triggered.

For example:
There are five CVMs in a scaling group, and the defined alarm scaling policy is "CPU utilization is more than 50% for 3 consecutive periods". The system takes a value per minute for each CVM, i.e. taking 25 CPU utilization values within one period (5 minutes). If any of the 25 values exceeds the threshold (50%), the period meets the alarm scaling rule. If the rule is met for 3 consecutive periods, the scaling activity will be triggered.

