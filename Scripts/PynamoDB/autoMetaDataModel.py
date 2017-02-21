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


class AutoMetaData(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "AutoMetaData"
        region = 'us-east-1'
    uuid = UnicodeAttribute(hash_key=True)
    project_name = UnicodeAttribute(null=True)
    

# Create the table
if not AutoMetaData.exists():
    AutoMetaData.create_table(wait=True)

# Create a thread
data_item = AutoMetaData(
    '1234-1223-1235-1222', project_name='foobar'
)

# try:
#     AutoMetaData.get('does not', 'exist')
# except AutoMetaData.DoesNotExist:
#     pass

# Save the thread
data_item.save()

# Batch write operation
with AutoMetaData.batch_write() as batch:
    data = []
    for x in range(100):
        dataItem = AutoMetaData('1334-5667-9001-{0}'.format(x), project_name='project-{0}'.format(x))
        data.append(dataItem)

    for dataItem in data:
        batch.save(dataItem)

# Get table count
print(AutoMetaData.count())

# Count based on a filter
print(AutoMetaData.count('1334-5667-9001-1'))

# Batch get
item_keys = [('1334-5667-9001-{0}'.format(x)) for x in range(100)]
for item in AutoMetaData.batch_get(item_keys):
    print(item)

# Scan
for item in AutoMetaData.scan():
    print(item)

# Query
for item in AutoMetaData.query('1334-5667-9001-1'):
    print(item)
