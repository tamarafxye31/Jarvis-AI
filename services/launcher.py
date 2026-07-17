import subprocess


class Launcher:

    @staticmethod
    def open(executable):

        subprocess.Popen(executable)