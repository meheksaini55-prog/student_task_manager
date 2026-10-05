import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-northeast-1.prod.aws.tidbcloud.com',
        user='2b83yPSLo4jhx25.root',
        password='vVxIW8grsM0DU5AE',
        database='student_task_manager',
        port=4000
    )

    return connection
