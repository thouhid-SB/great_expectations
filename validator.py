from pathlib import Path
import great_expectations as gx

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

checkpoint = context.checkpoints.get(
    "customer_checkpoint"
)

validation_results = checkpoint.run()

print(validation_results)