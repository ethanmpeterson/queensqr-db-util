import easygui

# PNG File Selector Function

def selector():
    return easygui.fileopenbox(msg = "Select A PNG File", title = "Specify PNG", filetypes = ("PNG", "*.png")) # returns string of file path to be used in upload process
