import pandas as pd

T2F = dict()
T2F['tutor_id'] = pd.Int64Dtype()
T2F['timestamp'] = 'datetime64[ns, UTC]'
T2F['student_rating'] = pd.Int64Dtype()
T2F['tutor_fired'] = bool
T2F['tutor_age'] = pd.Int64Dtype()
T2F['session_tag_no_material'] = pd.Int64Dtype()
T2F['session_tag_student_left'] = pd.Int64Dtype()
T2F['session_tag_student_not_engaging'] = pd.Int64Dtype()
T2F['student_complained'] = pd.Int64Dtype()
T2F['student_complaint_clarity'] = pd.Int64Dtype()
T2F['student_complaint_speed'] = pd.Int64Dtype()
T2F['student_complaint_subject'] = pd.Int64Dtype()
T2F['student_complaint_other'] = pd.Int64Dtype()
T2F['session_tag_cheating'] = pd.Int64Dtype()
T2F['session_tag_inappropriate'] = pd.Int64Dtype()
T2F['session_tag_other_subject'] = pd.Int64Dtype()