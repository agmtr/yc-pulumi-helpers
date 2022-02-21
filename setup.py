import pulumi_yandex
import yc_pulumi_helpers
from setuptools import setup, find_packages

setup(
    name='yc-pulumi-helpers',
    version=yc_pulumi_helpers.__version__,
    packages=find_packages(),
    install_requires=[
        "pulumi>=3.0.0,<4.0.0",
        "pulumi_yandex>=0.12.0,<0.13.0"
    ]
)
