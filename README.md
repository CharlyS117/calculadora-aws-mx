# AWS Mexico Multi-Service Calculator ☁️🇲🇽

Una herramienta moderna y profesional diseñada para desarrolladores en México que necesitan estimar costos de AWS en Pesos Mexicanos (MXN) con impuestos locales (IVA) incluidos.

## 🚀 Características

- **Multi-Servicio**: Calcula costos para EC2, S3, Lambda y Transferencia de Datos.
- **Localización Total**: 
  - Conversión automática a **MXN** con tipo de cambio en tiempo real (vía API).
  - Cálculo automático del **16% de IVA** conforme a la normativa mexicana.
- **Diseño Premium**: Interfaz oscura tipo "Dashboard" construida con Tailwind CSS, optimizada para escritorio y móviles.
- **Automatización de Precios (v3.0)**:
  - Los precios de AWS se extraen automáticamente de la nube.
  - Se sincronizan semanalmente mediante **GitHub Actions**.
  - La web carga los datos dinámicamente con un sistema de **fallback** (respaldo) para máxima confiabilidad.

## 🛠️ Estructura del Proyecto

- `index.html`: Aplicación Single Page App (SPA) principal. Incluye toda la lógica de UI y cálculos.
- `update_prices.py`: Script de Python que extrae los precios de AWS y genera el archivo de datos.
- `aws_prices.json`: Archivo de datos sincronizado que consume la aplicación web.
- `.github/workflows/update.yml`: Configuración de CI/CD para ejecutar la actualización de precios cada lunes a medianoche.

## 💻 Uso Local

Para usar la calculadora, simplemente abre el archivo `index.html` en cualquier navegador moderno. 

> [!TIP]
> No necesitas configurar un servidor web ni bases de datos para que funcione la interfaz básica.

## ⚙️ Automatización

Si deseas actualizar los precios manualmente:

1. Asegúrate de tener Python instalado.
2. Instala la dependencia necesaria:
   ```bash
   pip install requests
   ```
3. Ejecuta el script:
   ```bash
   python update_prices.py
   ```

Esto actualizará el archivo `aws_prices.json` con los valores vigentes de AWS para la región `us-east-1`.

---
Diseñado para la comunidad de desarrolladores en México. v3.0.0
