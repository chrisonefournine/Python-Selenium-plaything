import pytest
from pages import file_upload_page

class TestFileUpload():

    @pytest.fixture
    def upload(self, driver):
        return file_upload_page.FileUploadPage(driver)

    @pytest.mark.shallow
    def test_upload_success(self, upload):
        assert upload.upload_success() == True