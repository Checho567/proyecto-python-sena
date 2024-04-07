import sqlite3

# Conexión a la base de datos (se creará si no existe)
conexion = sqlite3.connect('sistema_sena.db')
cursor = conexion.cursor()

# Crear tabla programa
cursor.execute('''CREATE TABLE IF NOT EXISTS programa (
                    id_programa INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_programa VARCHAR(50) NOT NULL
                )''')

# Crear tabla resultado_aprendizaje
cursor.execute('''CREATE TABLE IF NOT EXISTS resultado_aprendizaje (
                    id_resultado_aprendizaje INTEGER PRIMARY KEY AUTOINCREMENT,
                    resultado_aprendizaje VARCHAR(50) NOT NULL
                )''')

# Crear tabla nota
cursor.execute('''CREATE TABLE IF NOT EXISTS nota (
                    id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota INTEGER(100) NOT NULL
                )''')

# Crear tabla instructor
cursor.execute('''CREATE TABLE IF NOT EXISTS instructor (
                    id_instructor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_instructor VARCHAR(50) NOT NULL
                )''')

# Crear tabla tipos de actividad
cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_actividad (
                    id_tipo_actividad INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_actividad VARCHAR(30) NOT NULL
                )''')

# Crear tabla aprendiz
cursor.execute('''CREATE TABLE IF NOT EXISTS aprendiz (
                    id_aprendiz INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20) NOT NULL,
                    ficha INTEGER(8) NOT NULL,
                    jornada VARCHAR(15) NOT NULL,
                    id_programa INTEGER,
                    id_nota INTEGER,
                    id_instructor INTEGER,
                    id_actividad INTEGER,
                    FOREIGN KEY (id_programa) REFERENCES programa(id_programa),
                    FOREIGN KEY (id_nota) REFERENCES nota(id_nota),
                    FOREIGN KEY (id_instructor) REFERENCES instructor(id_instructor),
                    FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad)
                )''')

# Crear tabla competencia
cursor.execute('''CREATE TABLE IF NOT EXISTS competencia (
                    id_competencia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_competencia VARCHAR(50) NOT NULL,
                    id_programa INTEGER,
                    id_resultado_aprendizaje INTEGER,
                    FOREIGN KEY (id_programa) REFERENCES programa(id_programa),
                    FOREIGN KEY (id_resultado_aprendizaje) REFERENCES resultado_aprendizaje(id_resultado_aprendizaje)
                )''')

# Crear tabla actividad
cursor.execute('''CREATE TABLE IF NOT EXISTS actividad (
                    id_actividad INTEGER PRIMARY KEY AUTOINCREMENT,
                    descripcion_actividad VARCHAR(400) NOT NULL,
                    fecha_asignacion VARCHAR(100) NOT NULL,
                    fecha_entrega VARCHAR(100) NOT NULL,
                    id_tipo_actividad INTEGER,
                    id_nota INTEGER,
                    id_instructor INTEGER,
                    FOREIGN KEY (id_nota) REFERENCES nota(id_nota),
                    FOREIGN KEY (id_tipo_actividad) REFERENCES tipo_actividad(id_tipo_actividad),
                    FOREIGN KEY (id_instructor) REFERENCES instructor(id_instructor)
                )''')

datos_resultado_aprendizaje = [
    ('aprobado',),
    ('plan de mejoramiento',),
    ('por evaluar',),
    ('citado a comité',)
]
cursor.executemany("INSERT INTO resultado_aprendizaje (resultado_aprendizaje) VALUES (?)", datos_resultado_aprendizaje)

tipos_actividad = [
    ('Actividad',),
    ('Plan de mejoramiento',)
]
cursor.executemany("INSERT INTO tipo_actividad (tipo_actividad) VALUES (?)", tipos_actividad)

programa = [
    ('ADSO',),
    ('Gestion empresarial',)
]
cursor.executemany("INSERT INTO programa (nombre_programa) VALUES (?)", programa)

instructor = [
    ('Edgar Delgado',),
    ('Amparo Rueda',)
]
cursor.executemany("INSERT INTO instructor (nombre_instructor) VALUES (?)", instructor)

notas = [
    [10,],
    [20,],
    [30,],
    [40,],
    [50,],
    [60,],
    [70,],
    [80,],
    [90,],
    [100,]
]
cursor.executemany("INSERT INTO nota (nota) VALUES (?)", notas)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
