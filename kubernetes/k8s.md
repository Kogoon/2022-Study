## Kubernetes

### Kubernetes 란?
 1. 컨테이너 오케스트레이션 툴 (Docker Swarm 같은...)  
 2. 컨테이너를 쉽고 빠르게 배포/확장하고 관리를 자동화해주는 오픈소스 플랫폼 = 1  
 3. Docker가 컨테이너 기반의 가상화를 실현한 플랫폼이라면, Docker Container를 관리하는 것이 Kubernetes
   -> 많은 Container를 관리하는 것이 쉽지 않으니..  
   -> 블루그린 배포, 카나리 배포 등을 실현할 수 있도록, Deployment, Daemonset, 등 다양한 배포 방식 지원  
   

### 쿠버네티스 클러스터 아키텍쳐 
 1. 여러 대의 서버가 하나의 클러스터로 연결
 2. 쿠버네티스 마스터 = 컨트롤 플레인이 실행됨. 클러스터의 두뇌.   
    컨테이너 스케쥴링, 서비스 관리, API 요청 수행.   
    (파드, 리소스 컨트롤러, 로드밸런서 관리)  
 3. 쿠버네티스 워커노드 = 사용자의 워크로드 실행 마스터의 관리 아래 실제 pod같은 리소스가 생성되는 노드.  
 4. kubectl : 쿠버네티스를 다루기 위한 명령행 도구  
 > [AWS 설명서 - kubectl 설치](https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/install-kubectl.html) 


### 관리형 Kubernetes vs 자체 호스팅  
 1. Kubernetes를 자체적으로 구축가능(= 자체 호스팅) -> 빠른 업데이트로 지속적 관리 필요.  
 2. 관리형 쿠버네티스 추천 -> AWS의 EKS, Google의 GKE, Azure의 AKS  
    -> 기업에서 고가용성이 보장된 쿠버네티스 클러스터 제공..  
    

### Kubernetes Object
 1. Kubernetes는 상태를 관리하기 위한 대상을 오브젝트로 정의.  
 2. Pod - Kubernetes의 가장 작은 배포 단위. 컨테이너의 모임. 하나 이상의 컨테이너로 구성.  
 3. Deployment - 애플리케이션 배포의 기본 단위가 되는 리소스.  
 4. Service - Pod를 외부에 노출시켜주는 로드밸런서.  
 5. 위의 오브젝트들을 yaml 파일로 정의하여 kubectl 명령어로 반영한다.  


### Kubernetes Object nginx 배포?
 1. [Deployment](https://github.com/Kogoon/Devops-Study/blob/main/kubernetes/nginx-deployment.yaml)를 정의하여 Nginx 컨테이너를 담은 Pod를 띄운다. 
 2. Pod를 LoadBalancer Type의 [Service](https://github.com/Kogoon/Devops-Study/blob/main/kubernetes/nginx-service.yaml)를 통해 배포한다. 
 3. 자동 생성된 ELB를 통해 Nginx가 배포된 것을 확인.   


