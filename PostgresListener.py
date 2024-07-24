# Generated from Postgres.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PostgresParser import PostgresParser
else:
    from PostgresParser import PostgresParser

# This class defines a complete listener for a parse tree produced by PostgresParser.
class PostgresListener(ParseTreeListener):

    # Enter a parse tree produced by PostgresParser#prog.
    def enterProg(self, ctx:PostgresParser.ProgContext):
        pass

    # Exit a parse tree produced by PostgresParser#prog.
    def exitProg(self, ctx:PostgresParser.ProgContext):
        pass


    # Enter a parse tree produced by PostgresParser#statement.
    def enterStatement(self, ctx:PostgresParser.StatementContext):
        pass

    # Exit a parse tree produced by PostgresParser#statement.
    def exitStatement(self, ctx:PostgresParser.StatementContext):
        pass


    # Enter a parse tree produced by PostgresParser#create_stmt.
    def enterCreate_stmt(self, ctx:PostgresParser.Create_stmtContext):
        pass

    # Exit a parse tree produced by PostgresParser#create_stmt.
    def exitCreate_stmt(self, ctx:PostgresParser.Create_stmtContext):
        pass


    # Enter a parse tree produced by PostgresParser#select_stmt.
    def enterSelect_stmt(self, ctx:PostgresParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by PostgresParser#select_stmt.
    def exitSelect_stmt(self, ctx:PostgresParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by PostgresParser#select_columns.
    def enterSelect_columns(self, ctx:PostgresParser.Select_columnsContext):
        pass

    # Exit a parse tree produced by PostgresParser#select_columns.
    def exitSelect_columns(self, ctx:PostgresParser.Select_columnsContext):
        pass


    # Enter a parse tree produced by PostgresParser#where_clause.
    def enterWhere_clause(self, ctx:PostgresParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by PostgresParser#where_clause.
    def exitWhere_clause(self, ctx:PostgresParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by PostgresParser#condition.
    def enterCondition(self, ctx:PostgresParser.ConditionContext):
        pass

    # Exit a parse tree produced by PostgresParser#condition.
    def exitCondition(self, ctx:PostgresParser.ConditionContext):
        pass


    # Enter a parse tree produced by PostgresParser#expression.
    def enterExpression(self, ctx:PostgresParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PostgresParser#expression.
    def exitExpression(self, ctx:PostgresParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PostgresParser#insert_stmt.
    def enterInsert_stmt(self, ctx:PostgresParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by PostgresParser#insert_stmt.
    def exitInsert_stmt(self, ctx:PostgresParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by PostgresParser#insert_columns_and_values.
    def enterInsert_columns_and_values(self, ctx:PostgresParser.Insert_columns_and_valuesContext):
        pass

    # Exit a parse tree produced by PostgresParser#insert_columns_and_values.
    def exitInsert_columns_and_values(self, ctx:PostgresParser.Insert_columns_and_valuesContext):
        pass


    # Enter a parse tree produced by PostgresParser#insert_columns.
    def enterInsert_columns(self, ctx:PostgresParser.Insert_columnsContext):
        pass

    # Exit a parse tree produced by PostgresParser#insert_columns.
    def exitInsert_columns(self, ctx:PostgresParser.Insert_columnsContext):
        pass


    # Enter a parse tree produced by PostgresParser#insert_values.
    def enterInsert_values(self, ctx:PostgresParser.Insert_valuesContext):
        pass

    # Exit a parse tree produced by PostgresParser#insert_values.
    def exitInsert_values(self, ctx:PostgresParser.Insert_valuesContext):
        pass


    # Enter a parse tree produced by PostgresParser#value_list.
    def enterValue_list(self, ctx:PostgresParser.Value_listContext):
        pass

    # Exit a parse tree produced by PostgresParser#value_list.
    def exitValue_list(self, ctx:PostgresParser.Value_listContext):
        pass


    # Enter a parse tree produced by PostgresParser#table_name.
    def enterTable_name(self, ctx:PostgresParser.Table_nameContext):
        pass

    # Exit a parse tree produced by PostgresParser#table_name.
    def exitTable_name(self, ctx:PostgresParser.Table_nameContext):
        pass


    # Enter a parse tree produced by PostgresParser#column_definition_list.
    def enterColumn_definition_list(self, ctx:PostgresParser.Column_definition_listContext):
        pass

    # Exit a parse tree produced by PostgresParser#column_definition_list.
    def exitColumn_definition_list(self, ctx:PostgresParser.Column_definition_listContext):
        pass


    # Enter a parse tree produced by PostgresParser#column_definition.
    def enterColumn_definition(self, ctx:PostgresParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by PostgresParser#column_definition.
    def exitColumn_definition(self, ctx:PostgresParser.Column_definitionContext):
        pass


    # Enter a parse tree produced by PostgresParser#column_name.
    def enterColumn_name(self, ctx:PostgresParser.Column_nameContext):
        pass

    # Exit a parse tree produced by PostgresParser#column_name.
    def exitColumn_name(self, ctx:PostgresParser.Column_nameContext):
        pass


    # Enter a parse tree produced by PostgresParser#data_type.
    def enterData_type(self, ctx:PostgresParser.Data_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#data_type.
    def exitData_type(self, ctx:PostgresParser.Data_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#basic_type.
    def enterBasic_type(self, ctx:PostgresParser.Basic_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#basic_type.
    def exitBasic_type(self, ctx:PostgresParser.Basic_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#character_string_type.
    def enterCharacter_string_type(self, ctx:PostgresParser.Character_string_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#character_string_type.
    def exitCharacter_string_type(self, ctx:PostgresParser.Character_string_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#numeric_type.
    def enterNumeric_type(self, ctx:PostgresParser.Numeric_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#numeric_type.
    def exitNumeric_type(self, ctx:PostgresParser.Numeric_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#date_time_type.
    def enterDate_time_type(self, ctx:PostgresParser.Date_time_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#date_time_type.
    def exitDate_time_type(self, ctx:PostgresParser.Date_time_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#boolean_type.
    def enterBoolean_type(self, ctx:PostgresParser.Boolean_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#boolean_type.
    def exitBoolean_type(self, ctx:PostgresParser.Boolean_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#serial_type.
    def enterSerial_type(self, ctx:PostgresParser.Serial_typeContext):
        pass

    # Exit a parse tree produced by PostgresParser#serial_type.
    def exitSerial_type(self, ctx:PostgresParser.Serial_typeContext):
        pass


    # Enter a parse tree produced by PostgresParser#column_constraint.
    def enterColumn_constraint(self, ctx:PostgresParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by PostgresParser#column_constraint.
    def exitColumn_constraint(self, ctx:PostgresParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by PostgresParser#table_constraint.
    def enterTable_constraint(self, ctx:PostgresParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by PostgresParser#table_constraint.
    def exitTable_constraint(self, ctx:PostgresParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by PostgresParser#primary_key_constraint.
    def enterPrimary_key_constraint(self, ctx:PostgresParser.Primary_key_constraintContext):
        pass

    # Exit a parse tree produced by PostgresParser#primary_key_constraint.
    def exitPrimary_key_constraint(self, ctx:PostgresParser.Primary_key_constraintContext):
        pass


    # Enter a parse tree produced by PostgresParser#unique_constraint.
    def enterUnique_constraint(self, ctx:PostgresParser.Unique_constraintContext):
        pass

    # Exit a parse tree produced by PostgresParser#unique_constraint.
    def exitUnique_constraint(self, ctx:PostgresParser.Unique_constraintContext):
        pass


    # Enter a parse tree produced by PostgresParser#column_name_list.
    def enterColumn_name_list(self, ctx:PostgresParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by PostgresParser#column_name_list.
    def exitColumn_name_list(self, ctx:PostgresParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by PostgresParser#value.
    def enterValue(self, ctx:PostgresParser.ValueContext):
        pass

    # Exit a parse tree produced by PostgresParser#value.
    def exitValue(self, ctx:PostgresParser.ValueContext):
        pass


    # Enter a parse tree produced by PostgresParser#literal.
    def enterLiteral(self, ctx:PostgresParser.LiteralContext):
        pass

    # Exit a parse tree produced by PostgresParser#literal.
    def exitLiteral(self, ctx:PostgresParser.LiteralContext):
        pass



del PostgresParser