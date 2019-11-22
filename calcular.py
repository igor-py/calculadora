# Classe para fazer os Cálculos


class Calcular:

    def __init__(self, exp=[]):
        # Expression to be solved
        # It needs to be in form of a list in order to work
        self.exp = exp
        # Dictionary with operations
        self.operadores = {'+': lambda x, y: x + y,
                           '-': lambda x, y: x - y,
                           '*': lambda x, y: x * y,
                           '/': lambda x, y: x / y,
                           '^': lambda x, y: x ** y}

    def get_subexp(self):
            # Localize subexpression
            pos1 = max([i for i, x in enumerate(self.exp) if x == '('])
            try:
                pos2 = self.exp.index(')', pos1 + 1)
            except ValueError:
                return None
            # Extract subexpression
            expr = self.exp[pos1 + 1: pos2]
            return pos1, pos2, expr

    def calculate(self, e):
        # Exponential
        while True:
            try:
                pos = e.index('^')
                # If the operator exists, calculate
                try:
                    op1, op2 = float(e[pos - 1]), float(e[pos + 1])
                except IndexError:
                    return ['Esqueceu 2° operando']
                try:
                    res = str(self.operadores[e[pos]](op1, op2))
                except OverflowError:
                    break
                # modify expression, replacing operation for its result
                e = e[:pos - 1] + [res] + e[pos + 2:]
            except ValueError:
                break
        # Multiplication and Division
        while True:
            try:
                pos = min([i for i, x in enumerate(e) if x in ['*', '/']])
                # If the operator exists, calculate
                try:
                    op1, op2 = float(e[pos - 1]), float(e[pos + 1])
                except IndexError:
                    return ['Esqueceu 2° operando']
                try:
                    res = str(self.operadores[e[pos]](op1, op2))
                except OverflowError:
                    print('here')
                # modify expression, replacing operation for its result
                e = e[:pos - 1] + [res] + e[pos + 2:]
            except ValueError:
                # If you can not find proceed
                break
        # Add and Subtract
        while True:
            try:
                pos = min([i for i, x in enumerate(e) if x in ['+', '-']])
                # If the operator exists, calculate
                try:
                    op1, op2 = float(e[pos - 1]), float(e[pos + 1])
                except IndexError:
                    return ['Esqueceu 2° operando']
                res = str(self.operadores[e[pos]](op1, op2))
                # modify expression, replacing operation for its result
                e = e[:pos - 1] + [res] + e[pos + 2:]
            except ValueError:
                # If you can not find proceed
                break
        # Return result
        return e

    def evaluate_exp(self):
        # Evaluate
        while self.exp.count('('):
            # 1
            tupla_exp = self.get_subexp()
            if tupla_exp is None:
                return 'Fechar parênteses!'
            pos1, pos2, exp = tupla_exp[0], tupla_exp[1], tupla_exp[2]
            # 2
            res = self.calculate(exp)
            # 3
            self.exp = self.exp[:pos1] + res + self.exp[pos2 + 1:]
        # Check if expression does not start with operator
        if self.exp[0] in self.operadores:
            return 'Expressão Incompleta!'
        # Check if there is more than one " . "
        count = self.exp[0].count('.')
        if count > 1:
            return 'Colocou ' + str(count) + ' vírgulas!'
        # Evaluate final expression
        if len(self.exp) > 1:
            self.exp = self.calculate(self.exp)
        # Return result
        try:
            return self.exp[0]
        except IndexError:
            pass


if __name__ == '__main__':
    eq = ['2', '^', '3']
    resultado = Calcular(eq).evaluate_exp()
    print(resultado)
