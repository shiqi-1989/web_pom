"""
登录页
http://tkproc.huatu.com/mk/#/login
"""
# 地址、账号、密码
url = "http://tkproc.huatu.com/mk/#/login"
username = "admin"
password = "admin"


"""
真题管理-试卷列表
"""
paper_management = ['xpath', '//span[text()="真题管理"]/..']
paper_list_btn = ['xpath', '//span[text()="试卷列表"]/..']
paper_add_btn = ['xpath', '//span[text()="添加试卷"]/..']
paper_name_input = ['xpath', '//input[@placeholder="请输入试卷名"]']
exam_type_input = ['xpath', '//input[@placeholder="考试类型"]']
exam_type_option = ['xpath', '//span[text()="{}"]/..']
exam_area_input = ['xpath', '//input[@placeholder="系统/地区"]']
exam_area_option = ['xpath', '//span[text()="党群及行政机关"]/..']
exam_form_input = ['xpath', '//input[@placeholder="考试形式"]']
exam_form_option = ['xpath', '//span[text()="结构化"]/..']
exam_time_input = ['xpath', '//input[@placeholder="选择考试时间"]']
exam_time_option = ['xpath', '//td[@class="available today"]']
exam_period_input = ['xpath', '//input[@placeholder="考试时段"]']
exam_period_option = ['xpath', '//span[text()="{}"]/..']
exam_duration_input = ['xpath', '//input[@placeholder="请输入时限(分)"]']
paper_submit_btn = ['xpath', '//span[text()="提交"]/..']

"""
课程管理
"""
# 课程管理按钮
course_management_btn = ['xpath', '//span[text()="课程管理"]/..']
# 课程列表按钮
course_list_btn = ['xpath', '//span[text()="课程列表"]/..']
# 条件：课程名称
criteria_course_name = ['xpath', '//input[@placeholder="请输入内容"]']
# 搜索按钮
search__btn = ['xpath', '//span[text()="搜索"]/..']
# 重置按钮
reset_btn = ['xpath', '//span[text()="重置"]/..']
# 列表课程标题
course_info_title = ['xpath', '//div[text()="{}"]']
# 添加课程按钮
course_add = ['xpath', '//*[text()="添加课程"]/..']


