#!/usr/bin/env python3

# Copyright (c) 2020 Daniel Jakots
#
# Licensed under the MIT license. See the LICENSE file.

import time

import feedparser
import jinja2

FEEDS_PER_LINE = 4
MAX_ENTRIES = 9


def parse_feed(feed):
    feed = feedparser.parse(feed)
    title = feed['feed']['title']
    parsed_entries = []
    for n, entry in enumerate(feed["entries"]):
        if n+1 > 100:
            break
        parsed_entry = {}
        parsed_entry["title"] = entry["title"]
        parsed_entry["link"] = entry["link"]
        parsed_entry["timestamp"] = time.mktime(entry["updated_parsed"])
        parsed_entries.append(parsed_entry)
    parsed_entries.sort(reverse=True, key=lambda i: i["timestamp"])
    parsed_feed = {title: parsed_entries[:MAX_ENTRIES]}

    # We need to parse more because their order is random so we may get older entries
    return parsed_feed


def create_html(chunk_feeds):
    with open("index.html.j2", "r") as f:
        template = f.read()
    jinja2_template = jinja2.Template(template)
    index = jinja2_template.render(chunk_feeds=chunk_feeds)
    with open(f"index.html", "w") as f:
        f.write(index)
        f.write("\n")


# https://stackoverflow.com/a/312464
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    feeds = []
    feeds.append("https://www.reddit.com/r/montreal/.rss")
    feeds.append("https://www.reddit.com/r/quebec/.rss")
    parsed_feeds = []
    for feed in feeds:
        parsed_feeds.append(parse_feed(feed))
    chunk_feeds = chunks(parsed_feeds, FEEDS_PER_LINE)
    create_html(chunk_feeds)


if __name__ == "__main__":
    main()
