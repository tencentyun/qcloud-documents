
DBMS_PIPE 包用于在同一实例的不同会话之间进行通信，需注意，如果用户要执行 DBMS_PIPE 包中的过程和函数，则必须要为用户授权。DBMS_PIPE 包含以下接口：

| 接口             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| \*CREATE_PIPE     | 用于建立公用管道或私有管道。如果将参数 private 设置为 TRUE，则建立私有管道；如果设置为 FALSE，则建立公用管道 |
| \*PACK_MESSAGE    | 用于将消息写入到本地消息缓冲区，包含类型 number，bytea，date，string，timestamp, record |
| \*SEND_MESSAGE    | 用于将本地消息缓冲区中的内容发送到管道                       |
| \*RECEIVE_MESSAGE | 用于接收管道消息                                             |
| NEXT_ITEM_TYPE	| 用于确定本地消息缓冲区下一项的数据类型。如果该函数返回0，则表示管道没有任何消息 |
| \*UNPACK_MESSAGE	| 用于将消息缓冲区的内容写入到变量中 |
| \*REMOVE_PIPE  |	 用于删除已经建立的管道 |
| PUGER	| 用于清除管道中的内容 |
| RESET_BUFFER |	用于复位管道缓冲区 |
| UNIQUE_SESSION_NAME |	用于为特定会话返回惟一的名称，并且名称的最长度为30字节|

