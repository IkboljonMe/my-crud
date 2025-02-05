#!/bin/bash

echo "Running MongoDB CRUD Operations"

echo "Creating Document..."
python3 mongo_create.py

echo "Reading Document..."
python3 mongo_read.py

echo "Updating Document..."
python3 mongo_update.py

echo "Deleting Document..."
python3 mongo_delete.py

echo "MongoDB CRUD Operations Completed."
