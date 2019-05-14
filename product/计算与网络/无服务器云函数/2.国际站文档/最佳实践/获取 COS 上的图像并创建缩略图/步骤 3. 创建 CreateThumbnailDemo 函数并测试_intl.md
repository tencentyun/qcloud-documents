In this section, you will create a function to implement thumbnail program, and test the function through the console or by calling APIs.

## Creating a CreateThumbnailDemo SCF
1) Log in to the [Serverless Cloud Function Console](https://console.cloud.tencent.com/scf). Select **Guangzhou** from the region list and click **Create**.

2) In **Function configuration** section, enter `CreateThumbnailDemo` as the function name, leave all other configuration options unchanged, and then click **Next**.

3) Go to the **Function code** section, and click **Local upload zip file**. Enter `CreateThumbnail.main_handler` as the execution method, select `CreateThumbnailDemo.zip` created in Step 2: Create Deployment Package, and click **Next**.

4) In the **Triggering method** section, you need to test the function manually, so no trigger method is added. Click **Done**.

## Testing the CreateThumbnailDemo SCF
When a function is created, it is generally tested through the console or API, to ensure the function output meets the expectation, and then you can bind it to a trigger for practical application.

1) In the details page of the CreateThumbnailDemo function you just created, click **Test**.

2) Choose **Upload File to COS/Delete File from COS Test Code** from the drop-down list of test templates.

3) In the test code, set `name` to the name of bucket `mybucket` created in "Step 1: Prepare COS Bucket", and set `key` to the key value of `/HappyFace.jpg` uploaded in "Step 1: Prepare COS Bucket", as shown in the example below:

```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"event-type",
          "eventTime":"Unix timestamp",
          "eventQueue":"qcs:0:cos:gz:1251111111:cos",
          "requestParameters":{
            "requestSourceIP": "111.111.111.111",
            "requestHeaders":{
              "Authorization": "Uploaded authentication information"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"Configured or returned ID",
            "cosBucket":{  
               "name":"mybucket", #set to demo bucket here
               "appid":"appId",
               "region":"gz"
            },
            "cosObject":{  
               "key":"/HappyFace.png", #set to demo file here
               "size":"1024",
               "meta":{
                 "Content-Type": "text/plain",
                 "x-cos-meta-test": "Custom meta",
                 "x-image-test": "Custom meta"
               },
               "url": "Origin server URL for accessing files"
            }
         }
      }
   ]
}
```

4) Click **Run** to view the results. This program is running normally if both upload and download are successful in the result。


5) Go to the [COS Console](https://console.cloud.tencent.com/cos4/index), and click `mybucketresized` created in "Step 1: Prepare COS Bucket", to check whether a thumbnail named `HappyFace.png` is generated.
![](https://main.qcloudimg.com/raw/9741d01c1b80393e74faaa250d10a6b2.png)

6) Download the picture and compare it with the size of original picture.

