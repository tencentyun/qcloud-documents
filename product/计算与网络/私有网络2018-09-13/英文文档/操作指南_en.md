## Creating Flow Logs
1. Log in to Tencent Cloud Console, select [Virtual Private Cloud](https://console.cloud.tencent.com/vpc) tab, and then select **Flow Logs**.
>**Note:** Flow Logs is under internal trial. [You can apply for it now](https://cloud.tencent.com/act/apply/VPCFlowLogs).

2. Click the **New** button at the upper left corner, and enter or confirm the following parameters in the pop-up box:
Collection Type: Specify that the traffic rejected/accepted by security groups or ACL, or all traffic should be captured by the flow log.
Logset: Specify the storage set of the flow log in CLS.
Topic: Specify the minimum dimension of log storage, which is used to distinguish different types of logs, such as logs of accepted traffic.

3. After selection, click **OK** to complete the creation of the flow log.
>**Note:**
>- It takes about 15 minutes to create a flow log for the first time (10 minutes for window capture, and 5 minutes for data pushing). After the creation is completed, you can view it in CLS.
>- The Flow Logs service is free of charge, but the data stored in CLS is charged according to the [standards](https://cloud.tencent.com/document/product/614/11323) set for CLS.


## Deleting Flow Logs
1. Log in to Tencent Cloud Console, select [Virtual Private Cloud](https://console.cloud.tencent.com/vpc), and then select **Flow Logs**.
2. Select the flow log to be deleted, and click the **Delete** button to delete it.
>**Note:**The logset and topic are not deleted together with the flow log.


## Viewing Flow Log Records
You can view flow logs in CLS to quickly locate business issues. You can select multiple topics in the same logset to perform cross-topic query. For more information, please see [Log Index](https://cloud.tencent.com/document/product/614/12504).

