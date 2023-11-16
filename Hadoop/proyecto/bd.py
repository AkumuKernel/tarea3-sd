import subprocess
import psycopg2

connection = psycopg2.connect(  user = "postgres",
                                password = "postgres",
                                host = "db",
                                port = "5432",
                                database = "proyecto")

try:
    cursor = connection.cursor()

    for i in range(30):
        if (i<15):
            output = subprocess.check_output(f"cat 1_15/search{i+1}.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py", shell=True)
        else:
            output = subprocess.check_output(f"cat 16_30/search{i+1}.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py", shell=True)

        lineas = output.split()
        contador=0
        for each in lineas:
            lineas[contador] = each.decode("utf-8")
            contador+=1

        print(f"{imprimir} - {len(lineas)}")
        valor=0
        while (valor<len(lineas)):
            cursor.execute(f"INSERT INTO registros (palabra,numero,archivo) VALUES ({lineas[valor]},{lineas[valor+1]},{imprimir})")
            valor+=2
        
    cursor.execute("SELECT * FROM registros ORDER BY palabra DESC")
    registros.cursor.fetchall()
    for linea in registros:
        print(row)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")