## 读取

| BSON 类型 | 内部类型 | 
|---------|---------|
|-	|TINYINT|
|	-|SMALLINT|
| Int	| INT| 
| Long| 	BIGINT| 
| 	-| FLOAT| 
|  Double	| DOUBLE| | 
| Decimal128	|  DECIMAL(p, s)| | 
| Boolean| 	BOOLEAN| 
| Date Timestamp| 	DATE| 
| Date Timestamp	| TIME| 
| Date	| TIMESTAMP(3) TIMESTAMP_LTZ(3)| 
| Timestamp	| TIMESTAMP(0) TIMESTAMP_LTZ(0)| 
| String，ObjectId，UUID ，Symbol ，MD5 ，JavaScript，Regex	| STRING| 
| BinData	| BYTES| 
| Object	| ROW| 
| Array| 	ARRAY| 
| DBPointer	| ROW&ltSTRING, STRING>| 


