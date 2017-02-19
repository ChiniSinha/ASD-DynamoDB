from pynamodb.models import Model	
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute)

class MetaData(Model):
	class Meta:
		table_name = 'MetaData'
		region = 'us-east-1'	

	UserName = UnicodeAttribute(hash_key=True)
	LastName = UnicodeAttribute(null=True)
	Major = UnicodeAttribute(null=True)
	YearOfGraduation = NumberAttribute(default=0)

metadata_item=MetaData(UserName='Patricia5859',LastName='Bagzai',Major='CS')
metadata_item.save()


