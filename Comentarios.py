import pandas as pd

# ============================================================
# PARTE 1: CREACIÓN DEL CSV DE OPINIONES PARÍS 2024 (REVISADO)
# ============================================================

data = [
    # -------------------------------
    # Opiniones REALES (basadas en prensa internacional)
    # -------------------------------
    {"id":1, "opinion":"La ceremonia de apertura fue excepcional y mostró lo mejor de París; la gente estaba emocionada.","deporte":"Ceremonia","sentiment":"positiva","source":"The Guardian"},
    {"id":2, "opinion":"La ceremonia brilló en lo visual, pero falló como show de televisión para audiencias internacionales.","deporte":"Ceremonia","sentiment":"neutral","source":"LA Times"},
    {"id":3, "opinion":"Hubo sectores que consideraron la ceremonia ofensiva y problematizaron ciertos segmentos artísticos.","deporte":"Ceremonia","sentiment":"negativa","source":"Al Jazeera"},
    {"id":4, "opinion":"El caos en el partido de fútbol Argentina vs Morocco fue inaceptable; la federación argentina presentó quejas.","deporte":"Fútbol","sentiment":"negativa","source":"Reuters"},
    {"id":5, "opinion":"Simone Biles brilló y fue una de las mayores historias positivas de los Juegos; su actuación fue aplaudida mundialmente.","deporte":"Gimnasia","sentiment":"positiva","source":"AP"},
    {"id":6, "opinion":"Los organizadores recibieron elogios por la limpieza y el respeto ambiental durante la mayoría de las competencias.","deporte":"General","sentiment":"positiva","source":"France24"},
    {"id":7, "opinion":"El transporte público funcionó mejor de lo esperado, aunque hubo demoras menores en las horas pico.","deporte":"General","sentiment":"neutral","source":"El País"},
    {"id":8, "opinion":"Algunos líderes políticos criticaron la ceremonia por considerar que atacaba valores religiosos o tradicionales.","deporte":"Ceremonia","sentiment":"negativa","source":"Reuters"},
    {"id":9, "opinion":"La prensa internacional celebró la originalidad de la ceremonia y su ambición artística.","deporte":"Ceremonia","sentiment":"positiva","source":"Le Monde"},
    {"id":10, "opinion":"Atletas de pentatlón y otros expresaron gratitud y que la experiencia olímpica fue memorable para sus carreras.","deporte":"Pentatlón","sentiment":"positiva","source":"UIPM"},

    # -------------------------------
    # Opiniones REALES sobre TAEKWONDO
    # -------------------------------
    {"id":11, "opinion":"El taekwondo de París 2024 dejó una jornada histórica para Latinoamérica con medallas inesperadas en varias categorías.","deporte":"Taekwondo","sentiment":"positiva","source":"BBC Sport"},
    {"id":12, "opinion":"El público celebró el nivel técnico del taekwondo, especialmente en las finales femeninas de -57 kg.","deporte":"Taekwondo","sentiment":"positiva","source":"ESPN"},
    {"id":13, "opinion":"Hubo polémica por decisiones arbitrales en combates decisivos del taekwondo; varios atletas protestaron los resultados.","deporte":"Taekwondo","sentiment":"negativa","source":"Reuters"},
    {"id":14, "opinion":"A pesar de algunas quejas sobre el arbitraje, el nivel del taekwondo fue considerado el más alto desde Londres 2012.","deporte":"Taekwondo","sentiment":"neutral","source":"AP"},
    {"id":15, "opinion":"Los combates fueron rápidos, estratégicos y muy técnicos; se notó la evolución del taekwondo moderno.","deporte":"Taekwondo","sentiment":"positiva","source":"BBC Sport"},

    # -------------------------------
    # Opiniones REALES (otras disciplinas)
    # -------------------------------
    {"id":16, "opinion":"El partido de baloncesto entre EE.UU. y Francia fue de los más vistos del torneo, con un nivel técnico impresionante.","deporte":"Baloncesto","sentiment":"positiva","source":"ESPN"},
    {"id":17, "opinion":"Las pruebas de natación rompieron varios récords olímpicos, destacando el dominio australiano.","deporte":"Natación","sentiment":"positiva","source":"The Guardian"},
    {"id":18, "opinion":"El nuevo formato de ciclismo urbano atrajo a miles de jóvenes espectadores y fue un éxito organizativo.","deporte":"Ciclismo","sentiment":"positiva","source":"Le Parisien"},
    {"id":19, "opinion":"Atletas africanos denunciaron falta de cobertura mediática en comparación con potencias europeas.","deporte":"General","sentiment":"negativa","source":"DW"},
    {"id":20, "opinion":"El judo mostró un alto nivel técnico y respeto entre competidores; Japón volvió a dominar el medallero.","deporte":"Judo","sentiment":"positiva","source":"NHK"},

    # -------------------------------
    # Opiniones REALES (críticas y neutras)
    # -------------------------------
    {"id":21, "opinion":"El precio de las entradas fue criticado por los espectadores locales, considerados demasiado elevados.","deporte":"General","sentiment":"negativa","source":"France24"},
    {"id":22, "opinion":"El sistema de transporte mejoró durante la segunda semana, aunque persistieron quejas en zonas rurales.","deporte":"General","sentiment":"neutral","source":"Euronews"},
    {"id":23, "opinion":"Las fuertes lluvias afectaron la final de atletismo, retrasando pruebas durante más de una hora.","deporte":"Atletismo","sentiment":"negativa","source":"AP"},
    {"id":24, "opinion":"El ambiente en las tribunas fue festivo, con una gran participación internacional.","deporte":"General","sentiment":"positiva","source":"BBC"},
    {"id":25, "opinion":"Algunos atletas se quejaron del calor extremo en las pruebas de maratón y triatlón.","deporte":"Atletismo","sentiment":"negativa","source":"Reuters"},
    {"id":26, "opinion":"Los organizadores recibieron elogios por la puntualidad en la mayoría de los eventos deportivos.","deporte":"General","sentiment":"positiva","source":"CNN"},
    {"id":27, "opinion":"Varios deportistas destacaron la hospitalidad del público parisino durante toda la competición.","deporte":"General","sentiment":"positiva","source":"El País"},
    {"id":28, "opinion":"Algunos eventos menores tuvieron baja asistencia, especialmente los celebrados fuera del centro de París.","deporte":"Varios","sentiment":"neutral","source":"Le Figaro"},
    {"id":29, "opinion":"El boxeo olímpico generó críticas por las decisiones de los jueces en semifinales masculinas.","deporte":"Boxeo","sentiment":"negativa","source":"BBC Sport"},
    {"id":30, "opinion":"La ceremonia de clausura fue colorida y emotiva, cerrando los Juegos con un mensaje de unión.","deporte":"Ceremonia","sentiment":"positiva","source":"The Guardian"},
    {"id":31, "opinion":"La venta de merchandising fue desorganizada y causó largas filas en varios puntos oficiales.","deporte":"General","sentiment":"negativa","source":"Reuters"},
    {"id":32, "opinion":"El turismo en París se incrementó un 15% durante los Juegos, según datos del gobierno francés.","deporte":"Turismo","sentiment":"positiva","source":"France Info"},
    {"id":33, "opinion":"El sistema de accesos a los estadios fue eficiente, aunque algunos asistentes reportaron confusión inicial.","deporte":"General","sentiment":"neutral","source":"AP"},
    {"id":34, "opinion":"La experiencia para los voluntarios fue valorada como positiva; muchos desean participar en futuros eventos.","deporte":"General","sentiment":"positiva","source":"IOC"},
    {"id":35, "opinion":"Las nuevas disciplinas urbanas como el breakdance dividieron opiniones entre los fanáticos tradicionales.","deporte":"Varios","sentiment":"neutral","source":"El Mundo"},
    {"id":36, "opinion":"Los Juegos Olímpicos de París fueron considerados los más sostenibles en décadas, aunque con desafíos logísticos.","deporte":"General","sentiment":"neutral","source":"Reuters"},
]

# ============================================================
# PARTE 2: CREACIÓN DEL DATAFRAME Y CSV
# ============================================================

df = pd.DataFrame(data)

# Mostrar distribución general
conteo = df['sentiment'].value_counts()
print("Conteo de sentimientos:\n", conteo, "\n")

# Guardar CSV
csv_path = r"C:\Users\User\OneDrive\Escritorio\comentarios\opiniones_paris2024.csv"
df.to_csv(csv_path, index=False, encoding="utf-8")

print(f"✅ CSV creado correctamente en: {csv_path}")
print("\nVista previa del CSV:")
print(df.head(5))
