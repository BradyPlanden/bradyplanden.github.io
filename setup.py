from distutils.core import setup

setup(
    name="mkdocs-custom",
    version="0.0.1",
    author="Brady Planden",
    packages=["custom"],
    description="Local custom plugin, and mkdocs dependencies",
    install_requires=[
        "mkdocs",
        "jinja2",
        "mkdocs-material",
        "pymdown-extensions",
        "mkdocs-material-extensions",
        "mkdocs-macros-plugin",
        "mkdocs-plotly-plugin",
        "mkdocs-timetoread-plugin",
    ],
    entry_points={
        "mkdocs.plugins": [
            "custom = custom:MyCustom",
        ]
    },
)
