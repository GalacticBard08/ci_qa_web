import json
import os
import constants
import sys


class JSON_file():
    """To save the obtained results and compare them with the reference ones"""

    def __init__(self, name_prj, level_control):
        self.name_prj = name_prj
        self.level_control = level_control
        self.path_to_file = constants.PATH_TO_RESULTS_FILE
        self.data = ''

    def open(self):
        """open and read the file"""
        with open(self.path_to_file) as f:
            self.data = json.loads(f.read())
            return self.data['results_web'][0]

    def create(self, value):
        """create a new json file and write the first result"""
        with open(self.path_to_file, 'w') as f:
            data = {}
            data['results_web'] = [{value[0]: value[1]}]
            data['results_cli'] = [{}]
            json.dump(data, f)

    def append_value(self, value):
        """Adding results"""
        with open(self.path_to_file, 'w') as f:
            self.data['results_web'][0][value[0]] = value[1]
            json.dump(self.data, f)


class BeforeWork():

    @staticmethod
    def prepare_path_project():
        if constants.NAME_TESTS_FOR_BENCH not in sys.argv:
            not_found_files = []
            projects = {}
            path_to_files = BeforeWork.search_files_for_analysis(constants.CURRENT_PATH, constants.FILES_FOR_ANALYSIS_DIRECTORY)
            if path_to_files:
                for language_prj in constants.ALL_LANGUAGE_PROJECTS:
                    for_stat = os.path.join(path_to_files, constants.ALL_LANGUAGE_PROJECTS[language_prj][0])
                    for_dyn = os.path.join(path_to_files, constants.ALL_LANGUAGE_PROJECTS[language_prj][1])
                    for file in [for_stat, for_dyn]:
                        if not os.path.exists(file):
                            not_found_files.append(file)
                    projects[language_prj] = [
                        for_stat,
                        for_dyn]
                if not_found_files != []:
                    files = ' '.join(not_found_files)
                    raise Exception(f'Files for analysis not found! ({files})') from None
            else:
                raise Exception(f'Files for analysis not found!') from None
        else:
            projects = {}
        return projects

    @staticmethod
    def prepare_link(link):
        if link[:7] != 'http://':
            return f'http://{link}'
        else:
            return link

    @staticmethod
    def get_path_standart_results():
        path = BeforeWork.search_files_for_analysis(constants.CURRENT_PATH, constants.RESULTS_ANALYSIS_FILE_NAME)
        if path == '':
            path = os.path.normpath(
                constants.CURRENT_PATH + os.sep + os.pardir + os.sep + constants.RESULTS_ANALYSIS_FILE_NAME)
        constants.PATH_TO_RESULTS_FILE = path
        return constants.PATH_TO_RESULTS_FILE

    @staticmethod
    def search_files_for_analysis(current_path, wanted_file):
        """функция ищет файл/каталог. Каждый раз при неудаче переходя в родительский каталог
        current_path - текущий каталог с которого начинается поиск
        wanted_file - искомый файл или каталог"""
        if os.path.exists(os.path.normpath(current_path + os.sep + wanted_file)):
            return os.path.normpath(current_path + os.sep + wanted_file)
        elif current_path == os.getenv('HOME'):
            return ''
        else:
            return BeforeWork.search_files_for_analysis(os.path.normpath(current_path + os.sep + os.pardir),
                                                        wanted_file)
