Make sure you have obtained the permission to use SCF before implementing this example.

1) Log in to the Tencent Cloud console, and select **Cloud Object Storage**.

2) Click the **Create Bucket** button in the **Bucket List** tab to create a source COS Bucket.

3) Configure the name of COS Bucket, such as `srcmr`, and set the region to `South China`, access permission to default `Public read and private write`, and CDN acceleration to default `Disabled`, and click the **Save** button to create a COS Bucket.

4) Create the intermediate Bucket `middlestagebucket` and target Bucket `destmr` in the same way.

5) Upload a text file to the source Bucket (i.e. srcmr). In this example, we use a text file [Serverless.txt](	http://srcmr-1251740579.cosgz.myqcloud.com/serverless.txt) for demonstration. (Before COS is associated, when manually calling the function to perform test and verification, you need to pass the sample data that contains this file to SCF, so that SCF can locate corresponding file according to this data. Therefore, you first need to create this sample file.)

![](https://main.qcloudimg.com/raw/190b51d8a914871e48f609d2665b17ae.png)

