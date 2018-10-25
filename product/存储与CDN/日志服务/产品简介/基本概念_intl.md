## Region

CLS is provided by regions. It is currently available in Shanghai, and will be available in Beijing, Guangzhou, Chengdu, and more regions.

## Logset

You can create up to 20 logsets in a region to store logs of different businesses, such as Cloudtrail log, streaming log, COS log, or external application log.

## Log Topic

Log topic is the smallest dimensionality at which logs are collected. Up to 10 log topics can be created under each logset, making it easier for you to classify different logs. For example, you can classify logs in a logset by topics into error logs, access logs, etc. Different log topics under the same logset share the same key for easier data search. When logs are collected by using an agent, a collection configuration and server group is specified for each log topic.

## Collection Configuration

Collection configuration is the configuration with which logs are collected using an agent. It is used to specify the path under which logs are collected.

## Server Group

Server group is a list of servers that need to collect logs.

