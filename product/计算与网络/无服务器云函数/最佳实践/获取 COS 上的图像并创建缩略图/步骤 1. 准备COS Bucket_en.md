Make sure you have obtained the permission to use SCF before implementing this example. Click [here](https://cloud.tencent.com/act/apply/SCF) to apply for the permission for internal trial

```
Note:
1. Source Bucket, target Bucket and function must reside in the same region. In this tutorial, South China (Guangzhou) region is used.
2. Two COS Buckets are required. If you use the same Bucket as both source and target buckets, each thumbnail uploaded to source bucket may trigger function again, therefore unnecessary recursion is generated.
```
1) Log in to Tencent Cloud console, and select "Cloud Object Storage".

2) Click "Create Bucket" button in the "Bucket List" tab to create a new source COS Bucket.

3) Configure the name of COS Bucket, such as `mybucket`, and set the region to `South China`, access permission to default `Public read and private write`, CDN acceleration to default `Disabled`, and click "Save" button to create a new COS Bucket.

4) Create target Bucket `mybucketresized` in the same way.

5) Upload any image file to source Bucket (i.e. mybucket). In this example, we use an image [HappyFace.png](https://mc.qcloudimg.com/static/img/eae5118ed07d95ac2837f000f1ab96e5/HappyFace.png) for demonstration. (Before COS is associated, when manually calling function to perform test and verification, you need to pass the sample data that contains this file to SCF, so that SCF can locate corresponding file according to this data. Therefore, you first need to create this sample object.)
![](//mc.qcloudimg.com/static/img/2f0c6645ff3b8097a4791e758facf4a7/image.png)

