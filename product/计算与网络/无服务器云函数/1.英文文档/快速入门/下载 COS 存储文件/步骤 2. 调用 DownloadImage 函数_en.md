Test `DownloadImage` function you just created by following the steps below.

## Using COS to Upload Files for Testing
1. Log in to Tencent Cloud console, navigate to "Cloud Object Storage", select `TestBucket` Bucket created in the first step in the Bucket list, and click "File Upload" button to upload a [sample image: testimage.jpeg](https://mc.qcloudimg.com/static/img/e683e8627510ec92344329c5219c1939/testimage.jpeg). You can download this image to a local machine for testing.

2. Navigate to "SCF", and select `DownloadImage` you just created.

3. Click "Log" tab, and check whether the function execution log of the uploaded image is generated. The log should contain the log of the image downloaded locally, such as:

```
Loading function
Uri is http://TestBucket-1251111111.cosgz.myqcloud.com/testimage.jpeg?sign=QlEyq+WH8g5RpD+L6sPk05XhVQthPTEyNTE3NjIyMjcmaz1BS0lEWURoMDg1eFFwNDgxNjF1T24yQ0tLVmJlZWJ2RHU2ak8mZT0xNDk2ODM5NDQ3JnQ9MTQ5NjgzOTE0NyZyPTk1NDI3NjgyNCZmPS8xNDcyNjQwNzgwXzg0X3cxNjE0X2g0NDAucG5nJmI9ZG9uZ3l1YW50ZXEE
Starting new HTTP connection (1): TestBucket-1251111111.cosgz.myqcloud.com
http://TestBucket-1251111111.cosgz.myqcloud.com:80 "GET /testimage.jpeg?sign=QlEyq+WH8g5RpD+L6sPk05XhVQthPTEyNTE3NjIyMjcmaz1BS0lEWURoMDg1eFFwNDgxNjF1T24yQ0tLVmJlZWJ2RHU2ak8mZT0xNDk2ODM5NDQ3JnQ9MTQ5NjgzOTE0NyZyPTk1NDI3NjgyNCZmPS8xNDcyNjQwNzgwXzg0X3cxNjE0X2g0NDAucG5nJmI9ZG9uZ3l1YW50ZXEE HTTP/1.1" 200 62296
Download file [/testimage.jpeg] Success
testimage.jpeg
```

## Manual Simulation Test
You can also observe the function's running statuses by manually entering test data similar to COS trigger.

1) In the pop-up of testing function, select `Upload File to COS/Delete File from COS Test Code` from test templates, and the following data will appear in the window. The following modifications are required:

 - Replace `name` in `cosBucket` with `TestBucket` you just created;
 - Replace `key` in `cosObject` with `\testimage.jpeg` you just uploaded;

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
2) Click "Run" button, and the code starts running and displays test result. Note:
 - The running result and the function execution result returned by `return` statement in the code will appear in the function return value.
 - The execution time, memory and other information of the function will appear in running information
 - Logs generated during the execution of function will appear in the log, including print statement in user code, trace stack for function execution failure, and so on, and will be written in the log module.

3) You can run the code a couple of times, and click "Log" tab to check the log information of each run.
