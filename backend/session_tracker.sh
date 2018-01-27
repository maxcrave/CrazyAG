#!/bin/bash
md5_str=$1

for i in $(seq 1 30);
do
    ssh_pid=`ps -ef|grep $md5_str|grep -v sshpass|grep -v grep|grep -v session_tracker.sh|awk '{print $2}'`
    echo "ssh session pid:$ssh_pid"
    if [ "$ssh_pid" = "" ];then
        echo "watting ssh pid"
        sleep 1
        continue
    else
        echo "ssh session pid:$ssh_pid"

        today=`date "+%Y_%m_%d"`
        today_audit_dir="logs/audit/$today"
        if [ today_audit_dir ]
        then
            echo " ----start tracking log---- "
        else
            echo "dir not exist"
            echo " today dir: $today_audit_dir"
            sudo mkdir -p $today_audit_dir
        fi;
        echo 123456 | sudo /usr/bin/strace -f -p $ssh_pid -ttt -o "$md5_str.log"
        break
    fi;
done;