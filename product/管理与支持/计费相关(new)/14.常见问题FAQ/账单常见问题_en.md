## 1. Why there is a difference between the amount in consumption details and that in the resource statement/income&-expense details?

The resources that do not support itemized billing, such as IDC and CDN, fall under "Default Projects" in the Resource Statement. This type of resources currently include IDC bandwidth, CDN bandwidth, COS, VOD and LVB.

These resources will be spread among various projects in the consumption details after "estimation" based on their proportions of usage. Therefore, consumption details can only be used to estimate the cost of each project.

<font color="red">Since the consumption details does not represent a complete inclusion of all products, it cannot be used for reconciliation. Please use income&expense details and resource statement for reconciliation.</font>

## 2. What is the difference between resource statement and income&expense details?

**Resource Statement**

Queries of monthly statement by month, platform, payment method and user project are supported.

The resource statement lists resource IDs to identify the corresponding resource.

The details of each data item in the statement include deduction time, due time and so on.

**Income&Expense Details**

Query of income&expense details of account by transaction type is supported.

Checking details of each deduction is supported.

## 3. How to obtain the statement for the resources consumed in a month?

Assuming that you want to get the statement for the resources consumed in October. Please combine the data of prepaid resources+ daily-settled resources + hourly-settled resources in the resource statement of October and the data of monthly-settled resources in the resource statement of November.





