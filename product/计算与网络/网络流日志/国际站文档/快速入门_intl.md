1. Log in to Tencent Cloud Console, and select [**Virtual Private Cloud**](https://console.cloud.tencent.com/vpc) -> **Flow Logs**.
2. Log in to Tencent Cloud Console, select [**Cloud Log Service**](https://console.cloud.tencent.com/cls/logset) tab, and then create a logset.
3. Log in to Tencent Cloud Console, select [**Virtual Private Cloud**](https://console.cloud.tencent.com/vpc), and then select **Flow Logs**.
4. Click **New** at the upper left corner, and enter or confirm the following parameters in the pop-up box:
"Collection Type" specifies the type of the traffic to be collected by flow logs: the traffic rejected/accepted by security groups or ACL, or all traffic.
"Logset" specifies the storage set of the flow logs in CLS.
"Log Topic" specifies the minimum dimension of log storage, which is used to distinguish different types of logs, such as Accept log.
5. After selection, click **OK** to complete the creation of flow log.
>**Notes:**
>- You can view the records of a newly created flow log in CLS after 15 minutes upon the creation (capture window is 10 minutes, and it takes 5 minutes for data pushing).
>- Flow Logs service itself is free of charge, but the data stored in CLS is charged according to the billing standard of CLS.

After the creation, you can view the flow log and search log data in CLS by keywords. For more information, see [Log Search](https://cloud.tencent.com/document/product/614/12504).

