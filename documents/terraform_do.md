## Terraform Digital Ocean. 

[참고](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs)

`main.tf`
~~~ tf
terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# Set the variable value in *.tfvars file
# or using -var="do_token=..." CLI option
variable "do_token" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.do_token
}

data "digitalocean_ssh_key" "test" {
  name = "test"
}

# Create a web server
resource "digitalocean_droplet" "web" {
  image  = "ubuntu-20-04-x64"
  name   = "web-terraform"
  region = "nyc3"
  size   = "s-1vcpu-1gb"
  tags   = ["terraform"]
  ssh_keys = [data.digitalocean_ssh_key.test.id]
}
~~~

`secret.tfvars`
~~~
do_token=<token>
~~~

### command
* plan
~~~
terraform plan -var-file="secret.tfvars"
~~~

* apply
~~~
terraform apply -var-file="secret.tfvars"
~~~

* destroy
~~~
terraform destroy -var-file="secret.tfvars"
~~~

