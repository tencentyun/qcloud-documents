Test the `DownloadImage` function you just create by following the steps below.

## Using COS to Upload Files for Testing
1. Log in to the Tencent Cloud console, navigate to **Cloud Object Storage**, select the `TestBucket` Bucket created in Step 1 in the Bucket list, and click the **Upload files** button to upload a [sample image: testimage.jpeg](https://mc.qcloudimg.com/static/img/e683e8627510ec92344329c5219c1939/testimage.jpeg). You can download this image to a local machine for testing.

2. Navigate to **SCF**, and select `DownloadImage` you just created.

3. Click **Log**, and check whether the function execution log of the image you just update is generated. The log of the image downloaded to the local machine should be included, such as:

```
Loading function
Uri is http://TestBucket-1251111111.cosgz.myqcloud.com/testimage.jpeg?sign=QlEyq+WH8g5RpD+L6sPk05XhVQthPTEyNTE3NjIyMjcmaz1BS0lEWURoMDg1eFFwNDgxNjF1T24yQ0tLVmJlZWJ2RHU2ak8mZT0xNDk2ODM5NDQ3JnQ9MTQ5NjgzOTE0NyZyPTk1NDI3NjgyNCZmPS8xNDcyNjQwNzgwXzg0X3cxNjE0X2g0NDAucG5nJmI9ZG9uZ3l1YW50ZXEE
Starting new HTTP connection (1): TestBucket-1251111111.cosgz.myqcloud.com
http://TestBucket-1251111111.cosgz.myqcloud.com:80 "GET /testimage.jpeg?sign=QlEyq+WH8g5RpD+L6sPk05XhVQthPTEyNTE3NjIyMjcmaz1BS0lEWURoMDg1eFFwNDgxNjF1T24yQ0tLVmJlZWJ2RHU2ak8mZT0xNDk2ODM5NDQ3JnQ9MTQ5NjgzOTE0NyZyPTk1NDI3NjgyNCZmPS8xNDcyNjQwNzgwXzg0X3cxNjE0X2g0NDAucG5nJmI9ZG9uZ3l1YW50ZXEE HTTP/1.1" 200 62296
Download file [/testimage.jpeg] Success
testimage.jpeg
```

## Manual Simulation Test
You can view the function's running status by entering the test data, such as COS trigger.

1) In the Test Function pop-up box, select `Upload File to COS/Delete File from COS Test Code` from test templates, and the following data will appear in the window. The following modifications are required:

 - Replace `name` in `cosBucket` with `TestBucket` you just created.
 - Replace `key` in `cosObject` with `\testimage.jpeg` you just uploaded.

As shown below:
```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"cos:ObjectCreated:*,
          "eventTime":"1970-01-01T00:00:00.000Z",
          "eventQueue":"qcs:0:cos:gz:1251111111:cos",
          "requestParameters":{
            "requestSourceIP": "111.111.111.111",
            "requestHeaders":{
              "Authorization": "Example"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"Configured or returned ID",
            "cosBucket":{  
               "name":"TestBucket", # Notice Here
               "appid":"1251111111",
               "region":"gz",
            },
            "cosObject":{  
               "key":"/testimage.jpg", # Notice Here
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
2) Click **Run**, and the code starts running and the test result is displayed. Notes:
 - The running result and the function execution result returned by `return` statement in the code will appear in the function return value.
 - The execution time of the function and memory will appear in the running information.
 - Logs generated during the function execution will appear in the log, including print statement in user codes and trace stack for function execution failure, and will be written in the log module.

3) You can run the code several times, and click the **Log** tab to check the log information of each run.

