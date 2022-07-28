## 写入

| HBase | 内部类型 | 
|---------|---------|
| byte[] toBytes(String s)，String toString(byte[] b)	| CHAR，VARCHAR，STRING| 
| byte[] toBytes(boolean b)，boolean toBoolean(byte[] b)	| BOOLEAN| 
| Returns byte[] as is.	| BINARY，VARBINARY| 
| byte[] toBytes(BigDecimal v)，BigDecimal toBigDecimal(byte[] b)	| DECIMAL| 
| new byte[] { val }，bytes[0] // returns first and only byte from bytes	| TINYINT| 
| byte[] toBytes(short val)，short toShort(byte[] bytes)	| SMALLINT| 
| byte[] toBytes(int val)，int toInt(byte[] bytes)	| INT| 
| byte[] toBytes(long val)，long toLong(byte[] bytes)	| BIGINT| 
| byte[] toBytes(float val)，float toFloat(byte[] bytes)	| FLOAT| 
| byte[] toBytes(double val)，double toDouble(byte[] bytes)	| DOUBLE| 
| Stores the number of days since epoch as int value.	| DATE| 
| Stores the number of milliseconds of the day as int value.	| TIME| 
| Stores the milliseconds since epoch as long value.	| TIMESTAMP| 
| Not supported	| ARRAY| 
| Not supported	| MAP，MULTISET| 
| Not supported| 	ROW| 
