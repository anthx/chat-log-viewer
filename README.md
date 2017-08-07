# chat-log-viewer
Parses chat log backups into easy to view HTML files.

Run the script with the parameter of a Viber or Facebook chat log CSV backup and a HTML output of the chat log should be created in the same location as the script.

(Facebook is kinda ugly for now though, but does work)

## How to get a CSV backup:
### Viber
(possibly, this only works on Android)

1. Outside of a chat, tap the overflow button (hamburger)
2. Tap Settings
3. Tap "Calls and Messages"
4. Tap "Email message history"
5. Choose Google Drive or email it to yourself.
6. It will be a ZIP file, so extract it some place.

### Facebook
1. Follow the directions at https://github.com/ownaginatious/fbchat-archive-parser
2. Use the sub-section for "Can I get each conversation into a separate file?"

### Usage
Pass the filename of the chat log as parameter 1 and either "viber" or "messenger" as parameter 2, sans quotes

Needs Jinja2 and Python 3.6

