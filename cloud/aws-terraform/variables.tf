variable "aws_region" {
  description = "Región AWS"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tipo de instancia"
  type        = string
  default     = "t3.medium"
}

variable "key_name" {
  description = "Nombre de key pair existente en AWS"
  type        = string
}

variable "my_ip_cidr" {
  description = "Tu IP pública en formato CIDR, por ejemplo 190.10.10.10/32. No usar 0.0.0.0/0 para laboratorio expuesto."
  type        = string
}
