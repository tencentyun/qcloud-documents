After the Linux kernel has received the ACK packet of three-way handshake while listening the socket, its status is changed from SYN_REVC to TCP_ESTABLISHED. In this case, the kernel calls the tcp_v4_syn_recv_sock function.
The Hook function tcp_v4_syn_recv_sock_toa calls the original tcp_v4_syn_recv_sock function, then extracts TOA OPTION from the TCP OPTION by calling the get_toa_data function, and saves it in the sk_user_data field.

After the above call is completed, the kernel calls inet_getname_toa hook inet_getname to obtain the source IP and port. It first calls the original inet_getname, and check whether the sk_user_data field is empty. If real IP and port can be extracted from this field, then replace the returned values of inet_getname with these two values.

The server program calls getpeername in the user mode, and the client's original IP and port are returned.

