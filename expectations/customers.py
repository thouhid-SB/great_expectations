from great_expectations.expectations.core.expect_column_values_to_not_be_null import (
    ExpectColumnValuesToNotBeNull,
)

from great_expectations.expectations.core.expect_column_values_to_be_unique import (
    ExpectColumnValuesToBeUnique,
)

from great_expectations.expectations.core.expect_column_values_to_be_between import (
    ExpectColumnValuesToBeBetween,
)

from great_expectations.expectations.core.expect_column_values_to_be_in_set import (
    ExpectColumnValuesToBeInSet,
)

from great_expectations.expectations.core.expect_column_values_to_match_regex import (
    ExpectColumnValuesToMatchRegex,
)

email_not_null = ExpectColumnValuesToNotBeNull(
    column="email"
)

customer_id_unique = ExpectColumnValuesToBeUnique(
    column="customer_id"
)

name_not_null = ExpectColumnValuesToNotBeNull(
    column="name"
)

age_between = ExpectColumnValuesToBeBetween(
    column="age",
    min_value=18,
    max_value=80
)

salary_positive = ExpectColumnValuesToBeBetween(
    column="salary",
    min_value=0
)

country_valid = ExpectColumnValuesToBeInSet(
    column="country",
    value_set=[
        "India",
        "USA",
        "Canada",
        "UK",
        "Australia",
        "Germany",
        "Singapore",
        "France",
        "Brazil",
        "Mexico",
        "UAE",
    ]
)

email_format = ExpectColumnValuesToMatchRegex(
    column="email",
    regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

join_date_not_null = ExpectColumnValuesToNotBeNull(
    column="join_date"
)