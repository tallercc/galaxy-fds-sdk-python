class Permission(object):
  '''
  The Permission definition class.
  '''

  '''
  The READ permission: when it applies to buckets it means allow the grantee to
  list the objects in the bucket; when it applies to objects it means allow the
  grantee to read the object data and metadata.
  '''
  READ = 0x01

  '''
  The WRITE permission: when it applies to buckets it means allow the grantee
  to create, overwrite and delete any object in the bucket; it is not applicable
  for objects.
  '''
  WRITE = 0x02

  '''
  The FULL_CONTROL permission: allows the grantee the READ and WRITE permission
  on the bucket/object.
  '''
  FULL_CONTROL = 0xff

  def to_string(self):
    value = self.get_value()
    if value == Permission.READ:
      return 'READ'
    elif value == Permission.WRITE:
      return 'WRITE'
    elif value == Permission.FULL_CONTROL:
      return 'FULL_CONTROL'
    else:
      raise RuntimeError('Fatal error')

  def get_value(self):
    permission = self.to_string()
    if permission == 'READ':
      return Permission.READ
    elif permission == 'WRITE':
      return Permission.WRITE
    elif permission == 'FULL_CONTROL':
      return Permission.FULL_CONTROL
    else:
      raise RuntimeError('Fatal error')

class UserGroups(object):
  '''
  The user groups class.
  '''
  ALL_USERS = 'ALL_USERS'
  AUTHENTICATED_USERS = 'AUTHENTICATED_USERS'

class GrantType(object):
  '''
  The grant type class.
  '''
  USER = 'USER'
  GROUP = 'GROUP'

class Grantee(dict):
  '''
  The grantee definition class.
  '''
  def __init__(self, id):
    self.id = id

  @property
  def display_name(self):
    return self['displayName']

  @display_name.setter
  def display_name(self, display_name):
    self['displayName'] = display_name

  @property
  def id(self):
    return self['id']

  @id.setter
  def id(self, id):
    self['id'] = id

class Owner(dict):
  '''
  The owner definition class.
  '''
  @staticmethod
  def from_json(json):
    if json != '':
      owner = {}
      if 'id' in json.keys():
        owner.id = json['id']
      if 'displayName' in json.keys():
        owner.display_name = json['displayName']
      return owner
    return None

  @property
  def id(self):
    return self.id

  @id.setter
  def id(self, id):
    self['id'] = id

  @property
  def display_name(self):
    return self.display_name

  @display_name.setter
  def display_name(self, display_name):
    self['displayName'] = display_name

class Grant(dict):
  '''
  The grant class.
  '''
  def __init__(self, grantee, permission):
    self.grantee = grantee
    self.type = GrantType.USER
    self.permission = permission
    self.int_perm = permission

  @property
  def permission(self):
    return self['permission']

  @permission.setter
  def permission(self, permission):
    self['permission'] = permission.to_string()
    self['int_perm'] = permission.get_value()

  @property
  def grantee(self):
    return self['grantee']

  @grantee.setter
  def grantee(self, grantee):
    self['grantee'] = grantee

  @property
  def type(self):
    return self['type']

  @type.setter
  def type(self, type):
    self['type'] = type

class AccessControlList(object):
  '''
  The access control list class.
  '''
  def __init__(self):
    self.acl = {}

  def add_grant(self, grant):
    self.acl['%s:%s' % (grant.grantee.id, grant.type)] = grant

  def get_grant_list(self):
    grants = []
    for k in self.acl:
      grants.append(self.acl[k])
    return grants





