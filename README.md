# Bot-de-Telegram-4

Este proyecto consiste en un bot básico para Telegram desarrollado en Python utilizando la librería TeleBot.

## Descripción

Este bot para Telegram tiene una función principal que consiste en generar excusas convincentes de manera aleatoria. Cada excusa creada incluye elementos como quién causó el problema, qué acción realizó, qué objeto se vio afectado y cuándo ocurrió. Además, el bot complementa estas excusas enviando una imagen relacionada con el personaje ficticio mencionado en la excusa. Por ejemplo, si la excusa menciona a "Pennywise", el bot enviará automáticamente una imagen de Pennywise junto con la excusa generada.

Este bot es la versión mejorada de [este](https://github.com/EduardoHernandezGuzman/Bot-de-Telegram-3-) otro bot.


## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Utiliza Git para clonar este repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/tu_usuario/Bot-de-Telegram-1.git
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza pip para instalar las dependencias necesarias:

    ```bash
    cd Bot-de-Telegram-1
    pip install -r requirements.txt
    ```

3. **Obtener Token de Bot**: Crea un nuevo bot en Telegram utilizando el BotFather y obtén el token del bot recién creado.

4. **Configurar el Token**:
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Abre el archivo `.env` en un editor de texto y agrega la siguiente línea, reemplazando `"TU_TOKEN_AQUÍ"` con el token obtenido en el paso anterior:

    ```plaintext
    TELEGRAM_TOKEN=TU_TOKEN_AQUÍ
    ```

5. **Asegurarse de que `.env` esté en `.gitignore`**:
    - Asegúrate de que el archivo `.env` esté incluido en `.gitignore` para que no se suba al repositorio. El contenido de `.gitignore` debería incluir `.env`:

    ```plaintext
    .env
    ```

6. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python para iniciar el bot:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida al usuario.

- **Comando `/about`**: Muestra información sobre el bot, incluyendo detalles sobre su propósito y quién lo creó.

- **Comando `/excusa`**: Genera una excusa convincente utilizando elementos aleatorios de quien, acción, qué y cuándo. Además te envía una imagen con la excusa.

## El bot en funcionamiento

![bot04](https://github.com/EduardoHernandezGuzman/Bot-de-Telegram-3-/assets/139759297/8bd1a2c2-5acf-4a95-93cc-2be1be16b269)


## Personalización

Si deseas agregar nuevas funcionalidades o personalizar el comportamiento del bot, puedes modificar el archivo `main.py` según tus necesidades. La documentación de TeleBot puede ser útil para comprender cómo extender la funcionalidad del bot.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.

