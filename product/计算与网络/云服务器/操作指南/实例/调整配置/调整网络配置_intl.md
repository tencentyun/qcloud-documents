## Change Billing Method
Tencent Cloud provides a variety of billing methods. You can switch between Bill-by-bandwidth and Bill-by-traffic in the console, but for each CVM, switching between the two methods can only be performed twice at most.
Billing description: [Overview of Billing Methods for Public Network](https://cloud.tencent.com/document/product/213/10578) 
## Adjustment for Public Network
Tencent Cloud provides two types of network configurations: exclusive public network and shared public network. The shared public network service is billed by bandwidth. You need to submit a ticket to apply for activating it. For more information about the billing methods, please see [Billing of Shared Public Network](https://cloud.tencent.com/document/product/213/10580). This document mainly describes the adjustment between exclusive public networks. For more information about the billing methods, please see [Billing of Exclusive Public Network](https://cloud.tencent.com/document/product/213/10579).

#### Bill-by-bandwidth for prepaid CVMs
This billing method supports adjusting network bandwidth. You can upgrade the bandwidth within the prepaid period, but cannot degrade the bandwidth.

#### Bill-by-bandwidth for postpaid CVMs
This billing method supports adjusting (upgrading or degrading) bandwidth at any time. If the bandwidth is changed several times during an hour, the billing is based on the highest bandwidth tier.

#### Bill-by-traffic
This billing method supports adjusting (upgrading or degrading) the bandwidth cap at any time and the change takes effect in real time.
>This billing method can be used for both prepaid and postpaid CVMs.

#### Bandwidth cap
The options vary with different payment methods and CVM configurations. For more information, please see [Bandwidth Cap of Public Network](https://cloud.tencent.com/document/product/213/12523).

## Procedure
1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/index), select the instance for which you want to change the network configuration, and then click **More** -> **CVM settings** -> **Adjust network**.

2. In the **Adjust network** popup page, you can change the billing method and bandwidth cap.

3. Click **OK**.

