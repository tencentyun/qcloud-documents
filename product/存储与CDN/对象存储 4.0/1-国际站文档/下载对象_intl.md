You can download the Object that has been uploaded to the Bucket using the access address.

Enter the COS console, click the Bucket of the Object, and click **File Information** on the right side of the Object list:

![](https://mc.qcloudimg.com/static/img/e26cf2de168ba9dc1de75dc775e5f480/image.png)

At this point, the system will pop up a window that contains the Object information. You can either click the download button to download the Object directly, or copy and paste the URL address into the browser to download:

![](https://mc.qcloudimg.com/static/img/7325519a5253375d117cc779ce4f8d04/image.png)


If the attribute of the Bucket to which the resource belongs is private read and write, the signature will be calculated automatically and added after the copied address as a suffix. For more information about the signature generation method, please refer to [Signature Algorithm](/doc/api/264/5993).

```
http://testbucket-10026302.file.myqcloud.com/test_uploadfile_1.txt?sign=eTgtgdjtdYm0fQ+5zGSLeQ9q3RdhPTEwMDI2MzAyJms9QUtJRG1tSURnYlk0a2h5YzJGVFZ0NjRZNUllZnd5WHhJb1VyJmU9MTQ2MjQzODA5NCZ0PTE0NTk4NDYwOTQmcj04ODYzOTQwOTkmZj0vdGVzdF91cGxvYWRmaWxlXzEudHh0JmI9dGVzdGJ1Y2tldA==
```


