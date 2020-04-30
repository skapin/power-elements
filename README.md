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


# Init (if needed)

- Start back end
- Load quesiton by calling 
- 127.0.0.1:90019/api/questions/load
- Check by browsing 
- http://localhost:8080/#/
- You can now export database