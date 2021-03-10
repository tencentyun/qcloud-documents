在部署了CHDFS的JAR包后，除了使用命令行, 大数据组件等操作CHDFS外，也可以通过JAVA代码来访问。

## 前提条件
- 确保已经部署了CHDFS的相关JAR包，可参考[挂载CHDFS](https://cloud.tencent.com/document/product/1105/36368)
- 确保运行JAVA程序的机器满足挂载点的vpc权限组的


## 实例代码
1. 新建maven工程, maven的pom.xml中添加以下依赖项(请根据自己实际hadoop环境设置hadoop-common包的版本)
```
    <dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.8.5</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
```xml

2. 参考如下操作hadoop的代码进行修改， 其中的配置项等可参考[挂载CHDFS](https://cloud.tencent.com/document/product/1105/36368)

```
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
        // the config for chdfs (you can visit https://cloud.tencent.com/document/product/1105/36368)
        // the config below is required

        conf.set("fs.ofs.impl", "com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter");
        conf.set("fs.AbstractFileSystem.ofs.impl", "com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter");
        conf.set("fs.ofs.tmp.cache.dir", "/data/chdfs_tmp_cache");
        conf.set("fs.ofs.user.appid", "1250000000");
        // please refer to https://cloud.tencent.com/document/product/1105/36368 for other optional config
        
        String chdfsUrl = "ofs://f4maaaaaa-bbbb.chdfs.ap-guangzhou.myqcloud.com/";
        return FileSystem.get(URI.create(chdfsUrl), conf);
    }

    private static void mkdir(FileSystem fs, Path filePath) throws IOException {
        // create a file, if exists overwrite it
        fs.mkdirs(filePath);
    }

    private static void createFile(FileSystem fs, Path filePath) throws IOException {
        // create a file, if exists overwrite it
        // if the parent dir does not exist, fs will create it!
        FSDataOutputStream out = fs.create(filePath, true);
        try {
            // write a file
            String content = "test write file";
            out.write(content.getBytes());
        } finally {
            IOUtils.closeQuietly(out);
        }
    }

    private static void readFile(FileSystem fs, Path filePath) throws IOException {
        // create a file, if exists overwrite it
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

    // default checksum type is COMPOSITE-CRC32C
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

    // the recursive delete flag is used to delete dir
    // if recursive is false and dir is not empty, the operation will fail
    private static void deleteFileOrDir(FileSystem fs, Path path, boolean recursive) throws IOException {
        fs.delete(path, recursive);
    }

    private static void closeFileSystem(FileSystem fs) throws IOException {
        fs.close();
    }


    public static void main(String[] args) throws IOException {
        // init fs
        FileSystem fs = initFS();

        // create file
        Path chdfsFilePath = new Path("/aaa/bbb.txt");
        createFile(fs, chdfsFilePath);

        // read file
        readFile(fs, chdfsFilePath);

        // query file or dir
        queryFileOrDirStatus(fs, chdfsFilePath);

        // get file checksum
        getFileCheckSum(fs, chdfsFilePath);

        // copy file from local
        Path localFilePath = new Path("file:///home/hadoop/ofs_demo/data/xxxx.txt");
        copyFileFromLocal(fs, chdfsFilePath, localFilePath);

        // get file to local
        Path localDownFilePath = new Path("file:///home/hadoop/ofs_demo/data/yyyy.txt");
        copyFileToLocal(fs, chdfsFilePath, localDownFilePath);

        // rename
        Path newPath = new Path("/aaa/ccc.txt");
        renamePath(fs, chdfsFilePath, newPath);

        // delete file
        // deleteFileOrDir(fs, newPath, false);

        // mkdir
        Path dirPath = new Path("/fff");
        mkdir(fs, dirPath);

        // delete dir
        // deleteFileOrDir(fs, dirPath, true);

        // close filesystem
        closeFileSystem(fs);
    }
}
4. 运行
在代码编译后，运行前确保正确的设置classpath，需包含 Hadoop common包以及CHDFS包的路径，对于




```java
