import great_expectations as gx
from pathlib import Path


# Get the Great Expectations context
context = gx.get_context()

# take the data source and asset which was created in setup.py
data_source = context.data_sources.get("customers")
customer_asset = data_source.get_asset("customers")


batch_definition = customer_asset.get_batch_definition( "customer_batch" )

batch = batch_definition.get_batch()

suite = context.suites.get("customer_suite")

validation_results = batch.validate(suite)

print(validation_results)