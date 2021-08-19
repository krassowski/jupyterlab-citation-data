"""
jupyterlab-citation-data setup
"""
import ast
from pathlib import Path

import setuptools
from glob import glob

HERE = Path(__file__).parent.resolve()


def get_version(path: Path):
    module = ast.parse(path.read_text('utf-8'))
    for statement in module.body:
        if not isinstance(statement, ast.Assign):
            continue
        target = statement.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if target.id != '__version__':
            continue
        constant = statement.value
        if not isinstance(constant, ast.Constant):
            continue
        return constant.value


long_description = (HERE / "README.md").read_text()
version = get_version(HERE / 'jupyterlab_citation_manager' / '_version.py')

setup_args = dict(
    name="jupyterlab-citation-data",
    version=version,
    url='https://github.com/krassowski/jupyterlab-citation-manager',
    author='Michał Krassowski',
    description='CSL styles for jupyterlab-citation-manager',
    license='Other/Proprietary License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "JupyterLab", "JupyterLab3"],
    data_files=[
        ("share/jupyter/csl-styles", [
            str(Path(path).relative_to(HERE))
            for path in glob(str(HERE / "csl-styles" / "**" / "*"), recursive=True)
        ])
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Jupyter",
        #"Framework :: Jupyter :: JupyterLab",
        #"Framework :: Jupyter :: JupyterLab :: 3",
        #"Framework :: Jupyter :: JupyterLab :: Extensions",
    ],
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
