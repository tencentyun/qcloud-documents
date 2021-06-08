1. tez 0.8.5版本的 tez-ui 文件路径为 `/usr/local/service/tomcat/webapps/tez-ui/scripts/configs.js` 对应0.9.2版本中的 `configs.env`。
2. yarn-site.xml 配置文件 
需要新建目录 `mkdir -p /usr/local/service/hadoop/filesystem/yarn/timeline`
 
| 参数                                                     | 值                                                 |
| -------------------------------------------------------- | -------------------------------------------------- |
| yarn.timeline-service.enabled                            | true                                               |
| yarn.timeline-service.hostname                           | `172.**.**.9`                                        |
| yarn.timeline-service.http-cross-origin.enabled          | true                                               |
| yarn.resourcemanager.system-metrics-publisher.enabled    | true                                               |
| yarn.timeline-service.address                            | `172.**.**.9:10201`                                  |
| yarn.timeline-service.webapp.address                     | `172.**.**.9:8188`                                   |
| yarn.timeline-service.webapp.https.address               | `172.**.**.9:2191`                                  |
| arn.timeline-service.generic-application-history.enabled | true                                               |
| yarn.timeline-service.leveldb-timeline-store.path        | `/usr/local/service/hadoop/filesystem/yarn/timeline` |
| yarn.timeline-service.handler-thread-count               | 24                                                 |


3. 0.8.5版本需要修改 tez-site.xml 中对应的配置项参数为：

| 参数                                                     | 值                                                 |
| -------------------------------------------------------- | -------------------------------------------------- |
| tez.allow.disabled.timeline-domains | true                                                         |
| tez.history.logging.service.class   | org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService |
| tez.tez-ui.history-url.base         | `http://172.**.**.9:2000/tez-ui/`                            |

