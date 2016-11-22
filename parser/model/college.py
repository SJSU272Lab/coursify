from pymodm import EmbeddedMongoModel, MongoModel, fields, connect
connect("mongodb://localhost:27017/myDatabase", alias="my-app")
class Address(EmbeddedMongoModel):
    city = fields.CharField()
    state = fields.CharField()
    street1 = fields.CharField()
    street2 = fields.CharField()
    #zipcode = fields.DecimalField()

class College(MongoModel):
    #department = fields.ReferenceField(Department)
    #degree = fields.ReferenceField(Department)
    name = fields.CharField()
    address = fields.EmbeddedDocumentListField(Address)
