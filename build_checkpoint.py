from pathlib import Path
import great_expectations as gx

from great_expectations.checkpoint.checkpoint import Checkpoint

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

validation = context.validation_definitions.get(
    "customer_validation"
)

checkpoint = Checkpoint(
    name="customer_checkpoint",
    validation_definitions=[validation],
)

context.checkpoints.add_or_update(checkpoint)

print(f"Checkpoint '{checkpoint.name}' created.")