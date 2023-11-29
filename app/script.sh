eval $(minikube docker-env)
docker build -f ../docker/Dockerfile -t python-on-kube:latest .
docker run -p 5001:5000 python-on-kube
minikube service python-on-kube-service --url