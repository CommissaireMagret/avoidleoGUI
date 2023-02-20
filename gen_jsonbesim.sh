#!/bin/bash

pip install pypredict

#cat ~/.disps/cospas70.txt

echo ""
echo " Utilisation ligne de commande : "
echo " ./gen_json.sh <Numéro sequence> <Durée séquence> <Nombre de crénaux> <Nom du fichier json> <Date et heure de départ : dd/mm/YYYY-HH:MM:SS>"
echo ""

if [ -z "$1" ]
then
	read -p "Numéro de la séquence : " n
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
	read -p "Durée des séquences en minutes : " d
	dur=$d
        if [ -z "$d" ]
        then
                dur="30"
	fi
else
        dur=$2
fi

if [ -z "$3" ]
then
	read -p "Nombre de créneaux : " s
        seqs=$s
        if [ -z "$s" ]
        then
                seqs="200"
	fi
else
        seqs=$3
fi

if [ -z "$4" ]
then
	read -p "Nom du fichier de sortie : " file
        file_json=$file
        if [ -z "$file" ]
        then
                file_json="default.json"
	fi
else
        file_json=$4
fi

if [ -z "$5" ]
then
	read -p "Date et heure de départ (dd/mm/YYYY-HH:MM:SS) :" d_t
        d_t_json=$d_t
        if [ -z "$d_t" ]
        then
                d_t_json=`date +"%d/%m/%Y-%T"`
	fi
else
        d_t_json=$5
fi

if [ -z "$6" ]
then
	read -p "Type : PERSONAL ou FACTORY (PERSONAL si rien de spécifié)" type
        type_json=$d_t
        if [ -z "$d_t" ]
        then
                type_json="PERSONAL"
	fi
else
        type_json=$6
fi

#wget https://celestrak.org/NORAD/elements/gp.php?CATNR=38771 -O tle1.txt
#wget https://celestrak.org/NORAD/elements/gp.php?CATNR=44387 -O tle2.txt
#wget https://celestrak.org/NORAD/elements/gp.php?CATNR=25338 -O tle3.txt
#wget https://celestrak.org/NORAD/elements/gp.php?CATNR=28654 -O tle4.txt
#wget https://celestrak.org/NORAD/elements/gp.php?CATNR=33591 -O tle5.txt

#cat tle1.txt tle2.txt tle3.txt tle4.txt tle5.txt > tlesar.txt

python3 besim.py $num $dur $seqs $file_json $d_t_json $type_json

#echo -e "\n$seqs créneaux créés pour la séquence $num de $dur minutes. Liste enregistrée dans "$file_json"\n"
