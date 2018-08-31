When a packet is forwarded through an acceleration tunnel, both SNAT and DNAT are performed on the packet to modify its source and destination addresses. The source address of the data packet shown on the origin server is the forwarding IP of the accelerate tunnel, instead of the real client IP. To send the client IP to the server, the acceleration tunnel places the client's IP and port into a custom field "tcp option", as shown below:
```
#define TCPOPT_ADDR  200    
#define TCPOLEN_ADDR 8      /* |opcode|size|ip+port| = 1 + 1 + 6 */

/*
 * insert client ip in tcp option, now only support IPV4,
 * must be 4 bytes alignment.
 */
struct ip_vs_tcpo_addr {
    __u8 opcode;
    __u8 opsize;
    __u16 port;
    __u32 addr;
};
```

