1. 下载并编译 [tez0.10.0 源码包](https://downloads.apache.org/tez/0.10.0/) 
```
tar -zxvf  apache-tez-0.10.0-src.tar.gz
chmod -R 777 apache-tez-0.10.0-src
cd  apache-tez-0.10.0-src
mvn -X clean package -DskipTests=true -Dmaven.javadoc.skip=true
```
2. 解压编译的 war 包
3. yarn-site.xml 配置文件 
新建目录 `mkdir -p /usr/local/service/hadoop/filesystem/yarn/timeline`

| 参数                                                      | 值                |
| --------------------------------------------------------- | ----------------- |
| yarn.timeline-service.enabled                             | true              |
| yarn.timeline-service.hostname                            | `172.**.**.9 `      |
| yarn.timeline-service.http-cross-origin.enabled           | true              |
| yarn.resourcemanager.system-metrics-publisher.enabled     | true              |
| yarn.timeline-service.address                             | `172.**.**.9:10201` |
| yarn.timeline-service.webapp.address                      | `172.**.**.9:8188`  |
| yarn.timeline-service.webapp.https.address                | `172.**.**.9:2191`  |
| yarn.timeline-service.generic-application-history.enabled | true              |
| yarn.timeline-service.handler-thread-count                | 24                |

4. tez.xml 配置

| 参数                              | 值                                                           |
| --------------------------------- | ------------------------------------------------------------ |
| tez.tez-ui.history-url.base       | `http://172.**.**.9:2000/tez-ui/`                              |
| tez.history.logging.service.class | org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService |

