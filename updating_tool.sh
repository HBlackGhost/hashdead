#! /bin/bash
s=$(cd /home/kali/ && find -name hashdead)
if [ "$s" == '' ]
then
echo "We can't found your tool"
else
echo "We found your tool and will update now"
sleep 5
cd /home/kali && cd $s && git pull 
fi
