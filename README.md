# 🌆 Smart Cities - Plataforma de Innovación Urbana

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-303030?style=for-the-badge&logo=pythonanywhere&logoColor=1F90FF)

Smart Cities es una aplicación web integral desarrollada con **Django** como proyecto final para el **Informatorio 2025**. La plataforma funciona como un portal dinámico de noticias y blog enfocado en la transformación digital de las ciudades, sostenibilidad y gestión inteligente.

---

## ✨ Características principales

* **📰 Portal de Noticias:** Visualización de artículos con imágenes y descripciones.
* **📂 Categorización:** Organización de contenidos por temáticas específicas.
* **💬 Interacción:** Sistema de comentarios para fomentar el debate urbano.
* **🛡️ Panel Admin:** Gestión completa de la base de datos para administradores.
* **📱 Diseño Responsivo:** Interfaz optimizada para móviles y escritorio basada en *LeadMark*.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** [Python 3.12](https://www.python.org/)
* **Framework:** [Django 5.0.12](https://www.djangoproject.com/)
* **Base de Datos:** SQLite (Desarrollo) / MySQL (Producción)
* **Estilos:** Bootstrap 5, CSS3 y HTML5.
* **Hosting:** [PythonAnywhere](https://jhorges.pythonanywhere.com/)

---

## 🚀 Instalación y Configuración Local

Seguí estos pasos para ejecutar el proyecto en tu computadora:

### 1. Clonar el repositorio

git clone [https://github.com/tu-usuario/Smart-Citties---Informatorio-2025.git](https://github.com/tu-usuario/Smart-Citties---Informatorio-2025.git)

cd Smart-Citties---Informatorio-2025

### 2. Crear el entorno
python -m venv env

### 3. Activar el entorno (en Windows)
.\env\Scripts\activate

### 4. Instalar dependencias 
pip install -r requirements.txt

### 5. Preparar la Base de Datos
python manage.py makemigrations
python manage.py migrate

### 6. Crear el Administrador(Superuser)
python manage.py createsuperuser

### 7. Iniciar el servidor
python manage.py runserver

### 8. Ingresá 
Ingresá a http://127.0.0.1:8000/ en tu navegador
