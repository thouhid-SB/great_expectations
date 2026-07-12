from pathlib import Path
import great_expectations as gx
from great_expectations.core.validation_definition import ValidationDefinition

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

data_source = context.data_sources.get("customers")

customer_asset = data_source.get_asset("customers")

batch_definition = customer_asset.get_batch_definition(
    "customer_batch"
)

suite = context.suites.get("customer_suite")

validation = ValidationDefinition(
    name="customer_validation",
    data=batch_definition,
    suite=suite,
)

context.validation_definitions.add_or_update(validation)

print(f"Validation '{validation.name}' created.")
