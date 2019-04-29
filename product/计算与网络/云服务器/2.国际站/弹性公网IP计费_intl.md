## Billing

### Public network fee

The EIPs bound to cloud product instances (such as CVM or NAT gateway) are free of charge. But you need to pay for public network traffic or public bandwidth when creating an EIP. For more information on the price, please see the [pricing page](https://buy.cloud.tencent.com/price/cvm#tab0-list2). For more information on billing rules, please see [purchasing public network](https://cloud.tencent.com/document/product/213/10579).

### Idle fee

For the bare IPs that are not bound with any cloud product instance and the bill-by-traffic EIPs, you are charged with a resource occupation fee based on the table below.

| Region of the EIP | Price per Hour for EIPs Without Bindings (If the duration is less than 1 hour, the EIP is billed on a pro rata basis) |
|---------|---------|
| Mainland China and Frankfurt | 0.20 CNY/hour |
| Hong Kong | 0.30 CNY/hour |
| North America and Western U.S. (Silicon Valley) | 0.25 CNY/hour |
| Singapore | 0.30 CNY/hour |

If the no-bindings duration is less than 1 hour, the EIP is billed **on a pro rata basis**. For example, if an EIP is idle for 30 minutes, it is billed as `price per hour * 0.5` and is settled once an hour.

To guarantee efficient resource usage and to save your cost, you are recommended to release the EIPs that are no longer used. For more information on operation instructions, please see [releasing EIPs](https://cloud.tencent.com/document/product/213/16586#.E9.87.8A.E6.94.BE.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip).

## Arrears Processing
**For bare IPs, IPs billed by bandwidth on an hourly basis and IPs billed by traffic on an hourly basis:**

- If your account balance has remained below 0 for more than **2** hours, the EIPs will be retained for 24 hours for free. All EIP addresses will be inoperable in the 24 hours, until the account balance has been topped up to an amount greater than 0.
- If your balance is still negative after the 24 + 2 hours, the EIPs will be released.

