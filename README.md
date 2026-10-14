Pasos para instalar la carpeta y sus diferentes archivos
-------------
1. Primero se clona el archivo desde el repositorio de GitHub:
git clone https://github.com/Sebas28290/Eva_SumativaU2.git

2. Luego se entra a la carpeta:
cd Eva_SumativaU2

3. Se crea el entorno virtual:
python -m venv .venv

4. Se activa el entorno virtual:
.venv/Scripts7/activate

5. Si tiene errores para ingresar al entorno virtual utilizar este comando:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
6. Instalar los diferentes requerimientos del proyecto:
pip install -r requirements.txt

7. Correr el entorno virtual:
python manage.py runserver

8. Ingresar según las credenciales que tenga.