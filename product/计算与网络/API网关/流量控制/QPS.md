您可在创建的使用计划中，创建 QPS 配置，并绑定密钥，即在此使用计划下，对最多可调用次数进行限制。

如：您创建了一对 secret_id + secret_key，并创建了一个 QPS 为 1000 的使用计划，将这对 secret_id + secret_key 绑定到此使用计划中。再将使用计划绑定到您需要限流的环境中，如 release 环境，则对 release 环境中的 API，secret_id + secret_key 调用的用户，最大以 QPS 为 1000 的频率调用此环境中的 API。

目前每个使用计划最大可配置 2000。
