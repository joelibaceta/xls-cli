import xlrd
from xls_cli.frame import Frame 
from xls_cli.grid import Grid 
from xls_cli.runner import Runner

def main():
    import argparse

    CLI_DESC = "It is a simple python tool to open xls files in the terminal"
    EPILOG = ("\033[1;37mThanks for trying xls-cli!\033[0m")

    PARSER = argparse.ArgumentParser(prog='xls-cli', description=CLI_DESC, epilog=EPILOG)
    PARSER.add_argument('file', type=str, help='input file') 

    ARGS = PARSER.parse_args()

    try:
        Runner.open_file(ARGS.file)
    except (KeyboardInterrupt):
        pass

if __name__ == '__main__':
    main()

