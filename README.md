# Dev :

- cd backend
- docker-compose up -d
- cd ../web
- npm i
- npm run dev
- browse localhost on given {port}

# Production :

Create alias to docker-compose.sh then: 
- docker-compose-base -f backend/docker-compose.prod.yml -f web/docker-compose.prod.yml up

