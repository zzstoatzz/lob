## Demo Line-of-Business Application

### Quickstart
- Setup application: `docker-compose up -d`
- Send a demo request:
```
» curl -X POST "http://0.0.0.0:8000/signup" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Overview
- Task worker serving 2 background tasks
  - Send welcome email
  - Capture analytics data
- Served deployment to capture socials for new signups
- FastAPI endpoint `POST /signup` to create a new user
  - Request body: `{"name": "John Doe", "email": "foo@gmail.com"}`
  - Triggers a run of each background task
  - Triggers a run of the deployment to capture socials
- Prefect server instance to monitor task runs
  - Access the dashboard at `http://localhost:4200`