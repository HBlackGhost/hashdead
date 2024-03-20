#! /bin/bash
s=$(cd /home/kali/ && find -name hashdead)
if [ "$s" == '' ]
then
echo "Not found"
else
echo "we found your tool and will update now"
cd $s && git pull 
fi
