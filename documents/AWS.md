# AWS
## Cloud Study 


### 목표 
 - [ ] AWS 직무부트캠프 (2022.01 ~ 02 ing)
 - [ ] AWS Certified Cloud Practitioner CLF-C01 exam 취득 

### Memo  
 - [x] Amazon EC2  
 - [ ] Amazon S3  
 - [ ] Amazon CloudFront  
 - [ ] AWS Lambda  
 - [ ] AWS Elastic Beanstalk  
 - [ ] Amazon Appstream  
 - [ ] Amazon Route53  
 - [ ] Amazon SES  
 - [ ] Amazon CloudWatch  
 - [x] Amazon VPC(subnet/routing)
 - [x] Amazon IAM


### AWS CLI
 - `--output (string)`의 옵션들 -> `json`, `text`, `table`
 - `help` : 옵션으로 도움말들 확인 가능 linux에서의 `man` 기능. 
 - `aws configure` : AWS 계정 구성 (Access Key / Secret Key / Region 필요)
 - `aws iam list-users` : IAM user 리스트를 CLI 에서 확인 가능.
 - `aws ec2 describe-vpcs` : 설정되어 있는 vpc 목록 확인 
 - `aws ec2 describe-instances` : 인스턴스 리스트 확인 가능.  
 - `aws ec2 create-security-group --group-name <Group_name> --description <"Description"> --vpc-id <Vpc_ID>` : 보안그룹 생성 
 - `aws ec2 authorize-security-group-ingress` : 인바운드 보안그룹 설정 
 - `aws ec2 authorize-security-group-egress` : 아웃바운드 보안그룹 설정 
 - 예시 `aws ec2 authorize-security-group-ingress --group-name <Group_name> --port <Port> --cidr <CIDR>`
 - `aws ec2 describe-security-groups` : 보안그룹 리스트 확인. `--group-name <Group_name>`, `--output <type>`
 - `aws ec2 run-instances 
      --instance-type t2.micro   
      --key-name <Key_name>  
      --security-group-ids <Security_ID>   
      --image-id <Image_ID>` : t2.micro 유형으로 <Image_ID>의 이미지로 <Security_ID> 및 <Key_name(ex .pem)> 설정 후 인스턴스 생성/실행
 - `aws ec2 describe-instance-status` : 인스턴스 상태 확인 가능. `--instance-ids <Instance-ID>`, 
     * `--query Reservations[*].Instances[*].PublicDnsName` ssh 접속을 위한 dns 찾기. 
 - `aws ec2 terminate-instances` : 인스턴스 종료 `--instance-ids <Instance_ID>`
 - `aws sts get-caller-identity` : AWS CLI 사용자 또는 역할 보기. 


## AWS CloudFormation
`JSON` or `YAML`

* JSON   
~~~ json
{
  "AWSTemplateFormatVersion" : "version date",

  "Description" : "JSON string",

  "Metadata" : {
    template metadata
  },

  "Parameters" : {
    set of parameters
  },
  
  "Rules" : {
    set of rules
  },

  "Mappings" : {
    set of mappings
  },

  "Conditions" : {
    set of conditions
  },

  "Transform" : {
    set of transforms
  },

  "Resources" : {
    set of resources
  },
  
  "Outputs" : {
    set of outputs
  }
}
~~~
  
 * YAML  
~~~ yaml
---
AWSTemplateFormatVersion: "version date"

Description:
  String

Metadata:
  template metadata

Parameters:
  set of parameters

Rules:
  set of rules

Mappings:
  set of mappings

Conditions:
  set of conditions

Transform:
  set of transforms

Resources:
  set of resources

Outputs:
  set of outputs
~~~

* `version date` : 2010-09-09

### 참고    
[Effective Devops](https://github.com/PacktPublishing/Effective-DevOps-with-AWS)  
[AWS Template](https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/template-anatomy.html)
  
