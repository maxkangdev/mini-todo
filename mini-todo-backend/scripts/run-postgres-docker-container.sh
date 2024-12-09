#!/bin/bash

# Variables
CONTAINER_NAME="my_postgres"
POSTGRES_USER="myuser"
POSTGRES_PASSWORD="mypassword"
POSTGRES_DB="mydatabase"
POSTGRES_PORT="5432"

# Check if the container is already running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "PostgreSQL container '$CONTAINER_NAME' is already running."
else
    # Check if the container exists but is stopped
    if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
        echo "Starting existing PostgreSQL container '$CONTAINER_NAME'..."
        docker start $CONTAINER_NAME
    else
        echo "Creating and starting a new PostgreSQL container '$CONTAINER_NAME'..."

        docker run -d \
            --name $CONTAINER_NAME \
            -e POSTGRES_USER=$POSTGRES_USER \
            -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
            -e POSTGRES_DB=$POSTGRES_DB \
            -p $POSTGRES_PORT:5432 \
            -v postgres_data:/var/lib/postgresql/data \
            postgres:13
    fi

    # Check if the container started successfully
    if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
        echo "PostgreSQL container '$CONTAINER_NAME' is running."
    else
        echo "Failed to start PostgreSQL container."
    fi
fi
