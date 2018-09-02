### 1. Billing models for CDH

CDH service offers prepaid purchase of dedicated host machines.
You can create CVMs on your CDH freely without extra expense.

### 2. Does CDH service support postpaid mode?

No, CDH service only supports a prepaid mode.

### 3. When a CDN expires and is moved to the recycle bin, what happens to CVMs on it?

If a CDH is not renewed after it expires, it is moved to the recycle bin.

When this happens,

- The CVM instances on this CDH are shut down and removed from the instance list on the CVM console.
- If you renew the CDH is renewed within 7 days, all CVM instances on it would be recovered automatically. Manual boot is not required.
- If the CDH is not renewed within 7 days, this CDH and CVMs on it are terminated. Tencent Cloud reclaims all resources.
