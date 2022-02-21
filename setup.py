import setuptools
import yc_pulumi_helpers

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="yc_pulumi_helpers",
    version=yc_pulumi_helpers.__version__,
    author="agmtr",
    author_email="agmtr@pm.me",
    description="Yandex Cloud Pulumi Helpers.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agmtr/yc-pulumi-helpers",
    packages=['yc_pulumi_helpers'],
    python_requires='>=3.8',
)
