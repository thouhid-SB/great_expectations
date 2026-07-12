from pathlib import Path
import great_expectations as gx

from expectations.customers import (
    email_not_null,
    customer_id_unique,
    name_not_null,
    age_between,
    salary_positive,
    country_valid,
    email_format,
    join_date_not_null,
)

context = gx.get_context(
    mode="file",
    project_root_dir=Path.cwd()
)

suite_name = "customer_suite"

suite = gx.ExpectationSuite(
    name=suite_name
)

suite = context.suites.add_or_update(suite)

# ADDING EXPECTATIONS
expectations = [
    email_not_null,
    customer_id_unique,
    name_not_null,
    age_between,
    salary_positive,
    country_valid,
    email_format,
    join_date_not_null,
]

for expectation in expectations:
    suite.add_expectation(expectation)

context.suites.add_or_update(suite)

print(
    f"Suite '{suite.name}' contains "
    f"{len(suite.expectations)} expectations."
)