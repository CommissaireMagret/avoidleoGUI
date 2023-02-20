import avoidleo
import argparse
import datetime
import time

# Variables pour mettre en forme le temps.
time_now = time.time()
date_time_format = "%d/%m/%Y-%H:%M:%S"

# Coordonées de la base d'émission (lat, long, alt).

latN = 43.559281
longE = 1.487430
# longW = 360 - longE
qth = (latN, longE, 146)

# Fichier où sont stockées les séquences binaires du PC de simu pour les émissions.
file_path = 'C:\Seb\sequences\\'

# Gestion des arguments en ligne de commande.
parser = argparse.ArgumentParser()
parser.add_argument("num_seq", nargs="?", default="6940", type=str, help='n° séq. bin')
parser.add_argument("duration_seq", nargs="?", default="21", type=int, help='durée séq. en min.')
parser.add_argument("num_cren", nargs="?", default="50", type=int, help='nombre de créneaux')
parser.add_argument("file", nargs="?", default="default", type=str, help="nom fichier sortie (sans extension)")
parser.add_argument("time_start", nargs="?",
                    default=datetime.datetime.fromtimestamp(time_now + 5 * 60).strftime(date_time_format),
                    help='date et heure locale de départ (pas UTC) : dd/mm/YYYY hh:mm:ss')
parsed_args = parser.parse_args()


def genlst():
    # Execution de la fonction pour l'écriture d'un .lst en évitant les LEO.
    avoidleo.writelst(parsed_args.num_seq, parsed_args.duration_seq, parsed_args.num_cren, parsed_args.file,
                      parsed_args.time_start, file_path, qth)
