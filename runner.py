import requests
import subprocess
import re
import multiprocessing

# Define a list of script-host URLs for the Python scripts
script_url = [
    "URL_HERE",
    # add more if u want
]

def run_script(script_content):
    try:
        process = subprocess.Popen(['python', '-u', '-c', script_content], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in iter(process.stdout.readline, ''):
            print(line.strip())

        process.communicate()  # Wait for the process to finish
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def fetch_and_run_script(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            script_content = response.text

            # Use the 're' module to extract content within <pre> tags
            script_content_match = re.search(r'<pre>(.*?)</pre>', script_content, re.DOTALL)
            if script_content_match:
                script_content = script_content_match.group(1)

                # Run the script in a separate process
                process = multiprocessing.Process(target=run_script, args=(script_content,))
                process.start()
                process.join()
            else:
                print(f"No <pre> tags found in the script content")
        else:
            print(f"Failed to fetch script from {url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    for url in script_url:
        fetch_and_run_script(url)
