# Generador de Códigos QR para Invitados

Este proyecto permite cargar un archivo Excel con los datos de los invitados y generar códigos QR personalizados para cada uno. Cada código QR contiene la información de los invitados que puede ser escaneada por dispositivos móviles. Ideal para eventos, conferencias y otras ocasiones donde se necesite identificar a los invitados mediante códigos QR.

---

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.7** o superior.
- **Pip** (gestor de paquetes de Python).
- **Un entorno virtual** (opcional pero altamente recomendado para evitar conflictos con dependencias globales).

---

## Instalación

Sigue estos pasos para configurar el proyecto y sus dependencias de manera sencilla.

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/generador-qr-invitados.git
   cd generador-qr-invitados


---

### 2. Crear un entorno virtual:
   - En **Windows**:

     ```bash
     python -m venv .venv
     ```

   - En **Mac/Linux**:

     ```bash
     python3 -m venv .venv
     ```
### 3. **Activa el entorno virtual:**

   - **Windows**:

     ```bash
     .venv\Scripts\activate
     ```

   - **Mac/Linux**:

     ```bash
     source .venv/bin/activate
     ```
### 4. **Instala las dependencias:**

   Si tienes un archivo `requirements.txt` con las dependencias del proyecto, instala las dependencias con el siguiente comando:

   ```bash
   pip install --no-cache-dir -r requirements.txt
```

    
---

### 5. Uso del proyecto:
## Uso

Una vez que hayas instalado las dependencias, sigue estos pasos para ejecutar y usar el proyecto.

1. **Ejecuta el script principal** para abrir la interfaz gráfica:

   ```bash
   python Guardian.py
```
Interfaz gráfica: La interfaz gráfica te permitirá:

Cargar un archivo Excel con los datos de los invitados.
Visualizar una lista de los invitados cargados.
Previsualizar un código QR al seleccionar un invitado de la lista.
Generar códigos QR para cada invitado.
