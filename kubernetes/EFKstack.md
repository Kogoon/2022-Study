## EFK STACK
> EFK Stack 구축을 통한 로그 수집   
> 1. 컨테이너 환경에서의 로그 수집을 위해 EFK(Elastick + Fluentd + Kibana) Stack을 구축.   
> 2. 로그 저장소인  ElasticSearch, 로그 수집기인 Fluentd, 로그 시각화 툴인 Kibana를 EKS 환경에서 구축.   
  
### EFK?
 1. ElasticSearch + Fluentd + Kibana  
 2. Kubernetes는 파드가 정상 상태가 아니면 새로 생성 -> 죽은 파드에 있는 컨테이너가 남긴 로그는 어디로?  
 3. 컨테이너의 로그를 로그 저장소에 수집.   
    -> 죽은 컨테이너의 로그도 남는다(Good).  
    
 * Fluentd -> 컨테이너의 스트림 로그를 수집하는 로그 수집기. 모든 노드마다 동일하게 배포되어야 함. -> Daemonset  
 * ElasticSearch -> 로그를 저장하기 위한 대용량 저장소.  
 * Kibana -> ElasticSearch와 연동하여 로그 시각화.  
    -> 로그 시각화를 통한 문제 해결 및 예방 가능.   
    
 * Daemonset?
    1. Kubernetes 컨트롤러(Deployment, ReplicaSet 등) 중 하나. 
        -> 컨트롤러란? Kubernetes 기본 Object를 생성하고 관리하는 역할. 
    2. DaemonSet은 Pod가 각각의 노드에 하나씩만 배포되게 하는 Pod 관리 컨트롤러. 
        ex) 모든 노드에 로그 수집용 Daemonset pod를 띄움. 
        
 * ElasicSearch?
    1. 텍스트, 숫자, 위치 기반 정보, 정형 및 비정형 데이터 등 모든 유형의 데이터를 위한 분산형 오픈 소스 검색 및 분석 엔진 = 많은 양의 데이터를 보관하고 실시간으로 분석하는 엔진. 
    2. ElasticSearch를 설치하려면? 
         -> java 8 설치 -> ElasticSearch install -> server 재시작... 등... 
         -> K8S? -> ElasticSearch yaml 파일 작성 -> kubectl apply로 배포 끝! 
    3. ElasticSearch를 NodePort type의 서비스로 배포하여 생성 한 Nginx의 loadbalancer에 연결하여 통신 확인. 
