#!/usr/bin/env python3
"""
verificar_setup.py -- Comprueba la conexión con el proxy.
Verifica tres cosas: que el proxy responde, que la clave funciona
y lista los modelos disponibles.
"""

import os
import urllib.request
import urllib.error
import json

print("=== Verificación de conexión para el taller ===\n")
errores = []

# Configuración (editar o cargar desde .env)
PROXY_URL = os.getenv("PROXY_URL", "https://aulife-proxy-66041181251.europe-west1.run.app")
API_KEY = os.getenv("API_KEY", "")

if not API_KEY:
    print("Aviso: no se ha encontrado API_KEY en las variables de entorno.")
    print("Puedes definirla con: export API_KEY=tu-clave-aquí\n")
    API_KEY = input("Introduce tu clave: ").strip()

# 1. Conexión al proxy
print("[1/3] Conexión al proxy:", end=" ")
try:
    req = urllib.request.Request(f"{PROXY_URL}/health")
    with urllib.request.urlopen(req, timeout=5) as resp:
        if resp.status == 200:
            print(f"OK ({PROXY_URL})")
        else:
            print(f"Respuesta inesperada: {resp.status}")
            errores.append("El proxy no responde correctamente")
except Exception as e:
    print(f"ERROR: {e}")
    errores.append("No se puede conectar al proxy")

# 2. Listar modelos disponibles
print("[2/3] Modelos disponibles:", end=" ")
modelos = []
primer_modelo = None
if not errores and API_KEY:
    try:
        req = urllib.request.Request(
            f"{PROXY_URL}/v1/models",
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            resultado = json.loads(resp.read().decode("utf-8"))
            modelos = [m["id"] for m in resultado.get("data", [])]
            if modelos:
                primer_modelo = modelos[0]
                print(f"OK ({len(modelos)} modelos)")
                for m in modelos:
                    print(f"      - {m}")
            else:
                print("Sin modelos disponibles")
                errores.append("No hay modelos configurados en el proxy")
    except Exception as e:
        print(f"ERROR: {e}")
        errores.append("No se pueden listar los modelos")
else:
    print("SALTADA (faltan requisitos previos)")

# 3. Llamada de prueba (usa el primer modelo disponible)
print(f"[3/3] Llamada de prueba al modelo:", end=" ")
if not errores and API_KEY and primer_modelo:
    try:
        datos = json.dumps({
            "model": primer_modelo,
            "messages": [{"role": "user", "content": "Di 'OK' y nada más."}],
            "max_tokens": 256,
            "metadata": {"request_type": "dev", "tags": ["dev"]},
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{PROXY_URL}/v1/chat/completions",
            data=datos,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            resultado = json.loads(resp.read().decode("utf-8"))
            texto = resultado["choices"][0]["message"]["content"].strip()
            print(f"OK (modelo: {primer_modelo}, respuesta: '{texto}')")
    except Exception as e:
        print(f"ERROR: {e}")
        errores.append("Fallo en la llamada al modelo")
else:
    print("SALTADA (faltan requisitos previos)")

# Resumen
print("\n" + "=" * 50)
if errores:
    print(f"HAY {len(errores)} PROBLEMA(S):")
    for e in errores:
        print(f"  - {e}")
    print("\nResuelve los problemas y vuelve a ejecutar este script.")
else:
    print("TODO LISTO. Puedes empezar a programar.")
