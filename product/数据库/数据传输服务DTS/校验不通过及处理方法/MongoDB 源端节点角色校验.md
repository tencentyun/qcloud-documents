## 检查详情
- 检查要求：MongoDB 迁移任务，源端为分片时，需要填写对应 mongos，config server，mongod 节点信息。
- 检查说明：mongos，config server 和 mongod 节点信息填写不能混乱，否则会导致数据迁移错乱，例如将 mongos 节点信息填入 mongod 填写框内。注意，每个分片只需要填写一个 mongod 节点。

## 修复方法
- DTS 任务填写框内填写正确节点信息。
- 每个分片只填写一个 mongod。
