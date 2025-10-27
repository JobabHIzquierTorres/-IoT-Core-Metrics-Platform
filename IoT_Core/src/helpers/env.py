"""
  Configuración base de rutas y entorno.

  Este módulo define rutas clave del sistema de archivos usando `pathlib.Path`, y prepara el acceso a variables de entorno mediante `python-decouple`.

  Rutas definidas:
  - BASE_DIR: raíz del proyecto (dos niveles arriba del archivo actual).
  - BASE_DIR_ENV: archivo `.env` en la raíz del proyecto.
  - REPO_DIR: raíz del repositorio (un nivel arriba de BASE_DIR).
  - REPO_DIR_ENV: archivo `.env` en el nivel del repositorio.
  - REPO_DIR_WEB_ENV: archivo `.env.web`, útil para configuración web o frontend.

  Funciones:
  - get_config(): importa y devuelve el objeto `config` de `decouple`, permitiendo acceder a variables de entorno con `config('NOMBRE_VARIABLE')`.

  Este enfoque permite mantener la configuración fuera del código fuente, siguiendo buenas prácticas de seguridad, despliegue y portabilidad.
"""

from pathlib import Path
from functools import lru_cache
from decouple import Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_ENV = BASE_DIR / '.env'

REPO_DIR = BASE_DIR.parent
REPO_DIR_ENV = REPO_DIR / '.env'
REPO_DIR_WEB_ENV = REPO_DIR / '.env.web'
REPO_DIR_DB_ENV = REPO_DIR / '.env.db'


@lru_cache  # se ejecuta 1 vez, mejora el rendimiento
def get_config():
    """
      Carga la configuración desde el primer archivo `.env` disponible.

      Prioriza `.env` en BASE_DIR, luego `.env.web` y `.env` en REPO_DIR.
      Si no encuentra ninguno, usa `decouple.config` por defecto.

      Devuelve un objeto `Config` para acceder a variables con `config('VAR')`.
    """

    if REPO_DIR_DB_ENV.exists():
        return Config(RepositoryEnv(str(REPO_DIR_DB_ENV)))
    elif BASE_DIR_ENV.exists():
        return Config(RepositoryEnv(str(BASE_DIR_ENV)))
    elif REPO_DIR_WEB_ENV.exists():
        return Config(RepositoryEnv(str(REPO_DIR_WEB_ENV)))
    elif REPO_DIR_ENV.exists():
        return Config(RepositoryEnv(str(REPO_DIR_ENV)))

    from decouple import config
    return config


config = get_config()
