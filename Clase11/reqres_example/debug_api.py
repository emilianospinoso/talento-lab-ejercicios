import requests
import json

def debug_api_connection():
    print("🔍 Diagnosticando conexión a reqres.in...")
    
    try:
        # Test básico de conectividad
        print("\n1. Probando conectividad básica...")
        response = requests.get("https://reqres.in/api/users?page=1", timeout=10)
        
        print(f"   Status Code: {response.status_code}")
        print(f"   URL final: {response.url}")
        print(f"   Headers: {dict(response.headers)}")
        
        if response.status_code == 401:
            print("   ❌ Error 401 - Unauthorized")
            print("   🔧 Posibles causas:")
            print("      - Proxy corporativo/universitario")
            print("      - Firewall bloqueando reqres.in")
            print("      - Problema temporal con reqres.in")
        
        try:
            data = response.json()
            print(f"   Response body: {json.dumps(data, indent=2)}")
        except:
            print(f"   Response text: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error de conexión: {e}")
    
    # Test con una API alternativa
    print("\n2. Probando API alternativa (jsonplaceholder)...")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
        print(f"   Status Code: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Conexión a APIs externas funciona")
        else:
            print("   ❌ Problema general de conectividad")
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    debug_api_connection()