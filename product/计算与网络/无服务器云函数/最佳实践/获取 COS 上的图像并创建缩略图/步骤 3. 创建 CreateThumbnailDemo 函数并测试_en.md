In this section, you will create a function to implement thumbnail program, and test the function through the console or by calling API.

## Creating CreateThumbnailDemo SCF
1) Log in to [SCF Console](https://console.cloud.tencent.com/scf). Select **Guangzhou** from the region list, and click **New**.

2) In function configuration section, enter the function name as `CreateThumbnailDemo`, leave all other configuration options unchanged, and then click **Next**.

3) Go to the function code section, and click **Upload local zip file**. Enter the execution method as `CreateThumbnail.main_handler`, select `CreateThumbnailDemo.zip` created in "Step 2: Create Deployment Package", and click "Next".

4) Go to the trigger method section. Now you need to manually test the function, so no trigger method is added currently. Click "Complete" button.

## Testing CreateThumbnailDemo SCF
When a function is created, it is generally tested through the console or API, to ensure the function output meets the expectation, and then you can bind it to a trigger for practical application.

1) In the details page of CreateThumbnailDemo function you just created, click "Test" button.

2) Select "Upload File to COS/Delete File from COS Test Code" from the drop-down list of test templates.

3) A slight changes on the test code are required: set `name` to the name of bucket `mybucket` created in "Step 1: Prepare COS Bucket", and set `key` to the key value of `/HappyFace.jpg` uploaded in "Step 1: Prepare COS Bucket", as shown in the example below:
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

4) Click "Run" button to observe the result. This program is running normally if both upload and download are successful in the result:
![](//mc.qcloudimg.com/static/img/aec9243fd45a41e562b9c17d530740a0/image.png)

5) Go to [COS Console](https://console.cloud.tencent.com/cos4/index), and click `mybucketresized` created in "Step 1: Prepare COS Bucket", to check whether a thumbnail named `HappyFace.png` is generated.
![](//mc.qcloudimg.com/static/img/5c4224adcef4231f1469956107f000aa/image.png)

6) Download the picture and compare it with the size of original picture.
