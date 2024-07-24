from antlr4 import *
from PostgresParser import PostgresParser
from PostgresVisitor import PostgresVisitor


class MyPostgresVisitor(PostgresVisitor):
    def __init__(self):
        super(MyPostgresVisitor, self).__init__()
        self.tables = {}  # Dictionary to store table definitions
        self.data = {}  # Dictionary to store inserted data

        self.reserved_keywords = {
            "ALL", "ANALYSE", "ANALYZE", "AND", "ANY", "ARRAY", "AS", "ASC", "ASYMMETRIC", "BINARY",
            "BOTH", "CASE", "CAST", "CHECK", "COLLATE", "COLUMN", "CONSTRAINT", "CREATE", "CROSS",
            "CURRENT_DATE", "CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER",
            "DEFAULT", "DEFERRABLE", "DESC", "DISTINCT", "DO", "ELSE", "END", "EXCEPT", "FALSE",
            "FETCH", "FOR", "FOREIGN", "FREEZE", "FROM", "FULL", "GRANT", "GROUP", "HAVING", "ILIKE",
            "IN", "INITIALLY", "INNER", "INTERSECT", "INTO", "IS", "ISNULL", "JOIN", "LATERAL",
            "LEADING", "LEFT", "LIKE", "LIMIT", "LOCALTIME", "LOCALTIMESTAMP", "NATURAL", "NOT",
            "NOTNULL", "NULL", "OFF", "OFFSET", "ON", "ONLY", "OR", "ORDER", "OUTER", "OVERLAPS",
            "PLACING", "PRIMARY", "REFERENCES", "RETURNING", "RIGHT", "SELECT", "SESSION_USER",
            "SIMILAR", "SOME", "SYMMETRIC", "TABLE", "TABLESAMPLE", "THEN", "TO", "TRAILING", "TRUE",
            "UNION", "UNIQUE", "USER", "USING", "VARIADIC", "VERBOSE", "WHEN", "WHERE", "WINDOW", "SELECT"
            "WITH"
        }

    # Visit a parse tree produced by PostgresParser#create_stmt.
    def visitCreate_stmt(self, ctx: PostgresParser.Create_stmtContext):
        table_name = ctx.table_name().getText()

        # Check if the table already exists
        if table_name in self.tables:
            raise ValueError(f"ERROR: table '{table_name}' already exists")

        # Check for table name conflict with reserved keywords or other objects
        if table_name.upper() in self.reserved_keywords:
            raise ValueError(f"ERROR: table name '{table_name}' conflicts with a reserved keyword or existing object")

        # Process column definitions
        columns = self.visit(ctx.column_definition_list())
        if isinstance(columns, str):
            raise ValueError(columns)  # Raise error from column processing

        self.tables[table_name] = columns
        return f"Table '{table_name}' created with columns: {columns}"

    # Visit a parse tree produced by PostgresParser#column_definition_list.
    def visitColumn_definition_list(self, ctx: PostgresParser.Column_definition_listContext):
        column_names = set()
        for column_def_ctx in ctx.column_definition():
            column_name, data_type = self.visit(column_def_ctx)

            # Check for column name conflict with reserved keywords or other objects
            if column_name.upper() in self.reserved_keywords:
                raise ValueError(
                    f"ERROR: column name '{column_name}' conflicts with a reserved keyword or existing object")

            # Check for duplicate column names
            if column_name in column_names:
                raise ValueError(f"ERROR: duplicate column name '{column_name}' in table")
            column_names.add(column_name)

            # Check for invalid column names
            if column_name.upper() in self.reserved_keywords:
                raise ValueError(f"ERROR: invalid column name '{column_name}'")

        return [(self.visit(column_def_ctx.column_name()), self.visit(column_def_ctx.data_type())) for column_def_ctx in
                ctx.column_definition()]

    def visitColumn_definition(self, ctx: PostgresParser.Column_definitionContext):
        column_name = self.visit(ctx.column_name())
        data_type = self.visit(ctx.data_type())
        return column_name, data_type

    def visitSelect_stmt(self, ctx: PostgresParser.Select_stmtContext):
        table_name = self.visit(ctx.table_name())
        if table_name not in self.tables:
            raise ValueError(f"ERROR: Table '{table_name}' does not exist")

        select_columns = self.visit(ctx.select_columns())
        where_clause = self.visit(ctx.where_clause()) if ctx.where_clause() else None

        # Fetch data from the table
        table_data = self.data.get(table_name, [])

        # Apply where clause filter if exists
        if where_clause:
            filtered_data = [row for row in table_data if self.evaluate_condition(row, where_clause)]
        else:
            filtered_data = table_data

        # Select specific columns or all (*) columns
        if select_columns == '*':
            selected_data = filtered_data
        else:
            selected_data = [{col: row[col] for col in select_columns if col in row} for row in filtered_data]

        # Print the selected data in a tabular format
        for row in selected_data:
            if select_columns == '*':
                formatted_row = ' , '.join([str(row[col]) for col in row])
            else:
                formatted_row = ' , '.join([str(row[col]) for col in select_columns if col in row])
            print(formatted_row)

        return selected_data

    def visitSelect_columns(self, ctx: PostgresParser.Select_columnsContext):
        if ctx.getText() == '*':
            return '*'
        else:
            return [identifier.getText() for identifier in ctx.column_name_list().IDENTIFIER()]

    def visitWhere_clause(self, ctx: PostgresParser.Where_clauseContext):
        # Check if the context has conditions (if not, return None)
        if ctx is None or ctx.condition() is None:
            return None

        # Visit the condition context to get the list of conditions and operators
        return self.visit(ctx.condition())

    def visitCondition(self, ctx: PostgresParser.ConditionContext):
        conditions = []
        for child in ctx.children:
            if isinstance(child, PostgresParser.ExpressionContext):
                # Visit expression to get the tuple (column, operator, value)
                conditions.append(self.visitExpression(child))
            elif child.getText().upper() in ["AND", "OR"]:
                # Logical operators are added as strings
                conditions.append(child.getText().upper())

        return conditions

    def evaluate_condition(self, row, conditions):
        result = None
        current_operator = None

        for condition in conditions:
            if isinstance(condition, str):  # Operator
                current_operator = condition
            else:  # Condition tuple
                column, operator, value = condition
                expression_result = self.evaluate_single_expression(row, column, operator, value)

                if current_operator == "AND":
                    result = result and expression_result if result is not None else expression_result
                elif current_operator == "OR":
                    result = result or expression_result if result is not None else expression_result
                else:
                    result = expression_result

        return result if result is not None else True  # Default to True if no conditions are provided

    def parse_expression(self, expression):
        # Parse an expression string into column, operator, and value
        for operator in ["!=", "=", "<", ">", "<=", ">="]:
            if operator in expression:
                column, value = expression.split(operator)
                return column.strip(), operator, value.strip()
        return None, None, None

    def evaluate_single_expression(self, row, column, operator, value):
        # Get the value from the row
        row_value = row.get(column)

        # Type conversion for row_value and value before comparison
        if isinstance(row_value, str) and row_value.isdigit():
            row_value = int(row_value)  # Convert to integer if it's a digit string
        if isinstance(value, str) and value.isdigit():
            value = int(value)  # Convert to integer if it's a digit string

        # Handle string values (strip quotes)
        if isinstance(row_value, str) and row_value.startswith("'") and row_value.endswith("'"):
            row_value = row_value[1:-1]  # Remove quotes
        if isinstance(value, str) and value.startswith("'") and value.endswith("'"):
            value = value[1:-1]  # Remove quotes

        # Evaluate based on the operator
        if operator == "=":
            return row_value == value
        elif operator == "!=":
            return row_value != value
        elif operator == "<":
            return row_value < value
        elif operator == ">":
            return row_value > value
        elif operator == "<=":
            return row_value <= value
        elif operator == ">=":
            return row_value >= value
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    def visitExpression(self, ctx: PostgresParser.ExpressionContext):
        # Assuming the expression is structured as [column, operator, value]
        # Extract the parts of the expression based on their position
        if len(ctx.children) >= 3:
            column = ctx.children[0].getText()  # First child is expected to be the column
            operator = ctx.children[1].getText()  # Second child is the operator
            value = ctx.children[2].getText()  # Third child is the value

            # Return the structured expression
            return (column, operator, value)
        else:
            # Handle other cases or raise an error
            raise ValueError("Invalid expression format")

    # Visit a parse tree produced by PostgresParser#insert_stmt.
    def visitInsert_stmt(self, ctx: PostgresParser.Insert_stmtContext):
        table_name = self.visit(ctx.table_name())
        # Check if the table exists
        if table_name not in self.tables:
            raise ValueError(f"ERROR: Table '{table_name}' does not exist")
        column_defs = self.tables[table_name]
        # Visit insert columns and values
        insert_data = self.visitInsert_columns_and_values(ctx.insert_columns_and_values(), table_name)
        insert_columns = insert_data['columns']
        values = insert_data['values']
        # Validate and process the insert operation
        self.validate_and_process_insert(table_name, column_defs, insert_columns, values)
        return None

    def validate_and_process_insert(self, table_name, column_defs, insert_columns, values):
        # Ensure the table exists
        if table_name not in self.tables:
            raise ValueError(f"ERROR: Table '{table_name}' does not exist")

        # Convert column definitions to a dictionary for easier access
        col_def_dict = {col_def[0]: col_def[1] for col_def in column_defs}

        # Check for each row in the values
        for row_values in values:
            # Check if the number of values matches the number of columns
            if len(row_values) != len(insert_columns):
                raise ValueError("ERROR: Number of values does not match number of columns")

            # Create a dictionary for the current row's values
            row_data = dict(zip(insert_columns, row_values))

            # Iterate over each column-value pair in the row
            for col_name, val in row_data.items():
                # Validate that the column exists in the table
                if col_name not in col_def_dict:
                    raise ValueError(f"ERROR: Column '{col_name}' does not exist in table '{table_name}'")

                # Validate NOT NULL constraint
                if 'NOT NULL' in col_def_dict[col_name] and val is None:
                    raise ValueError(f"ERROR: Column '{col_name}' cannot be NULL")

                # Validate data type
                self.check_data_type(col_name, col_def_dict[col_name], val)

            # Check for unique and primary key constraint violations
            self.check_unique_constraints(table_name, col_def_dict, row_data, values)

            # If all checks pass, add the row to the table data
            if table_name not in self.data:
                self.data[table_name] = []
            self.data[table_name].append(row_data)

    def check_data_type(self, column_name, data_type, value):
        if data_type in ['INT', 'INTEGER', 'SMALLINT', 'BIGINT', 'NUMERIC', 'DECIMAL'] and not value.replace('.', '',
                                                                                                             1).isdigit():
            raise ValueError(f"ERROR: Value for column '{column_name}' must be a numeric type, got '{value}'")

        if data_type in ['CHAR', 'VARCHAR', 'TEXT'] and not isinstance(value, str):
            raise ValueError(f"ERROR: Value for column '{column_name}' must be a string, got '{value}'")

        if data_type == 'BOOLEAN' and value.lower() not in ['true', 'false']:
            raise ValueError(f"ERROR: Value for column '{column_name}' must be a boolean, got '{value}'")

    def extract_length(self, data_type):
        if 'VARCHAR' in data_type:
            length = int(data_type[data_type.find("(") + 1:data_type.find(")")])
            return length
        return None  # Return None if it's not a VARCHAR type or no length is defined

    def check_unique_constraints(self, table_name, column_defs, insert_columns, values):
        if table_name not in self.tables:
            raise ValueError(f"ERROR: Table '{table_name}' does not exist")

        # Check for primary key and unique constraint violation
        for col_name, val in zip(insert_columns, values):
            if 'PRIMARY KEY' in column_defs[col_name] or 'UNIQUE' in column_defs[col_name]:
                for existing_row in self.data[table_name]:
                    if existing_row[col_name] == val:
                        raise ValueError(
                            f"ERROR: Duplicate key value violates unique constraint on column '{col_name}'")

    def visitInsert_columns_and_values(self, ctx: PostgresParser.Insert_columns_and_valuesContext, table_name):
        columns = self.visit(ctx.insert_columns()) if ctx.insert_columns() else None
        values = self.visit(ctx.insert_values())

        if columns is None:
            columns = [col_def[0] for col_def in self.tables[table_name]]

        return {'columns': columns, 'values': values}

    # Visit a parse tree produced by PostgresParser#insert_columns_and_values.
    def visitInsert_columns(self, ctx: PostgresParser.Insert_columnsContext):
        if ctx is None:
            return None
        # Here, we extract the IDENTIFIER tokens from the context and return their text
        return [identifier.getText() for identifier in ctx.column_name_list().IDENTIFIER()]

    # Visit a parse tree produced by PostgresParser#insert_values.
    def visitInsert_values(self, ctx: PostgresParser.Insert_valuesContext):
        if ctx is None:
            return None
        # Process value lists
        return [self.visit(value_list) for value_list in ctx.value_list()]

    def visitValue_list(self, ctx: PostgresParser.Value_listContext):
        # Visit and return a list of values
        return [self.visit(value) for value in ctx.value()]

    def visitValue(self, ctx: PostgresParser.ValueContext):
        if ctx is not None:
            return ctx.getText()
        else:
            return None

    def visitTable_name(self, ctx: PostgresParser.Table_nameContext):
        return ctx.getText()

    def visitColumn_name(self, ctx: PostgresParser.Column_nameContext):
        return ctx.getText()

    def visitData_type(self, ctx: PostgresParser.Data_typeContext):
        return ctx.getText()

    def visitBasic_type(self, ctx: PostgresParser.Basic_typeContext):
        return ctx.getText()

    def visitCharacter_string_type(self, ctx: PostgresParser.Character_string_typeContext):
        return ctx.getText()

    def visitNumeric_type(self, ctx: PostgresParser.Numeric_typeContext):
        return ctx.getText()

    def visitDate_time_type(self, ctx: PostgresParser.Date_time_typeContext):
        return ctx.getText()

    def visitBoolean_type(self, ctx: PostgresParser.Boolean_typeContext):
        return ctx.getText()
