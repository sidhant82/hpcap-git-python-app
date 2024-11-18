

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a form for user input
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> welcome  python Calculator</title>
</head>
<body>
<h1>sidhant kumar sah</h1>
<h1>prn 240840141019 </h1>
<h1>sidhant</h1>
    <h1>Calculator App by {{ name }} (PRN: {{ prn }})</h1>
    <form method="post" action="/">
        <label>Number 1:</label>
        <input type="number" name="num1" step="any" required>
        <br><br>
        
        <label>Number 2:</label>
        <input type="number" name="num2" step="any" required>
        <br><br>
        
        <label>Operation:</label>
        <select name="operation" required>
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <br><br>
        
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = "Raj Shree"  
    prn = "240840141015"    
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "undefined"
        except (ValueError, ZeroDivisionError):
            result = "Error"

    return render_template_string(html_template, name=name, prn=prn, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

