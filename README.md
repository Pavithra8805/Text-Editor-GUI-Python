# Modern Text Editor

A feature-rich, modern text editor built with Python and Tkinter, featuring a dark theme interface, line numbers, and comprehensive editing capabilities.

Powered by ProjectsHUB

---

## Project Overview

This is a fully functional text editor application with a modern user interface that supports multiple file formats, keyboard shortcuts, and essential text editing features. The application provides a clean, distraction-free environment for editing text files with professional-grade functionality.

---

## Features

### Core Functionality
- Create new files
- Open existing files (multiple format support)
- Save and Save As functionality
- Auto-save prompts before closing
- File modification tracking

### Editing Features
- Undo and Redo operations
- Cut, Copy, and Paste
- Select All functionality
- Line numbering
- Real-time cursor position tracking

### User Interface
- Modern dark theme
- Syntax-aware file type detection
- Customizable zoom levels
- Toolbar with quick access buttons
- Comprehensive menu system
- Status bar with file information

### Keyboard Shortcuts
- Ctrl+N: New file
- Ctrl+O: Open file
- Ctrl+S: Save file
- Ctrl+Shift+S: Save As
- Ctrl+Z: Undo
- Ctrl+Y: Redo
- Ctrl+X: Cut
- Ctrl+C: Copy
- Ctrl+V: Paste
- Ctrl+A: Select All
- Ctrl++: Zoom In
- Ctrl+-: Zoom Out
- Ctrl+0: Reset Zoom
- Alt+F4: Exit application

### Supported File Formats
- Text Files (.txt)
- Python Files (.py)
- JavaScript Files (.js)
- HTML Files (.html)
- CSS Files (.css)
- JSON Files (.json)
- XML Files (.xml)
- All Files (*.*)

---

## Technical Specifications

### Requirements
- Python 3.6 or higher
- Tkinter (included with standard Python installation)

### Dependencies
- tkinter (GUI framework)
- os (file operations)
- datetime (time tracking)

### Architecture
The application follows Object-Oriented Programming principles with a single class structure that encapsulates all functionality.

---

## Installation Guide

### Step 1: Prerequisites
Ensure Python 3.6 or higher is installed on your system.

Check Python version:
```bash
python --version
```

### Step 2: Download the Project
Clone or download the project files to your local machine.

### Step 3: Verify Files
Ensure the following file is present:
- main.py

### Step 4: Run the Application
Navigate to the project directory and execute:
```bash
python main.py
```

---

## Quick run (Windows)

If you'd like a one-click or scriptable way to run the editor on Windows, this project includes two helper launchers:

- `run.bat` — a double-clickable batch file that launches the app using the bundled Python path and pauses so console output is visible.
- `run.ps1` — a PowerShell script that runs the app using the explicit interpreter. You may need to allow local scripts with:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

To use them from the project folder:

```powershell
# From PowerShell (recommended)
.
cd 'C:\Users\Hi\Desktop\Test Editor GUI Python'
.
# Run PowerShell launcher
.\run.ps1

# Or run the batch launcher from PowerShell or Explorer
.\run.bat
```

Both scripts call the explicit Python interpreter: `C:\Program Files\Python313\python.exe`. If you prefer `python` on PATH, edit the scripts accordingly.


---

## Usage Guide

### Creating a New File

Step 1: Click on "File" menu or press Ctrl+N
Step 2: Start typing in the editor
Step 3: Save your work using Ctrl+S or File > Save

### Opening an Existing File

Step 1: Click "File" > "Open" or press Ctrl+O
Step 2: Navigate to your file location
Step 3: Select the file and click "Open"
Step 4: The file content will appear in the editor

### Saving Files

For New Files:
Step 1: Press Ctrl+S or click "File" > "Save"
Step 2: Choose a location and filename
Step 3: Select file type from the dropdown
Step 4: Click "Save"

For Existing Files:
Step 1: Press Ctrl+S
Step 2: File is automatically saved to current location

### Using Editing Features

Undo/Redo:
- Use Ctrl+Z to undo last action
- Use Ctrl+Y to redo undone action

