-- ARRANQUE DEL CLUSTER --

- Prerrequisitos:
    * Docker Desktop instalado y ejecutandose
    * Tener los puertos necesarios libres

- Iniciar el cluster:
    * Desde el directorio 'hadoop-cluster', ejecutar el comando: docker compose up -d
    * Comprobar que los contenedores namenode y los datanode estan en ejecucion con el comando: docker ps

-- EJECUCION COMANDO WORDCOUNT --

- Accedemos al contenedor namenode con el comando: docker exec -it namenode bash
- Creamos los directorios necesarios para trabajar con el siguiente comando: hdfs dfs -mkdir -p /Sergio/Prueba_WordCount
- Comprobamos que se hayan creado los directorios con el comando: hdfs dfs -ls /Sergio/
- Creamos un archivo de texto para probar el wordcount.
- Subimos el archivo de texto que hayamos creado a nuestro directorio Hadoop con el siguiente comando: hdfs dfs -put test.txt /Sergio/Prueba_WordCount
- Comprobamos que exista ese archivo en el directorio con el comando: hdfs dfs -ls /Sergio/Prueba_WordCount
- Ejecutamos el wordcount sobre ese archivo con el siguiente comando:
    hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar wordcount /Sergio/Prueba_WordCount/test.txt /Sergio/Prueba_WordCount/output
- Comprobamos la salida de la ejecucion del wordcount con el comando: 
    hdfs dfs -cat /Sergio/Prueba_WordCount/output/part-r-00000
