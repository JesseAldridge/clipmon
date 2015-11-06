launchctl unload ~/Library/LaunchAgents/com.jessealdridge.clipmon.plist
launchctl load ~/Library/LaunchAgents/com.jessealdridge.clipmon.plist
launchctl list | grep jesse
sleep 1
tail ~/clipmon.log ~/clipmon.err
