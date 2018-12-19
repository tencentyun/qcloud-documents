To use BM LB, you need to create an first.
## Creating LB
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
![](https://mc.qcloudimg.com/static/img/a6743dde4ff6a77a4ba2034f28f97445/image.png)
2. Click the **New** button at the upper left corner of the BM Load Balancer page.
![](https://mc.qcloudimg.com/static/img/1340eaddfd9d1611ca56c1fd9c66de7c/image.png)
3. Check the following parameters in the pop-up window and click **Purchase Now** to complete the creation of LB.
 - Region
 - Instance type
 - VPC where the LB resides
 - Network billing method
 - Quantity
![](https://mc.qcloudimg.com/static/img/1316d20eb93c257ddb384358c0802d92/image.png)

## Creating Listeners
After the LB is created, you can create listeners, including Layer-4 and Layer-7 listeners.

### Layer-4 Listener
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
2. Select the LB instance type (including public network generic LB, public network enhanced LB and private network LB). Click the ID of the LB in the LB list page to enter the LB details page.
![](https://mc.qcloudimg.com/static/img/a7bda427fbb40fa1c226170a35466993/image.png)
3. Select **Layer-4 Listener** in the LB details page, and click **New**, and make configurations by following step a, b, c below. Then click **OK** to complete the Layer-4 listener creation.
 a. Enter the listener name, protocol, port, and peak bandwidth (if the instance is billed by fixed bandwidth) in **Basic Configuration**.
 b. Select response timeout, check interval, unhealthy threshold, and healthy threshold in **Health Check**.
 c. Select persistence duration in **Session Persistence**.
![](https://mc.qcloudimg.com/static/img/a0dcf2eedb3ad64d4e26909599ceaf09/image.png)

### Layer-7 Listener
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
2. Select the LB instance type (including public network generic LB, public network enhanced LB and private network LB). Click the ID of the LB in the LB list page to enter the LB details page.
![](https://mc.qcloudimg.com/static/img/a7bda427fbb40fa1c226170a35466993/image.png)
3. Select **Layer-7 Listener** in LB details page, and click **New**, and then enter the listener name, protocol, port and peak bandwidth (if the instance is billed by fixed bandwidth), and click **OK**.
![](https://mc.qcloudimg.com/static/img/3e759ce2ea572290c712d6d337888429/image.png)
4. In the pop-up window, click **Add Forwarding Domain Name and URL**, and make the configurations by following step a, b, c below, and then click **OK** to complete the Layer-7 listener creation.
  a. Enter the forwarding domain name, URL and balancing mode in **Basic Configuration**.
  b. Enter the domain name, check directory, check interval, unhealthy threshold, healthy threshold, and HTTP status code check in **Health Check**.
  c. Select persistence duration in **Session Persistence**.
	![](https://mc.qcloudimg.com/static/img/c82b47666eda585de94b2d171391052d/image.png)
	
> **Note:**
> Layer-7 listener is not supported for public network enhanced LB.

## Binding a CPM
After the listeners are created, you can bind a CPM.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
2. Select the LB instance type (including public network generic LB, public network enhanced LB and private network LB) Click the ID of the LB in the LB list page to enter the LB details page.
![](https://mc.qcloudimg.com/static/img/a7bda427fbb40fa1c226170a35466993/image.png)
3. Click **Layer-4 Listeners** or **Layer-7 Listeners** in LB details page to enter the binding page and click **Bind**.
![](https://mc.qcloudimg.com/static/img/cf52bb7fcdb0f98a1fa45565563e8d32/image.png)
4. In the pop-up window, select the CPM to bind, configure the backend port and weight, and then click **OK** to complete the binding of the CPM.
![](https://mc.qcloudimg.com/static/img/d08f66eb31e8ad6fc92a8a135226d835/image.png)

## Viewing LB Listener Monitor
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
2. Select the LB instance type (including public network generic LB, public network enhanced LB and private network LB). Click the ID of the LB in the LB list page to enter the LB details page.
![](https://mc.qcloudimg.com/static/img/a7bda427fbb40fa1c226170a35466993/image.png)
3. Select **Monitor** tab in LB details page to enter the monitoring page. Select the listener and time to check the monitoring details.
![](https://mc.qcloudimg.com/static/img/305e3b3bcb4b84e439a8c614afead327/image.png)

## Deleting LB
An LB can be deleted when it is not needed.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Go to **Cloud Products** -> **BM Load Balancer**.
2. Select the LB instance type (including public network generic LB, public network enhanced LB and private network LB) Click the **Delete** button in the line where the LB to be deleted resides, and click **OK** to complete deletion.
![](https://mc.qcloudimg.com/static/img/8cfef1cbcae8aa04a7e97a693a93b4db/image.png)

