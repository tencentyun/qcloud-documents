## Image Repository Overview
Image repository is used to store Docker images which are used to deploy CCS. Each image has a unique ID (image's repository address + image name + image Tag).

## Image Types
Currently, official Docker Hub images and private user images are supported. Tencent Cloud community images will become available soon.

## Subscribing Image Registry
![Alt text](https://mc.qcloudimg.com/static/img/b0ce4b921b60f4f79fec6be455e16f4f/Image+005.png)
Users who use image registry for the first time need to activate this service first.

- **Namespace**: This is the prefix for the addresses of private images you create.
- **User name**: By default, this is the account of the current user. You need to use this ID to log in to Tencent Cloud Docker Image Registry.
- **Password**: This is the credential used to log in to Tencent Cloud Docker Image Registry.

## Creating Image
1. Click the "New" button on the image list page.
![Alt text](https://mc.qcloudimg.com/static/img/73e7951509c8bef8f7eaf703af6cb8df/Image+001.png)

2. Enter name and description of the image, then click **Submit**.
![Alt text](https://mc.qcloudimg.com/static/img/026b93deb76bfaeff5a27d24878529a2/Image+003.png)

## Pushing Image to Image Repository
### Log in to Tencent Cloud Registry

```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```
username: Tencent Cloud account registered upon service activation. Enter the password to complete login process.
### Upload Image
```
$ sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image Version Number]
$ sudo docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image Version Number]
```

- "ImageId" and image version number should be entered according to image information
- "namespace" is the namespace entered when activating your image warehouse
- "ImageName" is the image name created on the console


## Downloading Image
Enter the password and log in to image warehouse.
```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```

Download the image.
```
$ sudo docker pull ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[Image Version Number]
```

## Deleting Image
Select an image, click **Delete**, and then click **OK**. All tags of the image will be deleted if you delete the image.
![Alt text](https://mc.qcloudimg.com/static/img/7bc3adadf35e8d452a380c613abb264e/Image+050.png)

