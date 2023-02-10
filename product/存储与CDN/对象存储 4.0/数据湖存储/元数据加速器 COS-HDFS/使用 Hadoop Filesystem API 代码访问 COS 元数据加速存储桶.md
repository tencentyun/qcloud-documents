## 操作场景

如果对象存储（Cloud Object Storage，COS）存储桶开启了元数据加速，除了可以使用 Hadoop 命令行、大数据组件等方式操作外，还可以通过 Hadoop Filesystem API，使用 Java 代码来访问元数据加速桶。本文指导您如何通过 Java 代码访问元数据加速桶。

## 前提条件

- 确保已经开通元数据加速，并且进行了正确的环境部署和 HDFS 协议配置。具体部署和配置，详情请参见 [使用 HDFS 协议访问已开启元数据加速器的存储桶](https://cloud.tencent.com/document/product/436/68700)。
- 如果有 Hadoop 环境，可以验证下 Hadoop 命令行是否能正确访问。

## 操作步骤

1. 新建 maven 工程，并在 maven 的 pom.xml 中添加以下依赖项（请根据自己实际 Hadoop 版本及环境设置 hadoop-common 包、hadoop-cos 包和 cos_api-bundle 包的版本）。
```plaintext
<dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.8.5</version>
            <scope>provided</scope>
        </dependency>
         <dependency>
            <groupId>com.qcloud.cos</groupId>
            <artifactId>hadoop-cos</artifactId>
            <version>xxx</version>
        </dependency>
        <dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api-bundle</artifactId>
            <version>xxx</version>
        </dependency>
        
</dependencies>
```
2. 参考如下 hadoop 的代码进行修改。其中的配置项可参见 [配置项说明](https://cloud.tencent.com/document/product/1105/36368) 文档进行修改。**以及重点关注其中数据持久化和可见性相关的说明。**
   以下只列出了部分常见的文件系统的操作，其他的接口可参见 [Hadoop FileSystem 接口文档](https://hadoop.apache.org/docs/r2.8.2/api/org/apache/hadoop/fs/FileSystem.html)。
```java
package com.qcloud.cos.demo;

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
               // 配置项可参见 https://cloud.tencent.com/document/product/436/6884#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85
               // 以下配置是必填项

               conf.set("fs.cosn.impl", "org.apache.hadoop.fs.CosFileSystem");
               conf.set("fs.AbstractFileSystem.cosn.impl", "org.apache.hadoop.fs.CosN");
               conf.set("fs.cosn.userinfo.secretId", "xxxxxx");
               conf.set("fs.cosn.userinfo.secretKey", "xxxxxx");
               conf.set("fs.cosn.bucket.region", "xxxxxx");
               conf.set("fs.cosn.tmp.dir", "/data/chdfs_tmp_cache");

               // 配置项可参考 https://cloud.tencent.com/document/product/436/71550
               // 通过 POSIX 访问方式必填配置项(推荐方式)
               conf.set("fs.cosn.trsf.fs.AbstractFileSystem.ofs.impl", "com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter");
               conf.set("fs.cosn.trsf.fs.ofs.impl", "com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter");
               conf.set("fs.cosn.trsf.fs.ofs.tmp.cache.dir", "com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter");
               conf.set("fs.cosn.trsf.fs.ofs.impl", "com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter");
               conf.set("fs.cosn.trsf.fs.ofs.tmp.cache.dir", "/data/chdfs_tmp_cache");
               
               // appid 根据实际 appid 进行替换
               conf.set("fs.cosn.trsf.fs.ofs.user.appid", "1250000000");
               // region 根据实际地域进行替换
               conf.set("fs.cosn.trsf.fs.ofs.bucket.region", "ap-beijing");
               // 其他可选配置参考官网文档 https://cloud.tencent.com/document/product/436/6884#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85
               // 是否开启 CRC64 校验，默认不开启，此时无法使用 hadoop fs -checksum 命令获取文件的 CRC64 校验值
               conf.set("fs.cosn.crc64.checksum.enabled", "true");
               String cosHadoopFSUrl = "cosn://examplebucket-12500000000/";
               return FileSystem.get(URI.create(cosHadoopFSUrl), conf);
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
				Path localFilePath = new Path("file:///home/hadoop/cosn_demo/data/exampleobject.txt");
				copyFileFromLocal(fs, chdfsFilePath, localFilePath);


				// 获取文件到本地
				Path localDownFilePath = new Path("file:///home/hadoop/cosn_demo/data/exampleobject.txt");
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
> - 运行前，请确保已正确设置 classpath。classpath 需包含 Hadoop common 包以及元数据加速桶依赖的 Jar 包的路径。
> - 对于 EMR 环境，如果您按照 [使用 HDFS 协议访问已开启元数据加速器的存储桶](https://cloud.tencent.com/document/product/436/68700) 逐步操作，那么 Hadoop common 包通常在 `/usr/local/service/hadoop/share/hadoop/common/` 目录下，元数据加速桶依赖的 Jar 包通常在 `/usr/local/service/hadoop/share/hadoop/common/lib/` 目录下。
> 
