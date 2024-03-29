#!/bin/sh

echo ""
echo " Utilisation ligne de commande : "
echo " ./gen_lst.sh <Numéro sequence> <Durée séquence> <Nombre de crénaux> <Nom du fichier lst> <Date et heure de départ : dd/mm/YYYY-HH:MM:SS>"
echo ""

if [ -z "$1" ]
then
	read -p "Numéro de la séquence binaire : " n
	num=$n
	if [ -z "$n" ]
	then
		num="6940"
	fi
else
	num=$1
fi

if [ -z "$2" ]
then
	read -p "Durée de la séquence en minutes : " d
	dur=$d
        if [ -z "$d" ]
        then
                dur="12"
	fi
else
        dur=$2
fi

if [ -z "$3" ]
then
	read -p "Nombre de créneaux/répétitions : " s
        seqs=$s
        if [ -z "$s" ]
        then
                seqs="69"
	fi
else
        seqs=$3
fi

if [ -z "$4" ]
then
	read -p "Nom du fichier de sortie : " file
        file_lst=$file
        if [ -z "$file" ]
        then
                file_lst=`date +"%Y%m%d_"`${num}
	fi
else
        file_lst=$4
fi

if [ -z "$5" ]
then
	read -p "Date et heure UTC de départ (dd/mm/YYYY-HH:MM:SS) :" d_t
        d_t_lst=$d_t
        if [ -z "$d_t" ]
        then
                d_t_lst=`date +"%d/%m/%Y-%T"`
	fi
else
        d_t_lst=$5
fi

if [ -z "$6" ]
then
	read -p "Espacer les séquences de 30 minutes ? (O/N, O par défaut) :" esp
        esp_lst=$esp
        if [ -z "$esp" ]
        then
                d_t_lst="O"
	fi
else
        esp_lst=$6
fi

if [ -z "$7" ]
then
	read -p "Incrémenter les numéros des séquences dans le .lst ? (O/N, N par défaut) :" incr
        incr_lst=$incr
        if [ -z "$incr" ]
        then
                incr_lst="N"
	fi
else
        incr_lst=$7
fi

if [ "$incr_lst" = "O" ] || [ "$incr_lst" = "o" ]
then
  incr_lst=1

elif [ "$incr_lst" = "N" ] || [ "$incr_lst" = "n" ]
then
  incr_lst=0
else
  incr_lst=0
  echo "Pas compris, répondu N par défaut"
fi

if [ "$esp_lst" = "O" ] || [ "$esp_lst" = "o" ]
then
  python3 lst.py $num $dur $seqs $file_lst $d_t_lst $incr_lst
elif [ "$esp_lst" = "N" ] || [ "$esp_lst" = "n" ]
then
  python3 lst_condensed.py $num $dur $seqs $file_lst $d_t_lst $incr_lst
fi
