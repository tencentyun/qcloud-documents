## 背景
Alluxio 通过文件系统接口提供对数据的访问。Alluxio 中的文件提供一次写入语义：它们在被完整写下之后不可变，在完成之前不可读。Alluxio 提供了两种不同的文件系统 API：Alluxio API 和 Hadoop 兼容的 API。Alluxio API 提供了额外的功能，而 Hadoop 兼容的 API 为用户提供了无需修改现有代码使用 Hadoop API 的灵活性。

所有使用 Alluxio Java API 的资源都是通过 AlluxioURI 指定的路径实现。

## 获取文件系统客户端
要使用 Java 代码获取 Alluxio 文件系统客户端，请使用：
```
FileSystem fs = FileSystem.Factory.get();
```

## 创建一个文件
所有的元数据操作，以及打开一个文件读取或创建一个文件写入都通过 FileSystem 对象执行。由于 Alluxio 文件一旦写入就不可改变，创建文件的惯用方法是使用`FileSystem#createFile(AlluxioURI)`，它返回一个可用于写入文件的流对象。例如：
```
FileSystem fs = FileSystem.Factory.get();
AlluxioURI path = new AlluxioURI("/myFile");
// Create a file and get its output stream
FileOutStream out = fs.createFile(path);
// Write data
out.write(...);
// Close and complete file
out.close();
```

## 指定操作选项
对于所有的文件系统操作，可以指定一个额外的 options 字段，它允许用户可以指定操作的非默认设置。例如：
```
FileSystem fs = FileSystem.Factory.get();
AlluxioURI path = new AlluxioURI("/myFile");
// Generate options to set a custom blocksize of 128 MB
CreateFileOptions options = CreateFileOptions.defaults().setBlockSize(128 * Constants.MB);
FileOutStream out = fs.createFile(path, options);
```

## IO 选项
Alluxio 使用两种不同的存储类型：Alluxio 管理存储和底层存储。Alluxio 管理存储是分配给 Alluxio worker 的内存 SSD 或 HDD。底层存储是由在最下层的存储系统（如 S3、Swift 或 HDFS）管理的资源。用户可以指定通过 ReadType 和 WriteType 与 Alluxio 管理的存储交互。ReadType 指定读取文件时的数据读取行为。WriteType 指定数据编写新文件时写入行为，例如，数据是否应该写入 Alluxio Storage。

下面是 ReadType 的预期行为表。读取总是偏好 Alluxio 存储优先于底层存储。

|Read Type |	Behavior |
|--|--|
|CACHE_PROMOTE |	<li/>如果读取的数据在 Worker 上时，该数据被移动到 Worker 的最高层。<li/>如果该数据不在本地 Worker 的 Alluxio 存储中，那么就将一个副本添加到本地 Alluxio Worker 中。 <li/>如果 `alluxio.user.file.cache.partially.read.block` 设置为 true，没有完全读取的数据块也会被**全部**存到 Alluxio 内。相反，一个数据块只有完全被读取时，才能被缓存。
| CACHE	| <li/>如果该数据不在本地 Worker 的 Alluxio 存储中，那么就将一个副本添加到本地 Alluxio Worker 中。<li/>如果 `alluxio.user.file.cache.partially.read.block` 设置为 true，没有完全读取的数据块也会被**全部**存到 Alluxio 内。相反，一个数据块只有完全被读取时，才能被缓存。
| NO_CACHE |	仅读取数据，不在 Alluxio 中存储副本。

下面是 WriteType 的预期行为表。

| Write Type |	Behavior |
|--|--|
|CACHE_THROUGH|	数据被同步地写入到 Alluxio 的 Worker 和底层存储系统。
|MUST_CACHE |	数据被同步地写入到 Alluxio 的 Worker。但不会被写入到底层存储系统。这是默认写类型。
|THROUGH |	数据被同步地写入到底层存储系统。但不会被写入到 Alluxio 的 Worker。
|ASYNC_THROUGH |	数据被同步地写入到 Alluxio 的 Worker，并异步地写入到底层存储系统。处于实验阶段。

## 位置策略
Alluxio 提供了位置策略来选择要存储文件块到哪一个 worker。使用 Alluxio 的 Java API，用户可以设置策略在 CreateFileOptions 中向 Alluxio 写入文件和在 OpenFileOptions 中读取文件。

用户可以轻松地覆盖默认的策略类配置文件中的属性 `alluxio.user.file.write.location.policy.class`。内置的策略包括：
- LocalFirstPolicy (alluxio.client.file.policy.LocalFirstPolicy)：首先返回本地节点，如果本地 worker 没有足够的块容量，它从活动 worker 列表中随机选择一名 worker。这是默认的策略。
- MostAvailableFirstPolicy (alluxio.client.file.policy.MostAvailableFirstPolicy)：返回具有最多可用字节的 worker。
- RoundRobinPolicy (alluxio.client.file.policy.RoundRobinPolicy)：以循环方式选择下一个 worker，跳过没有足够容量的 worker。
- SpecificHostPolicy (alluxio.client.file.policy.SpecificHostPolicy)：返回具有指定节点名的 worker。此策略不能设置为默认策略。

Alluxio 支持自定义策略，所以您也可以通过实现接口 `alluxio.client.file.policyFileWriteLocationPolicy` 制定适合自己的策略。
>!默认策略必须有一个空的构造函数。并使用 ASYNC_THROUGH 写入类型，所有块的文件必须写入同一个 worker。

Alluxio 允许客户在向本地 worker 写入数据块时选择一个层级偏好。目前这种策略偏好只适用于本地 worker 而不是远程 worker；远程 worker 会写到最高层。默认情况下，数据被写入顶层。用户可以通过 `alluxio.user.file.write.tier.default` 配置项修改默认设置，或通过 `FileSystem#createFile(AlluxioURI)API` 调用覆盖它。

对现有文件或目录的所有操作都要求用户指定 AlluxioURI。使用 AlluxioURI，用户可以使用 FileSystem 中的任何方法来访问资源。AlluxioURI 可用于执行 Alluxio FileSystem 操作，例如修改文件元数据、ttl 或 pin 状态，或者获取输入流来读取文件。例如，要读取一个文件：
```
FileSystem fs = FileSystem.Factory.get();
AlluxioURI path = new AlluxioURI("/myFile");
// Open the file for reading
FileInStream in = fs.openFile(path);
// Read data
in.read(...);
// Close file relinquishing the lock
in.close();
```
