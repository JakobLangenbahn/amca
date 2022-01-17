AMCA
==============================

This project compares the communication of German politicians on Twitter and in the German Federal Parlament.


Setup database from open discourse
------------
We setup the plenary protocoll database from [open discourse](https://github.com/open-discourse/open-discourse). It is already preprocessed.

First step is to download and setup Docker from [here](https://www.docker.com/products/docker-desktop).

Login GitHub for Docker access
`docker login docker.pkg.github.com`

Then download the needed data
`docker pull docker.pkg.github.com/open-discourse/open-discourse/database:latest`

Run database
`docker run --env POSTGRES_USER=postgres --env POSTGRES_DB=postgres --env POSTGRES_PASSWORD=postgres  -p 5432:5432 -d docker.pkg.github.com/open-discourse/open-discourse/database`