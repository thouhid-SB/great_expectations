from pathlib import Path

import great_expectations as gx
from great_expectations.checkpoint.checkpoint import Checkpoint

from actions.data_docs import update_docs_action
from actions.email import email_action


# Get the File Data Context
context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

# Retrieve the existing Validation Definition
validation = context.validation_definitions.get(
    "customer_validation"
)

# Create the Checkpoint
checkpoint = Checkpoint(
    name="customer_checkpoint",
    validation_definitions=[validation],
    actions=[
        update_docs_action,
        email_action,
    ],
)

# Save (or update) the Checkpoint
context.checkpoints.add_or_update(checkpoint)

print(f"Checkpoint '{checkpoint.name}' created/updated successfully.")