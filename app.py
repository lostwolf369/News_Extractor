from flask import Flask, jsonify
import urllib.request

app = Flask(__name__)
app.json.sort_keys = False
url = "https://time.com"


def extract_latest_stories(html_content):
    """
        This function extracts the latest 6 stories from HTML 
        content by parsing specific HTML elements and attributes, 
        and returns them as a list of dictionaries containing the 
        story titles and links.
    """
    latest_stories = []
    off_set = 0

    for i in range(6):
        n = off_set + html_content[off_set:].find('<li class="latest-stories__item">')
        link_i = n + html_content[n:].find("<a href=") + len("<a href=") + 1
        link_j = link_i + html_content[link_i:].find(">") + len(">") - 2
        print(url + html_content[link_i:link_j])
        link = url + html_content[link_i:link_j]
        i = (
            off_set
            + html_content[off_set:].find('<h3 class="latest-stories__item-headline">')
            + len('<h3 class="latest-stories__item-headline">')
        )
        j = i + 1 + html_content[i + 1 :].find("</h3>")
        title = html_content[i:j]
        print(html_content[i:j])
        off_set = j

        latest_stories.append({"title": title, "link": link})

    return latest_stories


@app.route("/getTimeStories")
def get_time_stories():
    """
        This Flask route function get_time_stories sends a GET request 
        to a specified URL, reads the HTML content, extracts the latest 
        stories using the extract_latest_stories function, and returns 
        them as a JSON response
    """
    # Open the URL and read the HTML content
    with urllib.request.urlopen(url) as response:
        html_content: str = response.read().decode("utf8")

    # Extract the latest stories from the HTML content
    latest_stories = extract_latest_stories(html_content)

    # Return the latest stories as JSON response
    return jsonify(latest_stories)


if __name__ == "__main__":
    app.run()
