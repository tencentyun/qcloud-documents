1. Cloud Memcached is based on standard Memcached protocols and APIs. Here, we assume that developers already have certain knowledge towards Memcached when they use Cloud Memcached service.

Developers can refer to the introductions at the official Memcached website for information about Memcached:

http://memcached.org/

Open source Memcached extension libraries and API descriptions (extension libraries for multiple languages, such as C++/PHP/Java/Python/Ruby/Perl...):

https://code.google.com/archive/p/memcached/downloads 


2. The Memcached text protocol list contains a list of commands supported by Cloud Memcached. Download the list in the table below.

<table class="t2" style="display:table;width:80%;">

<tbody><tr>
<th width="150"> <b>Document name</b>
</th><th width="70"> <b>File size</b>
</th><th width="380"><b>Description</b>
</th></tr>
<tr>
<td>
<p><a href="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Memcached_text_protocol_list.zip" class="external text" title="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Memcached_text_protocol_list.zip" target="_blank" rel="nofollow">Memcached text protocol list</a>
</p>
</td><td> 16.1 KB<br><br>
</td><td> Added instructions for "gets" API, which supports a maximum of 255 key values.
</td></tr>
<tr>
<td>
<p><a href="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Memcached_text_ext_protocol.zip" class="external text" title="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Memcached_text_ext_protocol.zip" target="_blank" rel="nofollow">Memcached text extension protocol</a>
</p>
</td><td> 251 KB<br><br>
</td><td> Added two extension commands (get_ext, gets_ext), which allow clients to determine whether the data exists and the reason for unreturned data according to error code.
</td></tr></tbody></table>

3. Standard Memcached protocols come with certain defects, developers should pay particular attention to them. See [Standard Memcached Protocol Defect Solution](/doc/product/241/标准协议缺陷解决方案说明).

