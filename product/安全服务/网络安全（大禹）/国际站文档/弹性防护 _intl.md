## What is the Role of Elastic Defense?
With elastic defense enabled, if the attack traffic exceeds the purchased minimal defense volume, Tencent Cloud's High Defense IP can continue to provide defense till the upper limit of defense (minimal + elastic defense) is exceeded.

## How to Calculate the Defense Peak?
- The calculation of the elastic defense peak uses a overlapped mechanism. If the basic defense of 10 Gbps is selected, and the elastic defense of 20 Gbps is enabled at the same time, the final defense capacity is 10 Gbps+20 Gbps=30 Gbps.
- You can change the elastic defense volume at any time according to your own business needs, and customize the upper limit of elastic defense.

## How is elastic defense billed?
- You can enable the elastic defense for free. Only when the attack volume exceeds the minimal defense peak (namely, the elastic defense is triggered), the fee is charged. The billing mode of elastic defense is billing by volume on a daily basis. The fee is charged according to the elastic defense peak range of the day, and the bill is generated the next day.
For example: a user has purchased the minimal defense of 10 Gbps and set the elastic defense of 50 Gbps, and the actual attack traffic is 30 Gbps, then the elastic defense in the range of 20 Gbps to 30 Gbps will be charged.
- If an IP is attacked several times in a day, and the attack traffic exceeds the minimal defense value but does not exceed the elastic defense value each time, it is billed based on the highest attack traffic on that day.
- For more information, please see [Product Price](https://cloud.tencent.com/document/product/297/8799).

