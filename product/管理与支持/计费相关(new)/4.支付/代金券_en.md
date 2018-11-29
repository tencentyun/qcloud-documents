# Voucher
# About Voucher
Vouchers are deductible coupons that can be used in your purchase. You can check available vouchers on [Console] -> [Cost] -> [Vouchers] in the Tencent Cloud official website.
## Voucher Description
### Overview of Features
#### Usage
1. Applicable to prepaid products: users can choose to use vouchers while purchasing cloud products.
    
    ![](http://i.imgur.com/sr8uVwa.png)

    (1) In the payment page, the system matches available vouchers for applicable products based on payment type, order amount, and purchase period. Only these four conditions are met, eligible vouchers (that is available, used, and can be used for multiple times) are displayed while paying orders.
    
    (2) You can only use one voucher for one order. If there are multiple vouchers available, you can choose to use one of them or pay without vouchers by deselecting the [Use Voucher] option.

    (3) After setting the automatic renewal of resources, the system automatically uses vouchers and then use the account balance for renewal deductions (For more information about specific rules, please refer to auto-selection rules for postpaid mode).
2. Applicable to postpaid products: the system automatically select vouchers by hour/day/month for cloud product settlement fee.
    
    (1) Auto-selection rules: For vouchers available to applicable product, payment type, scenario, use conditions (available, used, can be used for multiple times), the system sorts the vouchers based on their expiration time and reverse deductible amount (vouchers with the same deductible amount will be sorted by balance from small to large) and deduct with eligible vouchers. Vouchers that are expiring will be optionally used. If multiple vouchers are expiring at the same time, the vouchers with greatest discount will be used based on their balance and deductible amount.
    
    **Example:**
   
    Assumed that Customer A has used postpaid CVM for one hour, the incurred cost is 4 CNY, and now there are five eligible vouchers can be used:
    
    Vouchers A: nominal amount: 10 CNY; Balance: 10 CNY, Valid until March 9 (deductible amount: 4 CNY)
    
    Vouchers B: nominal amount: 10 CNY; Balance: 8 CNY, Valid until March 9 (deductible amount: 4 CNY)
    
    Vouchers C: nominal amount: 20 CNY; Balance: 5 CNY, Valid until March 9 (deductible amount: 4 CNY)
     
    Vouchers E: nominal amount: 20 CNY; Balance: 2 CNY, Valid until March 9 (deductible amount: 2 CNY)

    Vouchers D: nominal amount: 20 CNY; Balance: 4 CNY, Valid until March 10 (deductible amount: 4 CNY)
    
    Based on the sequence above, the vouchers will be used in the order of C, B, A, E, D. Therefore,voucher C will be used in this payment.
    


   ![](http://i.imgur.com/Yd2FZkJ.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (2) After the system automatically selects the voucher for deduction, you can check deductible amount on "Income & Expense Details" -> "Details" -> "Resource Bill" -> "Cost".

#### Permission

Only creator and collaborator with the "Financial Management" permission can enter the cost center to use the vouchers.
#### How to redeem paper vouchers
Tencent Cloud vouchers are divided into paper vouchers and e-vouchers. After developers obtains e-vouchers, they will see the issued e-voucher in the "Cost Center" of the voucher page, which are in the status of [Available]. After the developers obtain paper vouchers, they must redeem them. After the paper vouchers are redeemed, the developers can check them in the "Cost Center" of the voucher page, which are in the status of [Available].Only paper vouchers need to be redeemed.

![](http://i.imgur.com/xcu9xIG.png)

(1) Go to "Cost Center" -> "Vouchers" -> "Voucher Management" -> "Redeem voucher".


![](http://i.imgur.com/BxFlK5c.png)

(2) In the pop-up, enter 18-digit promo code.

![](http://i.imgur.com/04Vxbnu.png)


(3) Click "OK" to redeemed the paper voucher and check it on the voucher status.

#### Voucher Status

A voucher has 4 status: Available, Frozen, Used, and Expired.

Available: voucher is not used and still valid.

Frozen: voucher is not used but order has been confirmed.

Used: voucher has been used.
