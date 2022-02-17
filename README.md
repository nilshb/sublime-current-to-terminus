# sublime-current-to-terminus

[Sublime Text](https://www.sublimetext.com/) plugin that sends current line to Terminus and advances cursor to 
end of next line.

# Install
- If you haven't already: Install [Terminus](https://packagecontrol.io/packages/Terminus "Package Control - Terminus")
- Copy `send-current-to-terminus.py` to your plugins folder (e.g. `.config/sublime-text/Packages/User`)
- Add your preferred key bindings, example:

```
{
  "keys": ["ctrl+alt+t"],
  "command": "toggle_terminus_panel",
  "args": {
    "cwd": "${file_path:${folder}}"
  }
},
{
  "keys": ["ctrl+enter"],
  "command": "send_current_to_terminus",
  "context": [
    { "key": "selection_empty", "operand": true },
    { "key": "num_selections", "operator": "equal", "operand": 1 },
  ],
}
```

Enjoy!
