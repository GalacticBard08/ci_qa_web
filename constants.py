import os

LOGIN = '0000'
PASSWORD = '0000'
NAME_PRJ = 'PrjTestWEB'

# for tests_web:
NEW_NAME_USER = 'new_name'
PASS_NEW_NAME = '1234'
NEW_PRJ_NAME = 'test_role'

ALL_LEVELS_CONTROL = [1, 2, 3, 4]
ALL_LANGUAGE_PROJECTS = {  # language : [file_name_for_stat_analysis, file_name_for_dyn_analysis]
    'java': ['test_java.zip', 'test_java.probed.zip'],
    'cpp': ['test_cpp.zip', 'test_cpp.probed.zip'],
    'cs': ['test_cs.zip', 'test_cs.probed.zip'],
}

# for tests_bench:
NAME_BENCH_PROJECT = "PrjTestBench"
PATH_TO_JAM_PROJECT = '~/jam_project'

CURRENT_PATH=os.path.dirname(__file__) #Родительская директория содержащая каталог с тестами
HOME_DIRECTORY = os.getenv('HOME')
FILES_FOR_ANALYSIS_DIRECTORY = 'files_for_analysis'
JAVA_ARHIVE = os.path.join(HOME_DIRECTORY, FILES_FOR_ANALYSIS_DIRECTORY, ALL_LANGUAGE_PROJECTS['java'][0])
RESULTS_ANALYSIS_FILE_NAME = 'results_analysis.json'
PATH_TO_RESULTS_FILE = ''

NAME_TESTS_FOR_BENCH = 'bench'
NAME_TESTS_FOR_WEB = 'web'
