
尊敬的用户：
您好，腾讯云官方监测到在腾讯云官网购买 Ubuntu14.04 云服务器 apt-get 安装 Tomcat 以及 Hadoop 时，可以正常监听端口，但是无法响应请求。现腾讯云给出相应规避措施，建议您如遇到此情况，可根据建议措施进行规避。

### 问题原因
Java Runtime Environment 的一个 [已知问题](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6202721) 导致。

### 问题分析
Tomcat 以及 Hadoop 使用 Java 开发，使用了 java.security.SecureRandom 的 API。
此 API 在某些 JRE 中默认使用 `/dev/random` 生成，而 `/dev/random ` 接收 CPU 温度，键盘等硬件杂讯来生成熵。因为云服务器是采用虚拟化技术的云服务器环境，很难感知 CPU 温度等信号则很难生成熵，因此 `cat /dev/random `几乎阻塞而导致 Tomcat，Hadoop 启动受阻问题。

### 规避措施
#### 修改 JRE 配置
修改原 `/etc/java-7-openjdk/security/java.security`（ URL 需依照实际情况）中的 ` securerandom.source=file:/dev/urandom `为 `securerandom.source=file:/dev/./urandom ` 来规避上述问题。




