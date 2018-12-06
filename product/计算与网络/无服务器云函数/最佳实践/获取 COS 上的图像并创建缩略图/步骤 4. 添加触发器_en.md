If you complete "Step 3: Create CreateThumbnailDemo Function and Test", and the test result meets the expectation, you can add COS configuration so that COS can publish event to SCF and call the function.

1) In the details page of CreateThumbnailDemo function you just created, select "Trigger Method" tab, and click "Add Trigger Method" button.

2) Select COS trigger for the trigger method, `mybucket` created in "Step 1: Prepare COS Bucket" for COS Bucket, `File Upload` for the event type, and click "Save" button.


Now you have completely implemented this example. You can test the configuration by following the steps below:

1. Go to [COS Console](https://console.cloud.tencent.com/cos4/index), select `mybucket`, upload a .jpg or .png picture, and check whether a file with the same name exists in `mybucketresized` after a certain period of time.
2. You can monitor the function activities in [SCF Console](https://console.cloud.tencent.com/scf), and select "Log" to check the logs in which the calling of the function is recorded.

