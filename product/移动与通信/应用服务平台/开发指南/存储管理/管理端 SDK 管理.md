您可以将管理端 manager-node SDK 部署在本地、云端服务器甚至云函数里对云存储空间内的文件进行批量上传、下载、删除、获取文件信息、获取临时链接以及设置文件权限等。

## 上传文件

在管理端调用 uploadFile 方法进行单个文件的上传。

```js
const CloudBase = require("@cloudbase/manager-node");

const path = require("path");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function uploadFile() {
  await storage.uploadFile({
    localPath: path.resolve("./data.txt"),
    cloudPath: "files/data.txt",
    onProgress: (data) => {}
  });
}

uploadFile();
```

## 上传文件夹

在管理端调用 uploadDirectory 可以将文件夹内的文件批量上传到云存储空间。

```js
const CloudBase = require("@cloudbase/manager-node");

const path = require("path");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function uploadDirectory() {
  await storage.uploadDirectory({
    localPath: path.resolve("./files"),
    cloudPath: "",
    onProgress: (data) => {}
  });
}

uploadDirectory();
```

## 下载文件

在管理端调用 downloadFile 方法进行单个文件的下载。

```js
const CloudBase = require("@cloudbase/manager-node");

const path = require("path");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function downloadFile() {
  await storage.downloadFile({
    cloudPath: "files/data.txt",
    localPath: path.resolve("./data.txt")
  });
}

downloadFile();
```

## 下载文件夹

在管理端调用 downloadDirectory 方法可以将云存储空间内指定文件夹下载到管理端指定文件夹。

```js
const CloudBase = require("@cloudbase/manager-node");

const path = require("path");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function downloadDirectory() {
  await storage.downloadDirectory({
    cloudPath: "files/music",
    localPath: path.resolve("./music")
  });
}

downloadDirectory();
```

## 删除文件

在管理端调用 deleteFile 方法进行单个或多个文件的批量删除。

```js
const CloudBase = require("@cloudbase/manager-node");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function deleteFile() {
  await storage.deleteFile(["files/data.txt", "uploads/logo.png"]);
}

deleteFile();
```

## 删除文件夹

在管理端调用 deleteDirectory 方法可以删除云存储空间内整个文件夹。

```js
const CloudBase = require("@cloudbase/manager-node");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function deleteDirectory() {
  await storage.deleteDirectory("files/");
}

deleteDirectory();
```

## 获取文件信息

在管理端调用 getFileInfo 方法可以获取文件的大小、类型、修改时间、对象的实体标签 ETag 。

```js
const CloudBase = require("@cloudbase/manager-node");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function getFileInfo() {
  const info = await storage.getFileInfo("files/data.txt");
  console.log(info);
}

getFileInfo();
```

## 列出文件夹内文件列表

在管理端调用 listDirectoryFiles 列出云存储空间内指定文件夹下的所有文件以及文件信息。

```js
const CloudBase = require("@cloudbase/manager-node");

const { storage } = new CloudBase({
  secretId: "Your SecretId",
  secretKey: "Your SecretKey",
  envId: "Your envId" // 云开发环境ID，可在腾讯云云开发控制台获取
});

async function listDirectoryFiles() {
  const res1 = await storage.listDirectoryFiles("dir/data");

  const res2 = await storage.listDirectoryFiles("dir/data", 20);

  const res3 = await storage.listDirectoryFiles("dir/data", 20, "dir/dat");

  for (let item in res1) {
    console.log(item);
  }
}
listDirectoryFiles();
```

## 参考

管理端 SDK 还可以获取文件临时链接、获取/设置文件存储权限，更多详细信息请参考：

[管理端 manager-node sdk ](https://docs.cloudbase.net/api-reference/manager/node/introduction)
