#!/bin/bash
# 本脚本的主要目的是获取指定证书的在对应VPN1虚拟局域网中的IP地址

# 第一个参数为需要获取IP地址的客户端证书名（不带.ovpn）-k

while getopts ':k:' OPT;
do
    case $OPT in
        k)  CLIENT_NAME="$OPTARG";;
        :)  echo "Please input the name of client key!"
            exit 1;;
        ?)  echo "Invalid option: -$OPTARG"
            exit 2;;
    esac
done
# 从证书名称中获取需要访问的路径
Dir=/etc/${CLIENT_NAME%_client*}/ipp.txt
for line in `cat $Dir`
do
    tmp=${line%,*}
    if [ $tmp == $CLIENT_NAME ];then
        IPAddress=${line#*,}
        echo $IPAddress
        exit 0
    fi
done
exit 1