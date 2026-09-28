import sqlite3
from datetime import datetime

import pandas as pd

df_movies = pd.read_csv("DataTransform/movies.csv")
peliculas_validas = set(df_movies['Título'].dropna().tolist())

def simular_streaming_visitantes():
    print("\n🚀 Simulador de Taquilla en Tiempo Real")

    while True:
        try:
            # Captura de datos interactivos desde la terminal
            nombre = input("👤 Ingrese el nombre del visitante: ").strip()
            dni = input("🆔 Ingrese el DNI (8 dígitos): ").strip()
            genero = input("⚥ Ingrese género (M/F): ").strip().upper()
            pelicula = input("🎬 Ingrese el título de la película: ").strip()
            formato = input("🎟️ Ingrese formato (Normal / 3D): ").strip()
            precio_str = input("💲 Ingrese precio del ticket (Dejar vacío para automático): ").strip()
            precio = float(precio_str) if precio_str else (12.0 if formato == '3D' else 8.0)
            fecha_visita = datetime.now().strftime("%Y-%m-%d")

            # 1. Validación en tiempo real: Verificar si la película existe en el catálogo
            if peliculas_validas and pelicula not in peliculas_validas:
                print(f"❌ La película '{pelicula}' no existe en el catálogo de IMDb. Intente de nuevo.\n")
                continue

            # Extraer metadatos de la película si existe
            pelicula_info = df_movies[df_movies['Título'] == pelicula].iloc[0] if (not peliculas_validas.issuperset({pelicula}) and not df_movies[df_movies['Título'] == pelicula].empty) else None
            anio = pelicula_info['Año'] if pelicula_info is not None else None
            gen_pel = pelicula_info['Género'] if pelicula_info is not None else None
            rating = pelicula_info['Rating'] if pelicula_info is not None else None
            votos = pelicula_info['Votos'] if pelicula_info is not None else None

            # 2. Construir el registro completo (enriquecido con datos del DW)
            nuevo_registro = {
                "nombre": nombre,
                "dni": int(dni) if dni.isdigit() else 0,
                "genero": genero,
                "pelicula": pelicula,
                "formato": formato,
                "precio": precio,
                "fecha_visita": fecha_visita,
                "Año": anio,
                "Género": gen_pel,
                "Rating": rating,
                "Votos": votos
            }

            df_nuevo = pd.DataFrame([nuevo_registro])

            # 3. Inyección incremental en visitors.csv (persistencia en origen)
            cols_visitors = ['nombre', 'dni', 'genero', 'pelicula', 'formato', 'precio', 'fecha_visita']

            with open("DataTransform/visitors.csv", mode='a', encoding='utf-8') as f:
                # Extraer los valores en el mismo orden de las columnas
                valores = [str(nuevo_registro[col]) for col in cols_visitors]
                f.write(",".join(valores) + "\n")
                # Forzar el vaciado del búfer al disco inmediatamente
                f.flush()

            # 4. Inyección en tiempo real a la base de datos SQLite (Data Warehouse)
            conn = sqlite3.connect('warehouse.db')
            df_nuevo.to_sql('sales', conn, if_exists='append', index=False)
            conn.close()

            # 5. Generar (yield) el evento procesado hacia el flujo
            print(f"✅ [STREAM SUCCESS] ¡Visitante '{nombre}' inyectado correctamente en tiempo real!\n")
            yield nuevo_registro

        except Exception as e:
            print(f"❌ Error en el flujo de streaming: {e}\n")

# --- Instrucciones de ejecución ---
stream = simular_streaming_visitantes()
for evento in stream:
    print("Datos emitidos:", evento)
