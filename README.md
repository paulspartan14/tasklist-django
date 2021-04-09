#### crear entorno virtual

```
virtualenv env
```

#### entrar al entorno virtual e instalar el requirements.txt

```
source env/bin/activate
pip install -r requirements.txt
```

# crear el archivo '.env.local' en base al '.env.example' y exportar variables 

```
cp .env.example .env.local
source .env.local
```

#### correr proyecto django

```
python manage.py runserver
```
