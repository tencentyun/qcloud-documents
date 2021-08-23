## 检查详情
- 检查要求：MongoDB迁移任务，源端为分片时，需要填写对应mongos，config server，mongod节点信息。
- 检查说明：mongos，config server和mongod节点信息填写不能混乱，否则会导致数据迁移错乱，例如将mongos节点信息填入mongod填写框内。注意，每个分片只需要填写一个mongod节点。

## 修复方法
- DTS任务填写框内填写正确节点信息。
- 每个分片只填写一个mongod。

