from pathlib import Path
import great_expectations as gx

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

validation = context.validation_definitions.get(
    "customer_validation"
)

validation_results = validation.run()

print(validation_results)