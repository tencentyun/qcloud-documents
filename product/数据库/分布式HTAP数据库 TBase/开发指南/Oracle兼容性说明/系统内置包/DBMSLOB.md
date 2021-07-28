
DBMS_LOB 用于在大对象上进行操作。DBMS_LOB 包提供了子程序可以在 BLOB、CLOB、NCLOB、BFILE 和临时 LOB 上操作的子程序。使用 DBMS_LOB 可以访问和处理 LOB 的特定部分或全部。

| 存储过程/函数                                                | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| APPEND(dest_lob IN OUT,src_lob)                              | Appends one large object to another.                         |
| COMPARE(lob_1, lob_2 [, amount[, offset_1 [, offset_2 ]]])   | Compares two large objects.                                  |
| CONVERTOBLOB(dest_lob IN OUT,src_clob, amount, dest_offsetIN OUT, src_offset IN OUT,blob_csid, lang_context IN OUT,warning OUT) | Converts character data to binary.                           |
| CONVERTTOCLOB(dest_lob IN OUT,src_blob, amount, dest_offsetIN OUT, src_offset IN OUT,blob_csid, lang_context IN OUT,warning OUT) | Converts binary data to character.                           |
| COPY(dest_lob IN OUT, src_lob,amount [, dest_offset [,src_offset ]]) | Copies one large object to another.          |
| ERASE(lob_loc IN OUT, amount IN OUT [, offset ])             | Erase a large object.                                        |
| GET_STORAGE_LIMIT(lob_loc)                                   | Get the storage limit for large objects.                     |
| GETLENGTH(lob_loc)                                           | Get the length of the large object.                          |
| INSTR(lob_loc, pattern [,offset [, nth ]])                   | Get the position of the nth occurrence of a pattern in the large object starting atoffset. |
| READ(lob_loc, amount IN OUT,offset, buffer OUT)              | Read a large object.                                         |
| SUBSTR(lob_loc [, amount [,offset ]])                        | Get part of a large object.                                  |
| TRIM(lob_loc IN OUT, newlen)                                 | Trim a large object to the specified length.                 |
| WRITE(lob_loc IN OUT, amount,offset, buffer)                 | Write data to a large object.                                |
| WRITEAPPEND(lob_loc IN OUT,amount, buffer)                   | Write data from the buffer to the end of a large object.     |

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
