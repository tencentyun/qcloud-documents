webank-vstation-adapter

1、mkdir -p /data/log/webank_vstation_adapter/
2、解压包，cd admin
3、./uninstall.sh all
4、cd .. && ./install.sh
5、ln -s /data/webank_vstation_adapter/webank_vstation_adapter/config.py /usr/local/services/webank_vstation_adapter-1.0/webank_vstation_adapter/config.py
6、cd /usr/local/services/webank_vstation_adapter-1.0/bin/
7、./restart.sh