示例：
```
create or replace procedure dbmspipe_crtpipe_pro(in_cno int) as
declare
v_no int;
v_bigint bigint;
v_bytea bytea;
v_date date;
v_int int;
v_num numeric;
v_text text;
v_tmptz timestamp with time zone;
begin
   select c,c_bigint,c_bytea,c_date,c_int,c_num,c_text,c_tmptz
   from dbmspipe_tbl
   where c=in_cno
   into v_no,v_bigint,v_bytea,v_date,v_int,v_num,v_text,v_tmptz;
   perform dbms_pipe.create_pipe('bigint_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_bigint);
   perform dbms_pipe.send_message('bigint_pipe1'||v_no);
   perform dbms_pipe.create_pipe('bigint_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_bigint);
   perform dbms_pipe.send_message('bigint_pipe2'||v_no);
   perform dbms_pipe.create_pipe('bigint_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_bigint);
   perform dbms_pipe.send_message('bigint_pipe3'||v_no);
   perform dbms_pipe.create_pipe('bigint_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_bigint);
   perform dbms_pipe.send_message('bigint_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('bytea_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_bytea);
   perform dbms_pipe.send_message('bytea_pipe1'||v_no);
   perform dbms_pipe.create_pipe('bytea_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_bytea);
   perform dbms_pipe.send_message('bytea_pipe2'||v_no);
   perform dbms_pipe.create_pipe('bytea_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_bytea);
   perform dbms_pipe.send_message('bytea_pipe3'||v_no);
   perform dbms_pipe.create_pipe('bytea_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_bytea);
   perform dbms_pipe.send_message('bytea_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('date_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_date);
   perform dbms_pipe.send_message('date_pipe1'||v_no);
   perform dbms_pipe.create_pipe('date_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_date);
   perform dbms_pipe.send_message('date_pipe2'||v_no);
   perform dbms_pipe.create_pipe('date_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_date);
   perform dbms_pipe.send_message('date_pipe3'||v_no);
   perform dbms_pipe.create_pipe('date_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_date);
   perform dbms_pipe.send_message('date_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('int_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_int);
   perform dbms_pipe.send_message('int_pipe1'||v_no);
   perform dbms_pipe.create_pipe('int_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_int);
   perform dbms_pipe.send_message('int_pipe2'||v_no);
   perform dbms_pipe.create_pipe('int_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_int);
   perform dbms_pipe.send_message('int_pipe3'||v_no);
   perform dbms_pipe.create_pipe('int_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_int);
   perform dbms_pipe.send_message('int_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('num_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_num);
   perform dbms_pipe.send_message('num_pipe1'||v_no);
   perform dbms_pipe.create_pipe('num_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_num);
   perform dbms_pipe.send_message('num_pipe2'||v_no);
   perform dbms_pipe.create_pipe('num_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_num);
   perform dbms_pipe.send_message('num_pipe3'||v_no);
   perform dbms_pipe.create_pipe('num_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_num);
   perform dbms_pipe.send_message('num_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('text_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_text);
   perform dbms_pipe.send_message('text_pipe1'||v_no);
   perform dbms_pipe.create_pipe('text_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_text);
   perform dbms_pipe.send_message('text_pipe2'||v_no);
   perform dbms_pipe.create_pipe('text_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_text);
   perform dbms_pipe.send_message('text_pipe3'||v_no);
   perform dbms_pipe.create_pipe('text_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_text);
   perform dbms_pipe.send_message('text_pipe4'||v_no);
    
   perform dbms_pipe.create_pipe('tmptz_pipe1'||v_no);
   perform dbms_pipe.pack_message(v_tmptz);
   perform dbms_pipe.send_message('tmptz_pipe1'||v_no);
   perform dbms_pipe.create_pipe('tmptz_pipe2'||v_no,50);
   perform dbms_pipe.pack_message(v_tmptz);
   perform dbms_pipe.send_message('tmptz_pipe2'||v_no);
   perform dbms_pipe.create_pipe('tmptz_pipe3'||v_no,100,true);
   perform dbms_pipe.pack_message(v_tmptz);
   perform dbms_pipe.send_message('tmptz_pipe3'||v_no);
   perform dbms_pipe.create_pipe('tmptz_pipe4'||v_no,200,false);
   perform dbms_pipe.pack_message(v_tmptz);
   perform dbms_pipe.send_message('tmptz_pipe4'||v_no);
end;
/
    
--创建接收pipe message，打印message子存储过程
create or replace procedure rec_subpro(in_pipename varchar) as
declare
v_num numeric;
v_bytea bytea;
v_date date;
v_str varchar;
v_tmptz timestamp with time zone;
begin
   perform dbms_output.disable();
   perform dbms_output.enable();
   perform dbms_output.serveroutput ('t');
   perform dbms_pipe.receive_message(in_pipename);
   if in_pipename like '%int%' or in_pipename like 'num' then
v_num := dbms_pipe.unpack_message_number();
perform dbms_output.put_line(in_pipename || ' message: '||v_num);
   elsif in_pipename like '%bytea%' then
v_bytea := dbms_pipe.unpack_message_bytea();
perform dbms_output.put_line(in_pipename || ' message: '||v_bytea);
   elsif in_pipename like '%date%' then
v_date := dbms_pipe.unpack_message_date();
perform dbms_output.put_line(in_pipename || ' message: '||v_date::text);
   elsif in_pipename like '%text%' then
v_str := dbms_pipe.unpack_message_text();
perform dbms_output.put_line(in_pipename || ' message: '||v_str);
   elsif in_pipename like '%tmptz%' then
v_tmptz := dbms_pipe.unpack_message_timestamp();
perform dbms_output.put_line(in_pipename || ' message: '||v_tmptz::text);
   end if;
   perform dbms_pipe.remove_pipe(in_pipename);
end;
/
--unpack_message_*测试：接收pipe中各种数据类型的message（record除外），接收后remove_pipe，打印出message
create or replace procedure dbmspipe_rec_pro(in_cno int) as
begin
   call rec_subpro('bigint_pipe1'||in_cno);
   call rec_subpro('bigint_pipe2'||in_cno);
   call rec_subpro('bigint_pipe3'||in_cno);
   call rec_subpro('bigint_pipe4'||in_cno);
    
   call rec_subpro('bytea_pipe1'||in_cno);
   call rec_subpro('bytea_pipe2'||in_cno);
   call rec_subpro('bytea_pipe3'||in_cno);
   call rec_subpro('bytea_pipe4'||in_cno);
    
   call rec_subpro('date_pipe1'||in_cno);
   call rec_subpro('date_pipe2'||in_cno);
   call rec_subpro('date_pipe3'||in_cno);
   call rec_subpro('date_pipe4'||in_cno);
    
   call rec_subpro('int_pipe1'||in_cno);
   call rec_subpro('int_pipe2'||in_cno);
   call rec_subpro('int_pipe3'||in_cno);
   call rec_subpro('int_pipe4'||in_cno);
    
   call rec_subpro('num_pipe1'||in_cno);
   call rec_subpro('num_pipe2'||in_cno);
   call rec_subpro('num_pipe3'||in_cno);
   call rec_subpro('num_pipe4'||in_cno);
    
   call rec_subpro('text_pipe1'||in_cno);
   call rec_subpro('text_pipe2'||in_cno);
   call rec_subpro('text_pipe3'||in_cno);
   call rec_subpro('text_pipe4'||in_cno);
   
   call rec_subpro('tmptz_pipe1'||in_cno);
   call rec_subpro('tmptz_pipe2'||in_cno);
   call rec_subpro('tmptz_pipe3'||in_cno);
   call rec_subpro('tmptz_pipe4'||in_cno);
end;
/
--sessionA:
call dbmspipe_crtpipe_pro(1);
--sessionB:
call dbmspipe_rec_pro(1);
--sessionA:
call dbmspipe_crtpipe_pro(2);
--sessionB:
call dbmspipe_rec_pro(2);
--sessionA:
call dbmspipe_crtpipe_pro(3);
--sessionB:
call dbmspipe_rec_pro(3);
--sessionA:
call dbmspipe_crtpipe_pro(4);
--sessionB:
call dbmspipe_rec_pro(4);
--sessionA:
call dbmspipe_crtpipe_pro(5);
--sessionB:
call dbmspipe_rec_pro(5);
```
    
