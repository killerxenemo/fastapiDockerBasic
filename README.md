#deployment example fastapi for docker

docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
docker compose up --build