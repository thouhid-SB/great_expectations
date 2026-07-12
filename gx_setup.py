from pathlib import Path
import great_expectations as gx

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)
print(type(context).__name__)

source_folder = Path("./data")
data_source_name = "customers"

data_source = context.data_sources.add_pandas_filesystem(
      name=data_source_name, base_directory=source_folder
)

customer_asset = data_source.add_csv_asset(
    name="customers"
)

batch_definition = customer_asset.add_batch_definition_path(
    name="customer_batch",
    path="customers.csv"
)
