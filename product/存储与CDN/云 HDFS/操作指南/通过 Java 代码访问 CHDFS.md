## 操作场景

在部署云 HDFS（Cloud HDFS，CHDFS） 的 JAR 包之后，除了可以使用命令行、大数据组件等方式操作 CHDFS ，还可以通过 Java 代码来访问 CHDFS。本文指导您如何通过 Java 代码访问 CHDFS。

## 前提条件

- 确保已经部署了 CHDFS 的相关 JAR 包。详情请参见 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368)。
- 确保运行 Java 程序的机器处于挂载点权限组允许访问的私有网络 VPC 中。

## 操作步骤

1. 新建 maven 工程，并在 maven 的 pom.xml 中添加以下依赖项（请根据自己实际 hadoop 环境设置 hadoop-common 包的版本）。
```plaintext
<dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.8.5</version>
            <scope>provided</scope>
        </dependency>
</dependencies>
```
2. 参考如下操作hadoop的代码进行修改， 其中的配置项等可参考[挂载CHDFS](https://cloud.tencent.com/document/product/1105/36368)。**并重点关注其中数据持久化以及可见性相关的说明.**
以下只列出了部分常见的文件系统的操作，其他的接口可参考[Hadoop FileSystem 接口文档](https://hadoop.apache.org/docs/r2.8.2/api/org/apache/hadoop/fs/FileSystem.html).
```java
package com.qcloud.chdfs.demo;

import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileChecksum;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.nio.ByteBuffer;

public class Demo {
			private static FileSystem initFS() throws IOException {
				Configuration conf = new Configuration();
				// CHDFS 的配置项可参见 https://cloud.tencent.com/document/product/1105/36368
				// 以下配置是必填项

			conf.set("fs.ofs.impl", "com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter");
				conf.set("fs.AbstractFileSystem.ofs.impl", "com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter");
				conf.set("fs.ofs.tmp.cache.dir", "/data/chdfs_tmp_cache");
				conf.set("fs.ofs.user.appid", "1250000000");
				// 其他可选配置项请参见 https://cloud.tencent.com/document/product/1105/36368 

			String chdfsUrl = "ofs://f4maaabbb-ccdd.chdfs.ap-guangzhou.myqcloud.com/";
				return FileSystem.get(URI.create(chdfsUrl), conf);
			}

		private static void mkdir(FileSystem fs, Path filePath) throws IOException {
				fs.mkdirs(filePath);
			}

		private static void createFile(FileSystem fs, Path filePath) throws IOException {
				// 创建一个文件（如果存在则将其覆盖）
				// if the parent dir does not exist, fs will create it!
				FSDataOutputStream out = fs.create(filePath, true);
				try {
						// 写入一个文件
						String content = "test write file";
						out.write(content.getBytes());
				} finally {
						// close 返回成功, 表示数据写入成功, 若抛出异常, 表示数据写入失败
						out.close();
				}
			}

		private static void readFile(FileSystem fs, Path filePath) throws IOException {
				FSDataInputStream in = fs.open(filePath);
				try {
						byte[] buf = new byte[4096];
						int readLen = -1;
						do {
								readLen = in.read(buf);
						} while (readLen >= 0);
				} finally {
						IOUtils.closeQuietly(in);
				}
			}


			private static void queryFileOrDirStatus(FileSystem fs, Path path) throws IOException {
				FileStatus fileStatus = fs.getFileStatus(path);
				if (fileStatus.isDirectory()) {
						System.out.printf("path %s is dir\n", path);
						return;
				}

			long fileLen = fileStatus.getLen();
				long accessTime = fileStatus.getAccessTime();
				long modifyTime = fileStatus.getModificationTime();
				String owner = fileStatus.getOwner();
				String group = fileStatus.getGroup();


				System.out.printf("path %s is file, fileLen: %d, accessTime: %d, modifyTime: %d, owner: %s, group: %s\n",
						path, fileLen, accessTime, modifyTime, owner, group);
			}


			// 默认的校验类型为 COMPOSITE-CRC32C
			private static void getFileCheckSum(FileSystem fs, Path path) throws IOException {
				FileChecksum checksum = fs.getFileChecksum(path);
				System.out.printf("path %s, checkSumType: %s, checkSumCrcVal: %d\n",
						path, checksum.getAlgorithmName(), ByteBuffer.wrap(checksum.getBytes()).getInt());
			}


			private static void copyFileFromLocal(FileSystem fs, Path chdfsPath, Path localPath) throws  IOException {
				fs.copyFromLocalFile(localPath, chdfsPath);
			}


			private static void copyFileToLocal(FileSystem fs, Path chdfsPath, Path localPath) throws  IOException {
				fs.copyToLocalFile(chdfsPath, localPath);
			}


			private static void renamePath(FileSystem fs, Path oldPath, Path newPath) throws IOException {
				fs.rename(oldPath, newPath);
			}


			private static void listDirPath(FileSystem fs, Path dirPath) throws IOException {
				FileStatus[] dirMemberArray = fs.listStatus(dirPath);


				for (FileStatus dirMember : dirMemberArray) {
						System.out.printf("dirMember path %s, fileLen: %d\n", dirMember.getPath(), dirMember.getLen());
				}
			}


			// 递归删除标志用于删除目录
			// 如果递归为 false 并且 dir 不为空，则操作将失败
			private static void deleteFileOrDir(FileSystem fs, Path path, boolean recursive) throws IOException {
				fs.delete(path, recursive);
			}


			private static void closeFileSystem(FileSystem fs) throws IOException {
				fs.close();
			}


			public static void main(String[] args) throws IOException {
				// 初始化文件系统
				FileSystem fs = initFS();


				// 创建文件
				Path chdfsFilePath = new Path("/folder/exampleobject.txt");
				createFile(fs, chdfsFilePath);


				// 读取文件
				readFile(fs, chdfsFilePath);


				// 查询文件或目录
				queryFileOrDirStatus(fs, chdfsFilePath);


				// 获取文件校验和
				getFileCheckSum(fs, chdfsFilePath);


				// 从本地复制文件
				Path localFilePath = new Path("file:///home/hadoop/ofs_demo/data/exampleobject.txt");
				copyFileFromLocal(fs, chdfsFilePath, localFilePath);


				// 获取文件到本地
				Path localDownFilePath = new Path("file:///home/hadoop/ofs_demo/data/exampleobject.txt");
				copyFileToLocal(fs, chdfsFilePath, localDownFilePath);


				// 重命名
				Path newPath = new Path("/doc/example.txt");
				renamePath(fs, chdfsFilePath, newPath);


				// 删除文件
				deleteFileOrDir(fs, newPath, false);


				// 创建目录
				Path dirPath = new Path("/folder");
				mkdir(fs, dirPath);


				// 在目录中创建文件
				Path subFilePath = new Path("/folder/exampleobject.txt");
				createFile(fs, subFilePath);


				// 列出目录
				listDirPath(fs, dirPath);


				// 删除目录
				deleteFileOrDir(fs, dirPath, true);


				// 关闭文件系统
				closeFileSystem(fs);
			}
}
```
3. 编译和运行。
>? 
> - 运行前，请确保已正确设置 classpath。classpath 需包含 Hadoop common 包以及 CHDFS 包的路径。
> - 对于 EMR 环境，如果您按照 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368) 逐步操作，那么 Hadoop common 包通常在 `/usr/local/service/hadoop/share/hadoop/common/` 目录下，CHDFS 包通常在`/usr/local/service/hadoop/share/hadoop/common/lib/` 目录下。
> 



