This is a simple script that polls your clipboard.
When it detects a line of text with a path and a line number, e.g.

    ReferenceError: get_extra_classes is not defined in /Users/Jesse/Dropbox/CardBrew/03_move/tests/move_test.js (line 25)

it will attempt to open that path at that line in your text editor.

Installation:

    ln com.jessealdridge.open_clipboard.plist ~/Library/LaunchAgents/
    launchctl unload ~/Library/LaunchAgents/com.jessealdridge.open_clipboard.plist && launchctl load ~/Library/LaunchAgents/com.jessealdridge.open_clipboard.plist

For troubleshooting, you can run it like this:

    launchctl unload ~/Library/LaunchAgents/com.jessealdridge.open_clipboard.plist && launchctl load ~/Library/LaunchAgents/com.jessealdridge.open_clipboard.plist && launchctl list | grep jesse && tail -f ~/open_clipboard.log ~/open_clipboard.err

MIT License
