from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Configurar la conexión a PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="estudiantes",
        user="root",
        password="",
        cursor_factory=RealDictCursor
    )

@app.get("/estudiantes")
async def obtener_estudiantes():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM estudiantes;")
            estudiantes = cursor.fetchall()
            return estudiantes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
