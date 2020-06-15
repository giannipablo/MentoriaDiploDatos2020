import pandas as pd

T2F = dict()
T2F['tutor_id'] = pd.Int64Dtype()
T2F['timestamp'] = 'datetime64[ns, UTC]'
T2F['student_rating'] = pd.Int64Dtype()
T2F['tutor_fired'] = bool
T2F['tutor_age'] = pd.Int64Dtype()
