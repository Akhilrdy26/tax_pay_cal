from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    total_hrs = float(request.form['hours'])
    pay_perhr = float(request.form['pay'])
    
    # Calculate before-tax pay
    bef_tax_pay = total_hrs * pay_perhr
    
    # Calculate PRSI (4.1% of before-tax pay, but minimum €12 rule applies)
    prsi = round((bef_tax_pay * 4.1) / 100, 2)
    if prsi < 12:
        prsi = 0

    # Calculate base tax (20% of before-tax pay)
    base_tax = round((bef_tax_pay * 20) / 100, 2)

    # PAYE (after deducting tax credit of 153.85)
    paye = round(base_tax - 153.85, 2) if base_tax > 153.85 else 0

    # Calculate after-tax pay
    aft_tax = round(bef_tax_pay - paye - prsi, 2)

    return f"""
    <html>
    <head>
        <title>Calculation Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 350px;
                margin: auto;
            }}
            h2 {{
                color: #333;
            }}
            p {{
                font-size: 18px;
                margin: 10px 0;
            }}
            .highlight {{
                font-weight: bold;
                font-size: 20px;
                color: #28a745;
            }}
            a {{
                display: inline-block;
                margin-top: 15px;
                padding: 10px 15px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Calculation Results</h2>
            <p>Before Tax Pay: <span class="highlight">€{bef_tax_pay}</span></p>
            <p>PRSI Deduction: <span class="highlight">€{prsi}</span></p>
            <p>PAYE Deduction: <span class="highlight">€{paye}</span></p>
            <p><strong>Your Net Pay: <span class="highlight">€{aft_tax}</span></strong></p>
            <a href='/'>Go Back</a>
        </div>
    </body>
    </html>
"""


if __name__ == '__main__':
    app.run(debug=True)
