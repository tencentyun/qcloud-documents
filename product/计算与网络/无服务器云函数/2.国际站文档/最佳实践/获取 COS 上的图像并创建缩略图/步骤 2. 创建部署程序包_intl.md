```
The version of image used in SCF underlying container environment is CentOS 7.2. Therefore, in this example, the Linux example is implemented under the CentOS 7.2 environment. Please make proper adjustments if your local environment is one of other released Linux versions.
```
## Creating Picture Processing Code
1) Create a directory
If the local environment is Windows, you can create a new folder named CreateThumbnail in any location.
If the local environment is Linux, you can create a new folder named CreateThumbnail in any location, as shown below:

![](http://mc.qcloudimg.com/static/img/a6999a456a083698490381246da19ac2/image.png)

2) Open text editor and enter the following code.
Note: Replace `appid, secret_id, secret_key, and region` with your actual data, where:
- appid can be found in **Account Information** in the console.

![](https://main.qcloudimg.com/raw/b4422964e268056ab17411bfa353f37a.png)

- secret_id and secret_key can be obtained from **Cloud API Key** in the console.

![](https://main.qcloudimg.com/raw/b2938e290b4bd9a345724cd6021edd20.png)
- region is the region in which the function and COS Bucket reside. `sh, gz, and bj` are supported. Note: The region must be the same with that of COS Bucket created in the previous step. The bucket created in "Step 1: Prepare COS Bucket" resides in South China (Guangzhou), so the region value in the code must be `gz`.

```
import uuid
import json
import os
import logging
from PIL import Image
import PIL.Image
import commands
import datetime
import urllib
from qcloud_cos import CosClient
from qcloud_cos import DownloadFileRequest
from qcloud_cos import UploadFileRequest


print('Loading function')
appid = 1251762222  #please change to your appid. Find it in Account Info
secret_id = u'AKIDYDh085xQp48161uOn2CKKVbeebvDu6j2'   #please change to your API secret id. Find it in API secret key pair
secret_key = u'lLkxx40kIfuyqW0IOI0WqyueCYjlgZQ2'  #please change to your API secret key. Find it in API secret key pair
region = u'gz' 

cos_client = CosClient(appid, secret_id, secret_key, region)
logger = logging.getLogger()

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)

def delete_local_file(src):
    logger.info("delete files and folders")
    if os.path.isfile(src):
        try:  
            os.remove(src)  
        except:  
            pass 
    elif os.path.isdir(src):  
        for item in os.listdir(src):  
            itemsrc=os.path.join(src,item)  
            delete_file_folder(itemsrc)  
        try:  
            os.rmdir(src)  
        except:  
            pass     
     
def main_handler(event, context):
    logger.info("start main handler")
    for record in event['Records']:
        try:
            bucket = record['cos']['cosBucket']['name']
            cosobj = record['cos']['cosObject']['key']
            cosobj = cosobj.replace("/"+str(appid)+"/"+bucket,"")
            key = urllib.unquote_plus(cosobj.encode('utf8'))
            download_path = '/tmp/{}{}'.format(uuid.uuid4(), key.strip('/'))
            upload_path = '/tmp/resized-{}'.format(key.strip('/'))
            print("Get from [%s] to download file [%s]" %(bucket,key))
           
            # download image from cos
            request = DownloadFileRequest(bucket, key, download_path)
            download_file_ret = cos_client.download_file(request)
            if download_file_ret['code'] == 0:
                logger.info("Download file [%s] Success" % key)
                logger.info("Image compress function start")
                starttime = datetime.datetime.now()
                    
                #compress image here
                resize_image(download_path, upload_path)
                endtime = datetime.datetime.now()
                logger.info("compress image take " + str((endtime-starttime).microseconds/1000) + "ms")
                    
                #upload the compressed image to resized bucket
                request = UploadFileRequest(u'%sresized' % bucket, key.decode('utf-8'), upload_path.decode('utf-8'))
                upload_file_ret = cos_client.upload_file(request)
                logger.info("upload image, return message: " + str(upload_file_ret))

                #delete local file
                delete_local_file(str(download_path))
                delete_local_file(str(upload_path))
            else:
                logger.error("Download file [%s] Failed, err: %s" % (key, download_file_ret['message']))
                return -1
        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. Make sure the object exists and your bucket is in the same region as this function.'.format(key, bucket))
            raise e

```
3) Save the file as `CreateThumbnail.py` in the directory you just created:
![](http://mc.qcloudimg.com/static/img/609faa717c1eefb5dd1c6747dfb99ab1/image.png)
![](http://mc.qcloudimg.com/static/img/66d8a074d8577257880c4713bb8a4c86/image.png)
## Creating a Deployment Package
### For Windows environment
Because the sample program is dependent on Pillow dependent library of Python, to avoid the dependent library installed under your local Windows environment conflicts with that in the platform, we recommend that you:

Click the link to download [Pillow Library](https://mc.qcloudimg.com/static/archive/66534c4192eefc53af8ce3b319c521c9/PIL.zip) directly, and decompress the zip file to the folder CreateThumbnail you just created.

Compress all the files in this folder into a zip file named CreateThumbnailDemo.zip (do not compress the folder): select all files, right-click on them, select a compress software (such as winrar), click **Add to Archive...**, then select the archive format as zip, and click **OK** to generate a zip file named `CreateThumbnailDemo.zip`.


### For Linux environment

```
Note: Assuming that the following steps are performed under CentOS 7.2 environment, if your environment is one of other released Linux versions, modify the instructions according to relevant method of the version, and ensure the Python version is 2.7.
```

1) Install Python environment.

```
sudo yum install python
```

2) Make sure that you have installed a necessary dependent library in the current Linux environment.

```
sudo yum install python-devel python-pip gcc libjpeg-devel zlib-devel python-virtualenv
```

3) Create and activate virtual environment.

```
virtualenv ~/shrink_venv
source ~/shrink_venv/bin/activate
```

4) Install Pillow library under the virtual environment.

```
pip install Pillow
```

5) Add the content related to lib and lib64 into a .zip file (the path is assumed to be `/CreateThumbnailDemo.zip`).

```
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r /CreateThumbnailDemo.zip *
cd $VIRTUAL_ENV/lib64/python2.7/site-packages
zip -r /CreateThumbnailDemo.zip *
```

6) Add the PY file created in the first step to this .zip file.

```
cd /CreateThumbnail
zip -g /CreateThumbnailDemo.zip CreateThumbnail.py
```

