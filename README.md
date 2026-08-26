# frontend-design-lab

Sandbox para prototipar y probar experimentos de diseño frontend: layouts, estilos y patrones de UI, cada uno aislado en su propia carpeta dentro de `experimentos/`. Incluye una API mock en FastAPI para poder probar componentes con datos reales (fetch, formularios, CRUD).

## Requisitos

- **Node.js** (con npm) — para el frontend.
- **Python 3.11+** y **[uv](https://docs.astral.sh/uv/)** — para la API. Instalar uv:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Levantar el frontend

```bash
npm install
npm run dev
```

Sirve en **http://localhost:4000** (puerto fijo, configurado en [vite.config.js](vite.config.js)).

## Levantar la API

```bash
cd api
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

Sirve en **http://localhost:8000**. Documentación interactiva (Swagger) en **http://localhost:8000/docs**.

Los experimentos que consumen la API asumen que corre en ese puerto, con CORS habilitado para `http://localhost:4000`.

### Endpoints disponibles

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/health` | Chequeo de estado |
| GET | `/api/users` | Lista de usuarios mock (`?limit=&offset=`) |
| GET | `/api/users/{id}` | Un usuario |
| GET | `/api/products` | Lista de productos mock (`?limit=&offset=`) |
| GET | `/api/products/{id}` | Un producto |
| GET | `/api/tasks` | Lista de tareas |
| POST | `/api/tasks` | Crear tarea |
| GET | `/api/tasks/{id}` | Una tarea |
| PATCH | `/api/tasks/{id}` | Editar tarea |
| DELETE | `/api/tasks/{id}` | Borrar tarea |

Los datos viven en memoria y se regeneran cada vez que reiniciás la API.

## Estructura

```
frontend-design-lab/
├── index.html              # índice con links a cada experimento
├── src/style.css           # reset y variables base compartidas
├── experimentos/
│   ├── ejemplo-01/          # tarjetas de usuario con datos de la API
│   └── ejemplo-02/          # landing SaaS B2B (modo claro/oscuro)
└── api/                    # API FastAPI (mock data + CRUD de tareas)
    ├── app/
    │   ├── main.py          # app + CORS + routers
    │   ├── models.py        # modelos Pydantic
    │   ├── data.py           # datos en memoria (Faker)
    │   └── routers/
    └── pyproject.toml
```

## Agregar un nuevo experimento

1. Creá una carpeta en `experimentos/<nombre>/` con su propio `index.html`, `style.css` y (si hace falta) `main.js`.
2. Sumala al listado en [index.html](index.html).
3. Si necesita datos, apuntá tus `fetch` a `http://localhost:8000/api/...` (con la API corriendo).

## Correr todo junto

Necesitás las dos terminales abiertas en simultáneo:

```bash
# terminal 1
npm run dev

# terminal 2
cd api && uv run uvicorn app.main:app --reload --port 8000
```
