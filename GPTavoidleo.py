# from datetime import datetime, timedelta
# import requests
# from skyfield.sgp4lib import EarthSatellite
#
#
# # Fonction pour télécharger les TLE depuis le lien direct
# def download_tle(url):
#     response = requests.get(url)
#     tle_data = response.text.split('\n')
#     return tle_data
#
# # Fonction pour calculer l'élévation d'un satellite à un point géographique à un moment donné
# def calculate_elevation(tle_data, lat, lon, alt, timestamp):
#     from skyfield.api import Loader, Topos
#
#     # Chargement des éphémérides et définition de la position de la station sol
#     load = Loader('/home/robin/PycharmProjects/avoidleoGUI/skyfield-data')
#     ts = load.timescale()
#     planets = load('de421.bsp')
#     earth = planets['earth']
#     station = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=alt)
#
#     # Récupération des TLE et définition de l'objet satellite
#     satellite = None
#     for i in range(0, len(tle_data)-1, 2):
#         if tle_data[i].startswith('1'):
#             name = tle_data[i].strip()
#             line1 = tle_data[i+1].strip()
#             line2 = tle_data[i+2].strip()
#             tle = name + '\n' + line1 + '\n' + line2
#             satellite = earth.satellite(name=name, line1=tle.split('\n')[1], line2=tle.split('\n')[2])
#             break
#
#     # Calcul de l'élévation du satellite à la position de la station sol
#     t = ts.utc(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
#     diff = satellite - station
#     topocentric = diff.at(t).frame_latlon(station)
#     elevation = topocentric.altaz()[0].degrees
#
#     return elevation
#
# # Fonction pour vérifier si un créneau horaire est disponible en ne trouvant aucun satellite en visibilité pendant la durée du créneau
# def is_slot_available(tle_data, lat, lon, alt, start_time, duration):
#     timestep = timedelta(seconds=30)
#     timestamp = start_time
#     while timestamp < start_time + timedelta(minutes=duration):
#         elevation = calculate_elevation(tle_data, lat, lon, alt, timestamp)
#         if elevation >= 5:
#             return False
#         timestamp += timestep
#     return True
#
# # Cette fonction prend en entrée les paramètres slot_duration, num_slots, output_file et observer, où observer est
# # l'objet Observer créé à partir des coordonnées géographiques. La fonction utilise également la bibliothèque
# # python-skyfield pour le traitement des TLE.
# # Fonction pour générer le fichier de sortie avec les créneaux horaires trouvés
# def generate_slots_file(slot_duration: int, num_slots: int, output_file: str, observer: Observer):
#     # Récupération des TLE depuis le lien fourni
#     satellites = fetch_tle(url)
#
#     # Génération de la liste de temps de début et de fin pour chaque créneau horaire
#     start_times = []
#     end_times = []
#     current_time = datetime.now()
#     for i in range(num_slots):
#         start_times.append(current_time)
#         current_time += timedelta(minutes=slot_duration)
#         end_times.append(current_time)
#
#     # Itération sur chaque créneau et chaque satellite pour vérifier si le satellite est visible
#     valid_slots = []
#     for start_time, end_time in zip(start_times, end_times):
#         visible = False
#         for sat in satellites:
#             t = ts.utc(start_time)
#             tle = EarthSatellite(sat['line1'], sat['line2'], sat['name'], ts)
#             difference = tle - observer
#             _, _, distance = difference.at(t).position.km
#             altitude = distance - observer.elevation.km
#             if altitude >= 5:
#                 visible = True
#                 break
#         if not visible:
#             valid_slots.append((start_time, end_time))
#
#     # Si aucun créneau n'est valide, on affiche un message d'erreur
#     if not valid_slots:
#         print("Aucun créneau valide trouvé. Durée du créneau trop longue.")
#     else:
#         # Création du fichier de sortie
#         with open(output_file, "w") as f:
#             for start_time, end_time in valid_slots:
#                 f.write(f"{start_time.isoformat()},{end_time.isoformat()}\n")
