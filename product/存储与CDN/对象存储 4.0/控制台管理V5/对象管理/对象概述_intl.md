Object is the content stored in Tencent Cloud COS with the key-value storage method which is used for the storing any amount of data. Object must be stored in one or more Buckets, and consists of the following basic elements:

Key: Object name. It is used to uniquely identify an Object in the Bucket
Value: After creating the Bucket, you can upload any types of local files to the Bucket. Each Bucket in COS is able to store an unlimited number of files. In a simple upload, upload of a single file not larger than 5G is supported, and in a multipart upload, upload of a single file not larger than 50T is supported.
Metadata: A set of key-value pairs, which can be used to store the information on Object. For more information, refer to [Object HTTP Header Settings](/doc/product/436/6258).
Access control information - Information on the control of the access permission of Object.

## Object Name
The Object uploaded in Tencent Cloud COS should have a valid name to uniquely identify the Object in the Bucket. You can traverse the Object names in the Bucket Object List on the console. Object name uses Unicode characters. Although any UTF-8 characters can be used in the name, each application may analyze special characters in a different way. The following principles are helpful to meet the requirements for DNS, Web security characters, XML parsers and other APIs to the greatest extent.

The following character sets can be securely used for the key names:

| Type     | Content                 |
| ------ | -------------------- |
| Alphanumeric Characters | [0-9 , a-z , A-Z]    |
| Special Characters   | `!`, `-`, `_`, `.`, `* ` |

The followings are some examples of secure Object names:

my-organization
my.great_photos-2016/01/me.jpg
videos/2016/birthday/video1.wmv

Please note that no Folder hierarchy exists in COS underlying implementation logic. However, users can create a Folder in COS and identify the file hierarchical levels with separators. For example, if a Bucket contains files with the following names:

Vedio/mybday.mp4

Document/lesson1.mp4

report.pdf

On the console, FolderVideos and Document are displayed with the name prefix (Vedio/, Document/) and separator ("/"). The Object "report.pdf" is not prefixed, so it will be displayed in the root directory of the Bucket.

> There is no hierarchy in COS. With prefix and separator in the Object name, hierarchical levels can be identified and the concept of Folder be introduced in COS.

## Object Address
Based on the access address of Bucket and the Object name, the access address of Object in Tencent Cloud is composed of `Bucket domain + "/" + Object name`. For more information about Bucket domain, refer to [Bucket Domain Management](/doc/product/436/6252).

