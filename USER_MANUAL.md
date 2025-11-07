# User Manual - Modern Text Editor

Complete guide for using Modern Text Editor

Powered by ProjectsHUB

---

## Table of Contents

1. Getting Started
2. Interface Overview
3. File Operations
4. Text Editing
5. Navigation
6. View Controls
7. Keyboard Shortcuts
8. Tips and Tricks
9. Troubleshooting

---

## 1. Getting Started

### Launching the Application

Method 1: Command Line
```bash
python main.py
```

Method 2: Double-click
Double-click main.py if Python is configured as default

### First Launch

When you first launch the application:
- A blank editor window opens
- Title shows "Text Editor - Untitled"
- You can immediately start typing
- Status bar shows cursor position at Line 1, Column 1

---

## 2. Interface Overview

### Main Window Components

The editor interface consists of five main areas:

#### Menu Bar (Top)
- File: File operations
- Edit: Text editing operations
- View: Display controls
- Help: Information and support

#### Toolbar (Below Menu Bar)
Quick access buttons for common operations:
- New: Create new file
- Open: Open existing file
- Save: Save current file
- Cut: Cut selected text
- Copy: Copy selected text
- Paste: Paste from clipboard
- Undo: Reverse last action
- Redo: Reapply undone action

#### Editor Area (Center)
- Line Numbers (Left): Shows line numbers
- Text Editor (Right): Main editing area
- Scrollbar (Right Edge): Navigate long documents

#### Status Bar (Bottom)
Left to Right:
- Cursor Position: Current line and column
- Modified Status: Shows if file has unsaved changes
- ProjectsHUB Branding
- File Type: Detected file format

### Color Scheme

