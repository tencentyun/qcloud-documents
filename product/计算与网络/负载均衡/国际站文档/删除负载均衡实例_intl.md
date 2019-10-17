After you confirm that a load balancer instance has no traffic and it is no longer needed, you can delete the instance via the Load Balance console or API.
After the instance is deleted, it will be completely terminated and cannot be restored. It is strongly recommend to unbind all the backend CVMs and wait for a period of time before deleting any instance.

## Deleting a Load Balancer Instance Through the Console
1. Log in to [CLB Console](https://console.cloud.tencent.com/loadbalance).
2. Find the load balancer instance you want to delete and click **Delete** in the right operation column.
 ![Delete](https://main.qcloudimg.com/raw/2fc0b28b647b407aa18dd7de84433283.png)
3. A dialog box pops up for you to confirm the operation. After verifying that the operation safety alert is normal, click **Confirm** to delete the instance.
The confirmation dialog box is shown in the figure below. Be sure to confirm that the number of CVMs is **0**, the CVM is **None**, and the operation safety alert is **Green** before the deletion.
 ![Confirmation Dialog Box](https://main.qcloudimg.com/raw/2b020108a681132192abf9566a8abf65.png)
>**Note:**
> Prepaid instances cannot be deleted. You can choose not to renew the instance after it expires.

## Deleting a Load Balancer Instance Through the API
For more information on the steps, please see [Delete Load Balancer](https://cloud.tencent.com/document/api/214/1257).

