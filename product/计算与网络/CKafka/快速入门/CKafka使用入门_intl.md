### 1. View the CKafka instance and create a topic

After your application is approved, the CKafka instance is displayed in the CKafka console. Click the instance to view its details, including region, private network vip and port.

![](https://mc.qcloudimg.com/static/img/d4876666b80726d2ac75295fb3f038fb/10112-01.jpg)
![](https://mc.qcloudimg.com/static/img/18bf42c30b42e07f58754727a8638a1d/10112-02.jpg)

In the topic management page, you can create a topic, and specify the number of partitions and replicas for the topic.
> Note: The current topic name cannot be changed after input. In addition, when you have specified the number of partitions, you can only add partitions. Number of replicas cannot be changed once being specified. 
![](https://mc.qcloudimg.com/static/img/23e2f2ecaa07d30eee635519e0016bb8/10112-03.jpg)
After the topic and partitions are created, you can perform the production and consumption operations on this instance via the Kafka client on CVM.

### 2. Download the Kafka toolkit locally

#### 2.1 Install the JDK environment
This document describes how to set up a CKafka environment on your CVM. First, [purchase a CVM](https://buy.cloud.tencent.com/cvm) on the purchase page and then log in to the CVM. The configuration of the test machine in this example is as follows:
> Machine configuration 
Operating system: CentOS 6.8 64-bit 
CPU: 1 core  
Memory: 2 GB 
Public network bandwidth: 1 Mbps 

Next, install JDK on the CVM.
(1). Download JDK, which can be obtained with the wget command. You can also download a different version from the official website.
It is recommended to use a version later than JDK 1.7. The version used in this example is JDK 1.7.0_79.

(2). Move it to a fixed folder and decompress it:
```
mkdir /usr/local/jdk
mv jdk-7u79-linux-x64.tar.gz /usr/local/jdk/
cd /usr/local/jdk/
tar -xzvf jdk-7u79-linux-x64.tar.gz
```
(3). Configure the environment variables.
```
vim /etc/profile
```
Add the configuration of the following environment variables to the end of the file.
```
export JAVA_HOME=/usr/local/jdk/jdk1.7.0_79(JDK's decompressed directory)  
export JRE_HOME=/usr/local/jdk/jdk1.7.0_79/jre
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH  
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JRE_HOME/lib
```
Save and exit wq, and then use the command 'source / etc / profile' to make the file take effect immediately.

(4). Verification
Verify whether the environment has been installed using the following command (javac command also applies), and then check whether the version numbers are consistent.
```
java -version
```
The following figure indicates the JDK installation is complete.
![](https://mc.qcloudimg.com/static/img/859143ff8986b24e80b3a9c3b31bd511/4.png)

#### 2.2 Download the Kafka toolkit

Download and decompress the Kafka installer package
CKafka is 100% compatible with Kafka 0.9. You're recommended to download this version of Kafka installer package from the official website http://kafka.apache.org/.
```
wget "http://mirrors.hust.edu.cn/apache/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz"
tar -xzvf kafka_2.11-0.9.0.1.tgz
mv kafka_2.11-0.9.0.1 /opt/
```
The Kafka is ready for use immediately after download and decompression, without the need of configuring other environments.
You can test whether this machine is connected to the CKafka instance with telnet command.
```
telnet ip 9092
```
![](https://mc.qcloudimg.com/static/img/c30a8d0e2fe57c109d3f7f1fa55b107f/5.png)

#### 2.3 Simple tests for Kafka APIs

Send messages
```
./kafka-console-producer.sh --broker-list xxx.xxx.xxx.xxx:9092 --topic topicName
This is a message
This is another message
```
> The IP in the broker-list is the vip in the CKafka instance, and topicName is the topic name in the CKafka instance.

Receive messages (Zookeeper cluster is hidden in CKafka by default)
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName
This is a message
This is another message
```
In the above commands, no consumer group is specified for consumption, so the system generates a group at random for consumption. In this way, it is very likely to reach the limit of group. Therefore, it is recommended to receive messages by **specifying a group**.
First, configure the specified group name in the consumer.properties, as shown below.

![](https://mc.qcloudimg.com/static/img/b39a4b9b75a734830a69cc66a7273485/111.png)

After the configuration, run the command that specifies the consumer group as shown below:
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```

Check the CKafka monitor.
![](https://mc.qcloudimg.com/static/img/5a3a256254da7d3ce2da952c5fe51610/10112-04.jpg)

### 3. Other features
#### 3.1 Enable the whitelist
CKafka supports enabling IP whitelist for a topic to ensure the data security.
You can enable the IP whitelist in both "New Topic" and "Edit Topic" pages.
![](https://mc.qcloudimg.com/static/img/dc4a5103ae5c98ec634c815fe19ca285/10112-05.jpg)

#### 3.2 Set message retention time
CKafka supports setting the message retention time (in minutes). The minimum is 1 minute, and the maximum is 30 days.
![](https://mc.qcloudimg.com/static/img/5330fa26e6a2e332db2c0e227b5af88d/10112-06.jpg)

