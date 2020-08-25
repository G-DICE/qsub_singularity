FQA:

Q1: The job fails with the following error:

WARNING: Authentication token file not found : Only pulls of public images will succeed
INFO:    Starting build...
FATAL:   Unable to pull docker://jupyter/datascience-notebook:latest: conveyor failed to get: unable to retrieve auth token: invalid username/password

Answer:
You may need to supply your Docker Hub login by exporting the following vars:

export SINGULARITY_DOCKER_USERNAME=DOCKERHUB_USER
export SINGULARITY_DOCKER_PASSWORD=DOCKERHUB_PW
