# Eduvos Student Registration API

A demo application showcasing CI/CD on AWS with Kiro IDE.

## Architecture

```
Developer (Kiro IDE) → GitHub → CodePipeline → CodeBuild (test) → CodeDeploy (deploy)
```

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

## Run Tests

```bash
pytest -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /students | List all students |
| POST | /students | Register a student |
| GET | /students/:id | Get student by ID |

## Example Request

```bash
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Ada Lovelace", "email": "ada@eduvos.co.za", "course": "Computer Science"}'
```
