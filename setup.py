from distutils.core import setup

setup(
    name="mkdocs-custom",
    version="0.0.1",
    author="Scott Pierce",
    author_email="ddrscott@gmail.com",
    packages=["custom"],
    description="Local custom plugin",
    install_requires=["mkdocs", "jinja2"],
    entry_points={
        "mkdocs.plugins": [
            "custom = custom:MyCustom",
        ]
    },
)
