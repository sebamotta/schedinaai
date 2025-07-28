# SchedinaAI

## Architettura
- Backend: Python FastAPI su Render (Docker)
- Frontend: React su Vercel

## Deployment CI/CD
- GitHub Actions: backend → test + deploy su Render
- Vercel: deploy automatico frontend

## Configurazione locale
- `cd ai_model && python train.py`
- `docker-compose up --build`
- `cd frontend && npm install && npm start`

## Variabili d’ambiente
- Su Vercel: `REACT_APP_BACKEND_URL`
- Su GitHub: `RENDER_DEPLOY_HOOK_URL`