# IoT Core Metrics Platform

[![Docker Compose Ready](https://img.shields.io/badge/docker--compose-ready-blue)](https://docs.docker.com/compose/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-enabled-green)](https://www.django-rest-framework.org/)
[![Celery Workers](https://img.shields.io/badge/Celery-distributed-yellow)](https://docs.celeryq.dev/)
[![TimescaleDB](https://img.shields.io/badge/TimescaleDB-series--data-orange)](https://www.timescale.com/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-TimescaleDB-blue)](https://www.timescale.com/)
[![Redis](https://img.shields.io/badge/Redis-broker-red)](https://redis.io/)

---
## Estructura
```
IoT-Core-Metrics-Platform/
├── src/                          # Código fuente principal
│   ├── IoT_Core/                 # Configuración Django principal
│   │   ├── __init__.py
│   │   ├── settings.py           # Configuración principal
│   │   ├── urls.py               # URLs globales
│   │   ├── celery.py             # Configuración Celery
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── sensors/                  # App de sensores y métricas
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py             # Modelos de datos
│   │   ├── tasks.py              # Tareas Celery
│   │   ├── views.py              # Vistas API
│   │   ├── serializers.py        # Serializers DRF
│   │   ├── urls.py               # URLs de la API
│   │   ├── admin.py              # Admin Django
│   │   ├── apps.py
│   │   ├── collect.py            # Utilidades de recolección
│   │   └── tests.py
│   ├── helpers/                  # Utilidades
│   │   ├── __init__.py
│   │   └── env.py                # Manejo de variables entorno
│   └── manage.py
├── compose.yaml                  # Orquestación Docker
├── Dockerfile                    # Imagen Django
├── requirements.txt              # Dependencias Python
├── .env.db-sample                # Variables de entorno ejemplo
├── .dockerignore
└── celery_windows_info.txt       # Info Celery en Windows
```

---

## Índice

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Instalación](#instalación)
- [Variables de entorno](#variables-de-entorno)
- [Despliegue con Docker](#despliegue-con-docker)
- [Tareas periódicas](#tareas-periódicas)
- [API REST](#api-rest)
- [Requisitos (`requirements.txt`)](#requisitos-requirementstxt)
- [Verificación](#verificación)
- [Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](#licencia--creative-commons-attribution-noncommercial-40-international-cc-by-nc-40)

---

## Descripción

Sistema distribuido para recolección y almacenamiento de métricas simuladas en tiempo real. Utiliza Django, Celery, Redis y TimescaleDB para ofrecer una arquitectura escalable y modular, ideal para entornos IoT, educativos o de monitorización técnica.

---

## Arquitectura

- **Django**: Backend principal y API REST
- **Celery**: Tareas periódicas distribuidas por nodo
- **Redis**: Broker de mensajes
- **TimescaleDB**: Base de datos optimizada para series temporales
- **Docker Compose**: Orquestación de servicios
- **DRF**: Exposición de métricas vía API

---

## Instalación

```bash
git clone https://github.com/tuusuario/iot-core-platform.git
cd iot-core-platform
```
---

## Variables de entorno
Ver .env.db-sample para la configuración correcta, ejemplo:
```env
    DJANGO_SECRET_KEY=''
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    DJANGO_SECRET_KEY=''
    DATABASE_URL=""
    CELERY_BROKER_REDIS_URL=""
```

---

## Despliegue con Docker
```bash
    docker compose up -d
```

Está configurado para que los cambios en Django se guarden automáticamente en la base de datos.
Para ello levantar también:
```bash
    docker compose watch
```

Los servicios incluidos son:
  -  web: Django + DRF
  -  beat: Celery Beat para tareas periódicas
  -  workers distribuidos (node_1, node_2, etc)
  -  redis-db: Broker de Redis
  -  timescaledb: base de datos de TimescaleDB

---

## Tareas periódicas
Cada nodo ejecuta `measure_temp_task` cada 3 segundos.
Las tareas se distribuyen por colas dedicadas (`node-1`, `node-2`, etc.) y se registran en la tabla `Metric`.

---

## API REST
Endpoint principal:

- `GET /api/metrics/`: lista de métricas registradas

Se podría mejorar para ordenación, búsqueda por nodo y filtrado por fecha.

---

## Pruebas y verificación
- Verifica Redis: `redis-cli ping`
- Verifica workers: `docker compose logs -f node_1 node_2 node_3`
- Verifica API: accede a `http://localhost:8088/api/metrics/` (previamente levantar el servidor de desarrollo)

---

## Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

Este proyecto se encuentra bajo la licencia **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

### Permisos otorgados

Puedes:

- **Compartir**: copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar**: remezclar, transformar y construir a partir del material.

### Restricciones

No puedes:

- Usar el material con fines comerciales.
- Aplicar restricciones legales o tecnológicas que impidan a otros hacer lo que permite esta licencia.

### Enlace oficial

Consulta los términos completos de la licencia en el sitio oficial de Creative Commons:  
[https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

### Garantía

Este software se proporciona **"tal cual"**, sin garantías de ningún tipo.  
El autor no se hace responsable de posibles daños derivados del uso del código.

### Contribuciones

Las contribuciones son bienvenidas siempre que respeten la licencia.  
Si deseas colaborar:

1. Haz un **fork** del repositorio.
2. Crea una **rama** para tu mejora o corrección.
3. Realiza un **pull request** con una descripción clara de los cambios.

### 📬 Contacto

📧 jhizquier.dev@gmail.com
