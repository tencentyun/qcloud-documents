## Activating Image Repository
![Alt text](https://mc.qcloudimg.com/static/img/f2e8ed97b9b24031de57a92acba066eb/1.jpg)
Users who use Image Registry for the first time need to activate this service first.

- **Namespace**: This is the prefix for the addresses of private images you create.
- **User name**: By default, this is the account of the current user. You need to use this ID to log in to Tencent Cloud Docker Image Registry.
- **Password**: This is the credential used to log in to Tencent Cloud Docker Image Registry.

## Create Image
1. Click the **New** button on the image list page.
![Alt text](https://mc.qcloudimg.com/static/img/a03d1cb4a0158b024d5e0a31186085b9/2.jpg)

2. Enter name and description of the image, then click **Submit**.
![Alt text](https://mc.qcloudimg.com/static/img/9f41fb872b429422d42d0565c073018f/3.jpg)

## Pushing Image to Image Repository
### Log in to Tencent Cloud Registry

```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```
username: Tencent Cloud account registered upon service activation. Enter the password to complete login process.
### Upload Image
```
$ sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image Tag Number]
$ sudo docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image Tag Number]
```

- "ImageId" and image tag number should be entered according to image information
- "namespace" is the namespace entered when activating your image repository
- "ImageName" is the image name created on the console


## Downloading Image
Enter the password and log in to image repository.
```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```

Download the image.
```
$ sudo docker pull ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image tag number]
```

## Deleting Image
Select an image, click **Delete**, and then click **OK**. All tags of the image will be deleted if you delete the image.
![Alt text](https://mc.qcloudimg.com/static/img/92f092ee054ac80ed3b9a036db2b2013/4.jpg)