The application uses a modern dark theme:
- Background: Dark gray (#1e1e1e)
- Text: Light gray (#d4d4d4)
- Selection: Blue (#264f78)
- Toolbar: Dark (#2d2d30)
- Status Bar: Blue (#007acc)

---

## 3. File Operations

### Creating a New File

Steps:
1. Click File > New (or press Ctrl+N)
2. If current file is modified, choose to save or discard
3. Editor clears and shows blank document
4. Title changes to "Text Editor - Untitled"
5. Start typing

### Opening an Existing File

Steps:
1. Click File > Open (or press Ctrl+O)
2. Navigate to file location in dialog
3. Select file from list
4. Click "Open" button
5. File content loads in editor

Supported Formats:
- Text Files (.txt)
- Python Files (.py)
- JavaScript Files (.js)
- HTML Files (.html)
- CSS Files (.css)
- All Files (*.*)

### Saving a File

For New Files:
1. Click File > Save (or press Ctrl+S)
2. Choose save location
3. Enter filename
4. Select file type from dropdown
5. Click "Save"

For Existing Files:
1. Click File > Save (or press Ctrl+S)
2. File saves automatically to current location
3. Success message appears

### Save As (Create Copy)

Steps:
1. Click File > Save As (or press Ctrl+Shift+S)
2. Choose new location or name
3. Select file type
4. Click "Save"
5. Editor switches to new file

### Closing Files

Proper Way:
1. Click File > Exit (or press Alt+F4)
2. If file is modified, dialog appears
3. Choose:
   - Yes: Save and exit
   - No: Exit without saving
   - Cancel: Return to editing

---

## 4. Text Editing

### Basic Typing

- Click in editor area
- Start typing normally
- Text appears at cursor position
- Line numbers update automatically

### Selecting Text

Method 1: Mouse
- Click and drag to select text
- Double-click to select word
- Triple-click to select line

Method 2: Keyboard
- Hold Shift + Arrow keys to select
- Ctrl+A to select all text

### Cut, Copy, and Paste

Cut Text:
- Select text
- Click Edit > Cut (or press Ctrl+X)
- Text removed and copied to clipboard

Copy Text:
- Select text
- Click Edit > Copy (or press Ctrl+C)
- Text copied to clipboard

Paste Text:
- Position cursor
- Click Edit > Paste (or press Ctrl+V)
- Clipboard content inserted

### Undo and Redo

Undo:
- Click Edit > Undo (or press Ctrl+Z)
- Reverses last change
- Can undo multiple times

Redo:
- Click Edit > Redo (or press Ctrl+Y)
- Reapplies undone change
- Only works after undo

### Text Modification

The editor tracks modifications:
- Asterisk (*) appears in title when modified
- "Modified" appears in status bar
- Save prompts appear before closing

---

## 5. Navigation

### Moving the Cursor

Keyboard:
- Arrow Keys: Move one character/line
- Home: Move to line start
- End: Move to line end
- Ctrl+Home: Move to document start
- Ctrl+End: Move to document end
- Page Up/Down: Move one screen

Mouse:
- Click anywhere to position cursor
- Use scrollbar for long documents

### Line Numbers

- Always visible on left side
- Update automatically
- Help identify current position
- Useful for debugging code

---

## 6. View Controls

### Zoom In

Steps:
1. Click View > Zoom In (or press Ctrl++)
2. Font size increases by 2 points
3. Maximum size: 32 points
4. Affects both editor and line numbers

### Zoom Out

Steps:
1. Click View > Zoom Out (or press Ctrl+-)
2. Font size decreases by 2 points
3. Minimum size: 8 points
4. Useful for viewing more content

### Reset Zoom

Steps:
1. Click View > Reset Zoom (or press Ctrl+0)
2. Font size returns to default (11 points)
3. Restores standard view

---

## 7. Keyboard Shortcuts

### File Operations
```
Ctrl+N          New file
Ctrl+O          Open file
Ctrl+S          Save file
Ctrl+Shift+S    Save As
Alt+F4          Exit application
```

### Edit Operations
```
Ctrl+Z          Undo
Ctrl+Y          Redo
Ctrl+X          Cut
Ctrl+C          Copy
Ctrl+V          Paste
Ctrl+A          Select All
```

### View Operations
```
Ctrl++          Zoom In
Ctrl+-          Zoom Out
Ctrl+0          Reset Zoom
```

### Navigation
```
Home            Start of line
End             End of line
Ctrl+Home       Start of document
Ctrl+End        End of document
Page Up         Up one screen
Page Down       Down one screen
```

---

## 8. Tips and Tricks

### Productivity Tips

1. Use Keyboard Shortcuts
   - Faster than using mouse
   - Learn common shortcuts first
   - Practice regularly

2. Save Frequently
   - Press Ctrl+S often
   - Prevents data loss
   - Creates backup points for undo

3. Use Select All Wisely
   - Ctrl+A for quick selection
   - Useful for copying entire document
   - Good for formatting changes

4. Leverage Undo/Redo
   - Experiment fearlessly
   - Easy to revert changes
   - Multiple levels available

5. Monitor Status Bar
   - Check cursor position
   - Verify file type
   - Watch for unsaved changes

### File Management Tips

1. Use Descriptive Names
   - Clear, meaningful filenames
   - Include file extensions
   - Organize by project

2. Regular Backups
   - Save multiple versions
   - Use "Save As" for versions
   - Keep original copies

3. File Organization
   - Create project folders
   - Group related files
   - Use consistent naming

---

## 9. Troubleshooting

### Common Issues and Solutions

Issue: Application won't start
Solutions:
- Verify Python installation
- Check Python version (3.6+)
- Ensure tkinter is available
- Run: python --version

Issue: Cannot open file
Solutions:
- Check file exists
- Verify file permissions
- Ensure file path is correct
- Try "All Files" filter

Issue: Cannot save file
Solutions:
- Check folder permissions
- Verify disk space
- Close other programs using file
- Try different location

Issue: Keyboard shortcuts not working
Solutions:
- Ensure editor window has focus
- Click in editor area first
- Check if another program intercepts keys
- Try using menu instead

Issue: Text appears too small/large
Solutions:
- Use Ctrl+0 to reset zoom
- Adjust with Ctrl++ or Ctrl+-
- Check display settings

Issue: Line numbers not visible
Solutions:
- Restart application
- Check window width
- Maximize window

Issue: Changes not saving
Solutions:
- Check "Modified" indicator
- Use Ctrl+S explicitly
- Verify file path in title
- Check for error messages

### Error Messages

"Failed to open file"
- File may be in use by another program
- Check file permissions
- Verify file format is supported

"Failed to save file"
- Insufficient permissions
- Disk space full
- Invalid file path

### Performance Issues

If editor is slow:
- Close other applications
- Check available memory
- Restart application
- Reduce file size

### Getting Additional Help

For further assistance:
1. Check README.md for detailed documentation
2. Review QUICKSTART.md for basics
3. Check CHANGELOG.md for version info
4. Refer to CONTRIBUTING.md for support options

---

## Appendix A: File Format Support

### Text Files (.txt)
- Plain text format
- Universal compatibility
- Default format
- No special formatting

### Python Files (.py)
- Python source code
- UTF-8 encoding
- Supports all Python syntax
- Ideal for scripting

### JavaScript Files (.js)
- JavaScript source code
- Node.js compatible
- Browser script support
- Modern ES6+ syntax

### HTML Files (.html)
- Web page markup
- Full HTML5 support
- CSS and JavaScript embedding
- Preview in browsers

### CSS Files (.css)
- Stylesheet definitions
- All CSS3 features
- Responsive design support
- Framework compatible

---

## Appendix B: System Requirements

### Minimum
- OS: Windows 7, macOS 10.12, Linux
- Python: 3.6+
- RAM: 512 MB
- Storage: 10 MB

### Recommended
- OS: Windows 10/11, macOS 11+, Modern Linux
- Python: 3.9+
- RAM: 2 GB
- Storage: 50 MB

---

## Appendix C: Version Information

Current Version: 1.0.0
Release Date: October 20, 2025
Platform: Cross-platform (Windows, macOS, Linux)
License: MIT

---

Powered by ProjectsHUB

For the latest updates and documentation, refer to the project repository.

End of User Manual
