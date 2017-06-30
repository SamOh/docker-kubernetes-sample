# docker-kubernetes-sample
This project provides a quick crash course, high-level overview, and tutorial for getting started with Docker and Kubernetes. All the files you need are in this repo. However, the dockerfile isn't created yet to build a docker image or run a docker container. I will start with a high-level overview of both docker and kubernetes and then walk you through the instructions for creating your own docker images, containers, and kubernetes deployments (locally). I will also breifly talk through the process of deploying onto kubernetes instead of using minikube (local dev).

## Docker
In this section, I won't assume you have a lot of background knowledge about docker, but will review the basics quickly enough that people who are familiar can get a nice refresher. To really understand the importance of docker, I will first explain the history of docker and it's place in dev. Then, I will go through common vocab to understand what docker is. Finally, I will walk through a few common Docker commands (and a link to the docs) to get started creating your own images and containers.

### 1. What is Docker
Docker is a Software container platform to allow for containers to be used across devices with the same dependencies and environment. Used to run/manage apps side-by-side in isolated containers to get better compute density. In many ways, a docker container is very similar to a VM, however, it is much more "lightweight" in the sense that a VM has to copy the entire kernel whereas a docker container shares the kernel with the underlying VM (Linux kernel). Both, however, copy over all of the requirements, dependencies, etc. so that the environment is completely isolated from the underlying computer.

### 2. History (Why Docker)
As mentioned earlier, docker is much more lightweight than running a traditional VM...

### 3. Pertinent Terms
Docker image: A lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment vars, and config files.

Docker Container: Isolated package of everything needed to make a piece of software. Also known as a runtime instance of an image (make a conatiner from an image). It is what the image becomes in memory when it is actually executed. A container runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

Docker Registry: Collection of docker images. Dockerhub is the most notable. We have our own docker registry at https://registry.jpl.nasa.gov (quay.com)

Dockerfile: This is the file in an application that defines a portable image. In this file, you define what goes on in the environment inside the container. Because this container is isolated from the rest of your system, including resources like networking interfaces and disk drives, you need to map ports to the outside world and be specific about what files to copy in to that env. It may take a while to configure these, but it is worth it becuase it can guarantee that the build of an anpp will behave exactly the same wherever it runs (you need this to build a docker image). We'll walk through writing a dockerfile together later in this tutorial.

### 4. Common Commands
```
docker build -t friendlyname .         		                # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyname.                # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyname      			    # Same thing, but in detached mode
docker ps                                                       # See a list of all running containers
docker stop <hash>                                              # Gracefully stop the specified container
docker ps -a                                                    # See a list of all containers, even the ones not running
docker kill <hash>                                              # Force shutdown of the specified container
docker rm <hash>                                                # Remove the specified container from this machine
docker rm $(docker ps -a -q)               		        # Remove all containers from this machine
docker images -a                                                # Show all images on this machine
docker rmi <imagename>                           		    # Remove the specified image from this machine
docker rmi $(docker images -q)                         	# Remove all images from this machine
docker login                                                    # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag   	# Tag <image> for upload to registry
docker push username/repository:tag    			# Upload tagged image to registry
```


## Kubernetes
I will break up this section in the similar way as the docker section. In order to understand the role of kubernetes and the importance of a tool like kubernetes, we first have to understand the limitations of docker. Docker is really good at creating isolated, lightweight containers that run the way we want wherever we want, however, once we have many docker containers (as in the case with the microservices infrastructure), we will need a way to scale, work with, and different containers differently and easily. Kubernetes does just this.

### 1. What is Kubernetes
Kubernetes is an open source system for automating deployment, scaling, and management of containerized applications. It is a container orchestration tool provided by Google. This is the way that Docker and Kubernetes go together – docker creates the containers for apps, and kubernetes is the "captain" of the ship of docker containers. (Kubernetes means helmsman/governor in Greek).

### 2. Why Kubernetes
Modern web services expect applications to be available 24/7 and developers need to deploy new versions sometimes several times a day. Containerization helps package software to serve these goals, enabling applications to be released/updated in an easy/fast way without downtime. Kubernetes helps you make sure these containerized applications run where/when you want and helps them find the resources/tools they need to work.

Other technologies include Docker Swarm, Amazon ECS (EC2 container service), and Mesos. You can read up more on the other technologies which are very similar, but Kubernetes is the most comprehensive and flexible service. The downside is that there is a larger learning curve to start using Kubernetes.

### 3. Pertinent Terms
Cluster: Group of computers that Kubernetes coordinates to work together as a single unit (has to do with the abstraction level of Kubernetes. In other words, Kubernetes allows you to deploy containerized applications to a cluster without having to tie the application to an individual machine!!) In order for this new model of deployment to work, applications must be packaged in a way that decouples them from individual hosts (i.e. they need to be containerized). Containerized applications are more flexible and available than in past deployment models where apps had to be installed directly onto specific machines. Kubernetes automates the distribution/scheduling of application containers across a cluster in a more efficient way.

Pods: Basic unit of scheduling in Kubernetes. Have labels (key:val pairs). Group of containers intended to be deployed/scheduled together, coordinating to execute particular task.

Deployments:

Replication Controllers: Framework for defining horizontally scaled pods. Responsible for handling replicated pods. If containers go down, this will start up another contianer and kill the container when the first one comes back online.

Services: A unit that acts as a basic load balancer/ambassador for other containers. Way to interface with a group of containers. Allow you to simplify your container designs since they group together a logical collection of pods based on your labels.

Ingress: A way to expose your application to the outside world.

Minikube: lightweight Kubernetes implementation that creates a VM on local machine and deploys a simple cluster containing only one node

Node: the workers that run applications (similar to workers in docker). It is a VM or physical computer that serves as a worker machine in a Kubernetes cluster. Each node has a Kubelet (an agent for managing the node and communicating with the Kubernetes master).

Master: the nodes/resource that coordinates the cluster. Coordinates all activities in cluster such as scheduling applications, maintaining applications’ desired state, scaling applications, and rolling out new updates (think of hexagon with hexagon in center as master and nodes all around)

### 4. Common Commands
```
kubectl config set-context 
kubectl create -f <filename> --namespace=<namespace>  # This is 
kubectl a
kubectl get [pods/deployments/services/ingresses] # used to get a list of all instances of this resource in the current namespace
kubectl exec -it <podname> bash # Helpful debugging tool
```
## Tutorial
In this tutorial, I will teach you how get a test application up and running locally on kubernetes. To do this we will first need to download all the necessary tools, then create a docker image with a dockerfile (and run the image to get a container), then write the appropriate yaml files to create a deployment, service, and ingress so that we can visit our test site. At the end we will also go through the ways to update an application (using kubernetes built in rollout feature) without any downtime for our site.







