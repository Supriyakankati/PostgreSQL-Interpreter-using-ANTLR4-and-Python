import sys
from antlr4 import *
from PostgresLexer import PostgresLexer
from PostgresParser import PostgresParser
from MyPostgresVisitor import MyPostgresVisitor

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(argv):
    try:
        input_stream = FileStream(argv[1], encoding='utf-8')

        lexer = PostgresLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PostgresParser(stream)
        tree = parser.prog()

        # MyPostgresVisitor extends the generated visitor file
        visitor = MyPostgresVisitor()
        visitor.visitProg(tree) # Evaluate the expression

    except ValueError as e:
        print(e)  # Only print the error message

if __name__ == '__main__':
    main(sys.argv)
