from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os


class FileUploadPage(BasePage):
    _file_upload = {"by": By.ID, "value": "file-upload"}
    _file_submit = {"by": By.ID, "value": "file-submit"}
    _uploaded_files = {"by": By.ID, "value": "uploaded-files"}

    def __init__(self, driver, filename):
        self.driver = driver
        self._visit("http://the-internet.herokuapp.com/upload")

    def upload_file(self, filename):
        self.filename = filename
        filename = 'some-file.rtf'
        print ('filename done')
        file = os.path.join(os.getcwd(), filename)
        self._type(self._file_upload, file)
        print ('done typing')
        self._click(self._file_submit)
        print ('submitted')
        upload_file_title = self._verify_text(self._uploaded_files)
        print ('uploaded file')
        assert upload_file_title == "uploaded file should be %s" % filename
        print ('text matches')

    def upload_success(self):
        self._wait_for_is_displayed(self._uploaded_files, 10)
        print ('uploaded displayed')
        return self._is_displayed(self._uploaded_files)