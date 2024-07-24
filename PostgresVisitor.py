# Generated from Postgres.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PostgresParser import PostgresParser
else:
    from PostgresParser import PostgresParser

# This class defines a complete generic visitor for a parse tree produced by PostgresParser.

class PostgresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PostgresParser#prog.
    def visitProg(self, ctx:PostgresParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#statement.
    def visitStatement(self, ctx:PostgresParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#create_stmt.
    def visitCreate_stmt(self, ctx:PostgresParser.Create_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#select_stmt.
    def visitSelect_stmt(self, ctx:PostgresParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#select_columns.
    def visitSelect_columns(self, ctx:PostgresParser.Select_columnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#where_clause.
    def visitWhere_clause(self, ctx:PostgresParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#condition.
    def visitCondition(self, ctx:PostgresParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#expression.
    def visitExpression(self, ctx:PostgresParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#insert_stmt.
    def visitInsert_stmt(self, ctx:PostgresParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#insert_columns_and_values.
    def visitInsert_columns_and_values(self, ctx:PostgresParser.Insert_columns_and_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#insert_columns.
    def visitInsert_columns(self, ctx:PostgresParser.Insert_columnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#insert_values.
    def visitInsert_values(self, ctx:PostgresParser.Insert_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#value_list.
    def visitValue_list(self, ctx:PostgresParser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#table_name.
    def visitTable_name(self, ctx:PostgresParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#column_definition_list.
    def visitColumn_definition_list(self, ctx:PostgresParser.Column_definition_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#column_definition.
    def visitColumn_definition(self, ctx:PostgresParser.Column_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#column_name.
    def visitColumn_name(self, ctx:PostgresParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#data_type.
    def visitData_type(self, ctx:PostgresParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#basic_type.
    def visitBasic_type(self, ctx:PostgresParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#character_string_type.
    def visitCharacter_string_type(self, ctx:PostgresParser.Character_string_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#numeric_type.
    def visitNumeric_type(self, ctx:PostgresParser.Numeric_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#date_time_type.
    def visitDate_time_type(self, ctx:PostgresParser.Date_time_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#boolean_type.
    def visitBoolean_type(self, ctx:PostgresParser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#serial_type.
    def visitSerial_type(self, ctx:PostgresParser.Serial_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#column_constraint.
    def visitColumn_constraint(self, ctx:PostgresParser.Column_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#table_constraint.
    def visitTable_constraint(self, ctx:PostgresParser.Table_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#primary_key_constraint.
    def visitPrimary_key_constraint(self, ctx:PostgresParser.Primary_key_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#unique_constraint.
    def visitUnique_constraint(self, ctx:PostgresParser.Unique_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#column_name_list.
    def visitColumn_name_list(self, ctx:PostgresParser.Column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#value.
    def visitValue(self, ctx:PostgresParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgresParser#literal.
    def visitLiteral(self, ctx:PostgresParser.LiteralContext):
        return self.visitChildren(ctx)



del PostgresParser