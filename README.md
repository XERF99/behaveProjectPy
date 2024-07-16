# Behave con Python y Selenium
### Autor: Francisco Rodríguez

Este proyecto tiene como objetivo crear un ejemplo de como se utiliza behave junto con python para crear casos de prueba más completos y entendibles para el usuario no técnico.

## Requisitos Previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:
- Tener instalado Python 3.6+.
- Tener instalada la biblioteca Selenium
- Tener instalado PyCharm (preferiblemente la edición Profesional para mejor soporte con plugins).

## Instalación

Para instalar las dependencias necesarias, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/XERF99/behaveProjectPy.git
    cd behaveProjectPy
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
    ```

3. Instala los paquetes requeridos:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración


1. **Instalar WebDriver**:
    - Descarga el WebDriver apropiado para tu navegador (por ejemplo, ChromeDriver para Google Chrome).
    - Asegúrate de que el WebDriver sea accesible en tu PATH del sistema.

## Uso

1. Escribe tus casos de prueba en archivos `.behave` dentro del directorio `features`.

2. Para ejecutar las pruebas, navega al directorio del proyecto y usa el siguiente comando:
    ```bash
    behave .\ruta\archivo.feature
    ```

3. Visualiza los archivos de informe y registro generados en el directorio del proyecto para ver los resultados de las pruebas.

## Allure Report

1. Para observar un reporte es necesario ejecutar el siguiente comando desde la consola del sistema `cmd`
   ```bash
      pip install allure-behave
   ```
   
2. Para observar el reporte se debe ejecutar desde la consola de Pycharm el siguiente comando:
   ```bash
      behave -f allure_behave.formatter:AllureFormatter -o reports/ features 
   ```
   El comando mostrado indica que se generará el reporte en formato Allure en la carpeta que
   se especifique luego de -`o` en la carpeta llamada `reports` seguido de la ruta donde se 
   encuentren los `features`. Si se quiere generar el reporte de un solo feature se debe
   especificar el nombre del feature, ejemplo: login.feature.

   El comando presentado anteriormente da como resultado reportes en formato `.json`.


3. Ahora, para que los reportes generados en formato `json` se conviertan a formato `html`
   es necesario ejecutar lo siguiente:

   ```bash
      allure serve reports/
   ```
   En este comando se especifica que se tranforme a formato `html` a los reportes que
   se encuentran en el directorio `reports/` en caso de tener una ubicación distinta será
   necesario cambiar la ruta de destino.

   Ejecutar el comando de allure desde el `cmd` para evitar complicaciones, para ello es 
   necesario que ingrese a la ruta del proyecto.

