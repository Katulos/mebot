import re

from setuptools import setup

with open("requirements.txt", encoding="utf-8") as f:
    required = f.read().splitlines()


def format_branch_name(name):
    pattern = re.compile(r"^(bugfix|feature)\/issue-(?P<branch>[0-9]+)-\S+")

    match = pattern.search(name)
    if match:
        return match.group("branch")
    if name in {"master", "main", "dev", "develop"}:
        return name
    raise ValueError(f"Wrong branch name: {name}")


setup(
    install_requires=required,
    setuptools_git_versioning={
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}",
        "dirty_template": "{tag}.dev{ccount}",
        "branch_formatter": format_branch_name,
        "starting_version": "0.0.1",
    },
    setup_requires=["setuptools-git-versioning"],
    entry_points={"console_scripts": ["mebot = mebot.__main__:run"]},
)
