for i in `grep "logs" *`;  do scp $i root@portland05:/; done
