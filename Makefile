SHELL := /bin/bash
all: setup scrape animate

setup:
	# set up poetry environment and create data
	poetry install
	mkdir firecan/data
	mkdir firecan/data/gifs
	mkdir firecan/data/raw_png

scrape:
	# run task 01_image_collection in a poetry environment
	poetry run python3 firecan/tasks/01_image_collection/task.py

animate:
	# run task 02_animation in a poetry environment
	poetry run python3 firecan/tasks/02_animation/task.py