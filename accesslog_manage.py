import boto3
import os, time
import datetime

# Let's use Amazon S3
s3 = boto3.resource('s3')


class AccesslogManager:

    def __init__(self):
        self.bucketname = 'bucket name'
        self.log_directory = "/home/akhil/Documents/accesstest"
        self.delete_before_days = 7

    def s3_upload(self, file_path):
        data = open(file_path, 'rb')
        datetime_str = str(datetime.datetime.now())
        s3.Bucket(self.bucketname).put_object(Key='accesslog_' + datetime_str, Body=data)

    def delete_old_files(self):
        now = time.time()

        for f in os.listdir(self.log_directory):
            f = os.path.join(self.log_directory, f)
            if os.stat(f).st_mtime < now - self.delete_before_days * 86400:

                # Upload to s3 bucket
                self.s3_upload(f)

                # Delete log file
                if os.path.isfile(f):
                    os.remove(os.path.join(self.log_directory, f))


accesslog = AccesslogManager()
accesslog.delete_old_files()
# chron tab task daily
#  * 12 * * *  accesslog_manage.py


