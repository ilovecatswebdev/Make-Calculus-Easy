from flask import Flask, redirect, render_template, request, url_for
from sympy import Symbol,symbols,sympify, diff, simplify,integrate,idiff
web = Flask(__name__)

@web.route('/')
def main():
    return render_template('finalindex.html')
@web.route('/about')
def about():
    return render_template('about.html')
@web.route('/revisionguides')
def revisionguides():
    return render_template('rguides.html')
@web.route('/revisionguides/differentiation')
def differentiation():
    return render_template('dguides.html')
@web.route('/revisionguides/differentiation/differentiationASguide1')
def differentiationASguide1():
    return render_template('12.1,12.2.html')
@web.route('/revisionguides/differentiation/differentiationASguide2')
def differentiationASguide2():
    return render_template('12.3,12.4,12.5.html')
@web.route('/revisionguides/differentiation/differentiationASguide3')
def differentiationASguide3():
    return render_template('12.6.html')
@web.route('/revisionguides/differentiation/differentiationASguide4')
def differentiationASguide4():
    return render_template('12.7.html')
@web.route('/revisionguides/differentiation/differentiationASguide5')
def differentiationASguide5():
    return render_template('12.8.html')
@web.route('/revisionguides/differentiation/differentiationASguide6')
def differentiationASguide6():
    return render_template('12.9.html')
@web.route('/revisionguides/differentiation/differentiationASguide7')
def differentiationASguide7():
    return render_template('12.10.html')
@web.route('/revisionguides/differentiation/differentiationASguide8')
def differentiationASguide8():
    return render_template('12.11.html')
@web.route('/revisionguides/differentiation/differentiationA2guide1')
def differentiationA2guide1():
    return render_template('9.1.html')
@web.route('/revisionguides/differentiation/differentiationA2guide2')
def differentiationA2guide2():
    return render_template('9.2.html')
@web.route('/revisionguides/differentiation/differentiationA2guide3')
def differentiationA2guide3():
    return render_template('9.3.html')
@web.route('/revisionguides/differentiation/differentiationA2guide4')
def differentiationA2guide4():
    return render_template('9.4.html')
@web.route('/revisionguides/differentiation/differentiationA2guide5')
def differentiationA2guide5():
    return render_template('9.5.html')
@web.route('/revisionguides/differentiation/differentiationA2guide6')
def differentiationA2guide6():
    return render_template('9.6.html')
@web.route('/revisionguides/differentiation/differentiationA2guide7')
def differentiationA2guide7():
    return render_template('9.7.html')
@web.route('/revisionguides/differentiation/differentiationA2guide8')
def differentiationA2guide8():
    return render_template('9.8.html')
@web.route('/revisionguides/differentiation/differentiationA2guide9')
def differentiationA2guide9():
    return render_template('9.9.html')
@web.route('/revisionguides/differentiation/differentiationA2guide10')
def differentiationA2guide10():
    return render_template('9.10.html')
@web.route('/revisionguides/integration')
def integration():
    return render_template('iguides.html')
@web.route('/revisionguides/integration/integrationASguide1')
def integrationASguide1():
    return render_template('13.1.html')
@web.route('/revisionguides/integration/integrationASguide2')
def integrationASguide2():
    return render_template('13.2,13.3.html')
@web.route('/revisionguides/integration/integrationASguide3')
def integrationASguide3():
    return render_template('13.4.html')
@web.route('/revisionguides/integration/integrationASguide4')
def integrationASguide4():
    return render_template('13.5,13.6,13.7.html')
@web.route('/revisionguides/integration/integrationA2guide1')
def integrationA2guide1():
    return render_template('11.1.html')
@web.route('/revisionguides/integration/integrationA2guide2')
def integrationA2guide2():
    return render_template('11.2,11.4.html')
@web.route('/revisionguides/integration/integrationA2guide3')
def integrationA2guide3():
    return render_template('11.3.html')
@web.route('/revisionguides/integration/integrationA2guide4')
def integrationA2guide4():
    return render_template('11.5.html')
@web.route('/revisionguides/integration/integrationA2guide5')
def integrationA2guide5():
    return render_template('11.6.html')
@web.route('/revisionguides/integration/integrationA2guide6')
def integrationA2guide6():
    return render_template('11.7.html')
