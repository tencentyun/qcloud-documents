Tencent Cloud Bucket provides two types of access permission by default: public read permission and private write permission, and private read/write permissions.

- Public read permission and private write permission: Anyone (including anonymous visitors) has read permission to the files in the Bucket, but only the Bucket creator and accounts with the appropriate permission have write permission to the files in the Bucket. Accounts with appropriate permission should exercise [Authentication](/doc/api/264/5993) for write operations.
- Private read/write permissions: Only the creator of the Bucket and accounts with the appropriate permissions have read and write permissions to the files in the Bucket, and no one else has read and write permissions to the files in the Bucket. Accounts with appropriate permission should exercise [Authentication](/doc/api/264/5993) for read and write operations.

Users can modify Bucket access permission through the console and API

Users can set the access permission of Bucket when creating the Bucket, and modify the permission at any time Enter the COS console, and click the bucket of which you need to modify the permission. Enter the Bucket, and click **Permission**:

![](//mc.qcloudimg.com/static/img/e8099435d4e13da487db227fa08499c9/image.png)

Find **Public Permission**, and click **Edit** button to modify the Bucket access permission:

![](//mc.qcloudimg.com/static/img/983340044795356c1bd2182ba40a3621/image.png)

