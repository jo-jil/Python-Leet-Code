import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    stu = pd.DataFrame(students[students['student_id'] == 101])
    stu = stu.drop(columns=['student_id'])
    return stu
