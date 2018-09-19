If you are unsatisfied with the prepaid CVM you have purchased, you can apply for an unconditional return and refund within five days after the purchase. The 5-day unconditional return is allowed only for **one** CVM. The amount you paid is returned to the same account you used to make the payment. In addition, you can apply for an ordinary self-service return within five days after your purchase, in which case the fees for the resources you have used are deducted from the amount you have paid and the remaining refund amount is returned to your account in the form of vouchers. All of the above operations can be performed by yourself in CVM console.
## 5-Day Unconditional Self-Service Return
If you are unsatisfied with the CVM you purchased, you can apply for an unconditional self-service return within five days after the purchase. The rules for return and refund are as follows:
1. For a single account, you can apply for an unconditional return for **one** CVM within five days (inclusive) after the purchase.
2. The device purchased as a postpaid product on a monthly basis cannot be returned after being changed to a prepaid product.
3. If you change the network billing method from bill-by-bandwidth to bill-by-traffic within the 5 days of unconditional return, only the remaining fees for the CVM and network are returned after the change.
4. In case of any application for a return suspected to be exceptional/malicious, Tencent Cloud reserves the right to reject the application.

### Rules for 5-day unconditional self-service return
For an order eligible for 5-day unconditional return, the refund amount is **the total amount paid upon purchase**, including the amount of cash account, revenue account and complimentary account.

**<font color="red">Note: Rebates and vouchers are not returned.</font>**
**Refund amount** is **returned in full to the same accounts you used to make the payment**.

## Ordinary Self-Service Return
For the orders not eligible for 5-day unconditional return and refund policy, the refund policy is as follows:

If you have applied for 5-day unconditional return, you can return additional **3** prepaid CVMs in the console within 5 days (inclusive) after the purchase. For ordinary self-service return, the fees for the consumed resources are deducted from the amount paid and the remaining amount is returned to your account in the form of vouchers. For more information on refund rules, please see [Rules for Ordinary Self-Service Return of CVM](https://cloud.tencent.com/document/product/213/9711#cvm-.E8.87.AA.E5.8A.A9.E9.80.80.E8.BF.98.E8.AE.A1.E8.B4.B9.E8.A7.84.E5.88.99.E4.B8.BE.E4.BE.8B).


### Service limits on ordinary self-service return	
In the following scenarios, ordinary self-service return of prepaid instances is not supported:
1. Prepaid instances that have been purchased for more than 5 days are not eligible for self-service return.
2. Self-service return is not supported for standard network enhanced SN2 and computing network enhanced CN2 instances.
3. Self-service return is not supported for FPGA computing FX2 instances.
4. Self-service return is not supported for instances in Guangzhou Open Zone.
5. Self-service return is not supported for some resources in promotional activities. Please refer to the information provided on official website.

## Notes about Self-service Return of Prepaid CVM Instances
1. After a prepaid instance is returned, no fee for the instance is incurred once its status changes to "Terminating" or "Terminated".
2. When a prepaid instance is returned, the local disks and non-elastic cloud disks mounted to this instance are terminated, and the data stored on these disks will be lost. But the **elastic cloud disks mounted to this instance are retained**, and the data will not be affected.
3. After a prepaid instance is returned, it is moved to the **CVM Recycle Bin to be kept for 7 days**, and the services operating on this instance are terminated. If you want to resume a prepaid instance you have returned, you can go to the CVM Recycle Bin to renew and resume it.
4. In case of any application for a return suspected to be exceptional/malicious, Tencent Cloud reserves the right to reject the application.


### Rules for ordinary self-service return of CVMs
Refund amount=Amount of effective order + Amount of non-effective order - Value of used resources
**Amount of effective order**: The amount paid for the order in effect, excluding discounts and vouchers.
**Amount of non-effective order**: The amount paid for the order that will take effect in the future, excluding vouchers.
**The fees for used resources** are calculated based on the following policies:
- Fees for the used resources = Fees for the used CVM + Fees for the used network
 - If the application for return is submitted one month after the purchase, the fees for the used CVM are calculated on a monthly basis. If such application is submitted less than a month after the purchase, the fees are calculated by the actual consumption. 
 - Fees for the used network are calculated based on the network billing type. If the network is billed on a postpaid basis, the fees for the used network is calculated as 0. If the network is billed by bandwidth, fees for the used network=Bandwidth price per hour for postpaid CVMs * Usage duration.
- The consumed resources are calculated with an accuracy down to seconds.
- If refund amount<=0, it is considered 0 and resources are cleaned up.

**<font color="red">Note: Rebates and vouchers are not returned.</font>**
**Refund amount** will be returned to your account in the form of **vouchers applicable to all products (valid for 2 years)**.

## Examples of Billing Rules for Self-service Return of CVM
 > **Note:**
 > The following prices are only used as examples, and are not actual prices listed on the official website.
 
### Scenario of 5-day unconditional return
**Guangzhou Zone 2; Standard S1 (1-core 1 GB); 20-GB local disk; without bandwidth; 51 CNY/month, a voucher worth 100 CNY is used, purchased usage period is 1 year, with a discount of 17%.
Discounted price is 51×12×0.83=507.96 CNY
Amount actually paid is 507.96-100=407.96 CNY.**

The user is unsatisfied with the product and applies for a return within 5 days after the purchase. This is the first time the account requests a return.
Refund amount=Amount actually paid (407.96 CNY)

### Scenario of ordinary self-service return
**Guangzhou Zone 2; Standard S1 (1-core 1 GB); 20-GB local disk; without bandwidth; 51 CNY/month, a voucher worth 100 CNY is used, purchased usage period is 1 year, with a discount of 17%.
Discounted price is 51×12×0.83=507.96 CNY
Amount actually paid is 507.96-100=407.96 CNY.**

**Case 1: The user applies for an unconditional return within 5 days after the purchase and this is the first time the account requests a return**
Refund amount (cash)=amount actually paid (407.96 CNY)

**Case 2: The user applies for a return within 5 days after the purchase and this is not the first time the account requests a return. The resources have been used for a total of 48 hours before return.**
Refund amount (voucher)=407.96-48×0.42 (0.42 is the unit price for the same configuration)=387.8 CNY

**Case 3: The user applies for a return within 5 days after the purchase and this is not the first time the account requests a return. The resources have been used for 48 hours. The service is renewed for another year with a discount of 17%, and the amount paid for the renewal is 507.96 CNY.**
Refund amount (voucher)=407.96-48×0.42 (refund amount of effective order)+507.96 (amount of non-effective order)=895.76 CNY

**Case 4: The user applies for a return within 5 days after the purchase and this is not the first time the account requests a return. The configuration is upgraded when the resources have been used for 12 hours, with the amount paid for the upgrade being 100 CNY. The resources have been used for a total of 72 hours before return.**
Refund amount (voucher)=407.96-12×0.42 (0.42 is the unit price for the same configuration)+100/365 (unit price per day for upgraded configuration)×(365-3)(number of unused days of upgraded configuration)=502.1 CNY

Note: The unit prices in the examples are for reference only. Actual unit prices may vary with regions, activities, policies or other factors. Please refer to the actual unit prices in practice.

