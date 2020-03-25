# Truckpad - Case

## Instalação

    git clone https://github.com/augusto-nascimento/truckpad.git
    cd truckpad


Crie o arquivo .env conforme modelo abaixo

    DEBUG=1
    SECRET_KEY="z6*3&-1k4vx1(ou&2b^fugf&8f%f+_i37+g97e8-ryfsc#cujk"
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
    POSTGRES_USER=truckpad_user
    POSTGRES_PASSWORD=truckpad_pwd
    POSTGRES_DB=truckpad
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    DATABASE=postgres
    PYTHONPATH=truckpad

Suba os containers utilizando docker-compose

    docker-compose build
    docker-compose up -d

Acesse http://127.0.0.1:8000



## Casos de Uso

![CasosUso](/CasosUso.JPG)

## Diagrama de Classe

![DiagramaClasses](/DiagramaClasses.JPG)