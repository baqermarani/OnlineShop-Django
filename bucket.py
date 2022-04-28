import boto3
from django.conf import settings


class Bucket:
    """
    CDN bucket manager
    init method creates connection to AWS S3

    NOTE :
    - None of the methods in this class are async.
    """
    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

    def get_objects(self):
        ''' get object from bucket '''

        result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        return True

bucket = Bucket()