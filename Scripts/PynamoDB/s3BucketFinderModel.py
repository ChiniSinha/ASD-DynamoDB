import logging
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from datetime import datetime

logging.basicConfig()
log = logging.getLogger("pynamodb")
log.setLevel(logging.DEBUG)
log.propagate = True


class S3BucketFinderData(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "S3BucketFinderData"
        region = 'us-east-1'
    uuid = UnicodeAttribute(hash_key=True)
    s3_path = UnicodeAttribute(null=True)
    

# Create the table
if not S3BucketFinderData.exists():
    S3BucketFinderData.create_table(wait=True)

# Create a thread
data_item = S3BucketFinderData(
    '1234-1223-1235-1222', s3_path='foobar/test/project'
)

# try:
#     S3BucketFinderData.get('does not', 'exist')
# except S3BucketFinderData.DoesNotExist:
#     pass

# Save the thread
data_item.save()

# Batch write operation
with S3BucketFinderData.batch_write() as batch:
    data = []
    for x in range(100):
        dataItem = S3BucketFinderData('1334-5667-9001-{0}'.format(x), s3_path='foobar/test/project-{0}'.format(x))
        data.append(dataItem)

    for dataItem in data:
        batch.save(dataItem)

# Get table count
print(S3BucketFinderData.count())

# Count based on a filter
print(S3BucketFinderData.count('1334-5667-9001-1'))

# Batch get
item_keys = [('1334-5667-9001-{0}'.format(x)) for x in range(100)]
for item in S3BucketFinderData.batch_get(item_keys):
    print(item)

# Scan
for item in S3BucketFinderData.scan():
    print(item)

# Query
for item in S3BucketFinderData.query('1334-5667-9001-1'):
    print(item)
