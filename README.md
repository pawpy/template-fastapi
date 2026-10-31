# FastAPI starter

A minimal [FastAPI](https://fastapi.tiangolo.com) app served by uvicorn. Interactive API docs are at `/docs`.

## Run it locally

```sh
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then open http://localhost:8080. `GET /health` answers `ok` for health checks.

## Deploying

| Step | Command |
| --- | --- |
| Build | pip install -r requirements.txt |
| Start | uvicorn main:app --host 0.0.0.0 --port $PORT |

## Environment variables

| Variable | Meaning |
| --- | --- |
| `PORT` | Port to listen on. Default: 8080. |

## Notes

Dependencies are pinned in `requirements.txt`, generated from `requirements.in` with `uv pip compile requirements.in -o requirements.txt`.

## License

MIT
