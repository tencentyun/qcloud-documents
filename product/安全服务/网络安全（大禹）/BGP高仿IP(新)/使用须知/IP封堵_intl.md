## What is IP Blocking?
IP blocking is to point all the traffic accessing your domain name to NULL when the traffic passes through Tencent Cloud's cleaning cluster (also known as black hole routing or traffic dropping). If the IP is blocked, the business will not be accessible.

## When will the IP be Blocked?
- IP blocking is triggered when your IP is under an attack and the attack traffic exceeds the defense threshold (minimal + elastic defense). The general blocking duration is 2 hours. For large traffic attack, the duration is 24-72 hours.
- If the platform encounters multiple attacks at the same time, to ensure the stability of the platform, the Blocking by ISP will be triggered and your business will be inaccessible. If the defense threshold is not reached, the relevant elastic defense costs will be waived, and the Blocking by ISP is lifted after 24 hours by default.

## Blocking Alarm
- When your IP is attacked and blocked, we will send a blocking alarm message to you via an internal message, SMS, and email.
- For more information on blocking alarm, please see [Alarm Messages](https://cloud.tencent.com/document/product/297/15557).

## Early Unblocking
You can purchase or upgrade the Dayu high defense product for early unblocking.
- If you have not purchased the Dayu high defense product, we recommend that you purchase [Dayu High Defense Product](https://console.cloud.tencent.com/dayu/basic) to ensure normal running of your business.
- If you have purchased the Dayu high defense product, we recommend that you [Upgrade](https://console.cloud.tencent.com/dayu/basic) the product for early unblocking.

**Note:**
Enable [Elastic Defense](https://console.cloud.tencent.com/dayu/bgp) to help to protect you against massive traffic attacks. Elastic defense is paid on a daily basis, which can save costs for you. For more information on how to enable elastic defense, please see **Enable Defense** in [Tutorial](https://cloud.tencent.com/document/product/297/15563).

