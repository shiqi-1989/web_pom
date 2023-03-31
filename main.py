# -*- coding: UTF-8 -*-
import os
import webbrowser

import pytest

from Common.handle_path import *

if __name__ == '__main__':
    pytest.main()
    # print(f'allure generate {reports_temp_dir} -o {reports_html_dir} --clean')
    os.system(f'allure generate {reports_temp_dir} -o {reports_html_dir} -c')
    webbrowser.open("http://localhost:63342/web_pom/Outputs/reports/index.html", new=0)
