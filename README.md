    git clone https://github.com/JesseAldridge/clipmon
    cd clipmon
    chmod +x install.sh
    ./install.sh

This is a simple script that polls your clipboard.
When it detects a line of text with a path and a line number, such as

    ReferenceError: get_extra_classes is not defined in /Users/Jesse/Dropbox/CardBrew/03_move/tests/move_test.js (line 25)

it will attempt to open that path in your text editor at that line.
