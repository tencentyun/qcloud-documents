### What's the difference between event/parameter/metric/unit?
**Event**
An event is an "action" of a user behavior. For an application, an event can be a behavior actively triggered by a user. For example, clicking on the Borrow button is a loan application event. An event can also be a behavior passively triggered by a user. For example, failure to pay the loan on the due date is an overdue event.

Submit an event based on the event ID and name. [Learn More](/document/product/549/15150#.E4.BA.8B.E4.BB.B6.E3.80.81.E5.8F.82.E6.95.B0.E8.AF.B4.E6.98.8E)

**Parameter and parameter value**

The "action" and the specific scenarios such as when, where, and who, constitute a complete user behavior. For example, if a user clicks on the Borrow button at a certain time to borrow CNY 5,000 (loan amount) in 12 installments (number of installments).

The number of installments and loan amount are the parameters of the loan event, and 12 and 5,000 are the parameter values.

**Metric**

Analysis of daily product operations is actually the analysis of metrics. Metrics are used for numerical measuring of behavior events as specific numbers. In the loan industry template, metrics are a combination of events, attributes, and attribute values. Metrics are used with units (number of people/number of loans/amount).

**Dimensions of the data table**

By filtering by dimensions, you can view the performance of data metrics in different dimensions. Dimensions of the loan industry are as follows:

| Dimension | Data Table |
|----|----|
| Product | Funnel analysis/loan analysis/repayment analysis/overdue analysis/loan data |
| Number of installments | Loan analysis |
| User type (old and new users) | Loan analysis |
| Overdue date | Overdue analysis |
Products refer to loan products. You can view loan products by category. For example, Weilidai and Caifudai are two loan products of WeBank. Deduplication is applied to dimensions. If a user borrows money using both product A and product B, the user is counted as one user for all products.

### Some of the data metrics in the funnel/datasheet/profile are similar. Are the data results the same?
No. The calculation logic is different. Take loan as an example:

1. The data calculation logic of the funnel is as follows: Successful loan in the loan funnel refers to the number of users who have successfully applied for loans. The conversion calculation logic is involved.
2. The loan application/successful loan in the data table refers to the number of people who have applied for / successfully borrowed loans on the current day, which changes as events occur, and reflects application services of yesterday/last week.
3. Loan in the profile refers to a user who borrowed money. It is a tag. Profile is a relatively fixed attribute that does not change in a short period of time. Tags are often displayed for users.

**Are there any differences in cross-day data deduplication for funnel, data table, and portrait?**

1. Funnel: Cross-day data deduplication within last 30 days is supported.
2. Data table: Cross-day deduplication is not supported. Only single-day deduplication is supported.
3. Portrait: Cross-day data deduplication within last 30 days is supported.

### How do you make the vertical industry profile?
The vertical portrait of the loan industry is made based on data from Tencent's 800 million QQ users and account IDs submitted by dependent applications.

### How do you control the permissions of loan analysis?
The loan industry is provided with exclusive permissions, which are separated with existing permissions, to fully protect user data security.

The permissions are as follows:

Administrator user group: After the industry is added to the App, administrators can directly view and work with the loan analysis.

Report viewer user group: After the industry is added to the App, report viewers can directly view the loan analysis.

Others: The person with operation management permission can configure industry data permissions.
![](https://main.qcloudimg.com/raw/029e9fad6eff39a5523ba77a91ded7a3.png)



### Why are there so many requirements in credit certification?
This is determined by the characteristics of the industry. We have listed a number of certification methods applicable to the loan industry. You can choose a suitable certification method for your App to upload. If any certification method is not listed, contact customer service at the official website.

### Why is the "product" dimension not provided in credit analysis?
Loan quota and products do not share a one-to-one relationship. A user can borrow money from multiple loan products in an App as long as the borrowed amount is within the loan quota.

### How is data accuracy guaranteed?
Data is reported at the server terminal to guarantee data accuracy. For more information, please see [Reporting Method](/document/product/549/15150).

### Why both optional and required events/parameters are provided?
Because our general industry solution is designed to large-, medium-, and small-sized enterprise users. Small-sized enterprise users that do provide advanced features such as installment repayment and early repayment can choose not to add these configurations in their Apps. If your APP has such features, we recommend you to add these configurations.

### How long can I see the data after reporting?
If your report is successfully received and the log is confirmed to be valid, you can view the data on the next day.

### Notes
1. Statistics is based on the uploaded user account IDs. Supported account ID types include QQ account number, mobile number, email, WeChat account number and others. When you use loan profile, it is recommended to upload your mobile number for higher accuracy.

2. You must upload the event ID and parameter ID strictly as per that in the event and parameter description. Do not make any changes, including capitalization and the number of underlines. Otherwise, it will be invalid.

3. You must report data in an appropriate time frame, or data discrepancy may occur.

4. The amount is in CNY. Check the amount before uploading.

5. Product ID is displayed in the product dimension. You can change the product ID to the product name.
![](https://main.qcloudimg.com/raw/7ddff1bf7eda72a67c046feeec1520fd.png)

More industry solutions will be available soon.
