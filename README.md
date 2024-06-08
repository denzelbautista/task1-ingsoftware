# Tarea 1 - Ingeniería de Software, Test Driven Development

Alumno: Denzel Bautista Rodriguez

Docente: Eric Biagioli

## Proceso de ejecución del mini proyecto: geoapi

Estos pasos serán para una computadora con linux, o utilizando la consola gitbash en windows

1. Crear entorno virtual

```shell
$ python3 -m venv .venv
```

2. Entrar al entorno virtual

```shell
# Ubuntu
$ source .venv/bin/activate

# Windows - Git Bash
$ source .venv/Scripts/activate
```

3. Instalar las dependencias

```shell
$ pip install -r requirements.txt
``` 

4. Correr los tests

```shell
$ pytest --cov=src/geoapi --cov-report=term-missing test/test_geoapi.py
``` 
