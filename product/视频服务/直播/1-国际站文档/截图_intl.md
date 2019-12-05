### How to Activate
1. You can take screenshots of LVB channels through the API. For more information on how to use API for creating screenshot task, please see [Create Screenshot Task](https://cloud.tencent.com/document/product/267/4726). To end a screenshot task in time, use the API for ending screenshot task. For more information, please see [End Screenshot Task](https://cloud.tencent.com/document/product/267/4727).
2. You can also start a screenshot task on the console (recommended).
![](https://main.qcloudimg.com/raw/1619cdd771130c5b4cce0788f568546f.png)

>**Note:**
> Due to historical reasons, for some registered customers, the screenshots are stored in the COS platform. Therefore, before using the screenshot feature, these users need to activate COS service in advance and purchase space and traffic for storing and downloading screenshot files. Now, the screenshot feature has been optimized for Tencent Cloud LVB service. Customers can directly activate screenshot feature instead of activating COS service.

### Querying Screenshots
You can get screenshot information by using the queue query API. The queue query API must be enabled separately. You can submit a request through the after-sales QQ number 514025596 to enable the API. You can send the request by simply indicating that "Request to enable the LVB screenshot query queue API service" as well as the account information in the message. The service is enabled within one work day.

**Specifications:**
1. Screenshots are captured based on the original LVB bitrate. The frequency is one screenshot every 10 seconds, which is fixed and cannot be modified.
2. The output format is JPG.
3. When the task starts, you can get the screenshot file after 20 seconds upon the start of LVB process.
4. **Note:** Fees for the screenshot file are generated in the COS platform. Pay attention to the relevant costs based on your actual needs. For more information on billing methods, please see [Cloud Object Storage](http://cloud.tencent.com/product/cos.html).
