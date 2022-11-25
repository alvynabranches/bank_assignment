# Bank Assignment

Problem Statement Mistakes 
- In the mentioned (dataset)[https://www.kaggle.com/wordsforthewise/lending-club], there is no column risk_score hence moving average is taken of annual_inc

Problem Statement Solution (commits are done on main branch)
1. 6ea6a86
2. 6ea6a86
3. c2a0d8c
4. 6b1f45d

### Day 1 (17/11/2022)
- Searching image for kafka and zookeeper
- Implement the producer - consumer (produmer) python code
- Testing the code (images gave unexpected errors)
- Create Dockerfiles
- Create github workflows
- Create initial IAAS code (terraform used)

### Day 2 (18/11/2022)
- Search for official images
- Test with the produmer python code
- Create a FastAPI app for produmer
- Implement produmer as async code
- Create initial kubernetes deployment file

### Day 3 (19/11/2022)
- Create publisher - subscriber (pubsub) python
- Test the code
- Create a FastAPI app for pubsub
- Implement pubsub as async code
- Implement nginx
- Search for graph base database to store the data

21/11/2022 & 22/11/2022 was not feeling well

### Day 4 (23/11/2022)
- Create final IAAS code
- Create GCP project
- Create a billing account with trial usage (using free credit of $300 on a new account)
- Update the terraform code
- Run the terraform code on GCP
- Debug and fix the terraform code

### Day 5 (25/11/2022)
- Create final k8s code
- Create code for all problem statements
- Debug and fix the code

### Day 6 (26/11/2022)
- Check for problem by deploying on GKE
- Fix the bugs on GKE

### To Do List
- Implement websockets for pubsub and produmer
- Implement neo4j / mysql database in both apis. 
- Finalize kubenetes code
