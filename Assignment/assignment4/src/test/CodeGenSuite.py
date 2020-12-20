import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
                    Var: x = 1;
                    Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],([],[
    # 			CallStmt(Id("print"),[
    #                 CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    # 	expect = "120"
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test3(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Function: foo
    #     Body:
    #         print(string_of_int(1));
    #     EndBody.
    #     Function: main
    #     Body: 
    #         foo();
    #         print(string_of_int(120));
    #     EndBody."""
    #     expect = "1 \n 120"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))