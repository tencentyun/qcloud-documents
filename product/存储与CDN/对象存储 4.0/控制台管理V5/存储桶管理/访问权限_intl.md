Tencent Cloud Bucket provides two types of access permission by default: public read permission and private write permission, and private read/write permissions.

- Public read permission and private write permission: Anyone (including anonymous visitors) has read permission to the files in the Bucket, but only the Bucket creator and accounts with the appropriate permission have write permission to the files in the Bucket. Accounts with appropriate permission should exercise [Authentication](/doc/api/264/5993) for write operations.
- Private read/write permissions: Only the creator of the Bucket and accounts with the appropriate permissions have read and write permissions to the files in the Bucket, and no one else has read and write permissions to the files in the Bucket. Accounts with appropriate permission should exercise [Authentication](/doc/api/264/5993) for read and write operations.

Users can modify Bucket access permission through the console and API

Users can set the access permission of Bucket when creating the Bucket, and modify the permission at any time Enter the COS console, and click the bucket of which you need to modify the permission. Enter the Bucket, and click **Basic Configuration**:

![](https://mc.qcloudimg.com/static/img/e2532927eb0ba207eb7838fe76e39797/image.png)

Find **Access Permission**, and click **Edit** button to modify the Bucket access permission:

![](https://mc.qcloudimg.com/static/img/2c6e7ac571068ac9a332a1eaac81ccad/image.png)



