import logging

# Configuración básica del logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log"),
                              logging.StreamHandler()])

# Crear logs en diferentes niveles
logging.debug("Esto es un mensaje de depuración")
logging.info("Esto es un mensaje informativo")
logging.warning("Esto es una advertencia")
logging.error("Esto es un mensaje de error")
logging.critical("Esto es un mensaje crítico")