Copy/Cut/Paste:
- Select text with mouse
- Use Ctrl+C to copy, Ctrl+X to cut
- Use Ctrl+V to paste

Zoom Control:
- Press Ctrl++ to increase font size
- Press Ctrl+- to decrease font size
- Press Ctrl+0 to reset to default size

### Understanding the Interface

Menu Bar:
- File: File operations (New, Open, Save, Exit)
- Edit: Editing operations (Undo, Redo, Cut, Copy, Paste)
- View: Display options (Zoom controls)
- Help: Information about the application

Toolbar:
- Quick access buttons for common operations
- Includes New, Open, Save, Cut, Copy, Paste, Undo, Redo

Editor Area:
- Main text editing area with line numbers
- Dark theme for comfortable viewing
- Automatic line wrapping

Status Bar:
- Shows current line and column position
- Displays file modification status
- Shows detected file type
- ProjectsHUB branding

---

## Project Structure

```
Text Editor GUI/
|
|-- main.py                 # Main application file
|-- README.md              # Project documentation
```

---

## Code Structure

### Class: ModernTextEditor

Main application class that handles all functionality.

#### Methods:

Initialization:
- __init__(root): Initializes the application
- setup_styles(): Configures color scheme and styles

UI Creation:
- create_menu(): Builds menu bar
- create_toolbar(): Creates toolbar with buttons
- create_status_bar(): Sets up status bar
- create_editor(): Initializes text editor widget
- create_line_numbers(): Adds line number display

File Operations:
- new_file(): Creates new blank document
- open_file(): Opens existing file
- save_file(): Saves current file
- save_as_file(): Saves file with new name

Editing Operations:
- undo(): Undoes last action
- redo(): Redoes undone action
- cut(): Cuts selected text
- copy(): Copies selected text
- paste(): Pastes clipboard content
- select_all(): Selects all text

View Operations:
- zoom_in(): Increases font size
- zoom_out(): Decreases font size
- reset_zoom(): Resets to default font size

Helper Methods:
- update_line_numbers(): Updates line number display
- update_status_bar(): Updates status bar information
- update_title(): Updates window title
- update_file_type(): Detects and displays file type
- on_content_changed(): Handles content modifications
- on_closing(): Handles application exit
- bind_shortcuts(): Binds keyboard shortcuts
- show_about(): Displays about information

---

## Troubleshooting

### Issue: Application won't start
Solution: Verify Python installation and ensure Tkinter is available

### Issue: Cannot open files
Solution: Check file permissions and ensure file path is accessible

### Issue: Save operation fails
Solution: Verify write permissions in target directory

### Issue: Keyboard shortcuts not working
Solution: Ensure application window has focus

---

## Future Enhancements

Potential features for future versions:
- Syntax highlighting for programming languages
- Find and replace functionality
- Multi-tab support
- Auto-completion
- Theme customization
- Plugin system
- Search in files
- Recent files list
- Customizable keyboard shortcuts

---

## System Requirements

### Minimum Requirements:
- Operating System: Windows 7/8/10/11, macOS 10.12+, Linux
- Python: 3.6 or higher
- RAM: 512 MB
- Storage: 10 MB free space

### Recommended Requirements:
- Operating System: Windows 10/11, macOS 11+, Linux (latest)
- Python: 3.9 or higher
- RAM: 2 GB
- Storage: 50 MB free space

---

## License

This project is part of the ProjectsHUB collection.

---

## Version History

### Version 1.0.0 (Current)
- Initial release
- Core text editing functionality
- Modern dark theme UI
- Line numbering
- File operations (New, Open, Save, Save As)
- Edit operations (Undo, Redo, Cut, Copy, Paste)
- Zoom controls
- Status bar with file information
- Keyboard shortcuts
- Multiple file format support

---

## Contact and Support

For issues, suggestions, or contributions, please refer to the ProjectsHUB repository.

---

## Acknowledgments

Built with Python and Tkinter
Modern UI inspired by popular code editors
Part of the ProjectsHUB project collection

---

Powered by ProjectsHUB
