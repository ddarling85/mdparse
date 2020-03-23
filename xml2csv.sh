
awk -F'>|<' '/BILL_NO/{printf $3}/NAME\>/{if(NF==3) {print ",NA"} else{print ","$3}}' myfile

