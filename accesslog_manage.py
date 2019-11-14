import boto3
import os, time

# Let's use Amazon S3
s3 = boto3.resource('s3')


class AccesslogManager:

    def __index__(self):
        self.bucketname = ''
        self.log_directory = "/home/akhil/Documents/accesstest"
        self.delete_before_days = 7

    def s3_upload(self, file_path):
        data = open('test.jpg', 'rb')
        s3.Bucket(file_path).put_object(Key='test.jpg', Body=data)

    def delete_old_files(self):
        now = time.time()

        for f in os.listdir(self.log_directory):
            f = os.path.join(self.log_directory, f)
            print('file full path.....', f)
            if os.stat(f).st_mtime < now - self.delete_before_days * 86400:
                if os.path.isfile(f):
                    os.remove(os.path.join(self.log_directory, f))
