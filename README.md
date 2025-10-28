# 📇 Modulo de control de novedades empleados / RRHH - Odoo 8

## Nombre Tecnico: **odoo8_module_news_distefano**

📇Módulo administrativo para gestión de novedades de empleados (RRHH)
Este módulo, desarrollado para Odoo 8, permite gestionar y registrar novedades internas de RRHH para cada empleado de manera eficiente. Facilita la documentación de incidencias como faltas, ausencias, permisos, sanciones y otras novedades, asociadas directamente al empleado correspondiente.

Además, el módulo permite generar reportes anuales de novedades por empleado de forma automática, utilizando un código único para cada registro, generado a partir de las iniciales del empleado y el año del incidente.

Con esta herramienta, la gestión de RRHH se vuelve más ordenada, auditable y fácil de consultar, proporcionando información clara para la elaboración de reportes laborales y optimizando la administración de la planilla.

## 📱MODULO IMPLEMENTADO - ODOO8
 - 🌐 **URL DB NO.1:** [**AE_SOLUTIONS**](http://64.181.217.115/web)
 - 🌐 **URL DB NO.2:** [**DISTEFANO_RC**](http://40.233.20.224:8069/web)
### 🔐 *PARA ACCESO A BASES DE DATOS EN SERVIDOR/ODOO WEB, SOLICITAR CREDENCIALES A DESARROLLADORES RESPONSABLES* ‼️

---

## ⚙️ Características Especiales

El módulo de **Novedades de Empleados para RRHH - Odoo 8** incluye funcionalidades intuitivas que facilitan la gestión de incidencias laborales de manera profesional y organizada:

- **Vistas completas:** Tanto las novedades como los tipos de novedades cuentan con **vistas Tree, Form y Search**, incluyendo filtros de búsqueda y opciones de agrupación.
- **Calendario individual:** Las novedades incluyen una vista de **calendario**, permitiendo una mejor organización y visualización de incidencias por empleado.
- **Integración con RRHH:** El módulo funciona sobre el módulo de **Recursos Humanos de Odoo 8**, obteniendo automáticamente información del empleado como nombre, departamento, cargo y correo electrónico.
- **Fechas de inicio y fin:** Cada noticia o incidencia tiene un rango temporal definido para indicar su duración.
- **Descripción detallada:** Campo de descripción que permite añadir información adicional sobre cada novedad.
- **Reportes PDF:** Los reportes se generan agrupando las novedades por mes, incluyendo toda la información relevante del empleado y sus incidentes o  noticias.
- **Seguridad y permisos:** Solo accesible para usuarios pertenecientes al grupo **Manager** del sistema de Odoo en el módulo de Recursos Humanos.
- **Instalable:** ✅ Sí 

### ✅ Resumen de Vistas y Funcionalidades
| Funcionalidad          | Vista / Acción                       |
|------------------------|------------------------------------|
| Novedades              | Tree, Form, Search, Calendar       |
| Tipos de Novedades     | Tree, Form, Search                  |
| Reportes PDF            | Wizard - generación por empleado y mes |
| Integración con RRHH    | Obtiene nombre, cargo, departamento y correo del empleado |
| Seguridad               | Acceso restringido a grupo Manager |

---

## 📋 Manual de Usuario

### Acceso al Módulo
1. Ingresar a Odoo 8 como usuario con permisos de **Manager** del modulo de Recursos Humanos de odoo.
2. Navegar al menú de **Noticias R.R.H.H**.

### Gestión de Noticias
- **Crear Novedad:**
  1. Hacer clic en el boton de **Crear** en el apartado de Noticias.
  2. Seleccionar el **Empleado**.
  3. Definir la **Fecha de inicio** y, si aplica, la **Fecha de fin**.
  4. Elegir el **Tipo de noticia**.
  5. Añadir una **Descripción detallada** si es necesario.
  6. Guardar el registro.
- **Visualización:**
  - Tree: Lista general de todas las novedades, con búsqueda y filtros por empleado, tipo, fechas, departamento, etc.
  - Form: Detalle completo de cada novedad.
  - Calendar: Vista de calendario para seguimiento mensual de incidencias.

### Gestión de Tipos de Novedades
- **Crear Tipo de Novedad:**
  1. Ir al menú de **Clasificacion Noticias**.
  2. Crear un nuevo tipo y asignarle un nombre unico y descriptivo.
- **Visualización:**
  - Tree: Lista de todos los tipos creados.
  - Form: Detalle del tipo de novedad, mostrando las noticias asociadas.

### Generación de Reportes PDF
1. Seleccionar una **noticia específica** en el listado para visualizar su detalle..
2. Hacer clic en **Generar PDF**.
3. El sistema generará un reporte en base al codigo obteniendo todas las noticias del empleado en el año del codigo, agrupando por **meses** las noticias encontradas, incluyendo información completa del empleado y la descripción de cada novedad.

--- 

## 🔐 Roles y Permisos
### Consideraciones de Seguridad
- Solo los usuarios del **grupo Manager** del modulo de Recursos Humanos de odoo pueden acceder a este módulo.
- Los reportes PDF y la creación de novedades están restringidos según permisos del usuario.
- Se recomienda mantener actualizado el grupo de Managers y revisar permisos periódicamente.

---

## 💻 Tecnologías Utilizadas
| Componente        | Tecnología   | Versión     |
|-------------------|-------------|-------------|
| **Framework**     | Odoo (OpenERP) | 8.0 |
| **Backend** | Python | 2.7 |
| **Frontend** | XML | - |
| **Pillow** | Python | 2.7 o anteriores |
| **Base de Datos** | PostgreSQL | 9.6 |
| **Arquitectura**  | MVC Pattern | - |
| **Dependencias**  | base, web, hr | - |
| **Reportes PDF**  | ReportLab | 3.0+ |

---

## 📋 Manual de Usuario Tecnico

### 🚀 Instalación y Configuración

### 📋 Requisitos Previos
- Instancia funcional de **Odoo 8**.
- **Python 2.7** (ya incluido con Odoo 8).
- Acceso a la carpeta de **addons** de Odoo.
- Permisos de **Manager** en Recursos Humanos para usar todas las funcionalidades del módulo.

### 🔧 Instalación

#### **Paso 1: Clonar el Repositorio**
**1.1 Navegar a la carpeta de addons de tu instancia Odoo 8**

```
cd /path/to/odoo/addons
```

**1.2 Clonar repositorio del módulo dentro de la carpeta**
 *Solicitar acceso al repositorio a los desarrolladores responsables.*
```
git clone https://github.com/Distefano-Desarrollo/odoo8_module_news_distefano.git
```

#### **Paso 2: Actualizar la Lista de Módulos**
- En la **interfaz de Odoo**: Configuración > Módulos > Actualizar lista de módulos (Settings > Modules > Update Modules List)

#### **Paso 3: Instalar el Módulo**
- **3.1** - En la **interfaz de Odoo**: Configuración > Módulos > Modulos locales (Settings > Modules > Local Modules)
- **3.2** - **Buscar** módulo: **Modulo de Noticias empleados RRHH - Distefano** o nombre tecnico: **odoo8_module_news_distefano** 
- **3.3** - **Instalar** y recargar la interfaz de odoo

#### **Paso 4: Configuración de Roles y Permisos**
- **4.1** - Acceder como **Administrador** (con acceso a *Technical Features*) y activar **modo desarrollador**
- **4.2** - Configuración > Usuarios > *Grupos* (Settings > Users > Groups) y verificar que exista el grupo **Manager del modulo de Recursos Humanos**
- **4.3** - En la misma ventana Usuarios > Usuarios (Users > Users): editar el usuario actual y asignarle el grupo **Manager** del modulo de RRHH para poder acceder al módulo y visualizar los menus recargando la pagina.

---

### 🔄 Actualización a Nuevas Versiones
- **Paso 1:** - Desinstalar el módulo desde:  Configuración > Módulos > Modulos locales (Settings > Modules > Local Modules)
- **Paso 2:** - **Ingresar a la carpeta del módulo de addons y ejecutar git pull para actualizar a la última versión**.
 ```
 cd addons/odoo8_module_news_distefano/
 ```
- **Paso 3:** - Reinstalar el módulo desde la interfaz.

---

---

## 🗂️ Estructura del Proyecto

```
odoo8_module_news_distefano/
├── models/
│   ├── __init__.py                  # Importación de todos los modelos y wizards
│   ├── new.py                       # Modelo de noticias
│   ├── type.py                      # Modelo de tipos de noticias
│   └── news_report_wizard.py        # Wizard para generar reportes PDF
│   
├── security/
│   └── ir.model.access.csv          # Permisos y reglas CSV para permisos de grupos y modelos
|
├── views/
│   ├── new/new_tree_view.xml            # Vistas Tree de novedades
│   ├── new/new_form_view.xml            # Vistas Form de novedades
│   ├── new/new_search_view.xml          # Vistas Search de novedades con filtros y agrupación
│   ├── new/new_calendar_view.xml        # Vista de calendario para mejor visualización de novedades
│   ├── type/type_tree_view.xml          # Vistas Tree de tipos de novedades
│   ├── type/type_form_view.xml          # Vistas Form de tipos de novedades (muestra noticias relacionadas)
│   ├── type/type_search_view.xml        # Vistas Search de tipos de novedades
│   └── menu.xml                         # Menús y acciones por modelo
├── wizard/
│   └── news_report_wizard.xml           # Reporte PDF de novedades por empleado y por meses
├── __init__.py                           # Importación de models
├── __openerp__.py                        # Información del módulo y archivos de datos
├── README.md                             # Documentación del módulo
├── LICENSE                               # Licencia MIT
└── .gitignore                            # Archivos y carpetas ignoradas por Git

```
---

## 🔹 Buenas Prácticas y Consideraciones

### Credenciales Iniciales
- Solo los usuarios asignados al grupo **Manager de RRHH** pueden acceder al módulo y generar reportes.
- Se recomienda que los usuarios con acceso verifiquen sus credenciales y permisos antes de crear o modificar novedades.

### Permisos de Administrador
- Para utilizar todas las funcionalidades del módulo, incluyendo la generación de reportes PDF y la gestión completa de novedades, se recomienda que los usuarios tengan asignado el grupo **Manager de Recursos Humanos**.

---

## 💡Autoria
- **Modulo de Noticias empleados (R.R.H.H) - Distefano v1.1** bajo **DERECHOS RESERVADOS** 🏷️
- ### 📝 **Licencia**
  - **NO COPYRIGHT**

## 🤖 Desarrolladores: 
  ### **Anthony Josue Escobar Ponce**
  - 👀 **Portafolio Web:** [**CONOCE MAS SOBRE MI**](https://ae--technologies.web.app/index.html)  
  - 🔎 **LinkedIn:** [**TRABAJA CONMIGO**](https://www.linkedin.com/in/anthony-josu%C3%A9-escobar-ponce-71004437b/) 
  - 📭  **Contacto directo:** 📨 **anthonyescobarponce@Outlook.com** / [**CLICK AQUI**](https://ae--technologies.web.app/pages/contact.html)

  ### **Javier Eduardo Herrera Perez**
  - 👀 **Portafolio Web:** [**CONOCE MAS SOBRE MI**]( https://portafolio-kinal.web.app/)  
  - 📭  **Contacto directo:** 📨 **javierherrera5513@gmail.com**

  ### **Luis Rafael Cordova Ruiz**
  - 👀 **Portafolio Web:** [**CONOCE MAS SOBRE MI**](https://portafolio-lc.web.app/)  
  - 📭  **Contacto directo:** 📨 **jluisrafaelcc.r.27@gmail.com**

  ### **Fredy Alexander García Sicajau**
  - 👀 **Portafolio Web:** [**CONOCE MAS SOBRE MI**](https://portafolio-lc.web.app/)  
  - 📭  **Contacto directo:** 📨 **Alexander.garcia.sicajau@gmail.com**
  ---
