# Tarea 3 Sistemas Distribuidos

Tarea 3 de Sistemas Distribuidos EIT UDP CIT-2011

## Obtención
Para poder tener los contenedores hechos para esta actividad se tiene que hacer el siguiente comando:
```sh
git clone https://github.com/AkumuKernel/tarea3-sd.git
```

## Acciones previas

Antes de iniciar el docker compose se debe poner el siguiente comando para que todo funcione de manera correcta, en el caso de sistemas Unix:
```sh
sudo chmod +x Hadoop/proyecto/docker-entrypoint.sh
```

## Ejecución de instancias
Para poder ejecutar los contenedores que fueron descargados gracias al paso anterior, se debe hacer lo siguiente en la carpeta raíz del proyecto:
```sh
docker compose up -d --build
```

Para así poder iniciar los contenedores deseados.

## Acceso a los contenedores

Para acceder al contenedor para la ejecución correcta de los datos:

### Para Hadoop
```sh
docker exec -it hadoop bash
```

### Para el acceso a la base de datos
```sh
docker exec -it db bash
```

## Ejecución del programa paso a paso

Dentro del contenedor de Hadoop se deben ingresar los siguientes comandos:
Creación de carpeta para usuario:
```sh
hdfs dfs -mkdir /user
```
Creación de usuario en el directorio:
```sh
hdfs dfs -mkdir /user/hduser
```
Creación de directorio para el procesamiento archivos y/o textos:
```sh
hdfs dfs -mkdir input
```
Conseder el acceso completo al usuario.
```sh
sudo chown -R hduser .
```
Cargar los txt extraidos de wikipedia a hadoop mediante los siguientes comandos.
Acceder a la carpeta dónde están los archivos
```sh
cd proyecto/
```
Ejecutar el programa que obtiene los archivos
```sh
python api.py
```
Ejecutar hdfs
```sh
hdfs dfs -put */*.txt input
```
Validar el proceso
```sh
hdfs dfs -ls input
```
Ejecutar tanto el mapper como el reducer de hadoop.

```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py
```
Extraer los archivos procesados
```sh
hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/proyecto
```
Iniciar buscador
```sh
python buscador.py
```

## Ejecución del programa de forma simplificada
Ejecutar el programa completo
```sh
bash busqueda.sh
```

