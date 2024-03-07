# Top Latest News Extractor

## Problem Statement

- The task was to create an application which will return the latest 6 stories on Time.com's when called as a custom API.
- Instructions:
  - Do process HTML using a basic approach to extract the latest stories.
  - Do not use internal or external libraries/packages to process the text.
  - We can use any language of our choice.
- SPECIFICATIONS:
  - The API will be called as the service like this, assuming the URL to the service is 'http://<localhost>/getTimeStories' . This is a simple GET call. In response, we want a JSON object array with the latest 6 stories.

## Setup

```sh
pip install -r requirement.txt
```

## Explanation

- The Flask application defines a route (`/getTimeStories`) to handle GET requests.
- When a GET request is made, the application extracts the latest stories from `https://time.com`.
- The HTML content is parsed to extract story titles and links.
- The extracted stories are returned as a JSON response.