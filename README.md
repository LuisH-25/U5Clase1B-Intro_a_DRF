# Unidad 5 Clase 1B
Se avanzo otra forma de hacer djangorestframework en el aplicativo "todos"

### Instalaciones iniciales
- virtualenv env
- source env/Scripts/activate
- pip install django
- pip install djangorestframework
- django-admin startapp todos

### Pasos para usar la DB:
- crear la DB: U5Clase1B en MySql
- python manage.py makemigrations
- python manage.py migrate

### URL del taller:
http://127.0.0.1:8000/api/todos

### Resumen de la aplicacion "todos":
- En serializers.py defino:
    * Que atributos jalo del model
    * que atributos no son editables en el api
* api.py de todos = views.py de MyAPI
- En urls.py
    * from .api import TodoViewSet
    * router = routers.DefaultRouter(trailing_slash=False)
    * urlpatterns = router.urls
* no se edita en: views.py

### archivos nuevos y editados
* todos/api.py
* todos/models.py
* todos/views.py

### Link de la clase
- Por completar
