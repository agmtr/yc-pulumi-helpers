import pulumi
import pulumi_yandex as yandex

def allow_default_rules(sg_id: str):
    allow_egress(sg_id)
    allow_ingress_self_sg(sg_id)

def allow_egress(sg_id: str):
    yandex.VpcSecurityGroupRule("egress",
        direction="egress",
        v4_cidr_blocks=["0.0.0.0/0"],
        port=-1,
        protocol="ANY",
        security_group_binding=sg_id
    )

def allow_ingress_self_sg(sg_id: str):
    yandex.VpcSecurityGroupRule("ingress",
        direction="ingress",
        predefined_target="self_security_group",
        port=-1,
        protocol="TCP",
        security_group_binding=sg_id
    )

def allow_ssh(sg_id: str):
    yandex.VpcSecurityGroupRule("ssh",
        direction="ingress",
        v4_cidr_blocks=["0.0.0.0/0"],
        port=22,
        protocol="TCP",
        security_group_binding=sg_id
    )

def allow_ssh_self_sg(sg_id: str):
    yandex.VpcSecurityGroupRule("ssh",
        direction="ingress",
        predefined_target="self_security_group",
        port=22,
        protocol="TCP",
        security_group_binding=sg_id
    )
