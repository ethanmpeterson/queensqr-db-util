import easygui

#path = easygui.fileopenbox()

def selector(fileType):
    return easygui.fileopenbox(msg = "Select A PNG File", title = "Specify PNG", filetypes = fileType) # returns string of file path to be used in upload process

selector("*.png")