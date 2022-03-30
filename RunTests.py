import os

cd = os.getcwd()
import time

import subprocess



#Create Account test
def run_create_account_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateAccountTest'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(4, round(t1-t0, 3))


#Create Folder test
def run_create_folder_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateFolderTest.CreateFolderTestCase.test_create_folder_no_name'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateFolderTest.CreateFolderTestCase.test_create_folder_valid_name'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))



#Create Note test
def run_create_note_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateNoteTest.CreateNoteTestCase.test_create_file_success'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateNoteTest.CreateNoteTestCase.test_create_file_no_name'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateNoteTest.CreateNoteTestCase.test_create_file_no_folder'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.CreateNoteTest.CreateNoteTestCase.test_create_file_no_body'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(4, round(t1-t0, 3))


def run_delete_folder_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.DeleteFolderTest.DeleteFolderTestCase.test_delete_folder_empty'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.DeleteFolderTest.DeleteFolderTestCase.test_delete_folder_not_empty'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))


def run_delete_note_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.DeleteNoteTest.DeleteNoteTestCase.test_delete_file'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(1, round(t1-t0, 3))

def run_filter_folder_notes_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterFolderNotesTest.FilterFolderNotesTestCase.test_filter_folder_notes_hidden'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterFolderNotesTest.FilterFolderNotesTestCase.test_filter_folder_notes_visible'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterFolderNotesTest.FilterFolderNotesTestCase.test_filter_by_folder_folder1'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterFolderNotesTest.FilterFolderNotesTestCase.test_filter_by_folder_folder2'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(4, round(t1-t0, 3))

def run_filter_shared_notes_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterSharedNotesTest.FilterSharedNotesTestCase.test_filter_shared_notes_hidden'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FilterSharedNotesTest.FilterSharedNotesTestCase.test_filter_shared_notes_visible'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))


def run_formatting_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FormattingTest.FormattingTestCase.test_bold_before_writing'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FormattingTest.FormattingTestCase.test_bold_after_writing'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FormattingTest.FormattingTestCase.test_italics_before_writing'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.FormattingTest.FormattingTestCase.test_italics_after_writing'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(4, round(t1-t0, 3))

def run_login_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.LoginTest.LoginTestCase.test_login_invalid_creds'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.LoginTest.LoginTestCase.test_login_success'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.LoginTest.LoginTestCase.test_login_null'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(3, round(t1-t0, 3))

def run_security_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_secure_password'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_no_password'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_insecure_password_too_short'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_insecure_password_too_similar'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_insecure_password_completely_numeric'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_insecure_password_commonly_used'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SecurityTest.SecurityTestCase.test_create_account_bad_confirmation'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(7, round(t1-t0, 3))

def run_shared_notes_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SharedNotesTest.SharedNotesTestCase.test_edit_shared_note'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.SharedNotesTest.SharedNotesTestCase.test_view_shared_note'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))

def run_share_notes_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ShareNotesTest.ShareNotesTestCase.test_share_note_edit'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ShareNotesTest.ShareNotesTestCase.test_share_note_view'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))

def run_store_notes_in_folder_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.StoreNotesInFolderTest.StoreNotesInFolderTestCase.test_store_note_old'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.StoreNotesInFolderTest.StoreNotesInFolderTestCase.test_store_note_new'], cwd=cd)
    p.wait()
    p.kill()

    t1 = time.time()

    print_out(2, round(t1-t0, 3))

def run_updated_time_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdatedTimeTest.UpdatedTimeTestCase.test_update_local_note'], cwd=cd)
    p.wait()
    p.kill()


    t1 = time.time()

    print_out(1, round(t1-t0, 3))


def run_update_folder_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateFolderTest.UpdateFolderTestCase.test_update_folder_not_empty'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateFolderTest.UpdateFolderTestCase.test_update_folder_empty'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateFolderTest.UpdateFolderTestCase.test_update_folder_no_name'], cwd=cd)
    p.wait()
    p.kill()


    t1 = time.time()

    print_out(3, round(t1-t0, 3))


def run_update_note_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateNoteTest.UpdateNoteTestCase.test_update_shared_note'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateNoteTest.UpdateNoteTestCase.test_update_local_note'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateNoteTest.UpdateNoteTestCase.test_update_note_name'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.UpdateNoteTest.UpdateNoteTestCase.test_update_note_folder'], cwd=cd)
    p.wait()
    p.kill()


    t1 = time.time()

    print_out(4, round(t1-t0, 3))


def run_response_time_test():
    t0 = time.time()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ResponseTimeTest.ResponseTimeTestCase.test_response_time_home'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ResponseTimeTest.ResponseTimeTestCase.test_response_time_create_account'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ResponseTimeTest.ResponseTimeTestCase.test_response_time_login'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ResponseTimeTest.ResponseTimeTestCase.test_response_time_notes'], cwd=cd)
    p.wait()
    p.kill()

    p = subprocess.Popen(['python3', 'manage.py', 'test', 'website.test.ResponseTimeTest.ResponseTimeTestCase.test_response_time_folders'], cwd=cd)
    p.wait()
    p.kill()


    t1 = time.time()

    print_out(5, round(t1-t0, 3))



def print_out(tests, time):
    print("----------------------------------------------------------------------")
    print("Ran " + str(tests) + " test in " + str(time) + "s")
    print("")
    print("OK")


# run_create_folder_test()
# run_login_test()
# run_create_note_test()
# run_update_note_test()
# run_delete_note_test()
# run_updated_time_test()
# run_create_folder_test()
# run_update_folder_test()
# run_delete_folder_test()
# run_store_notes_in_folder_test()
# run_share_notes_test()
# run_shared_notes_test()
# run_filter_folder_notes_test()
# run_filter_shared_notes_test()
# run_formatting_test()
# run_security_test()
run_response_time_test()
