UTL_FILE 包提供文本文件输入和输出功能。
UTL_FILE 包含以下接口：

| 接口         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| \*FOPEN       | 用于打开文件                                                 |
| IS_OPEN      | 用于确定文件是否已经被打开                                   |
| FCLOSE       | 用于关闭已经打开的文件                                       |
| FCLOSE_ALL   | 该过程用于关闭当前打开的所有文件                             |
| GET_LINE     | 用于从已经打开的文件中读取行内容，行内容会被读取到输出缓冲区 |
| GET_NEXTLINE | 用于从已经打开的文件中读取下一条行内容                       |
| \*PUT         | 用于将缓冲区内容写入到文件中。当使用 PUT 过程的时候，文件必须以写方式打开，在写入缓冲区之后，如果要结束行，那么可以使用 NEW_LINE 过程 |
| NEW_LINE     | 该过程用于为文件增加行终止符                                 |
| \*PUT_LINE    | 该过程用于将文本缓冲区内容写入到文件中。当使用该过程为文件追加内容时，会自动在文件的尾部追加行终止符  |
| FFLUSH       | 用于将数据强制性写入到文件中，正常情况下，当给文件写入数据的时候，数据会被暂时的放到缓存中。过程 FFLUSH 用于强制将数据写入到文件中  |
| FREMOVE      | 用于删除磁盘文件                                             |
| \*FCOPY       | 用于将源文件的全部或者部分内容复制到目标文件中              |
| \*FRENAME     | 该过程用于修改已经存在的文件名字，其作用与 UNIX 的 MV 命令完全相同，在修改文件名字的时候，通过指定 overwrite 参数可以覆盖已经存在的文件 |
| FGETATTR     | 读取磁盘上的文件并返回文件的属性                             |
| FRENAME      | 将一个存在的文件重命名                                       |
| PUTF         | 写入格式化的内容到文件中                                     |

示例：
```
create or replace procedure utlfile_open_prowa() as
declare
v_count int;
v_fileint integer;
begin
   --open_node=w
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','w');
   perform utl_file.put_line(v_fileint,'write file test.');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','w',50);
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'一二三四五六七八九十');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','w',18,'SQL_ASCII');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'nice to meet you');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','w',31,'UTF-8');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'abcdefg hijklmn opq rst uvw xyz');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','w',88,'GBK');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'hello');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   --open_mode=a
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','a');
   perform utl_file.put_line(v_fileint,'write file test.');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','a',50);
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'一二三四五六七八九十');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','a',18,'SQL_ASCII');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'nice to meet you');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','a',31,'UTF-8');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'abcdefg hijklmn opq rst uvw xyz');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
   v_fileint := utl_file.fopen('/data1/tbasev5_autotest/tbaseTest/TbaseV5/pro_package/data/utl_file_dir','file_w.txt','a',88,'GBK');
   perform utl_file.new_line(v_fileint);
   perform utl_file.put_line(v_fileint,'hello');
   if utl_file.is_open(v_fileint) then
perform utl_file.fclose(v_fileint);
   end if;
exception
   when others then
raise notice 'EXP: something wrong.';
end;
/
call utlfile_open_prowa();
```
   
