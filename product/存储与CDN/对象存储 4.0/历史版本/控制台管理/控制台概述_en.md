## Basic Concepts

Tencent Cloud COS is an HTTP protocol-based file storage service and access protocol.

The COS console is one of the interfaces that help users to use the COS. With the COS console, you can operate COS directly without programming or running programs.

For your better understanding, the basic resources of COS and the corresponding traditional file system are explained below:

- COS: an Internet distributed file system that uses HTTP protocol for I/O operations.
- Bucket: a separate partition similar to / dev/sda1 or C:\ , and can not be moved or renamed after created.
- Object: the stored files, which can be accessed through a URL and is similar to the traditional file path.
- Folder: used to distinguish files stored in different paths through the symbol / .

## Bucket

### Overview

because COS is an HTTP protocol-based file storage service, a Bucket needs to be created before any file (Object) is stored. Users can create a Bucket via the Tencent Cloud console and upload an object.

### Configuring Attributes

Tencent Cloud COS supports the configuration of various Bucket attributes. For example, users can configure a Bucket for static website hosting, customize the Bucket access path, and configure its access permission.

### Relevant Restrictions

- The maximum number of Buckets is 200 (The number is the same in all regions), but there is no limit to the number of directories and files under a Bucket.
- Buckets are created under projects, and one Bucket can only belong to one project. Switch between projects is supported.
- In Tencent Cloud COS, the Bucket name under all the projects with the same APPID must be unique.
- Once created, the Bucket cannot be renamed. It is recommended that you define your Bucket name before uploading a file.
- When creating a Bucket, you can select a region. The region cannot be changed once set. 

### Naming Rules

- The Bucket name cannot be longer than 40 bytes.
- The Bucket name can only be a combination of lowercase letters and numbers.
- The Bucket name cannot contain symbols and underscores.

The following examples are valid Bucket names:

`mynewbucket`

`newproject1`

## Object

### Overview

Object is the specific content stored in Tencent Cloud COS. In the way of key-value storage, it specializes in the storage of any number of data. Object must be stored in one or more Buckets, consisting of the following basic contents:

- Key: Object name. It identifies an Object uniquely in the Bucket, and each Bucket supports an unlimited number of file storage.


- Value: used to upload local files of any type to the Bucket according to the Key you specified. For single file upload, the maximum supported size is 50 GB; and for single file storage, the maximum supported size is 500 G.


- Metadata: a group of key-value pairs, which can be used to store information about an object.

### Path Concept

Unlike the file system of computers, COS does not provide a tree index structure, which is one of the reasons why COS can support high concurrent requests. However, users can still use COS to create folders. COS requests a logical index relation through an address representing folder structure, but in fact it does not have any physical hierarchical structure.

For example, there are three files or folders in a Bucket root directory: a file `test.jpg`, a folder `photos/2015`, and a folder `photos/2016`, and there is a picture named `Me.jpg` in the `photos/2016` folder.

Tencent Cloud COS will build relative paths like `/test.jpg` and `/photos/2016/me.jpg` to make object requests.

To cater to users' viewing habits, in the COS console, the index structure will be displayed in a folder-like hierarchy.

### Naming Rule

The Object uploaded to Tencent Cloud COS needs a valid name to exclusively identify the Object in the Bucket. Object name uses Unicode characters. Although any UTF-8 characters can be used in the name, each application may analyzes special characters in different ways. The following principles are helpful to meet the requirements of DNS, Web security characters, XML parsers and other APIs to the greatest extent.

The following character sets are applicable for the key names in a secure way:

| Type | Content                |
| ------ | ----------------- |
| Alphanumeric Characters | [0-9 , a-z , A-Z] |
| Special Characters | `!`, `-`, `_`, `.`   |

The followings are some examples of secure Object names:

`my-organization`

`my.great_photos-2016/01/me.jpg`

`videos/2016/birthday/video1.wmv`

It is important to note that there is no Folder hierarchical structure in COS underlying implementation mechanism. However, users can create a Folder in COS, and identify the file hierarchical structure with separators. For example, a Bucket contains some files with the following names:

Videos/mybday.mp4

Document/lesson1.mp4

report.pdf

In the console, FolderVideos and Document are displayed with the name prefixes (Videos/ and Document/) and the solidus ("/"). However, the Object report.pdf is not prefixed, so it is displayed in the root directory of the Bucket.

### Access Address

In COS, the access address of an Object consists of the Object name and the access address of Bucket, and thus takes the form of `Bucket domain + "/" + Object name`. For more information about Bucket domain, please refer to [Bucket Domain Management](/doc/product/436/6252).

For more information about the console of historical version, please click to view [Historical Version Documentation](/document/product/430/5904)

