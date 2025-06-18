# ☕ Coffee Shop – Plataforma de pedidos en línea

**Este proyecto forma parte de mi proceso de aprendizaje del curso “Desarrollo Web con Django” dictado en Platzi.**  
Se desarrolló una aplicación tipo Coffee Shop para aplicar conceptos de vistas, modelos, formularios, autenticación y diseño responsivo con TailwindCSS.

---

## 🚀 Funcionalidades principales

- Registro e inicio de sesión de usuarios
- Listado de productos con imágenes y precios
- Agregar productos a una orden
- Visualizar detalles de cada orden
- Panel administrativo de Django
- Interfaz responsiva y moderna con TailwindCSS

---

## 🛠️ Tecnologías utilizadas

- [Python 3.11+](https://www.python.org/)
- [Django 5.2+](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [SQLite3](https://www.sqlite.org/) (base de datos por defecto)
- [Git](https://git-scm.com/) y GitHub para control de versiones

---

## 📦 Instalación del proyecto

### 🔧 Requisitos previos

- Python 3 instalado y configurado en el PATH
- Git (opcional, pero recomendado)
- Editor de código como VS Code

### ▶️ Pasos para ejecutar localmente

1. **Clona el repositorio:**

```bash
git clone https://github.com/medison0001/django-platzi-course.git coffee_shop
cd coffee_shop
```

2. **Crea y activa un entorno virtual:**

```bash
python -m venv venv
# En Windows PowerShell
.env\Scripts\Activate.ps1
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Aplica las migraciones y crea un superusuario:**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Ejecuta el servidor:**

```bash
python manage.py runserver
```

6. Abre en tu navegador:

```
http://localhost:8000/
```

---

## 🔐 Autenticación

- Usa el sistema de autenticación de Django.
- El login está personalizado con un formulario estilizado con TailwindCSS.
- Solo usuarios autenticados pueden agregar productos o ver órdenes.

---

## 📁 Estructura de carpetas relevante

```
coffee_shop/
│
├── products/          # App para productos
├── orders/            # App para órdenes
├── templates/         # Plantillas HTML
├── static/            # Archivos estáticos
├── db.sqlite3         # Base de datos local
├── manage.py
└── requirements.txt
```

---

## 📸 Captura de pantalla (opcional)

Puedes incluir aquí una imagen como:

```markdown
![Pantalla principal](https://ruta-a-tu-imagen.png)
```

---

## ✍️ Autor

**Edison Monsalve**  
📧 edison@email.com  
🔗 [LinkedIn](https://linkedin.com/in/tu-perfil) | [GitHub](https://github.com/medison0001)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 🎯 Próximas mejoras (ideas)

- Agregar carrito de compras persistente
- Implementar pasarela de pagos (ej. Stripe)
- Generación de facturas en PDF
- API REST con Django Rest Framework

---

## 🙌 Créditos

Este proyecto fue desarrollado como parte del curso **"Django Web Framework"** en [Platzi](https://platzi.com/).  
Agradezco a los instructores y a la comunidad por su apoyo en el proceso de aprendizaje.