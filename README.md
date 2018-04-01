# chat-log-viewer
Parses chat log backups into easy to view HTML files.

Run the script with the parameter of a Viber or Facebook or KakaoTalk chat log CSV backup and a HTML output of the chat log should be created in the same location as the script.

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

### KakaoTalk
(possibly this only works on Android)

1. Inside the chat you want to export, tap the overflow button (hamburger)
2. Tap Settings (cog wheel on the bottom-right corner)
3. Tap "Export Messages"
4. Either:
   * Export the text only:
       1. Tap Send Text Only
       2. Choose Google Drive or email or some other app
       to get it off the phone
       3. It's a plain text file, which should be called "KakaoTalkChats.txt"
   * Export the messages and media to phone storage
       1. Tap Save All Messages to Internal Storage
       2. It will be saved to /storage/emulated/internal/0/KakaoTalk/Chats/KakaoTalk_Chats_<the current time>
       3. You'll need to conect your phone to your PC with a USB cable or 
       use some program to explore the contents of the 
       storage and get it off the phone.
       4. Note that currently this parser script doesn't 
       handle the multimedia contents from this export,
       but I plan to add this.

### Usage
Pass the filename of the chat log as parameter 1 and either "viber" or "messenger" or "kakao" as parameter 2, sans quotes

Needs Jinja2 and Python 3.6 and python-dateutil

