terraform {
  required_providers {
    linode = {
      source = "linode/linode"
    }
  }
}

provider "linode" {
  token       = var.token
  api_version = "v4beta"
}

# linode server
resource "linode_instance" "sudoku_resource_instance" {
  label           = "sudoku_instance_label"
  image           = "linode/ubuntu20.04"
  region          = "eu-central"
  type            = "g6-nanode-1"
  root_pass       = var.root_pass
  authorized_keys = [var.ssh_key]

  provisioner "file" {
    source      = "sudoku_solver_img.tar.gz"
    destination = "/root/sudoku_solver_img.tar.gz"
    connection {
      type     = "ssh"
      host     = self.ip_address
      user     = "root"
      password = var.root_pass
    }
  }

  provisioner "remote-exec" {
    inline = [
      "apt-get update -y",
      "apt-get install -y docker.io",
      "docker network create -d bridge sudoku_solver_net.local",
      "docker load -i sudoku_solver_img.tar.gz",
      "docker run --name=sudoku_solver_fastapi --network=sudoku_solver_net.local --rm=true -p 80:80 -itd sudoku_solver_img:v1.0",
    ]

    connection {
      type     = "ssh"
      host     = self.ip_address
      user     = "root"
      password = var.root_pass
    }
  }
}

# domain
resource "linode_domain" "sudoku_domain" {
  domain    = "ambardas.nl"
  soa_email = "ambardeepdas@gmail.com"
  type      = "master"
}
# domain record
resource "linode_domain_record" "sudoku_domain_record" {
  domain_id   = linode_domain.sudoku_domain.id
  name        = "ambardas.nl"
  record_type = "A"
  target      = linode_instance.sudoku_resource_instance.ip_address
  ttl_sec     = 300
}


# firewall
resource "linode_firewall" "sudoku_firewall" {
  label = "sudoku_firewall_label"

  inbound {
    label    = "allow-http"
    action   = "ACCEPT"
    protocol = "TCP"
    ports    = "80"
    ipv4     = ["0.0.0.0/0"]
    ipv6     = ["ff00::/8"]
  }
  inbound_policy  = "DROP"
  outbound_policy = "ACCEPT"

  linodes = [linode_instance.sudoku_resource_instance.id]

}

# variables
variable "token" {}
variable "ssh_key" {}
variable "root_pass" {}
