class DataConfig:
	reader_path = 'model.py'
	writer_path = './writer.py'
	SQLALCHEMY_DATABASE_URL = "postgresql://mollify@localhost/mollify_default"
	TEST_SQLALCHEMY_DATABASE_URL = "postgresql://mollify@localhost/mollify_test"
	APP_NAME = "mollify_default"
	CONTAINER = True