
The subnet of the CVM instance in VPC can be directly replaced in the console.

## Limits

- The associated CVM restarts automatically after its subnet is replaced.
- The subnet cannot be replaced for the secondary ENI.

## Procedure

- Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/index).
- Select a region.
- Click the ID of the instance to go to its details page.
- On the instance details page, click **ENI**, and then click the ID of primary ENI.
![](https://main.qcloudimg.com/raw/06f216d4a3ba31586e26792dc3788a0c.png)
- Go to the primary ENI details page, and click **Replace Subnet**.
![](https://main.qcloudimg.com/raw/9f3196503a29b23668334dd8a0774bc6.png)
- Select the new subnet in the pop-up subnet replacement page, enter the new primary IP, and click **OK**. Then, the instance restarts to complete the replacement.
![](https://main.qcloudimg.com/raw/4234772c49fb11bc12cd5a35cc4a32c8.png)
>Note:
>
>1. If you have not created a subnet in this availability zone, create a new subnet first.
>2. You can only enter the private IP of the current subnet CIDR.

