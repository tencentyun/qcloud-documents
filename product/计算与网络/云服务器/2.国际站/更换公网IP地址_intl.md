The public network IP of the instance can be replaced by binding and unbinding the EIP. After the EIP is bound, the original public network IP will be lost and cannot be retrieved. After the EIP is released, a new free public IP will be assigned to complete the public IP replacement.

> **Note:**
> Release the unbound EIP as soon as possible if you no longer use it. Otherwise, you will be billed for the idle EIP. The released EIP cannot be retrieved. For more information, please see [Billing Method](https://cloud.tencent.com/document/product/215/11145).

## Binding an EIP
1. Log in to Tencent Cloud, enter the CVM [management page](https://console.cloud.tencent.com/cvm/index) of the CVM console, and click **More** -> **IP Operation** -> **Bind EIP**.
![](https://main.qcloudimg.com/raw/d9c315bdbc0ddb0355794b2bf255ab2c.png)
2. After confirming the information in the pop-up box, click **Convert**.
![](https://main.qcloudimg.com/raw/1dee2e6fae92713aec29669c8b13e63d.png)
3. The EIP converted successfully is shown as below:
![](https://main.qcloudimg.com/raw/7dfeb52aaf8d2378678e902813cd8644.png)

> **Note:**
> It is recommended to bind the applied EIP with the CVM immediately. Otherwise, you will be billed for the idle EIP. For more information on billing, please see [Billing Method](https://cloud.tencent.com/document/product/215/11145).

## Unbinding EIP
1. To convert the EIP back to public network IP, click **More** -> **IP Operation** -> **Unbind EIP**.
![](https://main.qcloudimg.com/raw/9caabaf86b4b0a8ce5531c00feb3f96c.png)
2. In the pop-up box, select **Assign Public IP for Free after Unbinding**, and click **OK** to unbind the EIP.
![](https://main.qcloudimg.com/raw/0bd483df02504e6bb5eeb6e08e70aa20.png)

## Releasing EIP
1. Click **Elastic Public IP** on the navigation bar on the left side to go to the Elastic Public IP Management page. Select the target EIP, and click **Release** in the Action column.
![](https://main.qcloudimg.com/raw/ed50aea2f759bfc0b687770f1fffaba5.png)
2. Confirm the information in the pop-up box, and click **OK** to release the EIP.
![](https://main.qcloudimg.com/raw/7dfded2b053f6def4aa9292076c0e019.png)

