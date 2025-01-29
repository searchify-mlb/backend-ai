docker build -t fastapi-backend .

docker run -d --name fastapi-backend -p 8000:8000 --env-file .env -e GOOGLE_APPLICATION_CREDENTIALS="/app/mlb-hacks-sa.json" -v /mnt/e/Ionify/MLB/mlb-hacks-sa.json:/app/mlb-hacks-sa.json fastapi-backend

docker run -d --name fastapi-backend -p 8000:8000 GOOGLE_APPLICATION_CREDENTIALS="/app/mlb-hacks-sa.json" -v /home/qaisjabbar004/mlb-hacks-sa.json:/app/mlb-hacks-sa.json fastapi-backend


docker exec -it fastapi-backend bash
docker logs fastapi-backend