@web.route('/revisionguides/integration/integrationA2guide7')
def integrationA2guide7():
    return render_template('11.8.html')
@web.route('/revisionguides/integration/integrationA2guide8')
def integrationA2guide8():
    return render_template('11.9.html')
@web.route('/revisionguides/integration/integrationA2guide9')
def integrationA2guide9():
    return render_template('11.10,11.11.html')
@web.route('/revisionguides/integration/integrationA2guide10')
def integrationA2guide10():
    return render_template('11.12.html')
@web.route('/calculatorfunction')
def calculatorfunction():
    return render_template('cfunction.html')
@web.route('/home')
def home():
    return render_template('finalindex.html')
@web.route("/submit", methods=["POST"])
def submit():
    user_inp = request.form["display"]
    user_inp = str(user_inp).replace("**", "^")
    user_inp = str(user_inp).replace("e^", "exp")
    user_inp = str(user_inp).replace("arccos", "acos")
    user_inp = str(user_inp).replace("arcsin", "asin")
    user_inp = str(user_inp).replace("arctan", "atan")
    user_inp = str(user_inp).replace("cosec", "csc")
    if '=' in str(user_inp):
        user_inp=str(user_inp)[:str(user_inp).find('=')]+"-("+str(user_inp)[str(user_inp).find('=')+1:]+")"
    if 'derivative' in request.form:
        return redirect(url_for("derivative", dexpr=user_inp))
    elif 'integral' in request.form:
        return redirect(url_for("integral", iexpr=user_inp))            

@web.route("/calculatorfunction/input/dexpr=<path:dexpr>")
def derivative(dexpr):
    try:
        x, y = symbols('x y')
        expr = sympify(dexpr)
        if y in expr.free_symbols:
            deriv = simplify(idiff(expr, y, x))
        else:
            deriv = simplify(diff(expr, x))
        dexpr = str(dexpr).replace("exp", "e^")
        dexpr = str(dexpr).replace("acos", "arccos")
        dexpr = str(dexpr).replace("asin", "arcsin")
        dexpr = str(dexpr).replace("atan", "arctan")
        dexpr = str(dexpr).replace("csc", "cosec")
        deriv = str(deriv).replace("**", "^")
        deriv = str(deriv).replace("exp", "e^")
        deriv = str(deriv).replace("acos", "arccos")
        deriv = str(deriv).replace("asin", "arcsin")
        deriv = str(deriv).replace("atan", "arctan")
        deriv = str(deriv).replace("csc", "cosec")
        deriv = str(deriv).replace("log", "ln")
    except (MemoryError, TypeError, ValueError) as error:
        return render_template(
            "cfunctionresult.html",
            func_error=f"{dexpr} (Invalid input!)",
            deriv_error=f"{error} (Error occurred!)",
        )
    else:
        return render_template(
            "cfunctionresult.html",
            func=f"`{dexpr}`",
            deriv=f"`{deriv}`",
        )
@web.route("/calculatorfunction/input/iexpr=<path:iexpr>")
def integral(iexpr):
    try:
        x=Symbol('x')
        i= simplify(integrate(iexpr, x))
        iexpr = str(iexpr).replace("exp", "e^")
        iexpr = str(iexpr).replace("acos", "arccos")
        iexpr = str(iexpr).replace("asin", "arcsin")
        iexpr = str(iexpr).replace("atan", "arctan")
        iexpr = str(iexpr).replace("csc", "cosec")
        i= str(i).replace("**", "^")
        i= str(i).replace("exp", "e^")
        i = str(i).replace("acos", "arccos")
        i = str(i).replace("asin", "arcsin")
        i = str(i).replace("atan", "arctan")
        i = str(i).replace("csc", "cosec")
        i = str(i).replace("log", "ln")
    except (MemoryError, TypeError, ValueError) as error:
        return render_template(
            "cfunctionresult.html",
            func_error=f"{iexpr} (Invalid input!)",
            i_error=f"{error} (Error occurred!)",
        )
    else:
        return render_template(
            "cfunctionresult.html",
            func=f"`{iexpr}`",
            i=f"`{i}`",
        )

@web.errorhandler(Exception)
def exception_handler(error):
    return str(error)
if __name__ == "__main__":
    web.run(debug=False)