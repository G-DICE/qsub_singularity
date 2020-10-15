***DISCLAIMER***
This repository is provided to the HPC community for educational and inspirational 
purposes only. The scripts inside might have worked in the past but not now. To
understand, modify and use the scripts require proficiency or require a steep 
learning curve in the following:

1) Git
2) SSH, SSh tunnelling 
3) SGE Job Scheduler, qsub scripts
4) bash, shell scripts
5) Singularity, docker etc


FQA:

Q1: The job fails with the following error:

WARNING: Authentication token file not found : Only pulls of public images will succeed
INFO:    Starting build...
FATAL:   Unable to pull docker://jupyter/datascience-notebook:latest: conveyor failed to get: unable to retrieve auth token: invalid username/password

Answer:
You may have the following setup in your .bashrc from the previous use of docket:

export SINGULARITY_DOCKER_USERNAME=DOCKERHUB_USER
export SINGULARITY_DOCKER_PASSWORD=DOCKERHUB_PW
