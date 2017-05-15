## What are the consumption details?

The consumption details calculate the monthly usage and consumption amount of cloud services of a user account, and support itemized consumption statistics.

Currently, this feature is only supported for five types of cloud services: Cloud Virtual Machine, Cloud Database (MySQL), Cloud Load Balance, CDN bandwidth and IDC public network bandwidth.

## What is the difference between consumption details and income & expense details?

Income & expense details are the income/expense records of a user account (i.e., top-up/deduction).

1. For **postpaid (bill-by-traffic) products**, if the payment is charged hourly or daily, income & expense details and consumption details have the same amount for the month. If the payment is charged monthly, there is no deduction records in income & expense details for the month, which will be generated on the settlement day of the next month. The consumption details include the usage and corresponding consumption amount. For the device products such as Cloud Virtual Machine, Cloud Database and Cloud Load Balance, the amount of consumption is calculated on the basis of the number of days used. For the network products such as CDN bandwidth and IDC network bandwidth, the consumption record of the month is generated on the settlement day of the next month.

2. For the network products such as CDN bandwidth and IDC network bandwidth, the usage and corresponding amount is apportioned to each item based on a certain algorithm in the consumption details, and the income & expense details do not support this function.

## Usage of consumption details

Consumption details are mainly used to view the monthly consumption of cloud services, and are provided to the users to help them estimate the cost. As apportionment is based on item or month and not all products are supported currently, the consumption details can not be used for account checking. Please use income & expense details for reconciliation.
