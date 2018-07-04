1) Log in to the Tencent Cloud console, and select **Cloud Object Storage**.

2) Click the **Create Bucket** button in the **Bucket List** tab to create a new COS Bucket.

3) Configure the name of COS Bucket, such as `testbucket`, and set the region to `South China`, access permission to default `public read and private write`, CDN acceleration to default `Disabled`, and click **OK** to create a new COS Bucket.

4) Navigate to **SCF** in the console, and click **Create Function** under the region `Guangzhou` to enter the page for creating a new function.

5) Enter `DownloadImage` as the function name and leave all other configuration options unchanged.

6) Click **Next** to enter the page for editing function codes, and then select default **Online Edit**, and the `COS Put Object` template in **Template**. At this time, the default values in the template will be entered for the execution method and the code:

Execution method is `index.main_handler`. SCF console stores this code in an `index.py` file automatically, and compresses and uploads the file to the SCF platform to create a SCF.

The following code snippets are displayed in the function code: Replace the parameter field `appid, secret_id, secret_key, and region` with your actual data. Notes:

- appid can be found in **Account Information** in the console.
![](https://main.qcloudimg.com/raw/b4422964e268056ab17411bfa353f37a.png)
- secret_id and secret_key can be obtained from **Cloud API Key** in the console.
![](https://main.qcloudimg.com/raw/b2938e290b4bd9a345724cd6021edd20.png)
- region is the region in which the function and COS Bucket reside. `sh, gz, and bj` are supported. Note: The function must be in the same region with COS Bucket. The storage bucket created in the first step resides in South China (Guangzhou), so the region value in the code must be `gz`.

```
import json
import urllib
import commands
import logging
from qcloud_cos import CosClient
from qcloud_cos import DownloadFileRequest
print('Loading function')
appid = 1251111111  #please change to your appid. Find it in Account Info
secret_id = u'AKIDYDh085xQp48161uOn2CKKVbeebvDu9Ib'   #please change to your API secret id. Find it in API secret key pair
secret_key = 'lLkxx40kIfuyqW0IOI0WqyueCYjlgzqE'  #please change to your API secret key. Find it in API secret key pair
region = u'gz'  
def main_handler(event,context):
    logger = logging.getLogger()
    bucket = event['Records'][0]['cos']['cosBucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['cos']['cosObject']['key'].encode('utf8'))
    try:
        cos_client = CosClient(appid, secret_id, secret_key, region)
        request = DownloadFileRequest(bucket, key, '/tmp'+key)
        download_file_ret = cos_client.download_file(request) 
        if download_file_ret['code'] == 0:
            logger.info("Download file [%s] Success" % key)
            logger.info("find local file:" + commands.getoutput('ls /tmp'))
            return "download success"
        else:
            logger.error("Download file [%s] Failed, err: %s" % (key, download_file_ret['message']))
            return -1
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure the object exists and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


```

7) Click **Next** to enter the trigger method page. Click **Create Trigger Method** to add a new trigger for the function. Set the trigger method to **COS Trigger**, select the `testbucket` storage bucket you just create, and the `File Upload` for the event type, and then click **Save**.

8) Click **Complete** at the bottom. At this point, the console generates a code package automatically and uploads it to the SCF platform to create a SCF. Click the `DownloadImage` function you just create in the SCF list page to enter the SCF details page.


