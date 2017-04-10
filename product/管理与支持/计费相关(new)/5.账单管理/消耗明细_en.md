## What are the consumption details?

The consumption details will calculate the usage and the corresponding amount of cloud services under the user account, and support itemized consumption statistics.

Currently, only supports the consumption statistics for five types of cloud services: Cloud Virtual Machine, Cloud Database (MySQL), Cloud Load Balance, CDN bandwidth and IDC public network bandwidth.

## What is the difference between consumption details and income&expense details?

Income&expense details is the record of the receipts/disbursements of the user account (i.e., top-up/deduction).

1. For **postpaid (Bill-by-Traffic) products**, if the payment is charged on hourly/daily basis, then for current month, the amount of statistics of income&expense details and consumption details is the same. If the payment is charged on monthly basis, then for current month, there is no deduction records in income&expense details, which will be generated on the account day of the next month. The consumption details include the usage and the corresponding amount of consumption. For the equipment products such as Cloud Virtual Machine, Cloud Database and Cloud Load Balance, the amount of consumption will be calculated on the basis of the number of days used. For the network products such as CDN bandwidth and IDC network bandwidth, the consumption record of the month will be generated on the account day of the next month.

2. For the network products such as CDN bandwidth and IDC network bandwidth, the usage and the corresponding amount will be apportioned to each item based on a certain algorithm in the consumption details, and the income&expense details do not support this function.

## Usage of consumption details

Consumption details are mainly used to view the monthly consumption of cloud services, and are provided to the users for reference to estimate the cost. As a result of apportionment based on item or month and not all products are supported currently, the consumption details can not be used for account checking. Please use income&expense details for reconciliation.
