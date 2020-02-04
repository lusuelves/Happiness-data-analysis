"""
@author: luciasuelves
"""

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("SENDGRID_APIKEY")
print(f"We have a github token: {token[0:3]}")

def send_mail(sub_happy, to):
    message = Mail(
    from_email='luciasuelves@gmail.com',
    to_emails= to,
    subject='Happiness data report',
    html_content = """\
        <html>
          <head></head>
          <body>
            <h1>Happiness data analysis</h1>
            <p style = "font-size: 1">
               Here you have a representative sample of the dataframe<br>
               If you are interested on how happiness score is calculated you can find more information here <a href="https://worldhappiness.report/ed/2016/">Happiness report 2016</a> .
            </p>"""
            +sub_happy.to_html()+"""
            <h2> Suicide vs Happiness</h2>
                <img src = 'https://github.com/lusuelves/Happiness-data-analysis/blob/master/images/temperature.png?raw=true' width = '500' height = '400' alt = 'Temperature vs happiness'  />
            <h2> Temperature vs Happiness</h2>
                <img src = "https://github.com/lusuelves/Happiness-data-analysis/blob/master/images/precipitations.png?raw=true" alt = "Temperature vs happiness" width = '500' height = '400'>
            <h2> Precipitations vs Happiness</h2>
                <img src = "https://github.com/lusuelves/Happiness-data-analysis/blob/master/images/suicide.png?raw=true" alt = "Suicide vs happiness" width = '500' height = '400'/>
            <h2> Olympic medals vs Happiness</h2>
                <img src = "https://raw.githubusercontent.com/lusuelves/Happiness-data-analysis/master/images/olympic.png" alt = "Medals vs happiness" width = '500' height = '400'/>
          </body>
        </html>
        """)
    try:
        sg = SendGridAPIClient(token)
        sg.send(message)
        print("Email sent")
    except Exception as e:
        print(e.message)
    