from pynamodb.models import Model	
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute)
import logging

logging.basicConfig()
log = logging.getLogger("pynamodb")
log.setLevel(logging.DEBUG)
log.propagate = True

class User(Model):
	class Meta:
		table_name = 'User'
		region = 'us-east-1'	

	UserName = UnicodeAttribute(hash_key=True)
	LastName = UnicodeAttribute(null=True)
	Major = UnicodeAttribute(null=True)
	YearOfGraduation = NumberAttribute(default=0)

metadata_item=MetaData(UserName='Patricia5859',LastName='Bagzai',Major='CS')
metadata_item.save()


