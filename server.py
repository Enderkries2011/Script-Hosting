from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Script Hosting Service</title>
            <link rel="icon" type="image/png" href="static/python.png">
        </head>
        <body>Welcome to the Script Hosting Service!</body>
    </html>
    """

@app.route('/raw/<script_name>')
def get_script(script_name):
    try:
        # Define the directory where your Python scripts are stored in Replit
        script_directory = "scripts"

        # Create the directory if it doesn't exist
        if not os.path.exists(script_directory):
            os.makedirs(script_directory)

        # Check if the script_name includes the .py extension, and add it if missing
        if not script_name.endswith('.py'):
            script_name += '.py'

        script_path = os.path.join(script_directory, script_name)

        # Read the content of the script file
        with open(script_path, 'r') as script_file:
            script_content = script_file.read()

        # Set the title of the HTML page to the script name
        title = script_name

        # Define CSS style to increase font size
        style = "<style>pre { font-size: 1.2em; }</style>"

        # Construct the HTML page with the script content and title
        html_page = f"""
        <html>
            <head>
                <title>{title}</title>
                <link rel="icon" type="image/png" href="static/python.png">
                {style}
            </head>
            <body>
                <pre>{script_content}</pre>
            </body>
        </html>
        """

        return html_page
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/download/<script_name>')
def download_script(script_name):
    try:
        # Define the directory where your Python scripts are stored in Replit
        script_directory = "scripts"

        # Check if the script_name includes the .py extension, and add it if missing
        if not script_name.endswith('.py'):
            script_name += '.py'

        script_path = os.path.join(script_directory, script_name)

        return send_file(script_path, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
