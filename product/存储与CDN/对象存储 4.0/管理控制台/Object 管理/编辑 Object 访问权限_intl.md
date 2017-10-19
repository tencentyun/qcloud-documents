## Basic Concepts

Object access permission allows access control at Object dimension and has a higher priority than Bucket permission.

By modifying the Object access permission, you can, for example, set the Objects which allow public access in a private Bucket, or the Objects that only allow access after authentication in a public Bucket. There are the following Object permission types:

- Default: Any new Object has no any permission attribute when created. For an access request, Object will be skipped and Bucket permission will be directly matched.

- Public read and private write: When receiving an access request, COS will learn that the Object allows public read access. In this case, the Object can be download directly regardless of the Bucket permission.

- Private read and write: When receiving an access request, COS will learn that the Object allows private read/write access. In this case, no matter what the Bucket permission is, the Object can only be accessed by going through [Signature Authentication](/doc/api/264/5993).

- Inherit Bucket permission: The Object permission returns to being same as Bucket permission after being modified. When receiving an access request, COS will learn that the Object permission is inherited from Bucket permission, and then match the Bucket permission to respond to the access request.

> The configured Object permission is valid only if the access is made using the default domain. For the access attempt using CDN accelerated domain (e.g. file.myqcloud.com, or a custom domain bound to CDN), the authentication must be subject to the Bucket permission.

Assuming that you have created a Bucket named test with the **public read and private write** permission under the APPID of 1250000000, and uploaded Object a.txt to the root directory of the Bucket: You can download the Object successfully by accessing `http://test-1250000000.cosgz.myqcloud.com/a.txt`.

## Private Read and Write

Set the permission of Object a.txt to private read and write, and make an access attempt.

Upon the access to `http://test-1250000000.cosgz.myqcloud.com/a.txt`, the error code "403 Forbidden" will be returned with the message {"errorcode":-45086,"errormsg":"sign check fail"} indicating the signature authentication failed. The access to `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[Signature String]` can be achieved successfully after the [Signature](/doc/api/264/5993) is completed.

## Public Read and Private Write

Set the permission of Object a.txt to public read and private write, and make an access attempt.

You can download it successfully by accessing `http://test-1250000000.cosgz.myqcloud.com/a.txt`. Modify the Bucket attribute to set its permission to **private read and write**, and make an access attempt to `http://test-1250000000.cosgz.myqcloud.com/a.txt`. In this case, the download still can be performed normally.

## Overwriting Bucket Permission

Change the Bucket permission to **private read and write**, set the Object permission to "private read and write", and make an access attempt.

Upon the access to `http://test-1250000000.cosgz.myqcloud.com/a.txt`, error code "403 Forbidden" will be returned with the message {"errorcode":-45086,"errormsg":"sign check fail"} indicating the signature authentication failed. The access to `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[Signature String]` can be achieved successfully after the signature is completed.

At this point, change the Bucket permission to **public read and private write** and make an access attempt to `http://test-1250000000.cosgz.myqcloud.com/a.txt`. Error code "403 Forbidden" will be returned with the message {"errorcode":-45086,"errormsg":"sign check fail"} indicating the signature authentication failed. The access to `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[Signature String]` can be achieved successfully after the signature is completed.

## Setting Custom Permission
Locate the Object whose permission needs to be modified, click "More", and select **Set Permission** from the drop down menu:

![](https://mc.qcloudimg.com/static/img/fb3f7470ee8ed5ddfdc6c12996ae8843/image.png)

Set the permission in the pop-up window.
![](https://mc.qcloudimg.com/static/img/994dbbf53b567c5ae947e1e5962bdc90/image.png)

