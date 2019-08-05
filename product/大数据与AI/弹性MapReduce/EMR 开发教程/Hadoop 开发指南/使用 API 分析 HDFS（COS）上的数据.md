学习 MapReduce 会接触的第一个程序通常都是 WordCount，统计给定文件的单词的词频。本节将会介绍如何自己建立一个工程并编写程序，并且使用编译打包好的程序去统计 HDFS 和腾讯云对象存储 COS 上面的数据，使用的程序基本和 Hadoop 社区的示例程序相同。

## 1. 开发准备
- 由于任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建一个存储桶（Bucket）](https://cloud.tencent.com/document/product/436/6232)。

- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候在基础配置页面勾选“开启 COS”，并在下方填写自己的 SecretId 和 SecretKey。SecretId 和 SecretKey 可以在 [API 密钥管理界面](https://console.cloud.tencent.com/cam/capi) 查看。如果还没有密钥，请单击【新建密钥】建立一个新的密钥。

## 2. 登录 EMR 服务器
在做相关操作前需要登录到 EMR 集群中的任意一个机器，最好是登录到 Master 节点。EMR 是建立在 Linux 操作系统的腾讯云服务器（CVM）上的，所以在命令行模式下使用 EMR 需要登录 CVM 服务器。

创建了 EMR 集群之后，在控制台中选择弹性 MapReduce，在集群列表中找到刚刚创建的集群，选择右侧【详情】>【节点信息】>【Master 节点】中活跃的 Master 节点的 CVM ID 即可进入云服务器控制台并且找到 EMR 对应的云服务器。

登录 CVM 的方法请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。

输入正确后，即可进入 EMR 集群的命令行界面。所有的 Hadoop 操作都在 Hadoop 用户下，登录 EMR 主机之后默认在 root 用户，需要切换到 Hadoop 用户。使用如下命令切换用户，并且进入  Hadoop 文件夹下：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/hadoop
[hadoop@172 hadoop]$
```

## 3. 数据准备
您需要准备统计的文本文件。分为两种方式：**将数据存储在 HDFS 集群**和**数据存储在 COS**。 

首先在本地新建一个 txt 文件 test.txt，并且添加一些英语单词：
```
Hello World.
this is a message.
this is another message.
Hello world, how are you?
```

把本地的数据上传到云服务器。可以使用 scp 或者 sftp 服务来把本地文件上传到 EMR 集群的云服务器中。在本地 shell 使用：
```
scp $localfile root@公网IP地址:$remotefolder
```
其中，$localfile 是您的本地文件的路径加名称；root 为 CVM 服务器用户名；公网 IP 地址可以在 EMR 控制台的节点信息中或者在云服务器控制台查看；$remotefolder 是您想存放文件的 CVM 服务器路径。

上传完成后，在 EMR 集群命令行中即可查看对应文件夹下是否有相应文件，此处上传到了 EMR 集群的 `/usr/local/service/hadoop` 路径下。
```
[hadoop@172 hadoop]$ ls –l
```

### 数据存放在 HDFS
将数据上传到腾讯云服务器之后，可以把数据拷贝到 HDFS 集群。通过如下指令把文件拷贝到 Hadoop 集群：
```
[hadoop@172 hadoop]$ hadoop fs -put /usr/local/service/Hadoop/test.txt /user/hadoop/
```
拷贝完成后使用以下指令查看拷贝好的文件：
```
[hadoop@172 hadoop]$ hadoop fs -ls /user/hadoop
输出：
-rw-r--r-- 3 hadoop supergroup 85 2018-07-06 11:18 /user/hadoop/test.txt
```
如果 Hadoop 下面没有 `/user/hadoop` 文件夹，用户可以自己创建，指令如下：
```
[hadoop@172 hadoop]$ hadoop fs –mkdir /user/hadoop
```
更多 hadoop 指令见 [HDFS 常见操作](https://cloud.tencent.com/document/product/589/12289)。

### 数据存放在 COS
数据存放在 COS 中有两种方式：**从本地直接通过 COS 的控制台上传**和**通过 Hadoop 命令上传**。
- 从本地直接通过 [COS 控制台直接上传](https://cloud.tencent.com/document/product/436/13321)，数据文件上传之后可以通过如下命令查看：
```
[hadoop@10 hadoop]$ hadoop fs -ls cosn://$bucketname/ test.txt
-rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://$bucketname/test.txt
```
其中 $bucketname 替换成您的储存桶的名字加路径。
- 通过 Hadoop 命令上传，指令如下：
```
[hadoop@10 hadoop]$ hadoop fs -put test.txt cosn://$bucketname /
[hadoop@10 hadoop]$ bin/hadoop fs -ls cosn:// $bucketname / test.txt
-rw-rw-rw- 1 hadoop hadoop 1366 2017-03-15 19:09 cosn://$bucketname / test.txt
```

## 4. 使用 Maven 创建工程
推荐您使用 Maven 来管理您的工程。Maven 是一个项目管理工具，能够帮助您方便的管理项目的依赖信息，即它可以通过 pom.xml 文件的配置获取 jar 包，而不用去手动添加。

首先下载并安装 Maven，配置好 Maven 的环境变量，如果您使用 IDE，请在 IDE 中设置好 Maven 相关配置。

### 新建一个 Maven工程
在命令行下进入您想要新建工程的目录，例如 `D://mavenWorkplace` 中，输入如下命令新建一个 Maven 工程：
```
mvn     archetype:generate     -DgroupId=$yourgroupID     -DartifactId=$yourartifactID 
-DarchetypeArtifactId=maven-archetype-quickstart
```
其中 `$yourgroupID` 即为您的包名；`$yourartifactID` 为您的项目名称；`maven-archetype-quickstart` 表示创建一个 Maven Java  项目，工程创建过程中需要下载一些文件，请保持网络通畅。
创建成功之后，在 `D://mavenWorkplace` 目录下就会生成一个名为 `$yourartifactID` 的工程文件夹。其中的文件结构如下所示：
```
simple
　　　---pom.xml　　　　核心配置，项目根下
　　　---src
　　　　　---main　　　　　　
　　　　　　　---java　　　　Java 源码目录
　　      　---resources　  Java 配置文件目录
　　　　---test
　　　　　　---java　　　　测试源码目录
　　　　　　---resources　  测试配置目录
```
主要关注 pom.xml 文件和 main 下的 Java 文件夹。pom.xml 文件主要用于依赖和打包配置，Java 文件夹下放置您的源代码。

首先在 pom.xml 中添加 Maven 依赖：
```
<dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.7.3</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-core</artifactId>
            <version>2.7.3</version>
        </dependency>
</dependencies>
```
继续在 pom.xml 中添加打包和编译插件：
```
<build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>utf-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
</build>
```
在 src>main>java 下右键新建一个 Java Class，输入 Class 名，这里使用 WordCount，在 Class 添加样例代码：
```
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;
import java.util.StringTokenizer;

/**
 * Created by tencent on 2018/7/6.
 */
public class WordCount {
    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, IntWritable>
    {
        private static final IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
                throws IOException, InterruptedException
        {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens())
            {
                this.word.set(itr.nextToken());
                context.write(this.word, one);
            }
        }
    }

    public static class IntSumReducer
            extends Reducer<Text, IntWritable, Text, IntWritable>
    {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values, Reducer<Text, IntWritable, Text, IntWritable>.Context context)
                throws IOException, InterruptedException
        {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            this.result.set(sum);
            context.write(key, this.result);
        }
    }

    public static void main(String[] args)
            throws Exception
    {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
        if (otherArgs.length < 2)
        {
            System.err.println("Usage: wordcount <in> [<in>...] <out>");
            System.exit(2);
        }
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        for (int i = 0; i < otherArgs.length - 1; i++) {
            FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
        }
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[(otherArgs.length - 1)]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```
可以看到其中有一个 Map 函数和一个 Reduce 函数。
如果您的 Maven 配置正确并且成功的导入了依赖包，那么整个工程应该没有错误可以直接编译。在本地 shell 下进入工程目录，执行下面的命令对整个工程进行打包：
```
mvn package
```
运行过程中可能还需要下载一些文件，直到出现 build success 表示打包成功。然后您可以在工程目录下的 target 文件夹中看到打好的 jar 包。
使用 scp 或者 sftp 服务来把打包好的工程文件上传到 EMR 集群的云服务器中。在本地 shell 使用：
```
scp $jarpackage root@公网IP地址: /usr/local/service/hadoop
```
其中，`$jarpackage` 是您的本地 jar 包的路径加名称；root 为 CVM 服务器用户名；公网 IP 地址可以在 EMR 控制台的节点信息中或者在云服务器控制台查看。这里上传到了 EMR 集群的 `/usr/local/service/hadoop` 文件夹下。

### 统计 HDFS 中的文本文件
进入 `/usr/local/service/hadoop` 目录，和数据准备中一样。通过如下命令来提交任务：

```
[hadoop@10 hadoop]$ bin/hadoop jar 
/usr/local/service/hadoop/WordCount-1.0-SNAPSHOT-jar-with-dependencies.jar
WordCount /user/hadoop/test.txt /user/hadoop/WordCount_output
```
>!以上整个命令为一条完整的指令，`/user/hadoop/ test.txt` 为输入的待处理文件，`/user/hadoop/ WordCount_output` 为输出文件夹，在提交命令之前要保证`WordCount_output` 文件夹尚未创建，否则提交会出错。

执行完成后，通过如下命令查看执行输出文件：

```
[hadoop@172 hadoop]$ hadoop fs -ls /user/hadoop/WordCount_output
Found 2 items
-rw-r--r-- 3 hadoop supergroup 0 2018-07-06 11:35 /user/hadoop/MEWordCount_output/_SUCCESS
-rw-r--r-- 3 hadoop supergroup 82 2018-07-06 11:35 /user/hadoop/MEWordCount_output/part-r-00000
```
通过如下指令查看 part-r-00000 中的统计结果：
```
[hadoop@172 hadoop]$ hadoop fs -cat /user/hadoop/MEWordCount_output/part-r-00000
Hello	2
World.	1
a	1
another	1
are	1
how	1
is	2
message.	2
this	2
world,	1
you?	1……
```

### 统计 COS 中的文本文件
进入 `/usr/local/service/hadoop` 目录。通过如下命令来提交任务：
```
[hadoop@10 hadoop]$ hadoop jar
/usr/local/service/hadoop/WordCount-1.0-SNAPSHOT-jar-with-dependencies.jar
WordCount cosn://$bucketname/test.txt cosn://$bucketname /WordCount_output
```
命令的输入文件改为了 `cosn:// $bucketname/ test.txt`，其中 $bucketname 为您的存储桶名字加路径。处理结果同样也输出到 COS 中。使用如下指令查看输出文件：
```
[hadoop@10 hadoop]$ hadoop fs -ls cosn:// $bucketname /WordCount_output
Found 2 items
-rw-rw-rw- 1 hadoop Hadoop 0 2018-07-06 10:34 cosn://$bucketname /WordCount_output/_SUCCESS
-rw-rw-rw- 1 hadoop Hadoop 1306 2018-07-06 10:34 cosn://$bucketname /WordCount_output/part-r-00000
```
查看最后输出的结果：
```
[hadoop@10 hadoop]$ hadoop fs -cat cosn:// $bucketname /WordCount_output1/part-r-00000
Hello	2
World.	1
a	1
another	1
are	1
how	1
is	2
message.	2
this	2
world,	1
you?	1
```

