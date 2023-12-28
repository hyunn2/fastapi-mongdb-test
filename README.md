# 사용 방법

1. docker 이미지로 받아오기

```bash
# 이미지 받아오기
$ docker pull mongo

# 컨테이너 생성 및 실행
$ docker run --name mongo -p 27017:27017 -d mongo
```

2. fastapi 실행

```bash
$ poetry install

# 실행
$ poetry run uvicorn main:app --reload
```

- *fastapi 접속해서 테스트해보기* -> [접속](localhost:8000/docs)

- *curl 명령어로 테스트해보기*
```bash
1. crate
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Item 1", "description": "Description of Item 1"}' http://localhost:8000/items/

2. read
$ curl -X GET http://localhost:8000/items/{item_id}

3. update
$ curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item 1", "description": "Updated Description of Item 1"}' http://localhost:8000/items/{item_id}

4. delete
$ curl -X DELETE http://localhost:8000/items/{item_id}

```

- mongodb 접속해서 데이터 확인하기

```bash
# docker에서 mongoDB shell 실행
$ docker exec -it mongo mongosh

test> db
test> show dbs
test> use mydatabase
mydatabase> db.items.find()
```