import dotenv
import os
from collections import namedtuple

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(root_dir, ".env")
dotenv.load_dotenv(env_path)

dotenv.load_dotenv(".env", verbose=True)

# running mode
# production, development or staging
MODE = os.getenv("MODE")
MODE_CHOICES = ["production", "development", "staging"]
if MODE not in MODE_CHOICES:
    raise ValueError(
        "mode must be production, development or staging. actualy: {}".format(MODE))

AWSValues = namedtuple("aws", ("key_id", "secret_key", "bucket", "region"))

AWS = AWSValues(key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                bucket=os.getenv("AWS_STORAGE_BUCKET_NAME"),
                region=os.getenv("AWS_S3_REGION_NAME")
                )

CREATE_BUCKET = os.getenv("AWS_AUTO_CREATE_BUCKET") == "yes"

# locale
TIME_ZONE = os.getenv("DEFAULT_TIME_ZONE")
LOCALE = os.getenv("DEFAULT_LOCALE")

# 暗号系で使うキー
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "super-secret-key")
print(CREATE_BUCKET)
