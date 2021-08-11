DBMS_LOB 用于在大对象上进行操作。DBMS_LOB 包提供了子程序可以在 BLOB、CLOB、NCLOB、BFILE 和临时 LOB 上操作的子程序。使用 DBMS_LOB 可以访问和处理 LOB 的特定部分或全部。

|存储过程/函数|	描述|
|--|--|
|APPEND(dest_lob IN OUT,src_lob)	|将一个大对象追加到另一个对象|
|COMPARE(lob_1, lob_2 [, amount[, offset_1 [, offset_2 ]]])	|比较两个大对象|
|CONVERTOBLOB(dest_lob IN OUT,src_clob, amount, dest_offsetIN OUT, src_offset IN OUT,blob_csid, lang_context IN OUT,warning OUT)	|将字符数据转换为二进制数据|
|CONVERTTOCLOB(dest_lob IN OUT,src_blob, amount, dest_offsetIN OUT, src_offset IN OUT,blob_csid, lang_context IN OUT,warning OUT)	| 将二进制数据转换为字符数据                        |
|COPY(dest_lob IN OUT, src_lob,amount [, dest_offset [,src_offset ]])	| 将一个大对象复制到另一个对象             |
|ERASE(lob_loc IN OUT, amount IN OUT [, offset ])	|清除一个大对象|
|GET_STORAGE_LIMIT(lob_loc)	|获取大对象的存储限制|
|GETLENGTH(lob_loc)	| 获取大对象的长度                                  |
|INSTR(lob_loc, pattern [,offset [, nth ]])	|获取大对象中从 `offset` 开始模式第 n 次出现的位置|
|READ(lob_loc, amount IN OUT,offset, buffer OUT)	|读取一个大对象|
|SUBSTR(lob_loc [, amount [,offset ]])| 获取一个大对象的一部分 |
|TRIM(lob_loc IN OUT, newlen)	|将一个大对象裁剪到指定长度|
|WRITE(lob_loc IN OUT, amount,offset, buffer)| 向一个大对象写数据 |
|WRITEAPPEND(lob_loc IN OUT,amount, buffer)	|将数据从缓冲区写到大对象的末端|

示例：
```
DBMS_LOB.WRITEAPPEND (
lob_loc IN OUT NOCOPY BLOB, 
amount  ININTEGER, 
buffer  INRAW); 
    
DBMS_LOB.WRITEAPPEND (
lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, 
amount  ININTEGER, 
buffer  INVARCHAR2 CHARACTER SET lob_loc%CHARSET);

declare
v_clob1 clob;
begin
v_clob1:=to_clob('123456');
dbms_output.put_line(v_clob1);
DBMS_LOB.WRITEAPPEND(v_clob1,3,'789');
dbms_output.put_line(v_clob1);
end;
/
```
