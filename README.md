# Movies database API
Elastic Search based movies database API This API provides a structured way to interact with a film database, offering features like pagination, sorting, filtering, and detailed information retrieval.
## Tech

Movies project uses a number of open source projects to work properly:

- [FastAPI] - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints!
- [Elasticsearch] - Elasticsearch is a powerfull search and analytics engine
- [Redis] - Redis is famous for being an extremely fast database and it is used for caching queries
- [Pydantic] - Pydantic data validation is used on the project.

## Installation
1. clone project into local directory
2. make sure Docker is installed
3. Place .env file within movies_app directory next to docker-compose.yml with next context

REDIS_HOST=movies_redis
REDIS_PORT=6379
ES_HOST=movies_es
ES_PORT=9200
DB_NAME=movies_database
DB_PASSWORD=123qwe
DB_HOST=movies_db
DB_PORT=5432


4. open a terminal , go to project directory 'movies_sp5' and run
`` docker compose up --build
``
    This would download all necessary images and start up the project containers.

5. Open next url in your browser: http://0.0.0.0:8000/api/openapi

## Movies project basic information

Movies database is a cloud-enabled, production-ready, ElasticSearch-powered FastApi server.

- The API is built using FastAPI, a modern Python web framework.  Routes defined for handling film-related operations are under the '/v1' API version.

- The API uses Pydantic models (Film, FilmDetails, FilmGenre, FilmPerson) for request/response data validation and serialization.

- Dependency injection is used to provide services (FilmService) and pagination parameters to the route handlers.
- The API supports pagination through the Pagination dependency.

- Error handling is implemented, raising HTTP exceptions when appropriate (e.g., when a film is not found).

- The film service (FilmService) is responsible for interacting with the data layer and performing operations like retrieving, searching, and filtering films.

- The API supports sorting films by IMDb rating (ascending or descending) and filtering by genre.

- The search functionality looks for matches in film titles, descriptions, genres, and person names.

- Detailed film information includes related entities such as genres, actors, writers, and directors.
