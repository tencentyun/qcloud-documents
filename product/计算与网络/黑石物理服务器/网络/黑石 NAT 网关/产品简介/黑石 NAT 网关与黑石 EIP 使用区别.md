NAT 网关和 EIP 是物理主机访问 Internet 两种方式，您可以根据需要选择其中一种或两种：
方案 1：只使用 NAT 网关
物理主机不绑定 EIP，所有访问 Internet 流量通过 NAT 网关转发。此方案中，物理主机访问 Internet 流量会通过内网转发至 NAT 网关。
方案 2：只使用 EIP
物理主机只绑定 EIP，不使用 NAT 网关。此方案中，物理主机所有访问 Internet 流量通过 EIP 出。
方案 3：同时使用 NAT 网关和 EIP
物理主机绑定了 EIP，同时所在子网访问 Internet 流量指向了 NAT 网关，此方案中，物理主机通过 EIP 与外网进行通信。