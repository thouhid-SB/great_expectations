from pathlib import Path
import great_expectations as gx

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

"""
UpdateDataDocsAction automatically rebuilds the Data Docs
whenever the checkpoint runs (via validator.py).

context.build_data_docs() (manual build)

This script only opens the latest generated Data Docs.
"""

context.open_data_docs()

print("Opening Data Docs...")