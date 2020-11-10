# feeds2html

While I'm using a feed readers, I'm tired of going through all of them and
marking them as read. Here's a script to fetch a bunch of feed and create a
simple HTML page that I can check whenever I want to see the last items. We
don't keep any history as there is no point.

Result is available here: <https://os.chown.me/>

## Installation

1. Put the script somewhere
2. Install python packages *jinja2* and *feedparser*
3. Make a list of the feeds you're interested in, in a text file
4. Run the script with the path of the text file as the argument
5. Serve the html page
