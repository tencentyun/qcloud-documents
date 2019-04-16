If you complete "Step 3: Create CreateThumbnailDemo Function and Test", and the test result meets the expectation, you can add COS configurations so that COS can publish events to SCF and call the function.

1) In the details page of the CreateThumbnailDemo function you just created, select the **Triggering Method** tab, and click **Add trigger mode**.

2) Select COS trigger for the trigger method, `mybucket` created in Step 1: Prepare COS Bucket for COS Bucket, `File Upload` for the event type, and then click **Save**.


In this way, you have completed all steps. You can test the configuration by following the steps below:

1. Go to the [COS Console](https://console.cloud.tencent.com/cos4/index), select `mybucket`, upload a .jpg or .png picture, and check whether a file with the same name exists in `mybucketresized` after a period of time.
2. You can monitor the function activities in the [Serverless Cloud Function Console](https://console.cloud.tencent.com/scf), and select **Logs** to check the logs in which the calling of the function is recorded.

