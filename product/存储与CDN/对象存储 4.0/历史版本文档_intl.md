## Notifications about upgrade

Since the the Cloud Object Storage (COS) architecture has been upgraded to V4, users who registered after October, 2016 are provided with the console, API and SDK of the V4 version by default. If you are an user who started using COS before October, 2016, we will continue to provide maintenance for your console, API and SDK of the V3 version. **You can still use the original features**, but no new features will be developed for the V3 version.

## Console Document

- [Console Features](/document/product/430/5904)
- [Bucket Management](/document/product/430/5886)
- [Object Management](/document/product/430/5978)
- [Folder Management](/document/product/430/5914)

## API Documents

### How to distinguish API versions

The upload domain for API V3:

```
web.file.myqcloud.com
```

The upload domain for JOSN API V4:

```
<Region>.file.myqcloud.com
```

The upload domain for XML API V4 (**highly recommended**):

```
<BucketName>-<AppID>.<Region>.myqcloud.com
```

### Entry to documents for APIs of the V3 version

- [Signature Algorithm](/document/product/430/5993)
- [Call Method](/document/product/430/5994)

| Operation Type |    Function     | Request Method |                Detailed Description                 |
| :--: | :-------: | :--: | :---------------------------------: |
| Directory-related operation |   Create directories    | POST |   [About the API for creating directories](/doc/api/264/6000)    |
| Directory-related operation |   List directories    | GET  |   [About the API for list directories](/doc/api/264/6001)    |
| Directory-related operation |  Query directory attributes   | GET  |  [About the API for querying directory attributes](/doc/api/264/6002)   |
| Directory-related operation |   Delete directories    | POST |   [About the API for deleting directories](/doc/api/264/6003)    |
| File-related operation |  Simple upload of files   | POST |  [About the API for simple upload of files](/doc/api/264/6005)   |
| File-related operation |  Multipart upload of files   | POST |  [About the API for multipart upload of files](/doc/api/264/6006)   |
| File-related operation |  Query file attributes   | GET  |  [About the API for querying file attributes](/doc/api/264/6008)   |
| File-related operation |  Update file attributes   | POST |  [About the API for updating file attributes](/doc/api/264/6011)   |
| File-related operation | Move (rename) files | POST | [About the API for moving (renaming) files](/doc/api/264/6009) |
| File-related operation |   Delete files    | POST |   [About the API for deleting files](/doc/api/264/6010)    |

## SDK Documents

### Entry to documents for SDKs of the V3 version

| SDK            | Connection Documents                                     |
| :------------- | :--------------------------------------- |
| PHP SDK        | [PHP SDK Connection Instruction](/doc/product/430/5942)    |
| Python SDK     | [Python SDK Connection Instruction](/doc/product/430/5943) |
| Node.js SDK    | [Node.js SDK Connection Instruction](/doc/product/430/5947) |
| Java SDK       | [Java SDK Connection Instruction](/doc/product/430/5944)   |
| JavaScript SDK | [JavaScript SDK Connection Instruction](/doc/product/430/5946) |
| C++ SDK        | [C++ SDK Connection Instruction](/doc/product/430/5945)    |
| C sharp SDK    | [C sharp SDK Connection Instruction](/doc/product/430/5966) |
| Android SDK    | [Android SDK Connection Instruction](/doc/product/430/5950) |
| iOS SDK        | [iOS SDK Connection Instruction](/doc/product/430/5949)    |

## Developer tools

### How to distinguish tool versions

In the feature description of V4 tools, there is be a note indicating "for COS 4.0 only".

There is no such note for V3.

For example:

![](https://mc.qcloudimg.com/static/img/b9ae616606fddd64a4ddd7277915c98c/image.png)

### Entry to documents for tools of the V3 version

- [Batch deletion tool](/document/product/430/5918)
- [Local migration tool](/document/product/430/5919)
- [Qiniu migration tool](/document/product/430/6102)
- [OSS migration tool](/document/product/430/6103)
- [COS-Fuse tool](/document/product/430/6885)

