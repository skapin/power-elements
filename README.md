# Dev

- cd backend
- docker-compose up -d
- cd ../web
- npm i
- npm run dev
- browse localhost on given {port}

# Production

docker-compose -f backend/docker-compose.prod.yml -f web/docker-compose.prod.yml up

