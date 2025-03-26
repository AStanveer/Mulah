from flask import Flask, render_template

app = Flask(__name__)

import pandas as pd

#reading csv file
df = pd.read_csv('Table_Input.csv')

#converting to dict for processing
values_dict = df.set_index("Index #")["Value"].to_dict()

# computing values for table 2
alpha = int(values_dict.get("A5", 0) + values_dict.get("A20", 0))
beta = int(values_dict.get("A15", 1) // values_dict.get("A7", 1))  # Integer division
charlie = int(values_dict.get("A13", 0) * values_dict.get("A12", 0))

#Table 2 processed values
table_2 = pd.DataFrame({
    "Category": ["Alpha", "Beta", "Charlie"],
    "Value": [alpha, beta, charlie]
})

#styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {{
    border: 1px solid black;
    border-collapse: collapse;
}}
th, td {{
    text-align: center; 
    vertical-align: middle;
}}
#table2 {{
    width: 80%;
}}
#table2 th, #table2 td {{
    width: 40%;  
}}
</style>
</head>
<body>
    <h2>Table 1</h2>
    {df.to_html(index=False, border=1)}

    <h2> Table 2</h2>
    {table_2.to_html(index=False, border=1, table_id="table2")}
</body>
</html>
"""

with open("Table.html", "w") as f:
    f.write(html_content)


@app.route('/')
def home():
    return render_template('Table.html')

if __name__ == '__main__':
    app.run(debug=True)
