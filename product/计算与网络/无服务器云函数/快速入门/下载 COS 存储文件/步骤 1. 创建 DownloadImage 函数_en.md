1) Log in to Tencent Cloud console, and select "Cloud Object Storage".

2) Click "Create Bucket" button in the "Bucket List" tab to create a new COS Bucket.

3) Configure the name of COS Bucket, such as `testbucket`, and set the region to `South China`, access permission to default `public read and private write`, CDN acceleration to default `Disabled`, and click "OK" button to create a new COS Bucket.

4) Navigate to "SCF" in the console, and click "Create Function" button under the region `Guangzhou` to enter the page for creating new function.

5) Enter the function name as `DownloadImage` and leave all other configuration options unchanged.

6) Click "Next" button, to enter function code edit page, select default "Online Edit", and select `COS Put Object` template in "Template". At this time, execution method and code will be entered with the default values in template:

Execution method is `index.main_handler`. SCF console stores this piece of code as `index.py` file automatically, and uploads the file that is compressed to SCF platform to create cloud function.

The following code fragments are displayed in the function code. Replace the parameter field `appid, secret_id, secret_key, region` with your actual data. Note:

- appid can be found in "Account Information" in the console.
![](//mc.qcloudimg.com/static/img/8149e0d15b64340c2a2dca5569854af8/image.png)
- secret_id and secret_key can be obtained from "Cloud API Secret Key" in the console.
![](//mc.qcloudimg.com/static/img/e1eecfe7459069d0f453083ff459e30e/image.png)
- "region" is the region in which function and COS Bucket reside. `sh, gz, bj` are supported. Please note that, the function must be in the same region with COS Bucket. The storage bucket created in the first step resides in South China (Guangzhou), so the region value in the code must be `gz`.

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

7) Click "Next" button to enter triggering method page. Click "Create Triggering Method" button to add a new trigger for the function. Set the triggering method to "COS Trigger", choose the `testbucket` storage bucket you just created, select `File Upload` for the event type, and click "Save" button.

8) Click "Complete" button at the bottom. At this point, the console will generate a code package automatically and upload it to SCF platform to create cloud function. Click the `DownloadImage` function you just created in the cloud function list page, to enter the cloud function details page.


