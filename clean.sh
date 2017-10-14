./honsshctrl.sh clean
kill -9 `netstat -putan |grep ":22" |grep python|cut -d"/" -f1 |sed -e 's/.* \([0-9]*\)/\1/'`
