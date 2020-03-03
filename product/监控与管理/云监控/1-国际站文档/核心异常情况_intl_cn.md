监控概况模块为云产品的整体监控情况提供一个查看入口。监控异常部分为用户展示关键的几个异常情况。包括如下几部分：

## 云服务器 ping 不可达
显示最近 1 个月，告警列表中策略类型为【云服务器】，告警状态为【未恢复】，且告警类型为【 ping 不可达】的告警条数。这些未恢复的云服务器告警通常比较重要，可能会影响到您业务正常运行。

## 云服务器磁盘只读
显示最近 1 个月，告警列表中策略类型为【云服务器】，告警状态为【未恢复】，且告警类型为【磁盘只读】的告警条数。对于云服务器中有需要写入数据的业务来说，发生了磁盘只读会影响您业务正常运行。

## 云服务器无监控数据

无监控数据可能由于云服务器未安装[监控组件 Agent](https://cloud.tencent.com/doc/product/248/2258)导致，具体原因可通过以下步骤排查：

1. 判断是否安装barad_agent

   未安装监控组件会导致无法对您的服务器做更细致的监控，若服务器故障则将无法正常通知，存在高危风险。有关安装监控组件的更多内容，请参考 [安装监控组件](/doc/product/248/6211)。

2. 若已安装agent，判断barad_agent的日志是否每分钟实时滚动且成功上报 

   > 1) linux系统日志路径：/usr/local/qcloud/monitor/barad/log/dispatcher.log
   >
   > ​    且每条日志都有"nws send succ" 

   > 2) windows系统日志路径：C:\Program Files\QCloud\Monitor\Barad\logs\info.log
   >
   > ​    且每条日志都有"nws send succ"

3. 若日志无滚动，可能为agent调度问题（一般只出现在linux系统，可能是改过系统时间）

   可尝试重启barad_agent，同时确认日志/usr/local/qcloud/monitor/barad/log/executor.log有无错误。

4. 若上报失败(nws send fail)，需根据日志判断具体的问题（如超时、无法连接到服务器、无法解析域名等） 

   上报地址可以在etc目录的plugin.ini文件中的nws_url看到。

5. 若上报未出现 nws send fail

   1）检查uuid是否被修改过

   uuid文件路径：

   > linux：/etc/uuid

   > windows：c:\windows\system32\drivers\etc\uuid
   >
   > ​                    c:\windows\system32\drivers\etc\目录下uuid格式命名的最新文件

   2）若uuid文件未变动，检测子机的时间戳

    linux可使用命令 `/usr/sbin/ntpdate ntpupdate.tencentyun.com` 查看时间调整是否在50S以内，若时间相关较大，重启barad_agent后可恢复。![img](http://tapd.oa.com/tfl/captures/2016-05/tapd_10114711_base64_1464166851_22.png)

6. 若执行以上流程仍未解决问题，linux系统可使用check_agent_profile脚本

   在云服务器内执行如下命令：

   `wget http://update2.agent.tencentyun.com/check_barad_agent && sh check_barad_agent`

   将输出结果通过工单上报，我们将尽快为您定位解决问题。