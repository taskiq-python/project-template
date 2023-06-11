"""Project was generated using https://github.com/taskiq-python/project-template/."""

try:
    # Python 3.8+
    from importlib.metadata import version  # noqa: WPS433
except ImportError:
    # Python 3.7
    from importlib_metadata import version  # noqa: WPS433

__version__ = version("{{cookiecutter.project_name}}")

__all__ = [
    "__version__"
]