from pathlib import Path
import great_expectations as gx

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

validation = context.checkpoints.get(
    "customer_checkpoint"
)

validation_results = validation.run()

print(validation_results)