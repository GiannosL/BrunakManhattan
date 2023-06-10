import subprocess


def main():
    """
    main function which runs the gui
    """
    # command for streamlit 
    command: list[str] = ['streamlit', 'run', 'gui.py', 
                          '--browser.gatherUsageStats=False', 
                          '--server.maxUploadSize', '2000']
    
    # run command
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()

    return 0


if __name__ == '__main__':
    main()
