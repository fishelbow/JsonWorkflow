import importlib
import inspect
import pkgutil
import types
import pytest

import task_plugins  # your plugin package


# ------------------------------------------------------------
# Helper: discover all plugin modules in task_plugins/
# ------------------------------------------------------------
def discover_plugins():
    plugins = []
    package = task_plugins

    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        if is_pkg:
            continue  # no nested packages for now

        full_name = f"{package.__name__}.{module_name}"
        module = importlib.import_module(full_name)
        plugins.append(module)

    return plugins


# ------------------------------------------------------------
# TEST 1 — Every plugin must define TASK_TYPE
# ------------------------------------------------------------
def test_plugins_define_task_type():
    for plugin in discover_plugins():
        assert hasattr(plugin, "TASK_TYPE"), (
            f"{plugin.__name__} is missing TASK_TYPE"
        )
        assert isinstance(plugin.TASK_TYPE, str), (
            f"{plugin.__name__}.TASK_TYPE must be a string"
        )
        assert plugin.TASK_TYPE.strip(), (
            f"{plugin.__name__}.TASK_TYPE cannot be empty"
        )


# ------------------------------------------------------------
# TEST 2 — Every plugin must define run(task)
# ------------------------------------------------------------
def test_plugins_define_run_function():
    for plugin in discover_plugins():
        assert hasattr(plugin, "run"), (
            f"{plugin.__name__} is missing run(task)"
        )
        assert callable(plugin.run), (
            f"{plugin.__name__}.run must be callable"
        )

        # Validate signature: run(task)
        sig = inspect.signature(plugin.run)
        params = list(sig.parameters.values())
        assert len(params) == 1, (
            f"{plugin.__name__}.run must accept exactly one argument: run(task)"
        )


# ------------------------------------------------------------
# TEST 3 — Optional metadata fields must be valid if present
# ------------------------------------------------------------
def test_plugin_metadata_fields():
    for plugin in discover_plugins():
        if hasattr(plugin, "DESCRIPTION"):
            assert isinstance(plugin.DESCRIPTION, str), (
                f"{plugin.__name__}.DESCRIPTION must be a string"
            )

        if hasattr(plugin, "VERSION"):
            assert isinstance(plugin.VERSION, str), (
                f"{plugin.__name__}.VERSION must be a string"
            )
            assert plugin.VERSION.count(".") >= 1, (
                f"{plugin.__name__}.VERSION should look like semantic versioning"
            )

        if hasattr(plugin, "REQUIRED_FIELDS"):
            assert isinstance(plugin.REQUIRED_FIELDS, (list, tuple)), (
                f"{plugin.__name__}.REQUIRED_FIELDS must be a list or tuple"
            )
            for field in plugin.REQUIRED_FIELDS:
                assert isinstance(field, str), (
                    f"{plugin.__name__}.REQUIRED_FIELDS contains a non-string field"
                )


# ------------------------------------------------------------
# TEST 4 — Plugins must gracefully handle missing required fields
# ------------------------------------------------------------
def test_plugins_handle_missing_required_fields():
    for plugin in discover_plugins():
        required = getattr(plugin, "REQUIRED_FIELDS", [])

        if not required:
            continue  # nothing to test

        # Build a task missing all required fields
        bad_task = {}

        try:
            result = plugin.run(bad_task)
        except Exception as e:
            pytest.fail(
                f"{plugin.__name__}.run raised an exception on missing fields: {e}"
            )

        assert result in (True, False), (
            f"{plugin.__name__}.run must return True or False"
        )


# ------------------------------------------------------------
# TEST 5 — Plugins must return True/False and not raise exceptions
# ------------------------------------------------------------
def test_plugins_return_boolean():
    for plugin in discover_plugins():
        # Build a minimal valid task
        task = {}

        # Add required fields if needed
        for field in getattr(plugin, "REQUIRED_FIELDS", []):
            task[field] = "dummy"

        try:
            result = plugin.run(task)
        except Exception as e:
            pytest.fail(f"{plugin.__name__}.run raised an exception: {e}")

        assert isinstance(result, bool), (
            f"{plugin.__name__}.run must return a boolean"
        )