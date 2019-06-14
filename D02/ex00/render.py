# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    Reader.py                                   .::    .:/ .      .::         #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/12 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/12 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #
import sys
import os


class FileReader:
    """ classe generique qui gere le fichier en lecture """

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """ Methode generique doit etre specifiee """
        pass


class Settings(FileReader):
    """ classe derivee pour le fichier settings """

    def __init__(self, filename):
        super().__init__(filename)
        self.read_file()

    def read_file(self):
        """ Methode pour extraire les parametres du fichier settings dans un dictionnaire """
        self.params = dict()
        try:
            with open(self.filename) as f:
                for line in f:
                    data = line.split("=")
                    self.params[data[0].strip(" ")] = data[1].strip(
                        "\" \n")  # Eliminer les caraceteres inutiles
        except FileNotFoundError as e:
            print("Le fichier {0} n'existe pas".format(e.filename))
            exit(1)


class Reader(FileReader):
    """ classe derivee pour le fichier template """

    def __init__(self, filename, setting_filename):
        super().__init__(filename)
        self.settings = Settings(setting_filename)

    def format_line(self, line):
        """ cette remplace les {parametre} dans la ligne traitee """
        html_line = line
        for cle in self.settings.params:
            html_line = html_line.replace(
                "{" + cle + "}", self.settings.params[cle])
        return html_line

    def html_writer(self, html_filename):
        html_file = open(html_filename, "w")
        try:
            with open(self.filename) as f:
                for line in f:
                    html_line = self.format_line(line)
                    html_file.write(html_line)
        except FileNotFoundError as e:
            print("Le fichier {0} n'existe pas".format(e.filename))
            exit(1)

        html_file.close()


def Render(filename):
    file, extension = os.path.splitext(filename)
    if extension == ".template":
        t = Reader(filename, "settings.py")
        t.html_writer(file+".html")
    else:
        print(
            "Le fichier {0} n'a l'extension : '.template'".format(filename))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        Render(sys.argv[1])
