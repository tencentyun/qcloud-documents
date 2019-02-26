## Creating Mapper Configuration Package
1) Create a new folder named WordCount in any location.

2) Create a new `.py` file named `map_function`, enter the following code in it and save the file. Note: Replace `appid, secret_id, secret_key, region` with your actual data, where:
- appid can be found in "Account Information" in the console.
![](//mc.qcloudimg.com/static/img/8149e0d15b64340c2a2dca5569854af8/image.png)
- secret_id and secret_key can be obtained from "Cloud API Secret Key" in the console.
![](//mc.qcloudimg.com/static/img/e1eecfe7459069d0f453083ff459e30e/image.png)
- "region" is the region in which function and COS Bucket reside. `sh, gz, bj` are supported. Please note that, the region must be the same with that of COS Bucket created in the previous step. The bucket created in "Step 1: Prepare COS Bucket" resides in South China (Guangzhou), so the region value in the code must be `gz`:


```
import mapper_triggered as Mapper
import datetime
from qcloud_cos import CosClient

def map_caller(event, context):
    appid = 1251762222      # change to user's appid
    secret_id = u'AKIDYDh085xQp48161uOn2CKKVbeebvDu6EE'   # change to user's secret_id
    secret_key = u'lLkxx40kIfuyqW0IOI0WqyueCYjlgZEE'  # change to user's secret_key
    region = u'gz'          # change to user's region
    cos_client = CosClient(appid, secret_id, secret_key, region)
    
    bucket = event['Records'][0]['cos']['cosBucket']['name']
    key = event['Records'][0]['cos']['cosObject']['key']
    middle_stage_bucket = u'middlestagebucket'
    middle_file_key = '/' + 'middle_' + key.split('/')[-1]
    
    return Mapper.do_mapping(cos_client, bucket, key, middle_stage_bucket, middle_file_key)

def main_handler(event, context):
    start_time = datetime.datetime.now()
    res = map_caller(event, context)
    end_time = datetime.datetime.now()
    print("data mapping duration: " + str((end_time-start_time).microseconds/1000) + "ms")
    if res == 0:
        return "Data mapping SUCCESS"
    else:
        return "Data mapping FAILED"

```

Upon creation, create a `.py` file named `mapper_triggered` under **the same path**, enter the following code in it and save the file.
```
from qcloud_cos import UploadFileRequest
from qcloud_cos import DownloadFileRequest
import re
import os
import logging


logger = logging.getLogger()

#delete folders and files
def delete_file_folder(src):
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

# Download files
def download_file(cos_client, bucket, key, local_file_path):
    request = DownloadFileRequest(bucket, key, local_file_path)
    download_file_ret = cos_client.download_file(request) 
    if download_file_ret['code'] == 0:
        logger.info("Download file [%s] Success" % key)
        return 0
    else:
        logger.error("Download file [%s] Failed, err: %s" % (key, download_file_ret['message']))
        return -1

#  Upload file to bucket
def upload_file(cos_client, bucket, key, local_file_path):
    request = UploadFileRequest(bucket.decode('utf-8'), key.decode('utf-8'), local_file_path.decode('utf-8'))
    upload_file_ret = cos_client.upload_file(request)
    if upload_file_ret['code'] == 0:
        logger.info("Upload data map file [%s] Success" % key)
        return 0
    else:
        logger.error("Upload data map file [%s] Failed, err: %s" % (key, upload_file_ret['message']))
        return -1

# domapping
def do_mapping(cos_client, bucket, key, middle_stage_bucket, middle_file_key):
    src_file_path = u'/tmp/' + key.split('/')[-1]
    middle_file_path = u'/tmp/' + u'mapped_' + key.split('/')[-1]
    download_ret = download_file(cos_client, bucket, key, src_file_path)  #download src file
    if download_ret == 0:
        inputfile = open(src_file_path, 'r')  #open local /tmp file
        mapfile = open(middle_file_path, 'w') #open a new file write stream
    
        for line in inputfile:
            line = re.sub('[^a-zA-Z0-9]', ' ', line) #replace non-alphabetic/number characters
            words = line.split() 
            for word in words:
                mapfile.write('%s\t%s' % (word, 1)) #count for 1
                mapfile.write('\n') 

        inputfile.close()
        mapfile.close()
    
        upload_ret = upload_file(cos_client, middle_stage_bucket, middle_file_key, middle_file_path) #upload the file's each word
   
        delete_file_folder(src_file_path)
        delete_file_folder(middle_file_path)
        return upload_ret
    else:
        return -1
```

3) If the local environment is Windows, you can find two py files under this path, as shown below:
![](//mc.qcloudimg.com/static/img/c2c6e9eac73d93cd107a03dc31b79e27/image.png)

If the local environment is Linux, you can find two py files under this path, as shown below:
![](//mc.qcloudimg.com/static/img/4effe6d1503990d173823844313c3967/image.png)

Compress these two files into a zip file named mapper (note: you need to compress the files instead of the folder in which these files reside).

Under Windows environment:
Select these two files, right-click on them, select a compress software (such as winrar), click "Add to archive...", then select the archive format as zip, and click "OK" to generate a zip file.
![](//mc.qcloudimg.com/static/img/5543a76b69b40f270036c1d11b47c423/image.png)
![](//mc.qcloudimg.com/static/img/d04fbdf74087eb27f1f438e2528f99b1/image.png)
![](//mc.qcloudimg.com/static/img/f2a51e7876b8521e93ee64f428cc11a9/image.png)

Under Linux environment:
Enter the directory directly to run the command.
```
cd /WordCount
zip mapper.zip map_function.py mapper_triggered.py 
```

## Creating Reducer Configuration Package
1) Similarly, create a `.py` file named `reduce_function` under WordCount directory, enter the following code in it and save the file. Note: Replace `appid, secret_id, secret_key, region` with your actual data, where:
- appid can be found in "Account Information" in the console.
![](//mc.qcloudimg.com/static/img/8149e0d15b64340c2a2dca5569854af8/image.png)
- secret_id and secret_key can be obtained from "Cloud API Secret Key" in the console.
![](//mc.qcloudimg.com/static/img/e1eecfe7459069d0f453083ff459e30e/image.png)
- "region" is the region in which function and COS Bucket reside. `sh, gz, bj` are supported. Please note that, the region must be the same with that of COS Bucket created in the previous step. The bucket created in "Step 1: Prepare COS Bucket" resides in South China (Guangzhou), so the region value in the code must be `gz`:


```
import reducer_triggered as Reducer
import datetime
from qcloud_cos import CosClient

def reduce_caller(event, context):
    appid = 1251762222      # change to user's appid
    secret_id = u'AKIDYDh085xQp48161uOn2CKKVbeebvDu6EE'   # change to user's secret_id
    secret_key = u'lLkxx40kIfuyqW0IOI0WqyueCYjlgZEE'  # change to user's secret_key
    region = u'gz'          # change to user's region
    cos_client = CosClient(appid, secret_id, secret_key, region)

    bucket = event['Records'][0]['cos']['cosBucket']['name']
    key = event['Records'][0]['cos']['cosObject']['key']
    result_bucket = u'destmr'
    result_key = '/' + 'result_' + key.split('/')[-1]
    
    return Reducer.qcloud_reducer(cos_client, bucket, key, result_bucket, result_key)

def main_handler(event, context):
    start_time = datetime.datetime.now()
    res = reduce_caller(event, context)
    end_time = datetime.datetime.now()
    print("data reducing duration: " + str((end_time-start_time).microseconds/1000) + "ms")
    if res == 0:
        return "Data reducing SUCCESS"
    else:
        return "Data reducing FAILED"    
```

Upon creation, create a `.py` file named `reducer_triggered` under **the same path**, enter the following code in it and save the file.
```
from qcloud_cos import UploadFileRequest
from qcloud_cos import DownloadFileRequest
import os
import logging
from operator import itemgetter


logger = logging.getLogger()

#delete folders and files
def delete_file_folder(src):
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

# Download files
def download_file(cos_client, bucket, key, local_file_path):
    request = DownloadFileRequest(bucket, key, local_file_path)
    download_file_ret = cos_client.download_file(request) 
    if download_file_ret['code'] == 0:
        logger.info("Download file [%s] Success" % key)
        return 0
    else:
        logger.error("Download file [%s] Failed, err: %s" % (key, download_file_ret['message']))
        return -1

#  Upload file to bucket
def upload_file(cos_client, bucket, key, local_file_path):
    request = UploadFileRequest(bucket.decode('utf-8'), key.decode('utf-8'), local_file_path.decode('utf-8'))
    upload_file_ret = cos_client.upload_file(request)
    if upload_file_ret['code'] == 0:
        logger.info("Upload data map file [%s] Success" % key)
        return 0
    else:
        logger.error("Upload data map file [%s] Failed, err: %s" % (key, upload_file_ret['message']))
        return -1

# doreducing
def qcloud_reducer(cos_client, bucket, key, result_bucket, result_key):
    word2count = {}
    src_file_path = u'/tmp/' + key.split('/')[-1]
    result_file_path = u'/tmp/' + u'result_' + key.split('/')[-1]
    download_ret = download_file(cos_client, bucket, key, src_file_path)
    if download_ret == 0:
        map_file = open(src_file_path,'r')
        result_file = open(result_file_path,'w')
        
        for line in map_file:
            line = line.strip()
            word, count = line.split('\t', 1)
            try:
                count = int(count)
                word2count[word] = word2count.get(word, 0) + count
            except ValueError:
                logger.error("error value: %s, current line: %s" % (ValueError, line))
                continue
        map_file.close()
        delete_file_folder(src_file_path)

    sorted_word2count = sorted(word2count.items(), key=itemgetter(1))[::-1]
    for wordcount in sorted_word2count:
        res = '%s\t%s' % (wordcount[0], wordcount[1])
        result_file.write(res)
        result_file.write('\n')
    result_file.close()

    upload_ret = upload_file(cos_client, result_bucket, result_key, result_file_path)
    delete_file_folder(result_file_path)
    return upload_ret
```

3) Compress these two files into a zip file named reducer according to the above method (note: directly compress the files instead of the folder in which these files reside).
