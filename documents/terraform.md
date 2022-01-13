## Terraform
> Terraform is an infrastructure as code (IaC) tool

### install 
`ubuntu`
~~~ bash
$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
$ sudo apt-get update && sudo apt-get install terraform
~~~

#### 설치 확인 
`-help` or `-version`
~~~
$ terraform 
~~~

### Docker on Linux
make directory `terraform-docker-container`
change directory `terraform-docker-container`
~~~ bash
mkdir terraform-docker-container
cd terraform-docker-container
~~~

Create `main.tf`
~~~ tf
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}
~~~

### project init
~~~ bash
terraform init
~~~

### terraform apply
~~~ bash
terraform apply
~~~



### 참고
* [공식사이트-설치](https://www.terraform.io/downloads)
* [Get Started](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started)




* [Digital Ocean](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs/resources/certificate)
