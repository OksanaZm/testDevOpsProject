import os

def createFolder(path: str, prefix: str, counts: int, mode: int):
    for i in range(1, counts):
        try:
            os.mkdir(f"{os.sep}{path}{os.sep}{prefix}{str(i)}", mode)
        except FileExistsError:
            # directory already exists
            pass


if __name__ == '__main__':
    createFolder("home", "usr", 20, 551)
