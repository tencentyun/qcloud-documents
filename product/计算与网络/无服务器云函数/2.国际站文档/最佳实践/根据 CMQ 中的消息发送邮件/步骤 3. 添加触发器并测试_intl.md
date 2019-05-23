If you complete "Step 2: Create sendEmail Function and Test", and the test result meets the expectation, you can add a CMQ Topic trigger configuration so that the CMQ Topic can send message events to the SCF and call the function.

1. In the details page of the sendEmail function you just created, click the **Triggering Method** tab and click **Add trigger mode**.

2. Select **CMQ topic subscription trigger**, and `sendEmailQueue` created in [Step 1: Create a CMQ Topic](https://cloud.tencent.com/document/product/583/11696) for the CMQ Topic, and then click **Save**.

![](https://main.qcloudimg.com/raw/f5aeeade06e76dd927f04f99a6620e08.png)

---


In this way, you have completed all steps. You can test the configuration by following the steps below:

1. Go to [Messaging Service CMQ](https://console.cloud.tencent.com/mq). Select **Subscribe Topic** in the left navigation pane, find the created `sendEmailQueue` queue from the list, and click `Send MSG` in the Operation column of the queue. Enter the following message in the popup window:
You can modify the message content as needed, including "fromAddr", "toAddr", "title", and "body".
```
{
  "fromAddr":"xxx@qq.com",
  "toAddr":"xxx@qq.com",
  "title":"hello from scf & cmq",
  "body":"email content to send"
}
```

2. Monitor the activities of the `sendEmail` function you created in the [Serverless Cloud Function Console](https://console.cloud.tencent.com/scf) and select **Logs** to check the logs in which the calling of the function is recorded.

3. Log in to your receiving mailbox and check whether the email is received and the email content is correct.

After the test, you can embed the CMQ SDK in your application codes and send the message defined in the example to the `sendEmailQueue` queue to send the email.

